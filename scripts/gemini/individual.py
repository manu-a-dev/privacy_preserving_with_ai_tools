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
Start prompts!
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

prompt = (
    "Give the man a different photorealistic face. Change only the face and neck",
)
"""
End prompts!
"""

image = Image.open("../../imgs/original/individual.jpg")

response = client.models.generate_content(
    model="gemini-3.1-flash-image-preview", # Changed this model for image editing.
    # image_config=types.ImageConfig(
    #         aspect_ratio="1:1",
    # ),
    contents=[prompt, image],
)

for part in response.parts:
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        image = part.as_image()
        image.save("../../imgs/generated/gemini/individual/just_anonymized.jpg")
