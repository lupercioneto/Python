'''
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. 
Depois mostre:

a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time do Corinthians. - Desafio 073
'''

#Classificação dos times da campeonato brasileiro no dia 15/05/2024
times = ('Flamengo','Athletico-PR','Bahia','Botafogo','Atlético-MG','Bragantino',
         'Palmeiras','São Paulo','Internacional','Cruzeiro','Grêmio','Fortaleza',
         'Criciúma','Juventude','Corinthians','Fluminense','Vasco da Gama',
         'EC Vitória','Atlético-GO','Cuiabá')

#Lista de cores (Padrão ANSI)
cores = ['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[m']
auxindex = 1 

print(f"""{'=-=' * 12}
Lista dos {cores[1]}20 colocados{cores[4]} do Brasileirão: {times}
{'=-=' * 12}

{'=-=' * 12}
5 primeiros colocados: {times[0:5]}
{'=-=' * 12}

{'=-=' * 12}
4 últimos colocados: {times[-4:]}
{'=-=' * 12}

{'=-=' * 12}
Times em {cores[2]}ordem alfabética{cores[4]}: {sorted(times)}
{'=-=' * 12}

{'=-=' * 12}
Corinthians está na {cores[0]}{times.index('Corinthians') + auxindex}ª{cores[4]} posição
""")