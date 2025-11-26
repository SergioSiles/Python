import emoji

print(emoji.emojize("¡Bienvenido! :smile:", language="alias"))


def calcular_imc_con_emoji(peso, altura):
    imc = peso / (altura**2)
    if imc < 18.5:
        estado = "Bajo peso " + emoji.emojize(":warning:", language="alias")
    elif imc < 25:
        estado = "Normal " + emoji.emojize(":smile:", language="alias")
    else:
        estado = "Sobrepeso " + emoji.emojize(":exclamation:", language="alias")
    return imc, estado
