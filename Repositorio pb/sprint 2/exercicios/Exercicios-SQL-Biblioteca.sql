-- ex1 
SELECT * --- As colunas pedidas são iguais as originais da tabela
FROM livro
WHERE publicacao  > '2014-12-31'
ORDER BY cod ASC

-- ex2
select titulo,valor
from livro
order by valor desc
limit 10 

-- ex3
SELECT COUNT(*) as quantidade, edi.nome, en.estado, en.cidade
FROM livro AS li
--- Faz a ligação com a tabela editora e endereço para pegar os dados de cidade e estado das editoras
LEFT JOIN editora AS edi
	ON li.editora  = edi.codeditora 
LEFT JOIN endereco en 
	ON edi.endereco = en.codendereco 
GROUP BY edi.nome, en.estado, en.cidade
ORDER BY quantidade DESC 
LIMIT 5

-- ex4  
SELECT au.nome, au.codautor, au.nascimento, COUNT(li.cod) AS quantidade --- Conta a quantidade de livros da tabela livros relacionado a cada autor da tabela autor
FROM autor AS au
LEFT JOIN livro AS li
	ON li.autor = au.codautor 
GROUP BY au.nome, au.codautor, au.nascimento 
ORDER BY au.nome ASC -- Ordena alfabeticamente

-- ex5

SELECT DISTINCT au.nome
FROM autor AS au
LEFT JOIN livro AS li
    ON au.codautor = li.autor 
LEFT JOIN editora AS edi
    ON li.editora = edi.codeditora 
LEFT JOIN endereco AS en
    ON edi.endereco = en.codendereco 
WHERE en.estado NOT IN ('PARANÁ', 'SANTA CATARINA', 'RIO GRANDE DO SUL')
ORDER BY au.nome ASC;

-- ex6

SELECT au.codautor, au.nome, COUNT(*) AS quantidade_publicacoes --- Conta todos os livros por autor
FROM livro AS li
LEFT JOIN autor AS au 
	ON li.autor = au.codautor 
GROUP BY au.codautor, au.nome
ORDER BY quantidade_publicacoes DESC --- Lista do mais caro ao mais barato
LIMIT 1 --- Limita ao primeiro mais caro

-- ex7

SELECT nome
FROM autor AS au
LEFT JOIN livro AS li 
	ON au.codautor = li.autor
WHERE li.autor IS NULL --- Mostra apenas os autores que não tem correspondentes na tabela livros
ORDER BY autor ASC