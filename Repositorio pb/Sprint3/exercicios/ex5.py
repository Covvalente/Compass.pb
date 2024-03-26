import datetime 

dia =22
mes =10
ano = 2022

data = datetime.datetime(ano,mes,dia)

data_formatada=data.strftime('%d/%m/%Y')

print (data_formatada)