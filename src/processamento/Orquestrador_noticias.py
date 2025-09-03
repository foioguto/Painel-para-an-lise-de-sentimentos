import abstrato.Interfaces as Interfaces

class Orquestrador_noticias:
    """
    Classe de alto nível que orquestra o processo.
    Depende de abstrações e não de implementações concretas.
    """
    def __init__(self, coletor: Interfaces.Coletor_noticias, processador: Interfaces.Processador_texto, analisador: Interfaces.Analisador_sentimento):
        self.coletor = coletor
        self.processador = processador
        self.analisador = analisador

    def executar_analise(self, termo: str, max_noticias: int = 15):
        items = self.coletor.coletar(termo)
        
        noticias_processadas = 0
        for item in items:
            if noticias_processadas >= max_noticias:
                break
            
            titulo_raw = item.find('title').text if item.find('title') is not None else ""
            link = item.find('link').text if item.find('link') is not None else ""
            descricao_raw = item.find('description').text if item.find('description') is not None else ""
            
            titulo_limpo = self.processador.processar(titulo_raw)
            descricao_limpa = self.processador.processar(descricao_raw)
            sentimento = self.analisador.analisar(descricao_limpa)
            
            print(f"Título: {titulo_limpo}")
            print(f"Link: {link}")
            print(f"Sentimento: {sentimento}")
            print("-" * 50)
            noticias_processadas += 1
        
        print(f"\nTotal de notícias processadas: {noticias_processadas}")
