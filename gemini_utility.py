import os

import streamlit as st

from dotenv import load_dotenv
from google import genai
from google.genai import types


# Load .env for local development
load_dotenv()

# Get API key (Streamlit secrets first, fallback to .env)
api_key = st.secrets.get("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("GEMINI_API_KEY not found. Please set it in .env or Streamlit secrets.")
    st.stop()

# Create Gemini client
client = genai.Client(api_key=api_key)


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

#function for QnA model
def gemini_qna_response(input_text):
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=input_text
    )
    return response.text




