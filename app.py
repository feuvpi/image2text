from transformers import pipeline
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


# IMAGE-2-TEXT
def image2text(url):
    image_to_text = pipeline(
        "image-to-text", model="Salesforce/blip-image-captioning-base"
    )
    text = image_to_text(url)
    print(text)


image2text("tom.jpeg")
