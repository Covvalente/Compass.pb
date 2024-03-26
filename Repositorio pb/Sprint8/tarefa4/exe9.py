from pyspark.sql import SparkSession
from pyspark.sql.functions import rand

# Inicialize a SparkSession
spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Exercicio Intro") \
    .getOrCreate()

# Carregue o arquivo nomes_aleatorios.txt em um DataFrame chamado df_nomes
df_nomes = spark.read.csv("nomes_aleatorios.txt", header=False)

# Renomeie a coluna para "Nomes"
df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")

# Adicione uma coluna de ano de nascimento aleatório entre 1945 e 2010
df_nomes_com_ano_nascimento = df_nomes.withColumn("AnoNascimento", (rand() * (2010 - 1945 + 1) + 1945).cast("int"))

# Registre o DataFrame como uma tabela temporária
df_nomes_com_ano_nascimento.createOrReplaceTempView("pessoas")

# Execute a consulta SQL para contar o número de pessoas da geração Millennials
df_millennials = spark.sql("""
    SELECT COUNT(*) AS Total_Millennials 
    FROM pessoas 
    WHERE AnoNascimento BETWEEN 1980 AND 1994
""")

# Mostre o resultado
df_millennials.show()
