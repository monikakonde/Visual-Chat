import pyttsx3
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import requests
import torch

# Initialize models and processors outside the functions to avoid reloading
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# BLIP model for image captioning
blip_model_name = "Salesforce/blip-image-captioning-large"
blip_processor = BlipProcessor.from_pretrained(blip_model_name)
blip_model = BlipForConditionalGeneration.from_pretrained(blip_model_name).to(device)

# Unsplash API credentials
UNSPLASH_ACCESS_KEY = "-T1ArKi1o2oXAq84XjRlMSHBdeCTrBW2SuKXO-HfKgY"
UNSPLASH_API_URL = "https://api.unsplash.com/search/photos"


def get_image_caption(image_path, model=blip_model, processor=blip_processor, device=device):
    image = Image.open(image_path).convert('RGB')
    inputs = processor(image, return_tensors='pt').to(device)
    output = model.generate(**inputs, max_new_tokens=20)
    caption = processor.decode(output[0], skip_special_tokens=True)
    return caption


def batch_process_images(image_paths):
    return [get_image_caption(path) for path in image_paths]


def speak_caption(caption):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(caption)
    engine.runAndWait()


def get_similar_images(query, access_key=UNSPLASH_ACCESS_KEY, api_url=UNSPLASH_API_URL):
    headers = {"Authorization": f"Client-ID {access_key}"}
    params = {"query": query, "per_page": 3}
    response = requests.get(api_url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        return [result["urls"]["regular"] for result in data["results"]]
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return []