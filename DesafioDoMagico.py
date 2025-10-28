# Programa: Jogo do Número Secreto 
# Autor: Maria Julia Souza
# Descrição:
# Um jovem mágico escolheu um número secreto.
# O usuário deve tentar adivinhá-lo até acertar.
# Enquanto errar, ficará "preso" em um loop.
#Objetivo : testar a compreensão do While

# Número secreto escolhido pelo mágico
secret_number = 777

#Mensagem de boas vindas do mago
print(
"""
+===================================+
| Bem vindo ao meu jogo, trouxa!    |
| Insira um número inteiro          |
| e adivinhar o número que tenho    |
| escolhidos para você.             |
| Então, qual é o número secreto?   |
+===================================+
""")
#Primeira tentativa do usuário
resp = int(input("Insira o  numero secreto: "))

# Enquanto o número digitado for diferente do secreto...
while resp != secret_number:
    print("Ha ha! Você está preso no meu loop!")
    # Pede outro número ao jogador
    resp = int(input("Tente novamente: "))
    
# Quando o número estiver correto
print("Muito bem, trouxa! Você está livre agora.")

"""
 Enunciado:
Um jovem mágico escolheu um número secreto. Ele o ocultou em uma variável chamada secret_number.
O programa deve:
- Pedir que o usuário insira um número inteiro;
- Usar um laço while para manter o jogador tentando até acertar;
- Exibir uma mensagem divertida enquanto o usuário erra;
- Liberar o jogador quando ele adivinhar o número correto.
"""