def calcular_valor_maximo(operadores,operandos):
    # função a ser executada no map
    # eval calcula a operação passada em string
    operacao = lambda x: eval(f"{x[1][0]} {x[0]} {x[1][1]}")

    # junta os operadores com operandos através do 'zip', e usa essa lista para fazer os calculos com map
    return max(list(map(operacao, list(zip(operadores, operandos)))))