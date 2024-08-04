# app.py
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from generate import generate_text


# Initialize FastAPI app
app = FastAPI()


# Define a data model for the input
class TextInput(BaseModel):
    text: str


@app.post("/generate_text")
async def predict_endpoint(input: TextInput):
    text = input.text
    output_text = generate_text(text)
    return {"output": output_text}


# Run the app with Uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
