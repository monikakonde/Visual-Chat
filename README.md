UserInterface
![image](https://github.com/user-attachments/assets/792d19ff-01fb-4f0d-9d52-25ba2ee2cb02)
Uploade Image 
![butterfly](https://github.com/user-attachments/assets/fd3d8d04-af1d-497a-b950-722d4b7bba1d)
Generated Cpation 
![image](https://github.com/user-attachments/assets/868743ca-836b-4c09-819b-a4f02d34af33)
Generated Similar Images
![sI_dog](https://github.com/user-attachments/assets/c3bb7125-6aab-46df-92a4-19c83dae24c7)


# Visual-Chat
 
Visual Chat is an AI-based app where users upload or capture images to generate captions using the BLIP model. It uses text-to-speech to assist visually impaired users and fetches similar images via the Unsplash API. Built with Streamlit, it combines image captioning, voice guidance, and semantic image search in real time.


🧠 Key Features:
Image Upload or Camera Input: Users can upload an image from local storage or capture it directly using a webcam.

Automatic Image Captioning: Uses the BLIP model (Bootstrapped Language-Image Pretraining) from Hugging Face Transformers to describe the content of an image in natural language.

Voice Assistance (Text-to-Speech): Reads out captions and guides users during the interaction to support visually impaired individuals using pyttsx3.

Image Similarity Search: Uses the generated caption as a semantic query to retrieve 2–3 visually similar images using the Unsplash API.

Real-time Processing: Includes webcam input to allow real-time image capture and processing.

Accessible UI: Built using Streamlit for an easy-to-use web interface with buttons for all interactions.


🔄 Workflow:
Image Input: Upload an image or capture one using the webcam.

Caption Generation: Process the image using BLIP to generate a short caption.

Voice Output: Speak the caption aloud using pyttsx3.

Similar Image Retrieval: Use the caption as a query to fetch images from Unsplash.

Display: Show retrieved similar images in a visual layout.
