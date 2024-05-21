import pandas as pd

meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']
melhor_vendedor = ""
melhor_valor = 0.0
#Faz a leitura dos arquivos de controle de vendas de cada mês
for mes in meses:
    tabela_vendas = pd.read_excel(f'sheets/{mes}.xlsx')
    #Percorre linha por linha de cada arquivo e armazena o valor total de venda
    for linha, _ in tabela_vendas.iterrows():
        valor_venda = tabela_vendas.iloc[linha, 1]
        #Verifica se o valor total de vendas é maior que 55.000. Caso verdadeiro, armazena o nome e total de vendas do primeiro vendedor com mais de  55.000 em vendas e para de percorrer o arquivo
        if valor_venda > 55000:
            melhor_vendedor = tabela_vendas.iloc[linha, 0]
            melhor_valor = tabela_vendas.iloc[linha, 1]
            break
    #Se a variável melhor_vendedor já possuir um valor o programa imprime o mês em que ocorreu a melhor venda, o nome e o total de vendas do vendedor e é interrompido
    if melhor_vendedor != "":
        print(f'''
MÊS: {mes.upper()}
MELHOR VENDEDOR: {melhor_vendedor.upper()}
VALOR TOTAL: R$ {melhor_valor},00
''') 
        break




          