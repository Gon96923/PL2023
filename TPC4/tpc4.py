import re
import json

def search1(lista,texto):
    resultado = []

    er0 = re.compile(r'(.+)\{(\d+)\}')
    er0fun = re.compile(r'(.+)\{(\d+)\}::([a-z]+)')

    er1 = re.compile(r'(.+)\{(\d+),(\d+)\}')
    er1fun = re.compile(r'(.+)\{(\d+),(\d+)\}::([a-z]+)')

    for linhas in texto:
        linhas=linhas.strip().replace('\n', '')

        d = {}
        
        res = re.split(r',',linhas)

        i=0

      
        while i < len(lista):


            
            if er0fun.match(lista[i]):              

                h = i

                n = er0fun.match(lista[i]).group(2)

                fun = str(er0fun.match(lista[i]).group(3))
                soma = 0
                count = 0

                for j in range(int(n)):

                    soma += int(res[i])
                    count += 1
                    i += 1

                s = str(er0fun.match(lista[h]).group(1)) +"_"+ fun
                d[s] = []

                if fun.__eq__("sum"):
                    d[s] =soma
                if fun.__eq__("media"):
                    media = soma/count
                    d[s] = media
            


            elif er0.match(lista[i]):              

                h = i

                n = er0.match(lista[i]).group(2)

                d[er0.match(lista[h]).group(1)] = []

                for j in range(int(n)):

                    d[er0.match(lista[h]).group(1)].append(res[i])
                    i += 1



            elif er1fun.match(lista[i]):              

                h = i
                soma = 0
                count = 0

                n2 = er1fun.match(lista[i]).group(3)

                fun = str(er1fun.match(lista[i]).group(4))

                for j in range(int(n2)):

                    if res[i] != '':
                        soma += int(res[i])
                        count += 1
                    i += 1

                s = er1fun.match(lista[h]).group(1) +"_"+ fun
                d[s] = []

                if fun.__eq__("sum"):
                    d[s]=soma
                if fun.__eq__("media"):
                    media = soma/count
                    d[s]=media



            elif er1.match(lista[i]):              

                h = i

                n2 = er1.match(lista[i]).group(3)

                d[er1.match(lista[h]).group(1)] = []

                for j in range(int(n2)):

                    if res[i] != '':
                        d[er1.match(lista[h]).group(1)].append(res[i])
                    i += 1          



            else:
                if i < len(res):
                    d[lista[i]] = res[i]
                    i += 1
                else:
                    i = len(lista)

        
        resultado.append(d)
    
    return resultado







def main():
    resultadoFinal = []

    file = input("Indique o nome do ficheiro a lêr.\n")

    f = open(file, "r")

    linha = f.readline().strip('\n')

    texto = f.readlines()

    lista = []

    lista = re.split(r',(?!\S?\}|\{)', linha)

    resultadoFinal = search1(lista,texto)

    json_object = json.dumps(resultadoFinal, indent=len(lista))

    with open("output.json", "a") as outfile:
        outfile.write(json_object)

    
    f.close()


main()