# Decisões de Design e Arquitetura do Projeto de Monitoramento de Notícias

## 1. Por que a Análise de Sentimento com o Modelo BERT?

A análise de sentimento com o modelo **BERT** foi escolhida em detrimento de uma abordagem baseada em regras simples para garantir maior precisão e profundidade na análise.

### Capacidade de Entendimento de Contexto
Diferentemente de uma análise por regras, que apenas busca palavras-chave, o **BERT** é um modelo de **Processamento de Linguagem Natural (PLN)** que entende o contexto e a relação entre as palavras em uma frase.  
Isso permite que ele identifique sentimentos de forma mais precisa, capturando nuances como **ironia** e **sarcasmo**.

### Robustez e Abrangência
O modelo **neuralmind/bert-base-portuguese-cased** foi treinado com um vasto corpus de textos em português.  
Isso o torna mais robusto para lidar com o vocabulário variado de notícias sobre diferentes temas, minimizando a dependência de listas de palavras-chave fixas.

### Flexibilidade e Escalabilidade
A arquitetura do projeto, baseada em **princípios SOLID**, facilitou a integração do modelo BERT.  
A abstração `AnalisadorDeSentimento` permitiu que a implementação do BERT fosse injetada no sistema **sem modificar as outras partes do código**.  
Isso demonstra a capacidade do projeto de evoluir de uma solução mais simples para uma mais complexa, mantendo a integridade da estrutura.

---

## 2. Tratamento de Erros e Falta de Notícias

Para garantir a robustez do sistema, as seguintes estratégias foram implementadas para lidar com falhas de requisição e ausência de dados:

### Tratamento de Exceções
No módulo `Coletor_rss.py`, a requisição para o feed RSS está dentro de um bloco **try-except**.  
Isso captura erros comuns como:
- falhas de conexão (`requests.exceptions.RequestException`),  
- problemas no formato XML da resposta (`ET.ParseError`).  

Em caso de erro, o código **não falha**: ele apenas imprime uma mensagem de erro e retorna uma **lista vazia**, permitindo que o restante do programa continue sua execução.

### Validação de Dados
O `Orquestrador_noticias.py` e o dashboard no `app.py` verificam se a lista de notícias retornada pelo coletor está vazia.  
Se nenhum dado for encontrado, o sistema exibe uma **mensagem amigável** para o usuário:  
*"Não foi possível encontrar notícias..."*  
Em vez de quebrar ou exibir um gráfico vazio.

### Modularidade da Arquitetura
A separação das responsabilidades em módulos (**Coletor, Limpador, Analisador**) permite que um erro em um componente **não afete o sistema como um todo**.  
Por exemplo, se a coleta falhar, o **Orquestrador** lida com o resultado (lista vazia) e o resto do sistema não é comprometido.
