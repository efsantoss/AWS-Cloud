# 🖼️ Flask Image Processor - AWS Cloud Project

Este repositório contém um projeto desenvolvido na trilha formativa de **Cloud**, oferecida pela **PUC Campinas em parceria com AWS**, utilizando **Python**, **Flask**, **OpenCV**, **SQLite** e **Docker**.

---

## 📌 Objetivo

O objetivo deste projeto é criar uma aplicação web que permita ao usuário:

* Enviar imagens via upload.
* Processar essas imagens usando o filtro **Canny** (detecção de bordas com OpenCV).
* Salvar os caminhos das imagens (originais e processadas) em um banco de dados **SQLite**.
* Exibir a imagem original e a imagem processada diretamente na interface da aplicação.
* Gerenciar tudo via **Docker** e executar em uma instância na **AWS EC2**.

---

## 🧱 Tecnologias Utilizadas

* Python 3.9
* Flask
* OpenCV
* SQLite
* Docker
* Docker Compose
* HTML (Jinja2)
* AWS EC2 (Ubuntu)

---

## 📁 Estrutura de Diretórios

```
project/
├── app.py                   # Código principal da aplicação Flask
├── templates/
│   └── index.html           # Interface do usuário
├── uploads/                 # Imagens enviadas e processadas
├── database/
│   └── db_cloud.db          # Banco de dados SQLite (criado automaticamente)
├── requirements.txt         # Dependências Python
├── Dockerfile               # Dockerfile da aplicação
└── docker-compose.yml       # Orquestração com Docker Compose
```

---

## ⚙️ Como Executar na AWS

### Pré-requisitos

* Instância EC2 rodando Ubuntu (ou similar)
* Docker e Docker Compose instalados
* Porta 5000 liberada no **Security Group**

---

### Passo a Passo

1. **Conecte-se via SSH na instância EC2**:

   ```bash
   ssh -i "sua-chave.pem" ubuntu@SEU_IP_PUBLICO
   ```

2. **Clone este repositório** ou envie seus arquivos para a VM.

3. **Navegue até o diretório do projeto**:

   ```bash
   cd seu-projeto/
   ```

4. **Construa e suba os containers**:

   ```bash
   docker-compose up --build -d
   ```

5. **Acesse a aplicação no navegador**:

   ```
   http://SEU_IP_PUBLICO:5000
   ```

---

## 🚀 Funcionalidades da Aplicação

* Interface web para upload de imagens.
* Processamento com filtro de bordas (Canny).
* Retorno em JSON contendo:

  * Caminho da imagem original
  * Caminho da imagem processada
  * IP do usuário
  * Data e hora do envio
* Registro das imagens processadas em banco de dados.

---

## 📃 Banco de Dados

A aplicação utiliza **SQLite** para armazenar os seguintes dados:

* Nome do arquivo original
* Nome do arquivo processado
* IP do usuário
* Timestamp da operação

---

## 🧪 Testando a API via Insomnia/Postman

* Endpoint de Upload: `POST /upload`
* Parâmetro: `image` (tipo: arquivo)
* Retorno: JSON com caminhos e dados do processamento

---

## 📬 Contato

Projeto desenvolvido como parte da formação AWS Cloud.
Para dúvidas ou sugestões, entre em contato pelo github ou linkedin.

---
