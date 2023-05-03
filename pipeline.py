from PIL import Image
from transformers import AutoProcessor, Blip2ForConditionalGeneration
import torch
import os
import csv
from tqdm import tqdm




processor = AutoProcessor.from_pretrained("Salesforce/blip2-opt-2.7b")

# load in float16 # load in int8
model = Blip2ForConditionalGeneration.from_pretrained("Salesforce/blip2-opt-2.7b", load_in_8bit=True, device_map="auto")

device = "cuda" if torch.cuda.is_available() else "cpu"


# Read data from input file into memory
data = []
with open('dataset.csv', 'r') as csvinput:
    reader = csv.reader(csvinput, delimiter=',')
    # Add new column name to header row
    header = next(reader)
    header.append('BLIP-2 descriptions')
    data.append(header)
    # Add new column data to remaining rows
    for row in tqdm(reader):
        # Use data from one column to generate data for new column
        if len(row) > 0:

            raw_image = Image.open(row[0]).convert("RGB")
            inputs = processor(raw_image, return_tensors="pt").to(device, torch.float16)

            generated_ids = model.generate(**inputs, max_new_tokens=20)
            generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0].strip()
            data.append(row + [generated_text])

# Write updated data with new column back to input file
with open('dataset.csv', 'w') as csvoutput:
    writer = csv.writer(csvoutput)
    writer.writerows(data)