import plotly.graph_objects as go
import query as q
import similarity as s
import json

def create_chart(save_to_file=False):
    # Fazendo a requisição
    df = q.make_request()

    if df is not None:
        df = df.dropna(subset=['pl_bmasse', 'pl_rade', 'sy_dist'])
        if len(df) == 0:
            print("Nenhum dado disponível para visualização.")
        else:
            planets = df['pl_name'].tolist()
            distance_from_earth = df['sy_dist'].tolist()
            planet_diameter = (df['pl_rade'] * 2).astype(float).tolist()
            planet_radius = df['pl_rade'].tolist()
            planet_mass = df['pl_bmasse'].tolist()
            temperature = df['pl_eqt'].tolist()
            habitability_scores = [s.calculate_habitability(temp, dens, grav) for temp, dens, grav in zip(temperature, density, gravity)]

            sizeref_value = max(planet_diameter) / 30
            
            # Usar uma paleta de cores acessível
            colorscale = [
                [0, '#2E8BFF'],  # Azul
                [0.5, '#FFD700'],  # Amarelo
                [1, '#FF5733']  # Vermelho
            ]

            hover_text = [
                f"<span style='color: white; font-size: 14px;'>Planet: {planets[i]}<br>"
                f"Distance: {distance_from_earth[i]:.2f} pc<br>"
                f"Radius: {planet_radius[i]:.2f} X earth(radius)<br>"
                f"Mass: {planet_mass[i]:.2f} earths<br>"
                f"Habitability Score: {habitability_scores[i]}%</span>"
                for i in range(len(planets))
            ]

            fig = go.Figure(data=go.Scatter3d(
                x=distance_from_earth,
                y=density,
                z=gravity,
                text=hover_text,
                mode='markers',
                marker=dict(
                    sizemode='diameter',
                    sizeref=sizeref_value,
                    size=planet_diameter,
                    color=habitability_scores,
                    colorscale=colorscale,
                    colorbar_title='Habitability Score (%)',
                    line=dict(width=2, color='black'),  # Contorno dos marcadores
                    opacity=0.8  # Ajustando a opacidade
                ),
                hoverinfo="text"
            ))

            fig.update_layout(
                scene=dict(
                    xaxis=dict(
                        title='Distance from Earth (Parsecs)',
                        titlefont_color='white',
                        showbackground=True,
                        backgroundcolor='black',
                        gridcolor='gray',
                        zerolinecolor='white',
                        color='white'
                    ),
                    yaxis=dict(
                        title='Radius (x Earth(radius))',
                        titlefont_color='white',
                        showbackground=True,
                        backgroundcolor='black',
                        gridcolor='gray',
                        zerolinecolor='white',
                        color='white'
                    ),
                    zaxis=dict(
                        title='Mass (earths)',
                        titlefont_color='white',
                        showbackground=True,
                        backgroundcolor='black',
                        gridcolor='gray',
                        zerolinecolor='white',
                        color='white'
                    ),
                    bgcolor='black'
                ),
                paper_bgcolor='black',
                plot_bgcolor='black'
            )

            if save_to_file:
                # Exportar para JSON
                fig_json = fig.to_json()
                with open("./src/chart_data.json", "w") as f:
                    f.write(fig_json)
                print("Gráfico salvo em chart_data.json")
            else:
                fig.show()

# Chame a função para salvar o gráfico em JSON
create_chart(save_to_file=True)
