# Source: https://www.geeksforgeeks.org/artificial-intelligence/generate-images-with-openai-in-python/
# Error code: 400 - {'error': {'message': 'Billing hard limit has been reached', 'type': 'image_generation_user_error', 'param': None, 'code': 'billing_hard_limit_reached'}}
    # Resource: https://openai.com/api/pricing/

# Some suggestions:
    # Make a virtual environment.
        # Already ignored.
        # Useful resource: https://www.w3schools.com/python/python_virtualenv.asp 
        # Then, install OpenAI.
    # Store your API key in .env.
        # Already ignored.

import os
import requests
from PIL import Image # Run % pip install Pillow
from openai import OpenAI # https://github.com/openai/openai-python/discussions/742
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
  api_key=os.getenv('OPENAI_API_KEY'),
)   

text = "batman art in red and blue color"

res = client.images.generate(
    prompt=text,    # Text describing the generated image.
    n=1,            # Number of images to generate.
    size="256x256", # Size of each generated image.
)

print(res.data)
