from transformers import ViltProcessor, ViltForQuestionAnswering
import requests
from PIL import Image

processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
model = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa")

def pipeline_modelo(text:str, image:Image):
    # prepare inputs
    encoding = processor(image, text, return_tensors="pt")

    outputs = model(**encoding)
    logits = outputs.logits

    idx = logits.argmax(-1).item()
    return model.config.id2label[idx]