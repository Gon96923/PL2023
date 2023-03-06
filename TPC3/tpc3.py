import re
import json

def freq_por_ano(texto):
    anos = dict()

    er = re.compile(r'([0-9]*)::([0-9]{4})(-[0-9]{2}-[0-9]{2})(::.*:)')

    for linhas in texto:
        if er.match(linhas):
            if er.match(linhas).group(2) in anos:
                anos[er.match(linhas).group(2)] += 1
            else:
                anos[er.match(linhas).group(2)] = 1

                
    for i in anos:
        print("Ano: "+str(i) +"_______Processos: "+str(anos[i]) )

#575::1894-11-08::Aarao Pereira Silva::Antonio Pereira Silva::Francisca Campos Silva::kuugcgsictsiytcsv::
#()::()::(aarao)::(Antonio)::(Francisca)::()::
#2 -seculo
#4-nome 7 10
#6-sobrenome 9 12
'''
def freq_por_nome(texto):
    seculosNomes = dict()
    nomesSobreNomes = dict()

    er = re.compile(r'([0-9]*)::([0-9]{2})([0-9]{2}-.+)::([A-Z][a-z]+) (.+) ([A-Z][a-z]+)::([A-Z][a-z]+) (.+) ([A-Z][a-z]+)::([A-Z][a-z]+) (.+) ([A-Z][a-z]+)::(.*)::')

    for linhas in texto:
        if er.match(linhas):
            if er.match(linhas).group(2) in seculosNomes:
                #print("hello")
                if er.match(linhas).group(4) in seculosNomes[er.match(linhas).group(2)]:
                    seculosNomes[er.match(linhas).group(2)][er.match(linhas).group(4)] += 1
                    print("hello")
                if er.match(linhas).group(7) in seculosNomes[er.match(linhas).group(2)]:
                    seculosNomes[er.match(linhas).group(2)][er.match(linhas).group(7)] += 1
                if er.match(linhas).group(10) in seculosNomes[er.match(linhas).group(2)]:
                    seculosNomes[er.match(linhas).group(2)][er.match(linhas).group(10)] += 1
            else:
                seculosNomes[er.match(linhas).group(2)] = {}
                if er.match(linhas).group(4) in seculosNomes[er.match(linhas).group(2)]:
                    seculosNomes[er.match(linhas).group(2)][er.match(linhas).group(4)] += 1
                if er.match(linhas).group(7) in seculosNomes[er.match(linhas).group(2)]:
                    seculosNomes[er.match(linhas).group(2)][er.match(linhas).group(7)] += 1
                if er.match(linhas).group(10) in seculosNomes[er.match(linhas).group(2)]:
                    seculosNomes[er.match(linhas).group(2)][er.match(linhas).group(10)] += 1
            if er.match(linhas).group(2) in nomesSobreNomes:
                if er.match(linhas).group(6) in nomesSobreNomes[er.match(linhas).group(2)]:
                    nomesSobreNomes[er.match(linhas).group(2)][er.match(linhas).group(6)] += 1
                if er.match(linhas).group(9) in nomesSobreNomes[er.match(linhas).group(2)]:
                    nomesSobreNomes[er.match(linhas).group(2)][er.match(linhas).group(9)] += 1
                if er.match(linhas).group(12) in nomesSobreNomes[er.match(linhas).group(2)]:
                    nomesSobreNomes[er.match(linhas).group(2)][er.match(linhas).group(12)] += 1
            else:
                nomesSobreNomes[er.match(linhas).group(2)] = {}
                if er.match(linhas).group(6) in nomesSobreNomes[er.match(linhas).group(2)]:
                    nomesSobreNomes[er.match(linhas).group(2)][er.match(linhas).group(6)] += 1
                if er.match(linhas).group(9) in nomesSobreNomes[er.match(linhas).group(2)]:
                    nomesSobreNomes[er.match(linhas).group(2)][er.match(linhas).group(9)] += 1
                if er.match(linhas).group(12) in nomesSobreNomes[er.match(linhas).group(2)]:
                    nomesSobreNomes[er.match(linhas).group(2)][er.match(linhas).group(12)] += 1

                
    for i in seculosNomes:
        for j in seculosNomes[i]:
            print("Seculo: "+str(i)+"_______Nomes: "+str(j)+"_______Vezes: "+str(seculosNomes[i][j]) )
    for i in nomesSobreNomes:
        for j in nomesSobreNomes[i]:
            print("Seculo: "+str(i)+"_______Nomes: "+str(j)+"_______Vezes: "+str(nomesSobreNomes[i][j]) )
'''

def freq_relacao(texto):
    relacoes = dict()

    ertio = re.compile(r'(.+)::(.+)::(.+)::(.+)::(.+)::(.*[\.,\s][Tt]io[\.,\s].*)::')
    erirmao = re.compile(r'(.+)::(.+)::(.+)::(.+)::(.+)::(.*[\.,\s][Ii]rmaos?[\.,\s].*)::')
    erprimo = re.compile(r'(.+)::(.+)::(.+)::(.+)::(.+)::(.*[\.,\s][Pp]rimos?[\.,\s].*)::')
    ersobrinho = re.compile(r'(.+)::(.+)::(.+)::(.+)::(.+)::(.*[\.,\s][Ss]obrinho[\.,\s].*)::')
    erpai = re.compile(r'(.+)::(.+)::(.+)::(.+)::(.+)::(.*[\.,\s][Pp]ai[\.,\s].*)::')
    eravo = re.compile(r'(.+)::(.+)::(.+)::(.+)::(.+)::(.*[\.,\s][Aa]vo[\.,\s].*)::')
    erneto = re.compile(r'(.+)::(.+)::(.+)::(.+)::(.+)::(.*[\.,\s][Nn]etos?[\.,\s].*)::')
    erbisavo = re.compile(r'(.+)::(.+)::(.+)::(.+)::(.+)::(.*[\.,\s][Bb]isavos?[\.,\s].*)::')
    ermeioirmao = re.compile(r'(.+)::(.+)::(.+)::(.+)::(.+)::(.*[\.,\s][Mm]eio [Ii]rmao[\.,\s].*)::')

    for linhas in texto:
        if ertio.match(linhas):
            if "Tio" in relacoes:
                relacoes["Tio"] += 1
            else:
                relacoes["Tio"] = 1
        if erirmao.match(linhas):
            if "Irmao" in relacoes:
                relacoes["Irmao"] += 1
            else:
                relacoes["Irmao"] = 1
        if erprimo.match(linhas):
            if "Primo" in relacoes:
                relacoes["Primo"] += 1
            else:
                relacoes["Primo"] = 1
        if ersobrinho.match(linhas):
            if "Sobrinho" in relacoes:
                relacoes["Sobrinho"] += 1
            else:
                relacoes["Sobrinho"] = 1
        if erpai.match(linhas):
            if "Pai" in relacoes:
                relacoes["Pai"] += 1
            else:
                relacoes["Pai"] = 1
        if eravo.match(linhas):
            if "Avo" in relacoes:
                relacoes["Avo"] += 1
            else:
                relacoes["Avo"] = 1
        if erneto.match(linhas):
            if "Neto" in relacoes:
                relacoes["Neto"] += 1
            else:
                relacoes["Neto"] = 1
        if erbisavo.match(linhas):
            if "Bisavo" in relacoes:
                relacoes["Bisavo"] += 1
            else:
                relacoes["Bisavo"] = 1
        if ermeioirmao.match(linhas):
            if "Meio Irmao" in relacoes:
                relacoes["Meio Irmao"] += 1
            else:
                relacoes["Meio Irmao"] = 1

                
    for i in relacoes:
        print(str(i) +": "+str(relacoes[i]) )

def convert_json(texto):

    er = re.compile(r'(.+)::(.+)::(.+)::(.*)::(.*)::(.*)::')
    i=0
    lista = []

    for linhas in texto:
        if i < 20:
            d = {
            "Processo": er.match(linhas).group(1),
            "Data": er.match(linhas).group(2),
            "Nome": er.match(linhas).group(3),
            "Pai": er.match(linhas).group(4),
            "Mae": er.match(linhas).group(5),
            "Observacoes": er.match(linhas).group(6)
            }
            lista.append(d)
            i+=1
        else:
            break
    json_object = json.dumps(lista, indent=6)

    with open("output.json", "a") as outfile:
        outfile.write(json_object)
            

        

def main():
    f = open("processos.txt", "r")
    linhas = f.readlines()
    convert_json(linhas)
    f.close()


main()