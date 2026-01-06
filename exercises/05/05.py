"""
Exercício 05: Testando o método apply() do Pandas

O método apply() permite aplicar uma função a cada elemento, linha ou coluna de um DataFrame.

Desafios:
1. Classificar clientes por número de pontos em categorias
2. Calcular quantos dias cada conta existe
3. Aplicar função com parâmetros adicionais (args/kwargs)
4. Processar múltiplas colunas com axis=1
5. Usar lambda para transformações simples
6. Extrair e transformar dados de datetime
7. BONUS: Análise agregada com apply()
"""
#%%
import pandas as pd
import numpy as np
from datetime import datetime

# Carregar os dados
clientes = pd.read_csv('../../data/clientes.csv', sep=';')
transacoes = pd.read_csv('../../data/transacoes.csv', sep=';')
produtos = pd.read_csv('../../data/produtos.csv', sep=';')

# print("=" * 60)
# print("EXERCÍCIO 05: MÉTODO APPLY()")
# print("=" * 60)

#%%
# ============================================================================
# DESAFIO 1: Classificar clientes por número de pontos
# ============================================================================
# print("\n[DESAFIO 1] Classificar clientes por pontos")
# print("-" * 60)
# print("""
# Crie uma função que classifique um cliente em uma categoria baseada no 
# número de pontos (qtdePontos):
# - Bronze: menos de 5.000 pontos
# - Prata: 5.000 a 24.999 pontos
# - Ouro: 25.000 a 49.999 pontos
# - Platina: 50.000+ pontos

# Use apply() para criar uma coluna 'categoria' com o resultado.
# """)

def set_client_category(points: int):
  if points > 50000:
   return 'Platina'
  if points > 25000:
    return 'Ouro'
  if points > 5000:
    return 'Prata'
  return 'Bronze'

clientes["categoria"] = clientes['qtdePontos'].apply(set_client_category)
clientes
#%%
# ============================================================================
# DESAFIO 2: Calcular idade da conta em dias
# ============================================================================
# print("\n[DESAFIO 2] Calcular idade da conta em dias")
# print("-" * 60)
# print("""
# Crie uma função que calcula quantos dias uma conta foi criada até hoje.
# Use a coluna 'DtCriacao' para isso. Converta a data em datetime e calcule 
# a diferença em relação a hoje.

# Crie uma coluna 'dias_conta' com o resultado.
# """)

from datetime import datetime

clientes['dias_conta'] = (datetime.today() - pd.to_datetime(clientes['DtCriacao'])).dt.days
clientes
#%%
# ============================================================================
# DESAFIO 3: Usar apply com parâmetros extras (args/kwargs)
# ============================================================================
print("\n[DESAFIO 3] Apply com parâmetros extras")
print("-" * 60)
print("""
Crie uma função que incrementa os pontos de um cliente com:
- Um percentual de aumento (padrão 10%)
- Um bônus fixo em pontos (padrão 100)

Use apply() com args e/ou kwargs para aplicar a função à coluna qtdePontos
com um percentual de 15% e bônus de 250 pontos.

Crie uma coluna 'pontos_simulados' com o resultado.
""")

#%%
# ============================================================================
# DESAFIO 4: Lógica complexa com múltiplas colunas (axis=1)
# ============================================================================
print("\n[DESAFIO 4] Apply com múltiplas colunas (axis=1)")
print("-" * 60)
print("""
Use apply com axis=1 para processar linhas inteiras. Para cada cliente, 
avalie seu status baseado em:

1. Quanto de pontos ele tem (use a classificação do Desafio 1)
2. Quantas plataformas ele está conectado (flEmail, flTwitch, flYouTube, 
   flBlueSky, flInstagram)

Retorne um status descritivo:
- Se for Platina ou Ouro E tiver 2+ plataformas: "VIP - Engajado"
- Se for Ouro ou Platina: "Cliente Valioso"
- Se for Prata: "Cliente Regular"
- Caso contrário: "Cliente Novo"

Crie uma coluna 'status' com o resultado.
""")

# Seu código aqui





# ============================================================================
# DESAFIO 5: Apply com função lambda (forma condensada)
# ============================================================================
print("\n[DESAFIO 5] Apply com função lambda")
print("-" * 60)
print("""
Use lambda para criar uma coluna 'score_pontos' que calcula:
(qtdePontos²) / 1000

Exemplo: se um cliente tem 5000 pontos, o score seria (5000²)/1000 = 25000
""")

# Seu código aqui





# ============================================================================
# DESAFIO 6: Análise em transações - Extrair informações
# ============================================================================
print("\n[DESAFIO 6] Apply em transações")
print("-" * 60)
print("""
Na tabela de transações (DtCriacao), faça:

1. Extraia a hora (0-23) e crie uma coluna 'hora'

2. Classifique cada hora em períodos do dia:
   - Madrugada: 0-5
   - Manhã: 6-11
   - Tarde: 12-17
   - Noite: 18-23
   Crie uma coluna 'periodo'

3. Exiba a distribuição de transações por período com value_counts()
""")

# Seu código aqui





# ============================================================================
# DESAFIO 7: BONUS - Apply com pandas Series/arrays
# ============================================================================
print("\n[DESAFIO 7] BONUS - Análise agregada")
print("-" * 60)
print("""
Use groupby() + apply() para agregar transações por cliente (IdCliente).

Calcule a soma total de pontos por cliente e:
1. Quantos clientes fizeram transações
2. Qual é a média de pontos por cliente
3. Qual cliente teve mais pontos acumulados
4. Qual cliente teve menos pontos acumulados
""")

# Seu código aqui



