import logging
import boto3
from botocore.exceptions import ClientError
import os

# As chaves de acesso são acessadas por variáveis de ambiente (com docker pelo arquivo .env)
s3_client = boto3.client(
        's3', 
        aws_access_key_id=os.environ['AWS_ACCESS_KEY'], 
        aws_secret_access_key=os.environ['AWS_SECRET_KEY'], 
        aws_session_token=os.environ['AWS_SESSION_TOKEN'],
        region_name='us-east-1')

def upload_file(origem, bucket, destino):
    # tenta fazer o upload do arquivo no bucket, retorna True se der certo
    try:
        response = s3_client.upload_file(origem, bucket, destino)
    except ClientError as e:
        logging.error(e)
        return False
    return True

print(upload_file('./movies.csv', 's20', 'Raw/Local/CSV/Movies/2024/03/15/movies.csv'))
print(upload_file('./series.csv', 's20', 'Raw/Local/CSV/Series/2024/03/15/series.csv'))
