from fastapi import FastAPI, UploadFile, File, Form
from PIL import Image
from modelo import pipeline_modelo
import io
import uvicorn #servidor WSGI


app = FastAPI()

# Rota raiz
@app.get("/")
def inicio():
    return{"Projeto de respostas sobre imagens", "Priscila Dalepiane"}

# Raiz: "http://localhost:3000/"
# API: "http://localhost:3000/api/"

@app.post("/api")
async def api(text: str = Form(...), image: UploadFile = File(...)):

    image_read = await image.read()

    image = Image.open(io.BytesIO(image_read))

    resultado = pipeline_modelo(text, image)

    return {"Resposta:", resultado}

# Inicia o servidor WSGI Uvicorn com API
if __name__ == "__main__":
    uvicorn.run(app, host = "0.0.0.0", port = 3000)