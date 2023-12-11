import matplotlib.pyplot as plt
import holidays
import matplotlib
matplotlib.use('Agg')  # Usa o modo 'Agg' para gráficos sem GUI (necessário quando rodando em ambiente sem interface gráfica)
from collections import Counter
from datetime import date

def plot_holidays(year):
    # Obtém os feriados para o ano especificado
    feriados = holidays.Brazil(years=year)

    # Filtra apenas os feriados que ocorrem no ano especificado
    feriados_ano = [date(year, dt.month, dt.day) for dt in feriados.keys() if dt.year == year]

    # Agrupa feriados por mês
    feriados_por_mes = Counter(dt.month for dt in feriados_ano)

    # Nome dos meses
    nomes_meses = [date(year, i, 1).strftime('%b') for i in range(1, 13)]  # '%b' para abreviação de meses

    # Cria um gráfico de linha
    fig, ax = plt.subplots()
    ax.plot(nomes_meses, [feriados_por_mes.get(i, 0) for i in range(1, 13)], marker='o', color='red', linestyle='-')

    # Adiciona rótulos e título ao gráfico
    ax.set_xlabel('Mês')
    ax.set_ylabel('Número de Feriados')
    ax.set_title(f'Feriados por Mês no Ano {year}')

    # Ajusta o tamanho da fonte dos meses no eixo x
    plt.xticks(fontsize=8)

    # Exibe o gráfico
    plt.show()

# Substitua 2023 pelo ano desejado
ano_desejado = 2024
plot_holidays(ano_desejado)
plt.savefig('calendario.png')  # ou outro formato de imagem desejado
