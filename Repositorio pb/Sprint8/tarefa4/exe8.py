from pyspark.sql import SparkSession
from pyspark.sql.functions import rand, expr, col

# Inicialize a SparkSession
spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Contagem de Millennials") \
    .getOrCreate()

# Carregue o arquivo nomes_aleatorios.txt em um DataFrame chamado df_nomes
df_nomes = spark.read.csv("nomes_aleatorios.txt", header=False)

# Renomeie a coluna para "Nomes"
df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")

# Adicione a nova coluna "AnoNascimento" com valores aleatórios entre 1945 e 2010
df_nomes_com_ano_nascimento = df_nomes.withColumn("AnoNascimento", expr("cast(rand() * (2010 - 1945 + 1) + 1945 as int)"))

# Conte o número de pessoas que são da geração Millennials (nascidas entre 1980 e 1994)
millennials_count = df_nomes_com_ano_nascimento.filter((col("AnoNascimento") >= 1980) & (col("AnoNascimento") <= 1994)).count()

print("Número de pessoas da geração Millennials:", millennials_count)
