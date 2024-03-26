from pyspark.sql import SparkSession

# Inicializa a Spark Session
spark = SparkSession \
    .builder \
    .appName("Exercicio Intro") \
    .master("local[*]") \
    .getOrCreate()

# Lê o arquivo nomes_aleatorios.txt e cria um DataFrame
df_nomes = spark.read.csv("nomes_aleatorios.txt", header=False)

# Renomeia a coluna para 'Nomes'
df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")

# Imprime o esquema do DataFrame
df_nomes.printSchema()

# Mostra as primeiras 10 linhas do DataFrame
df_nomes.show(10)
