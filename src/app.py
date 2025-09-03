import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re

from processamento.Orquestrador_noticias import Orquestrador_noticias
from coleta.Coletor_rss import Coletor_rss
from processamento.Limpador_texto import Limpador_texto
from analise.Analisador_regras import Analisador_regras
from abstrato.Interfaces import Analisador_sentimento, Coletor_noticias, Processador_texto

# --- Funções de Preparação de Dados ---

@st.cache_data
def carregar_dados_e_analisar(termo_de_busca, max_noticias=20):
    """
    Função que orquestra a coleta e análise de notícias.
    Usa caching para evitar recarregamento desnecessário.
    """
    # Instancia as classes com base nas suas implementações
    coletor = Coletor_rss()
    limpador = Limpador_texto()
    analisador = Analisador_regras(
        palavras_positivas=["melhora", "crescimento", "sucesso", "inovação", "avanço"],
        palavras_negativas=["problema", "dificuldade", "falha", "crise", "prejuízo"]
    )

    orquestrador = Orquestrador_noticias(coletor, limpador, analisador)
    items = orquestrador.coletor.coletar(termo_de_busca.replace(" ", "+"))
    
    dados = []
    noticias_processadas = 0
    for item in items:
        if noticias_processadas >= max_noticias:
            break
        
        titulo_raw = item.find('title').text if item.find('title') is not None else ""
        link = item.find('link').text if item.find('link') is not None else ""
        descricao_raw = item.find('description').text if item.find('description') is not None else ""
        
        titulo_limpo = limpador.processar(titulo_raw)
        descricao_limpa = limpador.processar(descricao_raw)
        sentimento = analisador.analisar(descricao_limpa)
        
        dados.append({
            'Título': titulo_limpo,
            'Link': link,
            'Sentimento': sentimento
        })
        noticias_processadas += 1
    
    return pd.DataFrame(dados)

# --- Configuração do Dashboard ---

st.set_page_config(
    page_title="Monitoramento de Percepção Pública - Piauí",
    layout="wide",
)

st.title("Dashboard de Análise de Notícias")
st.markdown("Analise o sentimento e a frequência de termos em notícias sobre o Piauí.")

# Barra de pesquisa na barra lateral
st.sidebar.header("Configurações")
termo_pesquisa = st.sidebar.text_input("Digite o termo de busca:", "Inteligência Artificial Piauí")

if st.button("Analisar Notícias"):
    if termo_pesquisa:
        st.subheader(f"Resultados para: **{termo_pesquisa}**")
        
        df_noticias = carregar_dados_e_analisar(termo_pesquisa)
        
        if not df_noticias.empty:
            # --- 1. Gráfico de Pizza (Distribuição de Sentimentos) ---
            st.markdown("---")
            st.header("Distribuição de Sentimento")
            sentimentos_counts = df_noticias['Sentimento'].value_counts().reset_index()
            sentimentos_counts.columns = ['Sentimento', 'Quantidade']
            
            fig_pie = px.pie(sentimentos_counts, names='Sentimento', values='Quantidade', 
                             title='Distribuição de Sentimentos das Notícias',
                             color='Sentimento',
                             color_discrete_map={'Positivo':'green', 'Negativo':'red', 'Neutro':'blue'})
            st.plotly_chart(fig_pie, use_container_width=True)

            # --- 2. Tabela Interativa ---
            st.markdown("---")
            st.header("Dados Detalhados das Notícias")
            st.dataframe(df_noticias, use_container_width=True)
            
            # --- 3. Nuvem de Palavras ---
            st.markdown("---")
            st.header("Nuvem de Palavras-Chave")
            
            # Concatena todos os títulos e descrições para a nuvem de palavras
            texto_completo = " ".join(df_noticias['Título'])
            
            # Remove palavras comuns (stop words)
            stop_words = ["de", "do", "da", "em", "o", "a", "e", "para", "com", "por", "que", "uma", "um", "no", "na"]
            palavras = texto_completo.split()
            texto_processado = " ".join([word for word in palavras if word.lower() not in stop_words])

            # Gera a nuvem de palavras
            wordcloud = WordCloud(width=800, height=400, background_color='white').generate(texto_processado)
            
            plt.figure(figsize=(10, 5))
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis("off")
            st.pyplot(plt)
            
        else:
            st.warning("Não foi possível encontrar notícias para este termo de busca.")
            
    else:
        st.error("Por favor, digite um termo de busca.")

st.markdown("""
**Aviso sobre a Análise de Sentimento:**
A análise de sentimento utiliza um modelo de PLN (Processamento de Linguagem Natural) pré-treinado. Embora seja robusto, o modelo pode ter limitações e não deve ser considerado infalível. O resultado serve como uma indicação da polaridade do texto.
""")

# --- Identificando código gerado por IA ---

st.markdown("---")
st.markdown("""
#### Sobre este Projeto
Partes deste código foram desenvolvidas com o auxílio de um modelo de inteligência artificial. O modelo foi utilizado como um assistente para aprimorar a arquitetura (p. ex., aplicação de princípios SOLID), otimizar design e gerar documentação.
""")