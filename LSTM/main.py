from fastapi import FastAPI
from pydantic import BaseModel
from transformers import Tokenizer
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

# Load the trained model
model = load_model('lstm_model.h5')

# Tokenizer
tokenizer = Tokenizer(num_words=10000, oov_token='<OOV>')  # Update num_words accordingly
# Load the tokenizer vocabulary
tokenizer.word_index = json.load(open('tokenizer_word_index.json'))  # Make sure to save your tokenizer word_index during training

# Create a FastAPI app
app = FastAPI()

# Create a Pydantic model for request body
class Item(BaseModel):
    title: str
    description: str

# Define an endpoint for model inference
@app.post("/predict")
async def predict(item: Item):
    # Concatenate title and description
    text = item.title + " " + item.description

    # Tokenize and pad the input text
    sequence = tokenizer.texts_to_sequences([text])
    padded_sequence = pad_sequences(sequence, maxlen=40, padding='post', truncating='post')

    # Make prediction
    prediction = model.predict(padded_sequence)

    # Get the predicted class
    predicted_class = np.argmax(prediction)

    return {"predicted_class": predicted_class, "prediction": prediction.tolist()}





# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import Optional
# from fastapi.params import Body

# app = FastAPI()

# def pred(Title,Description):
#     answer = None
#     return answer


# @app.get("/")
# async def index(name):
#     return {"data":f"Hello my name is {name} and age is {age}"}


# @app.get("/predict")
# async def create_post(Title,Description):

#     answer = pred(Title=Title,Description=Description)
#     return {"data":answer}