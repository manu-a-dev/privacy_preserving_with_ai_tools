# Source: https://ai.google.dev/gemini-api/docs/image-generation
# You'll need to pay.

import os
from PIL import Image  # Run % pip install Pillow
from google import genai
from dotenv import load_dotenv
from google.genai import types # Run % pip install google-genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv('GOOGLE_API_KEY'),
)

"""
These prompts are dedicated for an individual.
"""
# prompt = (
#     "Give the man a different face with distinct human-like features",
# )

# prompt = (
#     "Give the man a different face.",
# )

# prompt = (
#     "Give the man a different face with distinct features",
# )

# prompt = (
#     "Give the man a different face. Change only the face and neck",
# )

"""
These prompts are dedicated for a group.
"""
# This gave a rather interesting result, as it only seemed to have anonymized the left-most face.
# prompt = (
#     "Give the people different faces. Change only their faces and necks",
# )

# This anonymized more faces. However, it still did not cover all faces.
# This didn't do much for 3_people.jpg.
# prompt = (
#     "Give all the people different faces. Change only their faces and necks",
# )

# For 3_people.jpg, it just closed their smiles. 
# prompt = (
#     "Give every person a different faces.",
# )

# For 3_people.jpg, it adjusted the middle person's face.
# prompt = (
#     "Give every person a distinct faces. Change only their faces and necks",
# )

# prompt = (
#     "Give everyone a very different and unrecognizable face.",
# )

# prompt = (
#     "Give everyone a distinct and unrecognizable face.",
# )

# prompt = (
#     "Give everyone a significantly different face.",
# )

# prompt = (
#     "Give everyone a distinct and unrecognizable face that is human-like.",
# )

# prompt = ( 
#     "Identify and mark all faces in the image"
# )

# prompt = ( 
#     "Identify and mark all faces in the image. Then, give each face a different realistic face"
# )

prompt = ( 
    "Identify all faces in the image. Give each face a different face with distinct features. Change only the face and neck"
)

"""
These prompts are dedicated for a license plate.
"""
# prompt = (
#     "Identify the license plate in the image" 
#     ""
# )

# TODO: Change this.
# image = Image.open("./imgs/gemini/individual/original.jpg")
# image = Image.open("./imgs/gemini/multiple_people/multiple_people.jpg")
image = Image.open("../original_imgs/3_people.jpg")

response = client.models.generate_content(
    model="gemini-3.1-flash-image-preview", # Changed this model for image editing.
    contents=[prompt, image],
)

for part in response.parts:
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        image = part.as_image()
        image.save("../generated_imgs/gemini/anonymized.jpg")
