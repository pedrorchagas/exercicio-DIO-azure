import streamlit as st
import blob_manager
import sql_manager

st.title("Pizza - Ecommerce")
st.write("O melhor e-commerce do mundo, aqui só vendemos pizzas!!")

st.title("Pizzas")
sabores_pizzas = sql_manager.get_products()
if not sabores_pizzas:
    st.write("Nenhum sabor de pizza encontrado.")
    st.write("Por favor, adicione um sabor de pizza.")
else:
    for pizza in sabores_pizzas:

        with st.container():
            st.header(f"Sabor: {pizza["product_name"]}")
            st.subheader(f"Ingredientes: {pizza["product_ingredients"]}")
            st.image(image=pizza["product_image_link"])
            st.write(f"Fatias: {pizza["product_slices"]}")
            st.write(f"Tamanho: {pizza["product_slices"]}")
            if st.button("Deletar", key=pizza["product_id"]):
                sql_manager.delete_product(pizza["product_id"])
                st.success("Sabor de pizza deletado com sucesso!")
                st.rerun()

st.title("Adicionar sabor de pizza")
with st.container():
    new_sabor = st.text_input("Sabor: ")
    new_fatias = st.text_input("Numero de fatias: ")
    new_ingredientes = st.text_input("Ingredientes: ")
    new_imagem = st.file_uploader("Escolha uma imagem", accept_multiple_files=False, type=["jpeg"])

    if st.button("Criar novo sabor de pizza"):
        image_url = blob_manager.upload_image(new_imagem)
        sql_manager.insert_product(
            product_name=new_sabor,
            product_image_link=image_url,
            product_ingredients=new_ingredientes,
            product_slices=int(new_fatias)
        )
        st.success("Sabor de pizza adicionado com sucesso!")
        st.rerun()

