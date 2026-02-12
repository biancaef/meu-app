import streamlit as st

# Título do seu site
st.title("💰 Calculadora de Desconto da Bianca")

# No site, usamos number_input em vez de input
preco = st.number_input("Digite o preço do produto:", min_value=0.0, step=0.01)
desconto = st.number_input("Qual a porcentagem do desconto?", min_value=0.0, step=1.0)

# Fazemos a conta (igual ao seu código!)
valordesconto = preco * (desconto / 100)
precofinal = preco - valordesconto

# No site, usamos st.write ou st.success para mostrar o resultado
if st.button("Calcular Valor Final"):
    st.subheader(f"O valor final é: R$ {round(precofinal, 2)}")
    st.write(f"Você economizou R$ {round(valordesconto, 2)}!")
