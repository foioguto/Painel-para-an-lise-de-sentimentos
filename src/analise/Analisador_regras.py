import src.Interfaces as Interfaces

class Analisador_regras(Interfaces.Analisador_sentimento):
    """
    Analisa o sentimento com base em palavras-chave.
    Responsabilidade Única: Apenas análise de sentimento por regras.
    """
    def __init__(self, palavras_positivas, palavras_negativas):
        self.positivas = palavras_positivas
        self.negativas = palavras_negativas

    def analisar(self, texto: str):
        if not texto:
            return "Neutro"
        texto_lower = texto.lower()
        pontuacao = 0
        for palavra in self.positivas:
            if palavra in texto_lower:
                pontuacao += 1
        for palavra in self.negativas:
            if palavra in texto_lower:
                pontuacao -= 1
        if pontuacao > 0:
            return "Positivo"
        elif pontuacao < 0:
            return "Negativo"
        else:
            return "Neutro"
        