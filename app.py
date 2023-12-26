import pandas as pd
import streamlit as st
from datetime import datetime
import joblib

st.set_page_config(
    page_title="Retenção360", 
    page_icon="",
    layout="wide",
    menu_items={
        'Get Help': 'mailto:kensleyw@gmail.com',
        'Report a bug': "mailto:kensleyw@gmail.com",
         'About': "**Objetivo** Prever o comportamento para reter clientes. Analisar todos os dados relevantes dos clientes e desenvolver programa que prevê a possibilidade de saída de clientes"
         }
    )

## altera o style da página
st.markdown("""
    <style>
    .st-emotion-cache-z5fcl4 {
        padding: 2rem 1rem 10rem;
        padding-left: 5rem;
        padding-right: 5rem;
    }
    </style>
""", unsafe_allow_html=True)

container1, container2, container3 = st.columns(3)

st.title("Retenção360")

st.write("Faça a análise do seu cliente, com dados relevantes e faça a retenção com base na possibilidade da saída do seu cliente")

st.subheader("Preencha os dados")

container1, container2, container3 = st.columns(3)

hoje = datetime.now()
data_min_nasc = datetime(year=hoje.year - 100, month=hoje.month, day=hoje.day)
data_max_nasc = datetime(year=hoje.year +18, month=hoje.month, day=hoje.day)
data_min_cliente = datetime(year=hoje.year - 50, month=hoje.month, day=hoje.day)


#formulario de dados
container1.write("**Informações pessoais**")
data_nasc = container1.date_input("Data nascimento", value=None, min_value=data_min_nasc, max_value=data_max_nasc)
sexo = container1.selectbox("Sexo", options=['<Selecione>', 'Feminino', 'Masculino'])
casado = container1.checkbox("Casado / União estável")
dependente = container1.checkbox('Possui dependentes')

container2.write("**Informações contratuais**")
fatura_mensal = container2.number_input(label = 'Fatura mensal', min_value=-0.0, value=None)
cliente_desde = container2.date_input("Cliente desde", value=None, min_value=data_min_cliente, max_value=hoje)
total_produtos = container2.number_input(label="Total de produtos", min_value=1, step=1)

container3.write("&nbsp;")
tipo_contrato = container3.selectbox(label="Tipo de contrato", options=['<Selecione>', 'Mensal', 'Anual', 'Bienal'])
forma_pagamento = container3.selectbox("Forma de pagamento", options=['<Selecione>', 'Cartão de crédito', 'Cheque eletrônico', 'Cheque', 'Outros'])
fatura_online = container3.checkbox('Fatura online')

btn_analise = st.button(label='Realizar análise')

def valida_dados():
    msg_validacao = ""
    
    if data_nasc is None:
        msg_validacao += "\n* Data de nascimento"

    if sexo == '<Selecione>':
        msg_validacao += "\n* Sexo"
   
    if (fatura_mensal is None or fatura_mensal < 0.01):
        msg_validacao += "\n* Fatura mensal"

    if cliente_desde is None:
        msg_validacao += "\n* Cliente desde"

    if tipo_contrato == '<Selecione>':
        msg_validacao += "\n* Tipo de contrato"
   
    if forma_pagamento == '<Selecione>':
        msg_validacao += "\n* Forma de pagamento"
   
    if msg_validacao != "":
        msg_validacao = "Alguns campos obrigatórios não foram preenchidos corretamente. Por favor, revise os seguintes itens e preencha-os para continuar:" + msg_validacao
        
    return msg_validacao

def transforma_dados_dataframe():
    dic_dados = {}
    
    # Calcular a idade do cliente
    hoje = datetime.now()
    idade_cliente = hoje.year - data_nasc.year - ((hoje.month, hoje.day) < (data_nasc.month, data_nasc.day))

    # Calcular a duração do contrato em meses
    duracao_contrato_meses = (hoje.year - cliente_desde.year) * 12 + hoje.month - cliente_desde.month

    dic_dados['Feminino']                       = 1 if sexo == 'Feminino' else 0
    dic_dados['Idoso']                          = 1 if idade_cliente >= 60 else 0    
    dic_dados['Possui parceiro']                = 1 if casado else 0
    dic_dados['Possui dependentes']             = 1 if dependente else 0
    dic_dados['Meses como cliente']             = duracao_contrato_meses
    dic_dados['Fatura online']                  = 1 if fatura_online else 0
    dic_dados['Fatura mensal']                  = fatura_mensal
    dic_dados['Contrato_Anual']                 = 1 if tipo_contrato == 'Anual' else 0
    dic_dados['Contrato_Bienal']                = 1 if tipo_contrato == 'Bienal' else 0
    dic_dados['Pagamento_Cartao_Credito']       = 1 if forma_pagamento == 'Cartão de crédito' else 0
    dic_dados['Pagamento_Cheque']               = 1 if forma_pagamento == 'Cheque' else 0
    dic_dados['Pagamento_Cheque_eletronico']    = 1 if forma_pagamento == 'Cheque eletrônico' else 0
    dic_dados['total_produtos']                 = total_produtos
    
    return pd.DataFrame([dic_dados])

def realizar_analise(dados):
    modelo = joblib.load("modelo_preditivo.joblib")
    
    resultado = modelo.predict(dados)
    return resultado 

if btn_analise:

    msg_validacao = valida_dados()
    
    if msg_validacao != "":
        st.subheader("Dados inválidos")
        st.error(msg_validacao)
    else:
        st.subheader("Resultado da análise")
            
        dados_cliente = transforma_dados_dataframe()
        
        resultado = realizar_analise(dados_cliente)
        
        print(resultado[0])
        if resultado == 1:
            st.error("**ATENÇÃO! Cliente com **alto risco** de sair")
        else:
            st.success("Cliente não corre risco de sair no momento")

        st.write("**Dados enviados**")
        st.dataframe(dados_cliente, hide_index=True)
            
        
