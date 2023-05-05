
def jogar():
    print("####")
    
    secret_word = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]
    enforcou = False
    acertou = False
    count=0
    tentativas=6
    erros=0
    repetidos=0
    
    print(letras_acertadas)


   
    while(not enforcou and not acertou and count<6):
        chute = input("Qual letra? ")
        chute = chute.strip()

        index = 0

        if(chute in letras_acertadas):
            repetidos+=1
            print('Você já tentou {} vezes esta letra'.format(repetidos))


        if(chute in secret_word):
            for letra in secret_word:
                    if(chute.upper() == letra.upper()):
                        letras_acertadas[index] = letra
                    index = index + 1
                    letras_faltando = str(letras_acertadas.count('_'))
               
        else:
            erros+=1
        
        enforcou = erros == 6
                
        count+=1
        tentativas-=1

        if("_" not in letras_acertadas):
            print("Acertou")
            break
        print(letras_acertadas)
        print('Ainda faltam acertar {} letras'.format(letras_faltando))
        print('Você tentou {} vezes'.format(count))
        print('Você errou {} vezes'.format(erros))
        print('Você somente pode tentar mais {} vezes'.format(tentativas))


if(__name__ == "__main__"):
    jogar()
 






