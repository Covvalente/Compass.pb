# Sprint 8

Durante esse sprint, dediquei-me à releitura dos conteúdos da sprint passada para relembrar como fazer certas coisas na AWS. Esta sprint consistiu de exercícios de:

## Exercício TMDB

No exercício 1, comecei criando minha conta no TMDB com o propósito de gerar minha chave de acesso. Em seguida, executei o código fornecido para avançar na atividade.

## Desafio 2

Minha ideia inicial era conseguir o filme de romance mais premiado e o ator de filmes do gênero drama que mais realizou filmagens de filmes de drama. Após os insights de colegas do squad e do próprio instrutor Daniel, resolvi incrementar o tema com dados mais precisos e lógicos e ficou assim:

### Lista 1: Filme de Romance Mais Premiado dos Últimos 20 Anos

1. **Identificar o Filme de Romance Mais Premiado**:
   - Analisar os filmes de romance dos últimos 20 anos e determinar o mais premiado em termos de Oscars, críticas e sucesso de bilheteria.

2. **Orçamento e Lucro do Filme**:
   - Extrair informações sobre o orçamento e a bilheteria do filme escolhido.

3. **Protagonistas Masculino e Feminino**:
   - Identificar os principais atores e atrizes que protagonizaram o filme de romance escolhido.

4. **Diretor e Ano de Lançamento**:
   - Identificar o diretor do filme e o ano de lançamento.

5. **Nota do Filme pelas Críticas**:
   - Analisar a pontuação média do filme com base nas críticas.



## Desenvolvimento de Código e Criação de Conjunto de Dados

Durante esta atividade, segui os seguintes passos:

- **Gerando uma Lista de Inteiros Aleatórios**:
  - Criei uma lista com 250 inteiros aleatórios e inverti sua ordem usando a função reverse.

- **Gerando uma Lista de Nomes de Animais**:
  - Compilei uma lista com 20 nomes de animais, os ordenei alfabeticamente e armazenei-os em um arquivo CSV chamado "nomes_animais.csv".

- **Gerando um Conjunto de Dados de Nomes de Pessoas Aleatórios**:
  - Segui os passos fornecidos no tutorial para criar um conjunto de dados de nomes de pessoas aleatórios, que incluiu a instalação da biblioteca "names". Armazenei esses nomes em um arquivo de texto chamado "nomes_aleatorios.txt" e verifiquei seu conteúdo usando um editor de texto. 

Com essas tarefas concluídas, adicionei os artefatos de código ao meu repositório no GitHub, conforme solicitado.

## Apache Spark

**Passo 1: Preparando o Ambiente**
Primeiramente, preparei o ambiente definindo o diretório onde o código seria desenvolvido e copiando o arquivo "nomes_aleatorios.txt" para esse diretório. Certifiquei-me de ter acesso ao arquivo.

**Passo 2: Importando Bibliotecas e Iniciando a Spark Session**
Em seguida, importei as bibliotecas necessárias do Spark, incluindo SparkSession e SparkContext. Iniciei a Spark Session e defini um contexto SQL para habilitar o processamento de comandos SQL.

**Passo 3: Lendo o Arquivo CSV e Mostrando Algumas Linhas**
Li o arquivo "nomes_aleatorios.txt" usando o comando spark.read.csv e carreguei-o em um DataFrame chamado "df_nomes". Para entender os dados, exibi algumas linhas do DataFrame usando o método show. Isso me ajudou a ter uma visão inicial dos dados.

**Passo 4: Renomeando Colunas e Imprimindo o Schema**
Como o Spark não identificou automaticamente o esquema, renomeei a coluna para "Nomes" usando o método withColumnRenamed. Em seguida, imprimi o schema do DataFrame para entender a estrutura dos dados.

**Passo 5: Adicionando Coluna "Escolaridade" Aleatoriamente**
Adicionei uma nova coluna chamada "Escolaridade" ao DataFrame "df_nomes" com valores aleatórios, como "Fundamental", "Médio" ou "Superior". Certifiquei-me de evitar o uso de iterações e usei métodos do Spark para realizar essa tarefa.

**Passo 6: Adicionando Coluna "Pais" Aleatoriamente**
Da mesma forma, adicionei uma nova coluna chamada "Pais" ao DataFrame "df_nomes" com nomes de países da América do Sul, escolhidos aleatoriamente.

**Passo 7: Adicionando Coluna "AnoNascimento" Aleatoriamente**
Adicionei uma nova coluna chamada "AnoNascimento" ao DataFrame "df_nomes" com valores de ano entre 1945 e 2010, escolhidos aleatoriamente.

**Passo 8: Selecionando Pessoas Nascidas neste Século**
Usei o método select do DataFrame "df_nomes" para selecionar as pessoas que nasceram neste século. Armazenei o resultado em um novo DataFrame chamado "df_select" e exibi 10 nomes deste novo DataFrame.

**Passo 9: Usando Spark SQL para Selecionar Pessoas Nascidas neste Século**
Para realizar a mesma seleção usando Spark SQL, registrei o DataFrame "df_nomes" como
uma tabela temporária, como "pessoas". Em seguida, usei o Spark SQL para selecionar pessoas nascidas neste século e exibir os resultados.

**Passos 10 e 11: Contando Pessoas por Geração e País**
Usando o Spark SQL, obtive a quantidade de pessoas de cada país para diferentes gerações, incluindo Baby Boomers, Geração X, Millennials e Geração Z. Armazenei o resultado em um novo DataFrame e, em seguida, exibi todas as linhas em ordem crescente de país, geração e quantidade.

Esses passos completaram as atividades relacionadas ao Apache Spark durante este sprint.

Com isso, encerrei as atividades planejadas para esta sprint, contribuindo assim para o progresso do projeto.