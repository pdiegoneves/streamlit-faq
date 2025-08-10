import numpy as np
import pandas as pd
import streamlit as st


@st.dialog("Visitantes ao longo do tempo")
def visitor_chart():
    st.write("Histórico de Visitas")
    chart_data = pd.DataFrame(np.random.randn(20, 1), columns=["a"])
    st.line_chart(chart_data)