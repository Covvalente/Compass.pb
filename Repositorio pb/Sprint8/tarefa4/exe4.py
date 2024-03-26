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

# Defina a lista de países da América do Sul
paises_americadosul = ["Brasil", "Argentina", "Chile", "Colômbia", "Uruguai", "Paraguai", "Equador", "Venezuela", "Bolívia", "Peru", "Suriname", "Guiana", "Guiana Francesa"]

# Adicione a nova coluna "Pais" com valores aleatórios dos países da América do Sul
df_nomes_com_pais = df_nomes_com_escolaridade.withColumn("Pais", 
                        when((rand() * 100).cast("int") < 100 / len(paises_americadosul), paises_americadosul[0])
                        .when((rand() * 100).cast("int") < 100 / len(paises_americadosul) * 2, paises_americadosul[1])
                        .when((rand() * 100).cast("int") < 100 / len(paises_americadosul) * 3, paises_americadosul[2])
                        .when((rand() * 100).cast("int") < 100 / len(paises_americadosul) * 4, paises_americadosul[3])
                        .when((rand() * 100).cast("int") < 100 / len(paises_americadosul) * 5, paises_americadosul[4])
                        .when((rand() * 100).cast("int") < 100 / len(paises_americadosul) * 6, paises_americadosul[5])
                        .when((rand() * 100).cast("int") < 100 / len(paises_americadosul) * 7, paises_americadosul[6])
                        .when((rand() * 100).cast("int") < 100 / len(paises_americadosul) * 8, paises_americadosul[7])
                        .when((rand() * 100).cast("int") < 100 / len(paises_americadosul) * 9, paises_americadosul[8])
                        .when((rand() * 100).cast("int") < 100 / len(paises_americadosul) * 10, paises_americadosul[9])
                        .when((rand() * 100).cast("int") < 100 / len(paises_americadosul) * 11, paises_americadosul[10])
                        .when((rand() * 100).cast("int") < 100 / len(paises_americadosul) * 12, paises_americadosul[11])
                        .otherwise(paises_americadosul[12]))

# Selecione as colunas na ordem desejada
df_final = df_nomes_com_pais.select("Nomes", "Escolaridade", "Pais")

# Mostre o DataFrame resultante
df_final.show(10, False)
