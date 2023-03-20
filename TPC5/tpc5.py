import re

erBloqueada = re.compile(r'(601|641)((\d){6})(?!.)')
er00 = re.compile(r'00\d{9}(?!.)')#1.5e
er2 = re.compile(r'2\d{8}(?!.)')#25c
er800 = re.compile(r'800\d{6}(?!.)')#0
er808 = re.compile(r'808\d{6}(?!.)')#10c

def printSaldo(saldo):
    euro, cent = divmod(saldo, 1)
    euroi = int(euro)
    centi = int(round(cent,2)*100)

    print("maq: saldo = " +str(euroi)+"e"+str(centi)+"c")

def aceitaMoedas(valores):


    for i in range(len(valores)):
        valores[i] = valores[i].strip(",")

    res = 0
    moedas = ["1c","2c","5c","10c","20c","50c","1e","2e"]

    for i in valores:
        if i in moedas:
            if(i==moedas[0]):
                res += 0.01
            if(i==moedas[1]):
                res += 0.02
            if(i==moedas[2]):
                res += 0.05
            if(i==moedas[3]):
                res += 0.1
            if(i==moedas[4]):
                res += 0.2
            if(i==moedas[5]):
                res += 0.5
            if(i==moedas[6]):
                res += 1
            if(i==moedas[7]):
                res += 2


        else:
            print("maq: " +i + "-moeda inválida.")

    return res



def precNumero(linha,saldo):

    er = re.compile(r'^T\s*=\s*(\d+)')

    if er.match(linha) == None:
        print("maq: Esse número não existe. Queira discar novo número!")
        return 0
    else:
        numero = er.match(linha).group(1)

    if erBloqueada.match(numero):
        print("maq: Esse número não é permitido neste telefone. Queira discar novo número!")
        return 0
    
    elif er00.match(numero):
        if saldo >= 1.5:
            return 1.5
        else:
            print("maq: Saldo Insuficiente!")
            return 0

    elif er2.match(numero):
        if saldo >= 0.25:
            return 0.25
        else:
            print("maq: Saldo Insuficiente!")
            return 0
        
    elif er800.match(numero):
        return 0
    
    elif er808.match(numero):
        if saldo >= 0.1:
            return 0.1
        else:
            print("maq: Saldo Insuficiente!")
            return 0

    else:
        print("maq: Esse número não existe. Queira discar novo número!")
        return 0


def main():
    saldo = 0

    flag = False
    naoLevantado = True

    erLevantar = re.compile(r'\s*LEVANTAR\s*')
    erPousar = re.compile(r'\s*POUSAR\s*')
    erAbortar = re.compile(r'\s*ABORTAR\s*')


    while(naoLevantado):
        linha = input()

        if erLevantar.fullmatch(linha):
            flag = True
            naoLevantado = False
            print("Introduza moedas.")
        elif erAbortar.fullmatch(linha):
            #abortar
            print("maq: ABORTADA!")
            flag=False
            break
        else:
            print("maq: Por favor inicíe o comando LEVANTAR para iniciar a interação.")

    
    erMoeda = re.compile(r'^MOEDA\s*')
    erNumero = re.compile(r'^T\s*=\s*')


    ercent = re.compile(r'\s*(\d+c)\s*[,|\.]?')
    ereuro = re.compile(r'\s*(\d+e)\s*[,|\.]?')

    while(flag):
        linha = input()

        if erLevantar.fullmatch(linha):
            #levantar
            print("maq: Auscultador já levantado.")


        elif(erMoeda.match(linha)):
            #moeda
            m = []
            m = m + ercent.findall(linha)
            m = m + ereuro.findall(linha)
            saldo += aceitaMoedas(m)
            printSaldo(saldo)

            
        elif(erNumero.match(linha)):
            #numero
            saldo = saldo - precNumero(linha,saldo)
            printSaldo(saldo)
            

        elif erPousar.fullmatch(linha):
            #pousar
            print("maq: troco="+str(round(saldo,2))+"; Volte sempre!")
            flag=False

        elif erAbortar.fullmatch(linha):
            #abortar
            print("maq: ABORTADA! Saldo devolvido = "+str(round(saldo,2))+"; Volte sempre!")
            flag=False

        else:
            #Comando Indisponível
            print("maq: Comando Indisponível!")


main()