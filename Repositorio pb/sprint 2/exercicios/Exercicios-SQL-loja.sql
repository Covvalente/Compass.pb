--ex 8
SELECT ven.cdvdd, vdd.nmvdd
FROM tbvendas AS ven
LEFT JOIN tbvendedor AS vdd
	ON ven.cdvdd = vdd.cdvdd 
WHERE status = 'Concluído' -- Seleciona apenas as vendas concluídas para a contagem
GROUP BY ven.cdvdd, vdd.nmvdd -- Agrupa por vendedor
ORDER BY count(ven.cdven) DESC -- Realiza a contagem e ordena pela mais alta
LIMIT 1 -- Limita ao primeiro vendedor com mais venda

--ex 9

SELECT cdpro, nmpro
FROM tbvendas 
WHERE status = 'Concluído' --Seleciona apenas os produtos com status concluído para a contagem
	AND dtven BETWEEN '2014-02-03' AND '2018-02-02' --Seleciona apenas os produtos vendidos entre as datas especificadas
GROUP BY nmpro --Agrupa pelo nome do produto
ORDER BY count(cdpro) DESC --Realiza a contagem do produto e ordena pela mais alta
LIMIT 1 --Limita a contagem 1 contagem mais alta

--ex 10
WITH valor_total_vendas AS ( --Calcula o toal de vendido por cada vendedor (valor unitário * quantidade)
	SELECT cdvdd, SUM(qtd*vrunt) AS valor_total_vendas
	FROM tbvendas 
	WHERE status = 'Concluído' --Somente vendas concluídas
	GROUP BY cdvdd --Agrupa por vendedor
	ORDER BY valor_total_vendas DESC
)

SELECT 
	vdd.nmvdd AS vendedor, 
	vtv.valor_total_vendas, 
	ROUND(vtv.valor_total_vendas*vdd.perccomissao/100, 2) AS comissao --Calcula a comissão (valor de vendas * percentual) e arredonda pra 2 casas decimais
FROM tbvendedor AS vdd
LEFT JOIN valor_total_vendas AS vtv
	ON vdd.cdvdd = vtv.cdvdd
GROUP BY vdd.nmvdd --Agrupa por vendedor
ORDER BY comissao DESC

--ex 11

SELECT 
	cdcli, 
	nmcli, 
	SUM(qtd*vrunt) AS gasto --Soma o total vendido para cada cliente (cada venda é dada por quantidade * valor unitário)
FROM tbvendas 
GROUP BY cdcli, nmcli --Agrupa pelo cliente
ORDER BY gasto DESC --Ordena pelo maior gasto
LIMIT 1

-- ex 12

WITH valor_total_vendas AS ( 
	--Calcula o total de vendas por cada vendedor (valor unitário * quantidade)
	SELECT cdvdd, SUM(qtd*vrunt) AS valor_total_vendas
	FROM tbvendas 
	WHERE status = 'Concluído' --Somente vendas concluídas
	GROUP BY cdvdd --Agrupa por vendedor
	ORDER BY valor_total_vendas ASC
	LIMIT 1 --Limita ao vendedor com menos vendas
)

--Seleciona os dependentes do vendedor com menos vendas
SELECT dep.cddep, dep.nmdep, dep.dtnasc, vtv.valor_total_vendas
FROM tbdependente AS dep
INNER JOIN valor_total_vendas AS vtv
	ON dep.cdvdd  = vtv.cdvdd
GROUP BY dep.cddep, dep.nmdep, dep.dtnasc  --Agrupa por dependente

--ex 13

SELECT 
    cdpro, 
    nmcanalvendas, 
    nmpro, SUM(qtd) AS quantidade_vendas --Soma todas as unidades vendidas de cada produto
FROM tbvendas
WHERE status = 'Concluído' --Apenas vendas concluídas
GROUP BY cdpro, nmcanalvendas, nmpro
ORDER BY quantidade_vendas ASC
LIMIT 10 --Limita aos 10 produtos menos vendidos

--ex 14

SELECT 
	estado, 
	ROUND(AVG(qtd*vrunt), 2) AS gastomedio --Faz a média do valor de cada venda e arredonda
FROM tbvendas 
WHERE status = 'Concluído' --Apenas vendas concluídas
GROUP BY estado --Agrupa por estado
ORDER BY gastomedio DESC --Ordena pelo maior gasto 

--ex 15

SELECT cdven 
FROM tbvendas
WHERE deletado <> 0 --Seleciona as vendas onde o campo "deletado" é true (1)
ORDER BY cdven ASC

--ex 16

SELECT 
	estado,
	nmpro,
	ROUND(AVG(qtd), 4) AS quantidade_media --Calcula a quantidade média vendida de cada produto e arredonda para até 4 casas decimais
FROM tbvendas
WHERE status = 'Concluído' --Seleciona só vendas concluídas 
GROUP BY estado, nmpro --Agrupa por estado e produto
ORDER BY estado, nmpro --Ordena pelo estado e depois pelo produto