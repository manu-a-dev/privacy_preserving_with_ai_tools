import os

import requests
from PIL import Image # Run pip install Pillow
from openai import OpenAI # https://github.com/openai/openai-python/discussions/742
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
  api_key=os.getenv('OPENAI_API_KEY'),
)
# to edit existing image
def censor(image):
  text = "TURN THIS MAN INTO ROCKS"
  out = openai.Image.create_edit(image= open(image),prompt=text,n=1)
  return requests.get(out['data'][0]['url'])