from transformers import pipeline
from dotenv import find_dotenv, load_dotenv
import streamlit as st
from PIL import Image
from io import BytesIO

load_dotenv(find_dotenv())


# IMAGE-2-TEXT
def image2text(image):
    image_to_text = pipeline(
        "image-to-text", model="Salesforce/blip-image-captioning-base"
    )
    text = image_to_text(image)
    return text


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

    st.title("About:")
    st.write(
        "Hi, this is a simple [AI](https://huggingface.co/Salesforce/blip-image-captioning-base) app that converts any image input to text output!."
    )

    # Adicione o botão "Donate" na barra lateral com link para "Buy Me a Coffee"
    st.markdown(
        '<div class="centered-button"><a href="https://www.buymeacoffee.com/fredvpgi" target="_blank"><img src="https://img.shields.io/badge/Buy%20Me%20a%20Coffee-Donate-yellow.svg"></a></div>',
        unsafe_allow_html=True,
    )

# Opção para fazer o upload da imagem
uploaded_file = st.file_uploader("Upload an image ;)", type=["jpg", "png", "jpeg"])

# Verifica se o usuário fez o upload da imagem
if uploaded_file is not None:
    # Exibe a imagem
    st.image(uploaded_file, caption="Imagem enviada.", use_column_width=True)

    # Executa a conversão de imagem em texto quando o botão for pressionado
    if st.button("Converter Imagem em Texto"):
        # Converte o objeto de arquivo do Streamlit em uma imagem PIL
        image = Image.open(uploaded_file)
        # Chama a função image2text para converter a imagem em texto
        result = image2text(image)

        # Exibe o resultado do texto obtido da imagem
        if result and len(result) > 0:
            st.subheader("Texto obtido da imagem:")
            st.write(result[0]["generated_text"])
        else:
            st.write("Não foi possível obter o texto da imagem. Tente novamente.")
