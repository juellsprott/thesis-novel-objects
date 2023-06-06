Can choose to either use transformers or Saleforce LAVIS library to load the BLIP-2 model. transformers variant is lighter and has been tested on various systems. LAVIS is much larger but should be able to be ran on the Snellius system. 

### Transformers
For transformers, use the following command to install the required modules:

```
%pip install bitsandbytes accelerate git+https://github.com/huggingface/transformers
```

Note that at the time of writing, bitsandbytes has not been compiled for GPU support on Windows and as such, requires a custom compiled installation instead: 

```
pip install https://github.com/acpopescu/bitsandbytes/releases/download/v0.37.2-win.1/bitsandbytes-0.37.2-py3-none-any.whl
```

The default usage with low memory bandwidth is as follows:

```
from transformers import AutoProcessor, Blip2ForConditionalGeneration

# load processor
processor = AutoProcessor.from_pretrained("Salesforce/blip2-opt-2.7b")

# load in float16 # load in int8
model = Blip2ForConditionalGeneration.from_pretrained("Salesforce/blip2-opt-2.7b",
                                                      load_in_8bit=True, device_map="auto")
# setup device
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
```

Then after loading the model:

```
raw_image = Image.open(img).convert("RGB")

inputs = processor(raw_image, return_tensors="pt").to(
        DEVICE, torch.float16)

generated_ids = model.generate(**inputs, max_new_tokens=20)

generated_text = processor.batch_decode(
        generated_ids1, skip_special_tokens=True)[0].strip()
```

For other decoding strategies, outlined in [this github issue](https://github.com/huggingface/transformers/issues/22146): 

```
# beam search:
# model.generate(**inputs, num_beams=5, max_new_tokens=30, repetition_penalty=1.0, length_penalty=1.0, temperature=1)

# nucleus sampling:
# model.generate(**inputs, do_sample=True, top_p=0.9)
```

### LAVIS
Personally haven't tested LAVIS yet, however they have a [documentation](https://github.com/salesforce/LAVIS/tree/main/projects/blip2) with a notebook demo which should work with sufficient memory, thus running the same code as described in there should in theory work just fine. The documentation also contains methods to ask questions and change decoding strategies.