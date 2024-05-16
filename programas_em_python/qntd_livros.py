qntdLivros =int(input("Quantos Livros precisam ser embalados? Digite:"))
qntLivrosEmbalados = 0
i=  qntdLivros
while (i >= 0):
    qntLivrosEmbalados  = qntdLivros - i
    qntLivrosSeremEmbalados = qntdLivros -  qntLivrosEmbalados
    print (qntLivrosEmbalados, "embalado e ", qntLivrosSeremEmbalados,"a serem embalados" )
    i-= 1