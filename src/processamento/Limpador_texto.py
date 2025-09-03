# Limpador_texto.py
from src.Interfaces import Processador_texto
from bs4 import BeautifulSoup
import re

class Limpador_texto(Processador_texto):
    """
    Processador de texto que remove apenas o necessário.
    Preserva a pontuação e estrutura para análise por modelos de PLN.
    """
    def processar(self, texto: str) -> str:
        """
        Limpa o texto removendo tags HTML e normalizando espaços.
        """
        if not texto:
            return ""

        # 1. Remove tags HTML
        soup = BeautifulSoup(texto, "html.parser")
        texto_limpo = soup.get_text()

        # 2. Normaliza espaços: substitui múltiplos espaços por um único
        texto_limpo = re.sub(r'\s+', ' ', texto_limpo).strip()
        
        return texto_limpo