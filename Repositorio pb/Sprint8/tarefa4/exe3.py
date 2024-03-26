from pyspark.sql import SparkSession
from pyspark.sql.functions import rand, when

# Inicialize a SparkSession
spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Exercicio Intro") \
    .getOrCreate()

# Carregue o arquivo nomes_aleatorios.txt em um DataFrame chamado df_nomes
df_nomes = spark.read.csv("nomes_aleatorios.txt", header=False)

# Renomeie a coluna para "Nomes"
df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")

# Adicione a nova coluna "Escolaridade" com valores aleatórios
df_nomes_com_escolaridade = df_nomes.withColumn("Escolaridade", 
                        when(rand() < 0.33, "Fundamental")
                        .when(rand() < 0.66, "Médio")
                        .otherwise("Superior"))

# Mostre 10 linhas do DataFrame com as colunas Nomes e Escolaridade
df_nomes_com_escolaridade.show(10, False)
