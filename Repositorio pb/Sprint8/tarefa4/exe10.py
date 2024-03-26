from pyspark.sql import SparkSession
from pyspark.sql.functions import expr, rand, when

# Inicialize a SparkSession
spark = SparkSession.builder \
    .master("local[*]") \
    .appName("CountPeopleByCountryAndGeneration") \
    .getOrCreate()

# Carregue os dados do arquivo de texto para um DataFrame Spark
# Supondo que cada linha do arquivo de texto contenha dados de uma pessoa no formato (Pais, AnoNascimento)
df_pessoas = spark.read.text("nomes_aleatorios.txt")

# Divida cada linha em colunas usando a vírgula como delimitador
df_pessoas = df_pessoas.selectExpr("split(value, ',') as data").selectExpr("data[0] as Nome", "cast(data[1] as int) as AnoNascimento")

# Lista de países da América do Sul
paises_americadosul = ["Brasil", "Argentina", "Chile", "Colômbia", "Uruguai", "Paraguai", "Equador", "Venezuela", "Bolívia", "Peru", "Suriname", "Guiana", "Guiana Francesa"]

# Adicione a nova coluna "Pais" com valores aleatórios dos países da América do Sul
df_pessoas_com_pais = df_pessoas.withColumn("Pais", 
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

# Adicione a nova coluna "AnoNascimento" com valores aleatórios entre 1945 e 2010
df_pessoas_com_pais = df_pessoas_com_pais.withColumn("AnoNascimento", expr("cast(rand() * (2010 - 1945 + 1) + 1945 as int)"))

# Crie uma visualização temporária para poder executar consultas SQL
df_pessoas_com_pais.createOrReplaceTempView("pessoas")

# Defina a query SQL para contar a quantidade de pessoas de cada país para cada geração
query = """
SELECT Pais, 
    CASE
        WHEN AnoNascimento BETWEEN 1945 AND 1964 THEN 'BabyBoomers'
        WHEN AnoNascimento BETWEEN 1965 AND 1979 THEN 'GeracaoX'
        WHEN AnoNascimento BETWEEN 1980 AND 1994 THEN 'GeracaoY/Millenials'
        WHEN AnoNascimento BETWEEN 1995 AND YEAR(CURRENT_DATE()) THEN 'GeracaoZ'
        ELSE 'Geração não identificada'
    END AS Geracao,
    COUNT(*) AS Quantidade 
FROM pessoas 
GROUP BY Pais, Geracao
ORDER BY Pais, Geracao, Quantidade
"""

# Execute a consulta SQL e armazene o resultado em um DataFrame
df_geracao = spark.sql(query)

# Mostrar o resultado
df_geracao.show()

# Encerre a sessão Spark
spark.stop()
