import streamlit as st
import blob_manager

st.title("Pizza - Ecommerce")
st.write("O melhor e-commerce do mundo, aqui só vendemos pizzas!!")

st.title("Pizzas")
sabores_pizzas = [
    {"Sabor": "Pepperoni", "Image-Link": "", "Fatias": 15, "Tamanho": "G", "Ingredientes": "Farinha de trigo, queijo, calabresa, oregano"},
    {"Sabor": "Bacon", "Image-Link": "", "Fatias": 5, "Tamanho": "P", "Ingredientes": "Farinha de trigo, queijo, bacon, oregano"}
    ]

for pizza in sabores_pizzas:
    with st.container():
        st.header(f"Sabor: {pizza["Sabor"]}")
        st.subheader(f"Ingredientes: {pizza["Ingredientes"]}")
        #st.image(image=pizza["Image-Link"])
        st.write(f"Fatias: {pizza["Fatias"]}")
        st.write(f"Tamanho: {pizza["Tamanho"]}")

st.title("Adicionar sabor de pizza")
new_sabor = st.text_input("Sabor: ")
new_fatias = st.text_input("Numero de fatias: ")
new_ingredientes = st.text_input("Ingredientes: ")
new_imagem = st.file_uploader("Escolha uma imagem", accept_multiple_files=False, type=["jpeg"])

if st.button("Criar novo sabor de pizza"):
    blob_manager.upload_image(new_imagem)

    