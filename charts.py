import plotly.graph_objects as go
import query as q

def create_chart():

    # Fazendo a requisição
    df = q.make_request()

    if df is not None:
        # Filtrando dados para garantir que todos os planetas tenham massa, raio, distância, densidade e gravidade conhecidos
        df = df.dropna(subset=['pl_bmasse', 'pl_rade', 'sy_dist_pc', 'density', 'gravity'])

        # Verificando se há dados após a filtragem
        print(f"Número de planetas filtrados: {len(df)}")

        if len(df) == 0:
            print("Nenhum dado disponível para visualização.")
        else:
            # Criando listas para armazenar os dados
            planets = df['pl_name'].tolist()  # Lista com os nomes dos planetas
            distance_from_earth = df['sy_dist_pc'].tolist()  # Usando a distância em parsecs
            planet_diameter = (df['pl_rade'] * 2).astype(float).tolist()  # Diâmetro como duas vezes o raio
            density = df['density'].tolist()
            gravity = df['gravity'].tolist()

            # Definindo um gradiente de cores para a temperatura dos planetas (usando pl_eqt)
            planet_colors = df['pl_eqt'].tolist()  # Usar temperatura do planeta para colorir

            # Garantindo que o tamanho das bolhas esteja correto ajustando o 'sizeref'
            sizeref_value = max(planet_diameter) / 120  # Ajustar para que o tamanho das bolhas fique visível

            # Criar a anotação no hover com nome do planeta, distância, densidade e gravidade
            hover_text = []
            for i in range(len(planets)):
                hover_text.append(f"Planet: {planets[i]}<br>"
                                f"Distance: {distance_from_earth[i]:.2f} pc<br>"
                                f"Density: {density[i]:.2f} kg/m³<br>"
                                f"Gravity: {gravity[i]:.2f} m/s²")

            # Criar traço, dimensionando as bolhas pelo diâmetro do planeta
            fig = go.Figure(data=go.Scatter3d(
                x=distance_from_earth,
                y=density,   # Densidade
                z=gravity,    # Gravidade
                text=hover_text,  # Mostra informações detalhadas no hover
                mode='markers',
                marker=dict(
                    sizemode='diameter',
                    sizeref=sizeref_value,  # Ajustado para melhorar a visibilidade das bolhas
                    size=planet_diameter,
                    color=planet_colors,  # Colorindo com base na temperatura
                    colorbar_title='Temperature (K)',  # Título para a barra de cores
                    colorscale=[[0, 'rgb(5, 10, 172)'], [1, 'rgb(178, 10, 28)']]
                ),
                hoverinfo="text"  # Exibe o conteúdo do hover_text
            ))

            # Atualizando o layout do gráfico
            fig.update_layout(width=800, height=800, title='Exoplanets Overview!',
                            scene=dict(
                                xaxis=dict(title='Distance from Earth (Parsecs)', titlefont_color='white'),
                                yaxis=dict(title='Density (kg/m³)', titlefont_color='white'),
                                zaxis=dict(title='Gravity (m/s²)', titlefont_color='white'),
                                bgcolor='rgb(20, 24, 54)'
                            ))

            # Mostrar o gráfico
            fig.show()
