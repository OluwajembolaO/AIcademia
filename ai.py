from openai import AzureOpenAI
from secret import *
from PIL import Image
import pytesseract
import io
import json
import os
#Setting up AI
AOAI_ENDPOINT = AZURE_OPENAI_ENDPOINT
AOAI_KEY = AZURE_OPENAI_API_KEY 
MODEL_NAME = "gpt-35-turbo"

openai_client = AzureOpenAI(
    api_key=AOAI_KEY,
    azure_endpoint=AOAI_ENDPOINT,
    api_version="2024-05-01-preview",
)

def getResponse(prompt):
    response = openai_client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {"role": "system", "content": f"You are a tutor.DONT GIVE THE ANSWERS TO THE QUESTIONS! Support the student and exsplain it to the best of your ability. Make them get closer to the answer without giving it away. Ask questions to the user as well. Make sure that if they respond to such questions you give me feedback make them feel good."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=500
            )
    ai_responce = (response.choices[0].message.content)

    return ai_responce




# Specify the path to tesseract executable if it is not in your PATH
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Windows example

def getResponse(prompt):
        response = openai_client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {"role": "system", "content": f"Your goal is to get the input and exsplain the input to the best of your ability. Make sure to not give the answer to the question however summerize the text to the best of your ability. I want you to write me a paragraph exsplaning why this is correct."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=500
            )
        ai_responce = (response.choices[0].message.content)

        return ai_responce

def imageToText_Depreciated(path):
    image = Image.open(path)
    #image = Image.open(io.BytesIO(path.read()))
    # Use Tesseract to do OCR on the image
    text = pytesseract.image_to_string(image)

    # Print the extracted text
    return text


def imageToText(path):
    image = Image.open(io.BytesIO(path.read()))
    # Use Tesseract to do OCR on the image
    text = pytesseract.image_to_string(image)

    # Print the extracted text
    return text


def textToSpeech(text):
    url