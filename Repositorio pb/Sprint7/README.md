## Minhas anotações dos cursos de hadoop e de spark

# hadoop e map reduce

Aqui está uma organização do texto em tópicos principais com explicações:

- **Distributed Computing**:
    - Descreve como a computação distribuída é uma abordagem melhor para processar grandes volumes de dados, permitindo o uso de vários servidores para reduzir o tempo de processamento e proporcionar escalabilidade quase ilimitada.
- **Hadoop**:
    - Introdução ao Hadoop como um framework de computação distribuída mantido pela Apache Software Foundation. É gratuito, open source e desenvolvido em Java.
- **Partes do Hadoop**:
    - Descrição das duas partes principais do Hadoop:
        - **HDFS (Hadoop Distributed File System)**: Sistema de arquivos distribuído para armazenar dados em múltiplos servidores.
        - **MapReduce**: Framework para processar dados em múltiplos servidores, dividido em duas partes: MapReduce e YARN.
- **HDFS (Hadoop Distributed File System)**:
    - Detalhamento do funcionamento do HDFS, incluindo a estrutura de nós (name node e data nodes), divisão de arquivos em blocos, replicação de dados para tolerância a falhas e distribuição de blocos entre os nós.
- **MapReduce**:
    - Explicação do processo de processamento de dados pelo MapReduce, com as fases de mapeamento e redução. Destaca a abstração fornecida pelo Hadoop para simplificar a alocação de recursos.
- **YARN (Yet Another Resource Negotiator)**:
    - Descrição do YARN como o framework responsável por monitorar falhas, alocar recursos e executar trabalhos MapReduce em múltiplos nós.
- **Exemplo de Uso do Hadoop com MapReduce**:
    - Demonstração de como contar o número de vezes que cada palavra aparece em um arquivo, utilizando o Hadoop. Descreve as etapas de mapeamento, ordenação/combinação e redução.
- **Desenvolvimento no Hadoop**:
    - Explicação de como desenvolver programas MapReduce no Hadoop, utilizando Java ou outras linguagens com APIs apropriadas. Destaca as classes base fornecidas pelo Hadoop, como Mapper e Reducer, e a criação de arquivos JAR para distribuição.
- **Tipos de Dados e Classes Básicas do Hadoop**:
    - Descrição dos tipos de dados básicos do Hadoop, como LongWritable, Text e IntWritable, e a utilização de classes base como Mapper e Reducer.
- **Funcionamento da Função Map e Reduce**:
    - Detalhamento dos parâmetros e funcionamento das funções map e reduce, incluindo o uso do contexto para comunicação entre as etapas do MapReduce.
- **Configuração da Função Reducer**:
    - Explicação sobre como configurar a classe Reducer, especificando os tipos de dados da chave e do valor, e lidar com diferentes tipos de entrada.
- **Desenvolvimento de Programas MapReduce**:
    - Descrição dos passos necessários para desenvolver e executar programas MapReduce no Hadoop, incluindo a especificação de caminhos de entrada e saída, e a verificação de parâmetros passados.

Essa organização facilita a compreensão e a referência aos diferentes aspectos do Hadoop e do desenvolvimento de programas MapReduce no ambiente Hadoop.

# Spark

### Introdução ao Spark

- **Spark**: Ferramenta de processamento de dados massivos distribuído em cluster.
- **Replicação**: Para tolerância a falhas durante o processamento.
- **Desenvolvimento**: Inicialmente desenvolvido com Scala, mas pode ser usado com outras linguagens.

### Componentes do Spark

- **Machine Learning (MLlib)**: Biblioteca para processamento de aprendizado de máquina.
- **Spark SQL**: Permite ler dados tabulares de várias fontes com SQL.
- **Processamento de dados em streaming**: Capacidade de processamento de fluxos contínuos de dados.
- **Processamento de Grafos (GraphX)**: Componente para processamento de grafos.

### Estrutura do Spark

- **Driver**: Inicializa SparkSession, solicita recursos do cluster manager e distribui operações em grafos (DAGs) para executores.
- **Cluster Manager**: Gerencia os recursos do cluster (Built-in standalone, YARN, Mesos, Kubernetes).
- **Executor**: Executa as tarefas em cada nó do cluster.

### Principais Conceitos do Spark

- **Data Frame**: Principal estrutura de dados, imutável. Uma transformação gera um novo data frame.
- **Lazy Evaluation**: Processamento das transformações ocorre apenas quando há uma ação.
- **Grafo Acíclico Direcionado (DAG)**: Utilizado pelo Spark para representar operações.

### Tipos de Transformações

- **Narrow**: Quando os dados estão em uma mesma partição.
- **Wide**: Quando os dados estão em mais de uma partição.

### Principais Componentes e Utilidades

- **SparkContext**: Fornecer conexão transparente com o cluster.
- **SparkSession**: Dá acesso ao SparkContext.
- **Formatos de Dados**: Parquet, Avro, ORC, escolhidos de acordo com as necessidades de escrita e leitura.
- **RDD (Resilient Distributed Datasets)**: Estrutura básica de baixo nível, imutável e distribuída.
- **Dataset e DataFrame**: Semelhantes a uma tabela de banco de dados, compatíveis com Pandas.

### Manipulação e Processamento de Dados

- **Ações em DataFrame**: Operações como `show`, `take`, `collect`, `count`.
- **Exportação e Importação de Dados**: Utilizando comandos `write` e `load`.
- **Spark SQL**: Cria um ambiente de banco de dados no Spark, com tabelas gerenciadas e não gerenciadas.
- **Joins**: Operações para unir DataFrames.
- **Spark-SQL**: Shell alternativo para executar SQL puro no Spark.

### Desenvolvimento e Aplicativos

- **Programação e Execução**: Desenvolvimento de aplicativos utilizando `spark-submit`.
- **Argumentos de Linha de Comando**: Personalização de aplicativos para entrada e saída de dados.
- **Particionamento e Bucketing**: Estratégias para armazenamento e processamento paralelo.
- **Cache e Persist**: Otimização de desempenho com persistência de dados.

### Interação com Pandas

- **Conversão de DataFrame**: Utilização de `createDataFrame` e `toPandas` para interação com Pandas.