indice = 0

def getNum(text):
    global indice
    flag = True
    num = ''

    while(flag and indice < len(text)):
        if text[indice].isdigit():
            num = num + text[indice]
            indice+=1
 
        else:
            flag = False
    if num== '':
        return 0
    else:    
        return int(num)



def getON(text):
    global indice

    if(indice < len(text)-1):
        if text[indice+1] == 'n' or text[indice+1] == 'N':
            indice += 2
            return True
    else:
        return False

def getOFF(text):
    global indice

    if(indice < len(text)-2):
        if (text[indice+1] == 'f' or text[indice+1] == 'F') and (text[indice+2] == 'f' or text[indice+2] == 'F'):
            indice += 3
            return True
    else:
        return False


def main():
    texto = input("Insira o texto a lêr:\n")
    total = 0
    global indice

    somar = True

    for h in range(len(texto)):
        
        if indice < len(texto):

            if texto[indice].isdigit() and somar:
                x=getNum(texto)
            
                total += x

            elif texto[indice] == 'o' or texto[indice] == 'O':

                if getON(texto):
                    somar = True
                elif getOFF(texto):
                    somar = False
                else:
                    indice +=1

            elif texto[indice] == '=':

                print(total)
                indice+=1

            else:

                indice +=1

            h = indice

    #print("Soma final: "+str(total))
    

main()
