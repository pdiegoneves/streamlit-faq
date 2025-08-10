import streamlit as st

from components.chart_dialog import visitor_chart
from components.question import question

st.set_page_config(
    page_title="FAQ - Teste",
    page_icon="https://docs.streamlit.io/logo.svg",
    layout="wide"
)

logo, titulo = st.columns([2, 10])

logo.image("https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png")
titulo.title("F.A.Q")

metricas = st.container()
metricas_col1, metricas_col2, metricas_col3 = st.columns([5, 5, 2])

with metricas:
    metricas_col1.metric(
        "Visitantes Semanais",
        135,
        border=True,
        delta=5
    )
    metricas_col2.metric(
        "Visitantes Mensais",
        520,
        border=True,
        delta=-20
    )
    metricas_col3.button("Mostrar", on_click=visitor_chart)
    
st.divider()

question(
    question="O que é uma F.A.Q?",
    answer='FAQ é a sigla para Frequently Asked Questions, que em português significa "Perguntas Frequentes". É uma página de um site que reúne as dúvidas mais frequentes dos clientes.'
)

question(
    question="O que é a linguagem Python?",
    answer='Python é uma linguagem de programação de alto nível, orientada a objetos, e de uso geral. É muito utilizada no desenvolvimento web, ciência de dados, machine learning, e automação.'
)
    

col1, col2, col3 = st.columns([3,3,6])

col1.header("Coluna 1")
col1.text("Texto da coluna 1")

col2.header("Coluna 2")
col2.text("Texto da coluna 2")


with col3:
    st.header("Coluna 3")
    st.text("Texto da coluna 3")
    
