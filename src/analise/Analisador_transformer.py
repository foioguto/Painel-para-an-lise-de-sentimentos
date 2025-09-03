from src.Interfaces import Analisador_sentimento
from transformers import pipeline

class Analisador_transformer(Analisador_sentimento):
    """
    Analisa o sentimento usando um modelo pré-treinado do Hugging Face.
    """
    def __init__(self, model_name="neuralmind/bert-base-portuguese-cased"):
        self.classifier = pipeline("sentiment-analysis", model=model_name)

    def analisar(self, texto: str):
        if not texto:
            return "Neutro"
        
        result = self.classifier(texto)[0]
        label = result['label'].lower()
        
        if "negativo" in label:
            return "Negativo"
        elif "positivo" in label:
            return "Positivo"
        else:
            return "Neutro"
