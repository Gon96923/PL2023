class distribuicao:
    def __init__(self,categoria,total,percentil,percentagem):
        self.categoria=categoria
        self.total=total
        self.percentil=percentil
        self.percentagem=percentagem

    def emLinha(self):
        return(str(self.categoria)+','+str(self.total)+','+str(self.percentil)+','+str(self.percentagem))
    
###################################################################################################################################################
class tabela:
    def __init__(self):
        self.listaTabela=[]

    def adiciona(self,linha):
        self.listaTabela.append(linha)

    def imprime(self):
        for x in range(len(self.listaTabela)):
            print(self.listaTabela[x])

###################################################################################################################################################
class modelo:
    def __init__(self,linhas):
        self.lista=[]
        for x in linhas:        
            sring=x.split(',')
            pac=paciente(sring[0],sring[1],sring[2],sring[3],sring[4],sring[5])
            self.lista.append(pac)

    def taxaGeneroDoentes(self):
        nM=0
        nF=0
        nMD=0
        nFD=0        
        for x in range(len(self.lista)):        
            pac = self.lista[x]
            if pac.fem():
                nF+=1
                if pac.estaDoente():
                    nFD+=1

            elif pac.mas():
                nM+=1
                if pac.estaDoente():
                    nMD+=1
            
        perF = float("{:.2f}".format((nFD/nF) * 100))
        perM = float("{:.2f}".format((nMD/nM) * 100))

        fem = distribuicao('F',nF,nFD,perF)
        feml = fem.emLinha()

        man = distribuicao('M',nM,nMD,perM)
        manl = man.emLinha()

        tabGeneros = tabela()
        tabGeneros.adiciona("Genero,Individuos,Doentes,Percentagem de Individuos Doentes")
        tabGeneros.adiciona(feml)
        tabGeneros.adiciona(manl)
        tabGeneros.imprime()

    def taxaIdadeDoentes(self):
        list = [0]*14
        total = 0
        listDoentes = [0]*14
        faixa=["30-34","35-39","40-44","45-49","50-54","55-59","60-64","65-69","70-74","75-79","80-84","85-89","90-95","95-99"]

        for x in range(len(self.lista)):        
            pac = self.lista[x]
            a=pac.faixaEtaria()
            if(a>=0):
                list[a]+=1
                if pac.estaDoente():
                    listDoentes[a]+=1
                    total+=1
        
        tabIdades = tabela()
        tabIdades.adiciona("Faixa Etaria,Individuos,Doentes,Percentagem de Individuos Doentes")

        for i in range(14):
            if list[i] > 0:
                taxa = float("{:.2f}".format((listDoentes[i]/list[i])*100))

                aux = distribuicao(faixa[i],list[i],listDoentes[i],taxa)
                auxl = aux.emLinha()
                tabIdades.adiciona(auxl)

        tabIdades.imprime()

    def taxaColesterol(self):
        menorValor=1000
        maiorValor=0

        for x in range(len(self.lista)):        
            pac = self.lista[x]
            val = pac.getColesterol()            
            if val > maiorValor:
                maiorValor = val
            if val < menorValor:
                menorValor = val

        if menorValor%10 != 0:
            menorValor = menorValor - (menorValor%10)
        if maiorValor%10 != 0:
            maiorValor = maiorValor + 9 - (maiorValor%10)
        
        ran = maiorValor//10-menorValor//10+1

        escaloesDoentes = [0]*ran
        escaloes = [0]*ran

        for x in range(len(self.lista)):        
            pac = self.lista[x]
            val = pac.getColesterol() // 10
            escaloes[val]+=1
            if(pac.estaDoente()):
                escaloesDoentes[val]+=1

        menor=0
        maior=9

        tabColesterol = tabela()
        tabColesterol.adiciona("Nivel de Colesterol,Individuos,Doentes,Percentagem de Individuos Doentes")

        for x in range(ran):
            if escaloes[x]>0:
                taxa = float("{:.2f}".format((escaloesDoentes[x]/escaloes[x])*100))

                h = str(menor)+'-'+str(maior)
                aux = distribuicao(h,escaloes[x],escaloesDoentes[x],taxa)
                auxl = aux.emLinha()
                tabColesterol.adiciona(auxl)

            menor+=10
            maior+=10
        
        tabColesterol.imprime()


###################################################################################################################################################
class paciente:
    def __init__(self,idade,sexo,tensao,colesterol,batimento,doente):
        self.idade=idade
        self.sexo=sexo
        self.tensao=tensao
        self.colesterol=colesterol
        self.batimento=batimento
        self.doente=doente

    def __str__(self):
        return f"Idade: {self.idade}, Sexo: {self.sexo}, Tensâo: {self.tensao}, Colesterol: {self.colesterol}, Batimento: {self.batimento}, Doente: {self.doente}"

    def faixaEtaria(self):
        idade = int(self.idade)
        if idade>=30 and idade<35:
            return 0
        elif idade>=35 and idade<40:
            return 1
        elif idade>=40 and idade<45:
            return 2
        elif idade>=45 and idade<50:
            return 3
        elif idade>=50 and idade<55:
            return 4
        elif idade>=55 and idade<60:
            return 5
        elif idade>=60 and idade<65:
            return 6
        elif idade>=65 and idade<70:
            return 7
        elif idade>=70 and idade<75:
            return 8
        elif idade>=75 and idade<80:
            return 9
        elif idade>=80 and idade<85:
            return 10
        elif idade>=85 and idade<90:
            return 11
        elif idade>=90 and idade<95:
            return 12
        elif idade>=95 and idade<100:
            return 13
        else:
            return -1
        
        
    def fem(self):
        if self.sexo == "F":
            return True
        else:
            return False
        
    def mas(self):
        if self.sexo == "M":
            return True
        else:
            return False
        
    def estaDoente(self):
        if int(self.doente) == 1:
            return True
        else: 
            return False
        
    def getColesterol(self):
        return int(self.colesterol)
###################################################################################################################################################


def main():
    f = open("myheart.csv", "r")
    next(f)
    linhas = f.readlines()
    f.close()

    mod = modelo(linhas)
    
    mod.taxaGeneroDoentes()
    mod.taxaIdadeDoentes()
    mod.taxaColesterol()
    
    
    
    

main()