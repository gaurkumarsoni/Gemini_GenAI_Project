import os

import json

from google import genai
from google.genai import types


# Load config
working_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(working_dir, "config.json"), "r") as f:
    config_data = json.load(f)

# API key comes automatically from environment OR config
os.environ["GEMINI_API_KEY"] = config_data["GEMINI_API_KEY"]

# Create client
client = genai.Client()


# function to load gemeni_model for chatbot response
def get_gemini_response(contents):
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=contents
    )
    return response.text

# function for image captioning
def get_image_caption(image):
    response = client.models.generate_content(
        model='gemini-3-flash-preview',
        contents=[
            types.Part.from_bytes(
                data=image,
                mime_type='image/jpeg',
            ),
            'Caption this image.'
        ]
    )

    return response.text

# function for image captioning
def gemini_embed_text(input):
    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=input
    )

    return response.embeddings[0].values





