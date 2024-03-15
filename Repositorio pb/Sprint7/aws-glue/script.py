import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)
source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']
df = glueContext.create_dynamic_frame.from_options(
"s3",
{
"paths": [
source_file
]
},
"csv",
{"withHeader": True, "separator":","},
)

data_frame = df.toDF()
data_frame.printSchema()

from pyspark.sql.functions import upper
data_frame = data_frame.withColumn("nome", upper(data_frame["nome"]))

print("Contagem de Linhas:", data_frame.count())

contagem_nomes = data_frame.groupBy("ano", "sexo").count()
contagem_nomes.show()

data_frame = data_frame.orderBy("ano", ascending=False)

nome_feminino_mais_registros = data_frame.filter(data_frame["sexo"] == "F").groupBy("nome").count().orderBy("count", ascending=False).first()
print("Nome feminino com mais registros:", nome_feminino_mais_registros["nome"])
print("Ano:", data_frame.filter((data_frame["sexo"] == "F") & (data_frame["nome"] == nome_feminino_mais_registros["nome"])).first()["ano"])
nome_masculino_mais_registros = data_frame.filter(data_frame["sexo"] == "M").groupBy("nome").count().orderBy("count", ascending=False).first()
print("Nome masculino com mais registros:", nome_masculino_mais_registros["nome"])
print("Ano:", data_frame.filter((data_frame["sexo"] == "M") & (data_frame["nome"] == nome_masculino_mais_registros["nome"])).first()["ano"])

total_registros_por_ano = data_frame.groupBy("ano").count()
total_registros_por_ano.show()

# Escreva o DataFrame Spark no formato JSON
data_frame.write.json(target_path + "/lab-glue/frequencia_registro_nomes_eua")

data_frame.show(10)

job.commit()