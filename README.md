# StarkBank Challenge

Este projeto implementa todo o fluxo do desafio proposto pela StarkBank utilizando **FastAPI**, **StarkBank SDK**, **Render** e **GitHub Actions** para automação.

A aplicação em produção está acessível em:

```
https://starkbank-challenge-invoices.onrender.com
```

---

## 🚀 Objetivo do Projeto

* Emitir automaticamente **8 a 12 invoices a cada 3 horas**.
* Receber via webhook o **evento de pagamento** de cada invoice.
* Efetuar uma **transferência automática** do valor pago (menos taxas) para a conta bancária definida no desafio.

---
## 🏗️ Arquitetura da Solução

### **1. FastAPI (Hospedada no Render)**

API principal responsável por:

* Gerar invoices sob demanda.
* Processar o webhook enviado pela StarkBank.
* Criar transferências automáticas quando um pagamento é confirmado.

**Rotas públicas:**

```
POST /api/invoices      → Emite de 8 a 12 invoices
POST /api/webhook       → Recebe eventos da StarkBank
GET  /healthz           → Health check usado pelo Render
```
---

### **2. GitHub Actions — Cron Job (A cada 3 horas)**

Para garantir execução periódica sem depender do Render, um workflow em:

```
.github/workflows/trigger.yaml
```

executa a cada 3 horas e envia uma requisição POST para:

```
https://starkbank-challenge-invoices.onrender.com/api/invoices
```

Assim, as invoices são geradas automaticamente de forma confiável.

---

### **3. Webhook da StarkBank**

A StarkBank envia eventos de pagamento para:

```
POST /api/webhook
```
---

## ⚙️ Como Rodar Localmente

### **1. Instalar dependências**

```bash
pip install -r requirements.txt
```

### **2. Executar servidor**

```bash
uvicorn main:app --reload
```

### **3. Testar emissão de invoices**

```bash
POST http://localhost:8000/api/invoices
```

### **4. Testar webhook manualmente (opcional)**

```bash
POST http://localhost:8000/api/webhook
```
---

## 🧰 Tecnologias Utilizadas

* **Python 3.11**
* **FastAPI**
* **Uvicorn**
* **StarkBank SDK**
* **Render** (deploy da API)
* **GitHub Actions** (disparo automático a cada 3h)
---


Gabriel Valzak
gaa.henrique@lilve.com
