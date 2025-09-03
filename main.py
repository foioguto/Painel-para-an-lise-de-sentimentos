from Coletor_rss import Coletor_rss
from Limpador_texto import Limpador_texto
from Analisador_regras import Analisador_regras
from Orquestrador_noticias import Orquestrador_noticias
from Analisador_transformer import Analisador_transformer


if __name__ == "__main__":
    # --- 3. Princípio da Substituição de Liskov (LSP) ---
    # As classes concretas podem ser substituídas por suas abstrações.
    
    # Instancia as implementações concretas.
    coletor_rss = Coletor_rss()
    limpador = Limpador_texto()

    analisador_avancado = Analisador_transformer()
    # Injeção de dependências no orquestrador.
    orquestrador = Orquestrador_noticias(coletor_rss, limpador, analisador_avancado)
    
    # Executa a análise para diferentes termos.
    termos = ["Inteligência Artificial Piauí", "SIA Piauí"]
    for termo in termos:
        orquestrador.executar_analise(termo.replace(" ", "+"))
        print("\n" + "="*80 + "\n")

