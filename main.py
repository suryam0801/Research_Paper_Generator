# app.py
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from generate import generate_text
from single_generate_outline import generate_detailed_outline


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


@app.post("/generate_outline")
async def generate_outline(topic: TextInput, context: TextInput):
    # Example usage
    # topic = "End-to-End Learning for Self-Driving Cars"
    # context = "We trained a convolutional neural network (CNN) to map raw pixels from a single front-facing camera directly to steering commands. This end-to-end approach proved surprisingly powerful. With minimum training data from humans the system learns to drive in traffic on local roads with or without lane markings and on highways. It also operates in areas with unclear visual guidance such as in parking lots and on unpaved roads. The system automatically learns internal representations of the necessary processing steps such as detecting useful road features with only the human steering angle as the training signal. We never explicitly trained it to detect, for example, the outline of roads. Compared to explicit decomposition of the problem, such as lane marking detection, path planning, and control, our end-to-end system optimizes all processing steps simultaneously. We argue that this will eventually lead to better performance and smaller systems. Better performance will result because the internal components self-optimize to maximize overall system performance, instead of optimizing human-selected intermediate criteria, e. g., lane detection. Such criteria understandably are selected for ease of human interpretation which doesn’t automatically guarantee maximum system performance. Smaller networks are possible because the system learns to solve the problem with the minimal number of processing steps. We used an NVIDIA DevBox and Torch 7 for training and an NVIDIA DRIVETM PX self-driving car computer also running Torch 7 for determining where to drive. The system operates at 30 frames per second (FPS)."
    detailed_outline = generate_detailed_outline(topic, context)
    return {"output": detailed_outline}


# Run the app with Uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
