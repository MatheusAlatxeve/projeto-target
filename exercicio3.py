#Apesar dos dados.json geralmente estarem no .gitignore, deixarei o json para facilitar a correção

import json

def processar_faturamento(caminho_arquivo):
    # Carregar dados do arquivo JSON
    with open(caminho_arquivo, 'r') as file:
        dados = json.load(file)
    
    faturamento = [item['valor'] for item in dados]
    faturamento_validos = [valor for valor in faturamento if valor > 0]
    
    if not faturamento_validos:
        return "Não há dados de faturamento válidos para processar."
    
    menor_faturamento = min(faturamento_validos)
    maior_faturamento = max(faturamento_validos)
    media_mensal = sum(faturamento_validos) / len(faturamento_validos)
    
    dias_acima_media = sum(1 for valor in faturamento_validos if valor > media_mensal)
    
    return {
        'menor_faturamento': menor_faturamento,
        'maior_faturamento': maior_faturamento,
        'dias_acima_media': dias_acima_media
    }


caminho_arquivo = 'C:\\Users\\ferot\\OneDrive\\Documentos\\processo seletivo\\projeto-target\\dados.json'

resultado = processar_faturamento(caminho_arquivo)


print("Menor faturamento:", resultado['menor_faturamento'])
print("Maior faturamento:", resultado['maior_faturamento'])
print("Número de dias acima da média:", resultado['dias_acima_media'])
