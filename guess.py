
def jogar():
    print("####")
    
    secret_word = "banana"
    enforcou = False
    acertou = False
    
    index = 0
    while(not enforcou and not acertou):
        chute = input("Qual letra? ")
        
        for letra in secret_word:
            if(chute.upper() == letra.upper()):
                print("Encontrou {} na posicao {}".format(chute, index))
            index = index + 1
        
        print("jogando")
        
    prin("Fim")
        

if(__name__ == "__main__"):
    jogar()
