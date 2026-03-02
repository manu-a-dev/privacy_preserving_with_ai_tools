# Source: https://ai.google.dev/gemini-api/docs/image-generation

import os
from PIL import Image  # Run pip install Pillow
from google import genai
from dotenv import load_dotenv
from google.genai import types # Run pip install google-genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv('GOOGLE_API_KEY'),
)

prompt = ("Create a picture of a nano banana dish in a fancy restaurant with a Gemini theme")
response = client.models.generate_content(
    model="gemini-2.0-flash-image",
    contents=[prompt],
)

for part in response.parts:
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        image = part.as_image()
        image.save("generated_image.png")

# Result: "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits."
    # Might be better than OpenAI because we get 100 images per day for free.
        # https://support.google.com/gemini/answer/16275805?hl=en
    # Did some digging, we'll still need to add payment information anyways. Annoying.
