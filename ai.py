from openai import AzureOpenAI
from secret import *
import io
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
                    {"role": "system", "content": f"You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=500
            )
    ai_responce = (response.choices[0].message.content)

    return ai_responce


from PIL import Image
import pytesseract

# Specify the path to tesseract executable if it is not in your PATH
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Windows example

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