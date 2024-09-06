distribuidora = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outro': 19849.53
}

#somatória total
total = sum(distribuidora.values())

#cálculo e print do percentual
print("Percentual de representação de cada estado no faturamento total:")
for estado, valor in distribuidora.items():
    percentual = (valor / total) * 100
    print(f"{estado}: {percentual:.2f}%")