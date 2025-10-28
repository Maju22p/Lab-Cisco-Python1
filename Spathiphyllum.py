# Programa: Verifica o nome da planta Spathiphyllum
# Autor: Maria Julia
# Descrição:
# O programa lê uma string e compara com o nome da planta "Spathiphyllum".
# Dependendo da forma escrita (maiúscula, minúscula ou diferente),
# ele retorna uma mensagem específica.

#Solicita o nome da planta ao usuario
resp = str(input("O nome da planta é..."))

# Caso o usuário digite exatamente "Spathiphyllum" (com S maiúsculo)
if resp == "Spathiphyllum":
    print("Sim - Spathiphyllum é a melhor fábrica de todos os tempos!")
    # Caso o usuário digite "spathiphyllum" em minúsculas
elif resp == "spathiphyllum":
    print("Não, eu quero um grande Spathiphyllum!")
    # Caso o usuário digite qualquer outro nome
else:
    print("Spathiphyllum! Não",resp,"!")
    # Observação:
# Esse exercício faz parte de um laboratório de condicionais simples em Python.
# É um exemplo básico, mas importante para entender comparações de strings
# e blocos de decisão com if, elif e else.
