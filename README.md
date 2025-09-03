# Monitoramento de Percepção Pública no Piauí

## Visão Geral do Projeto

Este projeto é uma ferramenta de web scraping e análise de dados para monitorar a percepção pública sobre temas específicos no estado do Piauí. Ele coleta notícias do Google Notícias usando um feed RSS, limpa o texto, analisa o sentimento de cada notícia (positivo, negativo ou neutro) usando um modelo de inteligência artificial e visualiza os resultados em um dashboard interativo.

A arquitetura do projeto foi desenvolvida seguindo os princípios SOLID para garantir um código modular, flexível e fácil de manter.

## Funcionalidades Principais

-   **Coleta de Notícias**: Faz requisições ao feed RSS do Google Notícias com base em termos de pesquisa personalizados.
-   **Análise de Sentimento**: Utiliza um modelo de Processamento de Linguagem Natural (PLN) pré-treinado do Hugging Face (BERT para português) para classificar o sentimento das notícias.
-   **Visualização de Dados**: Um dashboard interativo construído com Streamlit exibe os dados em:
    -   Um gráfico de pizza mostrando a distribuição de sentimentos.
    -   Uma nuvem de palavras com os termos mais frequentes.
    -   Uma tabela interativa com os dados brutos das notícias.

## Estrutura do Projeto

├── doc/
│ └── DECISIONS.md # Documento com as principais decisões de design e arquitetura.

├── requirements.txt # Dependências do projeto.

├── src/
│ ├── abstrato/
│ │ └── Interfaces.py # Classes abstratas (interfaces) que definem a arquitetura SOLID.
│
│ ├── analise/
│ │ ├── Analisador_regras.py # Implementação da análise de sentimento baseada em regras.
│ │ └── Analisador_transformer.py # Implementação da análise de sentimento com BERT.
│
│ ├── coleta/
│ │ └── Coletor_rss.py # Implementação do coletor de notícias via RSS.
│
│ ├── processamento/
│ │ ├── Limpador_texto.py # Classe para pré-processamento e limpeza de texto.
│ │ └── Orquestrador_noticias.py # Classe de alto nível que orquestra o fluxo de dados.
│
│ └── app.py # Script principal para iniciar o dashboard Streamlit.

└── README.md # Documentação principal do projeto.


## Como Usar

Siga os passos abaixo para configurar e executar o projeto.

### 1. Pré-requisitos

Certifique-se de ter o Python 3.7 ou superior instalado.

### 2. Instalação das Dependências

Instale todas as bibliotecas necessárias usando o arquivo `requirements.txt`:

- pip install -r requirements.txt

### 3. Execução do Dashboard

Após a instalação, inicie o dashboard com o Streamlit. Certifique-se de estar no diretório raiz do projeto.

- streamlit run src/app.py

Um navegador abrirá automaticamente com o dashboard em execução. Você pode então digitar os termos de busca e clicar em "Analisar Notícias" para ver os resultados.
