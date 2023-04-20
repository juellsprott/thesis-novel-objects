import requests
from PIL import Image
from transformers import Blip2Processor, Blip2ForConditionalGeneration

processor = Blip2Processor.from_pretrained("Salesforce/blip2-opt-2.7b")
model = Blip2ForConditionalGeneration.from_pretrained("Salesforce/blip2-opt-2.7b")

img_url = 'https://storage.googleapis.com/sfr-vision-language-research/BLIP/demo.jpg'
raw_image = Image.open(requests.get(img_url, stream=True).raw).convert('RGB')

question = "Question: which city is this? Answer:"
inputs = processor(raw_image, text=question, return_tensors="pt")

generated_ids = model.generate(**inputs, max_new_tokens=20)
print(generated_ids)
generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
print(generated_text)