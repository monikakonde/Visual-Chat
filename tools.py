from langchain.tools import BaseTool
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

class ImageCaptionTool(BaseTool):
    name = "Image captioner"
    description = "Use this tool when given the path to an image that you would like to be described."

    def _init_(self):
        super()._init_()
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model_name = "Salesforce/blip-image-captioning-large"
        self.processor = BlipProcessor.from_pretrained(self.model_name)
        self.model = BlipForConditionalGeneration.from_pretrained(self.model_name).to(self.device)

    def _run(self, img_path):
        image = Image.open(img_path).convert('RGB')
        inputs = self.processor(image, return_tensors='pt').to(self.device)
        output = self.model.generate(**inputs, max_new_tokens=20)
        caption = self.processor.decode(output[0], skip_special_tokens=True)
        return caption

    def _arun(self, query: str):
        raise NotImplementedError("This tool does not support async")