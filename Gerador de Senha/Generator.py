import random
def GerarSenha(senha, quantidade, tamanho):
    
    Minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    Maiusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    caracteres_especiais = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|',':', ';','<', '>', ',', '.', '?', '/']
    teste = 0
    for i in range(quantidade):
        
        while True:
    
            senha.append(random.choice(Minusculas))
            teste += 1
            if teste >= tamanho:
                break
            senha.append(random.choice(Maiusculas))
            teste += 1
            if teste >= tamanho:
                break
            senha.append(random.choice(numeros))
            teste += 1
            if teste >= tamanho:
                break
            senha.append(random.choice(caracteres_especiais))
            teste += 1
            if teste >= tamanho:
                break
    
    
        random.shuffle(senha)
        print("Sua senha é: " + "".join(str(c) for c in senha))