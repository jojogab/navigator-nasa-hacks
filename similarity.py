# Função para calcular a habitabilidade
def calculate_habitability(temperature, density, gravity):
    # Critérios simplificados de habitabilidade
    temperature_habitable = 273.15 <= temperature <= 323.15  # 0 °C a 50 °C
    density_habitable = 1000 <= density <= 5000  # Valores típicos de densidade para planetas rochosos
    gravity_habitable = 9.81 <= gravity <= 39.24  # Faixa de gravidade similar à da Terra

    # Cálculo de porcentagem de habitabilidade
    score = 0
    if temperature_habitable:
        score += 40  # 40% se a temperatura for habitável
    if density_habitable:
        score += 30  # 30% se a densidade for habitável
    if gravity_habitable:
        score += 30  # 30% se a gravidade for habitável

    return score
