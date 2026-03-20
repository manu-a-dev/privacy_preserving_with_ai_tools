import os
import argparse
import base64
from openai import OpenAI # https://github.com/openai/openai-python/discussions/742
from dotenv import load_dotenv

parser = argparse.ArgumentParser()
parser.add_argument('image', help='directory of image')
parser.add_argument('destination',help ='the filepath for the newly created image')
args = parser.parse_args()

#sets up openai client
load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

text = "find all the people in this image, remove their heads, then replace them with new unique heads"
out = client.images.edit(
model ="gpt-image-1.5",
image= [open(args.image,'rb')],
prompt=text,
n=1)
edited = base64.b64decode(out.data[0].b64_json)
with open(args.destination,'wb') as file:
  file.write(edited)

