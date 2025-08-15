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


# prepare image + question
url = "projetos/deploy-ml/04-api-texto-img/img/imagem3.jpg"
image = Image.open(url)

text = "what kind of dog is it?"

answer = pipeline_modelo(text, image)

print("Answer:", answer)