#A partir de um simples dicionário composto por trê itens, {'Alto Nível':'Python', 'Médio Nível':'C', 'Baixo Nível':'Assembly'}, verifique se 'Python consta no dicionário em questão, utilizando de negação lógica para tal verificação
#Criando o dicionário
tipo_linguagens = {"Alto Nível" : 'Python',
                   "Médio Nível" : "C",
                   'Baixo Nível' : "Assembly"}

for i in tipo_linguagens.values():
    if not i == 'Python':
        print(f"Python não consta na lista")
        
    else:
        print(f'Python consta na lista')
        break
