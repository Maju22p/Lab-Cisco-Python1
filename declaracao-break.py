# Programa: Loop 
# Autor: Maria Julia Souza
# Descrição:
# Programa no qual é um loop infinito e o usuário precisa digitar uma palavra certa para
#quebrar o loop
#Objetivo : testar a compreensão da declaração do break

#Estrutura do loop infinito
while True :
    #Mensagem de inicio
    print("Você está preso em um Loop!")
    #Solicita a palavra chave para sair do loop
    palavra = str(input("Digite uma palavra: "))
    #Compara a palavra digitada pelo o usuário com a palavra chave
    if palavra == "chupacabra":
        #Quebra do loop infinito
        break
    #Mensagem final
print("Você saiu do loop com sucesso")