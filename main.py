import os
import streamlit as st
from tempfile import NamedTemporaryFile
from functions import batch_process_images, get_similar_images, speak_caption

# BLIP (Bootstrapped Language Image Pretraining) for image captioning
# CLIP (Contrastive Language-Image Pretraining) similar image indirectly used via Unsplash search
# PIL (Python Imaging Library) to load and process images
# TTS (Text-to-Speech) library to vocalize captions
# Streamlit for UI and interactivity

# Initialize session state.
if "caption" not in st.session_state:
    st.session_state["caption"] = None

# Speak welcome once.
if "voice_greeted" not in st.session_state:
    speak_caption("Welcome to Visual Chat. Please upload or capture an image.")
    st.session_state["voice_greeted"] = True

# Title and header.
st.title('VISUAL CHAT')
st.header("Upload or capture an image")

# Upload file.
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Capture from webcam.
camera_image = st.camera_input("Or take a photo")

# Decide which image to use.
image_file = uploaded_file if uploaded_file else camera_image

# If image is provided.
if image_file is not None:
    st.image(image_file, caption='Your Image', use_container_width=True)

    # Voice assist after receiving image.
    if "image_voice_announced" not in st.session_state:
        speak_caption("Image received. Press generate caption button to continue.")
        st.session_state["image_voice_announced"] = True

    # Horizontal button layout.
    col1, col2, col3 = st.columns(3)

    with col1:
        generate_caption = st.button("🧠 Generate Caption")
    with col2:
        read_caption = st.button("🔊 Read Caption")
    with col3:
        generate_similar = st.button("🔍 Generate Similar Images")

    # Handle caption generation.
    if generate_caption:
        with NamedTemporaryFile(dir='.idea', delete=False, suffix=".png") as f:
            f.write(image_file.getbuffer())
            image_path = f.name

        captions = batch_process_images([image_path])
        if captions:
            st.session_state["caption"] = captions[0]
            st.write("Generated Caption:", st.session_state["caption"])
            speak_caption(f"The caption is: {st.session_state['caption']}")
        else:
            st.write("Failed to generate a caption.")

    # Handle text-to-speech manually.
    if read_caption and st.session_state["caption"]:
        speak_caption(st.session_state["caption"])

    # Handle similar image search.
    if generate_similar and st.session_state["caption"]:
        caption = st.session_state["caption"]
        st.write(f"Using caption as query: '{caption}'")
        similar_images = get_similar_images(caption)

        #  if similar_images and "similar_image_voice_announced" not in st.session_state:
        if similar_images:
            st.write("Similar Images:")
            # speak_caption("Similar Images Generated")
            # st.session_state["similar_image_voice_announced"] = True
            for img_url in similar_images:
                st.image(img_url)
        else:
            st.write("No similar images found.")