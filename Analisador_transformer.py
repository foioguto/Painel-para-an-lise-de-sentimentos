from Interfaces import Analisador_sentimento
from transformers import pipeline

class Analisador_transformer(Analisador_sentimento):
    """
    Analisa o sentimento usando um modelo pré-treinado do Hugging Face.
    """
    def __init__(self, model_name="neuralmind/bert-base-portuguese-cased"):
        # O modelo abaixo é um BERT para português, ideal para o seu caso.
        self.classifier = pipeline("sentiment-analysis", model=model_name)

    def analisar(self, texto: str):
        if not texto:
            return "Neutro"
        
        # O pipeline retorna um dicionário com o rótulo e a pontuação.
        result = self.classifier(texto)[0]
        label = result['label'].lower()
        
        if "negativo" in label:
            return "Negativo"
        elif "positivo" in label:
            return "Positivo"
        else:
            return "Neutro"
