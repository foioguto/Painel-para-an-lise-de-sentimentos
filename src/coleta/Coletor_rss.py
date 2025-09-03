from abstrato.Interfaces import Coletor_noticias
import requests
import xml.etree.ElementTree as ET


class Coletor_rss(Coletor_noticias):
    """
    Coleta notícias do Google Notícias via RSS.
    Responsabilidade Única: Apenas coleta de dados.
    """
    def coletar(self, termo: str):
        url = f"https://news.google.com/rss/search?q={termo}&hl=pt-BR&gl=BR&ceid=BR:pt-419"
        try:
            response = requests.get(url)
            response.raise_for_status()
            root = ET.fromstring(response.content)
            items = root.findall('./channel/item')
            return items
        except (requests.exceptions.RequestException, ET.ParseError) as e:
            print(f"Erro ao coletar notícias: {e}")
            return []
        