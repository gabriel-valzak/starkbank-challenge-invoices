**StarkBank Challenge**

Desafio: 

- Emitir automaticamente 8 a 12 invoices a cada 3 horas.
- Receber via webhook o evento de pagamento de cada invoice.
- Executar uma transferência automática do valor pago (descontadas as taxas) para a conta bancária definida pelo desafio.

Todo o fluxo foi implementado utilizando FastAPI, SDK oficial da Stark Bank e execução agendada via AWS EventBridge + AWS Lambda.

----
1. Arquitetura da Solução

A aplicação é composta por três partes principais:

1.1 FastAPI
> Emite invoices
> Processa o webhook de pagamento enviado pela StarkBank.
> Gerar transferências automaticamente após a confirmação de pagamento.

Rotas disponíveis:
POST /api/invoices   → Emissão de invoices
POST /api/webhook    → Recebimento de eventos

1.2 AWS EventBridge + Lambda
> Utilizado para agendar a emissão automática de invoices.
> O Lambda executa uma chamada HTTP para a rota /api/invoices a cada 3 horas.

1.3 StarkBank Webhook

>A Stark Bank envia eventos de invoice para o endpoint:

POST /api/webhook

> Quando o evento indica paid, uma transferência é criada automaticamente.
------


2. Como Executar o Projeto Localmente

2.1 Instalar dependências
pip install -r requirements.txt

2.2 Iniciar o servidor
uvicorn main:app --reload



**Validação**

Para validar o funcionamento do projeto:

POST /api/invoices

A transferência aparecerá como concluída no dashboard.


3. Tecnologias Utilizadas

Python 3.10+
FastAPI
Uvicorn
StarkBank SDK
AWS Lambda / EventBridge
Render
