# Rotatividade de clientes de telecomunicações
Programas focados em retenção de clientes

## Problema
A rotatividade é um dos maiores problemas da indústria de telecomunicações. A pesquisa mostrou que a taxa média de rotatividade mensal entre as 4 principais operadoras de telefonia móvel nos EUA é de 1,9% a 2%.

## Objetivo 
Prever o comportamento para reter clientes. Analisar todos os dados relevantes dos clientes e desenvolver programa que prevê a possibilidade de saída de clientes

## Como utilizar
* Instale as bibliotecas
```bash
pip install -r requirements.txt
```

* Execute o streamlit
```bash
streamlit run app.py
```
## Informações sobre o conjunto de dados
### Serviços nos quais cada cliente se inscreveu
Telefone, múltiplas linhas, internet, segurança online, backup online, proteção de dispositivos, suporte técnico e streaming de TV e filmes

### Informações da conta do cliente
Há quanto tempo ele é cliente, contrato, forma de pagamento, faturamento sem papel, cobranças mensais e cobranças totais

### Informações demográficas sobre clientes
Sexo, faixa etária e se possuem companheiros e dependentes

## Arquitetura dos dados utilizada para treino e teste
**customerID:** Identificação do Cliente

**gender:** Se o cliente é homem ou mulher

**SeniorCitizen:** Se o cliente é idoso ou não (1, 0)

**Partner:** Se o cliente tem parceiro ou não (Sim, Não)

**Dependents:** Se o cliente tem dependentes ou não (Sim, Não)

**tenure:** Número de meses que o cliente permaneceu na empresa

**PhoneService:** Se o cliente possui serviço telefônico ou não (Sim, Não)

**MultipleLines:** Se o cliente tem várias linhas ou não (Sim, Não, Não há serviço telefônico)

**InternetService:** Provedor de serviços de Internet do cliente (DSL, Fibra óptica, Não)

**OnlineSecurity:** Se o cliente tem segurança online ou não (Sim, Não, Não há serviço de internet)

**OnlineBackup:** Indica se o cliente assina algum serviço adicional de backup online fornecido pela empresa: Sim, Não

**DeviceProtection:** Indica se o cliente assina um plano adicional de proteção de dispositivos para seus equipamentos de Internet fornecido pela empresa: Sim, Não

**TechSupport:** Indica se o cliente assina algum plano de suporte técnico adicional da empresa com tempos de espera reduzidos: Sim, Não

**StreamingTV:** Indica se o cliente utiliza seu serviço de Internet para transmitir programação de televisão de um provedor terceirizado: Sim, Não. A empresa não cobra taxa adicional por este serviço.

**StreamingMovie:** Indica se o cliente utiliza seu serviço de Internet para transmitir filmes de um provedor terceirizado: Sim, Não. A empresa não cobra taxa adicional por este serviço.

**Contract:** Indica o tipo de contrato atual do cliente: Mês a Mês, Um Ano, Dois Anos.

**PaperlessBilling:** Indica se o cliente optou pelo faturamento sem papel: Sim, Não

**PaymentMethod:** Indica como o cliente paga sua fatura: Saque Bancário, Cartão de Crédito, Cheque físico

**MonthlyCharge:** Indica a cobrança mensal total atual do cliente por todos os serviços da empresa.

**TotalCharges:** Indica os encargos totais do cliente, calculados até o final do trimestre especificado acima.

**Churn:** Clientes que saíram no último mês

## Palavras-chave
#aprendizado #supervisionado #classificacao #machinelearning #supervioned #classifier #telecom #churn

## Fonte
https://www.kaggle.com/datasets/blastchar/telco-customer-churn

