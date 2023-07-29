from transformers import pipeline
from dotenv import find_dotenv, load_dotenv
import streamlit as st

load_dotenv(find_dotenv())


# IMAGE-2-TEXT
def image2text(url):
    image_to_text = pipeline(
        "image-to-text", model="Salesforce/blip-image-captioning-base"
    )
    text = image_to_text(url)
    print(text)


# Define o título e a descrição da página
st.title("Image 2 Text")
st.write("Upload a image and receive text as output!")

# Opção para fazer o upload da imagem
uploaded_file = st.file_uploader("Faça o upload da imagem", type=["jpg", "png", "jpeg"])

# Verifica se o usuário fez o upload da imagem
if uploaded_file is not None:
    # Exibe a imagem
    st.image(uploaded_file, caption="Imagem enviada.", use_column_width=True)

    # Executa a conversão de imagem em texto quando o botão for pressionado
    if st.button("Converter Imagem em Texto"):
        # Chama a função image2text para converter a imagem em texto
        result = image2text(uploaded_file)

        # Exibe o resultado do texto obtido da imagem
        if result and len(result) > 0:
            st.subheader("Texto obtido da imagem:")
            st.write(result[0]["caption"])
        else:
            st.write("Não foi possível obter o texto da imagem. Tente novamente.")


image2text("tom.jpeg")
