from transformers import pipeline

# from dotenv import find_dotenv, load_dotenv
import streamlit as st
from PIL import Image

# from io import BytesIO
import pyperclip

# load_dotenv(find_dotenv())


# IMAGE-2-TEXT
# def image2text(image):
#     image_to_text = pipeline(
#         "image-to-text", model="Salesforce/blip-image-captioning-base"
#     )
#     text = image_to_text(image)
#     return text
def image2text(image):
    image_to_text = pipeline(
        "image-to-text", model="Salesforce/blip-image-captioning-base"
    )
    text = image_to_text(image)
    return text[0]["generated_text"] if text and len(text) > 0 else None


# Use st.sidebar para criar a barra lateral


# Define o título e a descrição da página
st.title("Image-2-Text")


with st.sidebar:
    # Define o estilo CSS para centralizar apenas o botão na barra lateral
    st.markdown(
        """
        <style>
        .sidebar .stButton>button {
            display: block;
            margin: 0 auto;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title("About")
    st.write(
        "Hi, this is a simple [AI](https://huggingface.co/Salesforce/blip-image-captioning-base) app that generates text based on image input."
    )

    st.markdown(
        '<div class="centered-button"><a href="https://www.buymeacoffee.com/fredvpgi" target="_blank"><img src="https://img.shields.io/badge/Buy%20Me%20a%20Coffee-Donate-yellow.svg"></a></div>',
        unsafe_allow_html=True,
    )

# Opção para fazer o upload da imagem
uploaded_file = st.file_uploader("Upload an image ;)", type=["jpg", "png", "jpeg"])

# Verifica se o usuário fez o upload da imagem
if uploaded_file is not None:
    # Exibe a imagem
    st.image(uploaded_file, use_column_width=True)

    # Converte o objeto de arquivo do Streamlit em uma imagem PIL
    image = Image.open(uploaded_file)

    # Adiciona um spinner para mostrar que o processamento está ocorrendo
    with st.spinner("Processing the image..."):
        # Chama a função image2text para converter a imagem em texto
        result = image2text(image)

    # Exibe o resultado do texto obtido da imagem
    if result and len(result) > 0:
        # st.subheader("Texto obtido da imagem:")
        text_box = st.text_area("", result, height=200)
        if st.button("Copy Text"):
            pyperclip.copy(result)
            st.success("Copied to clipboard!")
    else:
        st.warning("We can't process the input image at this time, try again later.")
