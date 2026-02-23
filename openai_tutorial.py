# Source: https://www.geeksforgeeks.org/artificial-intelligence/generate-images-with-openai-in-python/

# Some suggestions:
    # Make a virtual environment.
        # Then, you can install OpenAI.
        # It should already be ignored when you push.
    # Store your API key in .env.
        # Again, should already be ignored.

import os
import requests
from PIL import Image # Run pip install Pillow
from openai import OpenAI # https://github.com/openai/openai-python/discussions/742
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
  api_key=os.getenv('OPENAI_API_KEY'),
)   

text = "batman art in red and blue color"

res = client.images.generate(
    # text describing the generated image
    prompt=text, # Text describing the generated image.
    n=1, # Number of images to generate.
    size="256x256", # Size of each generated image.
)

# Error code: 400 - {'error': {'message': 'Billing hard limit has been reached', 'type': 'image_generation_user_error', 'param': None, 'code': 'billing_hard_limit_reached'}}
    # https://openai.com/api/pricing/
    # I am at a loss for words.
print(res.data)
