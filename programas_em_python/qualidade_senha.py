numero_usuario = int(input("Digite a quantidade de usuarios: "))
for x in range(0,numero_usuario):
    senhas= (input("Digite a senha: "))
    tamanho_de_senha=len(senhas)
    if tamanho_de_senha < 6:
        print("Senha fraca: ")
        
    elif tamanho_de_senha >= 6 and tamanho_de_senha <= 8: 
        print("senha média: ")
    elif tamanho_de_senha > 8: 
        print("senha forte: ")