#definição do inversor de texto
def inverter(s):
    invertido = ""
    for i in range(len(s) - 1, -1, -1):
        invertido += s[i]
    return invertido

#main
texto = 'Target Sistemas'

novo_texto = inverter(texto)
print(f'O texto original é {texto}, e o texto invertido é {novo_texto}')





