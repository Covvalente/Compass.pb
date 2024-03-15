from pyspark.sql import SparkSession

# Inicializar uma sessão Spark
spark = SparkSession.builder \
    .appName("Contagem de Palavras") \
    .getOrCreate()

# Carregar o arquivo README.md
lines = spark.read.text("/home/jovyan/work/README.md").rdd.map(lambda r: r[0])

# Dividir as linhas em palavras
words = lines.flatMap(lambda line: line.split())

# Contar a ocorrência de cada palavra
wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)

# Exibir os resultados
for word, count in wordCounts.collect():
    print(f"{word}: {count}")

# Encerrar a sessão Spark
spark.stop()
