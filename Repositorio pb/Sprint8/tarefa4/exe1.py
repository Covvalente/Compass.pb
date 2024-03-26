from pyspark.sql import SparkSession

# Inicializa a Spark Session
spark = SparkSession \
    .builder \
    .appName("Exercicio Intro") \
    .master("local[*]") \
    .getOrCreate()

# Lê o arquivo nomes_aleatorios.txt e cria um DataFrame
df_nomes = spark.read.csv("nomes_aleatorios.txt", header=False)

# Exibe algumas linhas do DataFrame
df_nomes.show(5)
