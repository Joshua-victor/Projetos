from Generator import GerarSenha

print("===========================================")
print("            Gerador de Senhas")
print("===========================================\n")



quantidade = (int(input("Qual a quantidade de senhas você deseja? ")))
tamanho = int(input("\nQual o tamanho da senha você deseja? "))

senha = []

GerarSenha(senha, quantidade, tamanho)


