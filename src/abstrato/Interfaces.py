from abc import ABC, abstractmethod


class Coletor_noticias(ABC):
    """Abstração para coleta de notícias."""
    @abstractmethod
    def coletar(self, termo: str):
        pass
    
class Processador_texto(ABC):
    """Abstração para a limpeza de texto."""
    @abstractmethod
    def processar(self, texto: str):
        pass

class Analisador_sentimento(ABC):
    """Abstração para a análise de sentimento."""
    @abstractmethod
    def analisar(self, texto: str):
        pass