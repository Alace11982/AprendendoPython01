#usando funções de agregação
#como count, min, max, avg, sum
#para mostrar resultados

#agora usando o order by
#adiciona 'having' para listar apenas as regiões com mais de 5 estados
import sqlite3
print('Região Estados População    Mínina     Máxima      Média  Total(soma)')
print('====== =======           =========  =========  =========  ===========')
with sqlite3.connect('brasil.db') as conexao:
    for regiao in conexao.execute("""
        select regiao, count(*), min(populacao),
            max(populacao), avg(populacao), sum(populacao)
        from estados
        group by regiao
        having count(*) > 5 
        order by sum(populacao) desc"""):
        print("{0:6} {1:7} {2:18,} {3:10,} {4:10,.0f} {5:13,}".format(*regiao))
    print('\nBrasil: {0:6} {1:18,} {2:10,} {3:10,.0f} {4:13,}'.format(
        *conexao.execute("""
            select count(*), min(populacao), max(populacao), avg(populacao), sum(populacao) from estados""").fetchone()))
       