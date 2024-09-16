import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Dados fictícios baseados no mercado de jogos no Brasil
data = {
    'Ano': [2017, 2018, 2019, 2020, 2021, 2022],
    'Estúdios de Jogos': [245, 300, 375, 480, 800, 1009],  # Crescimento de estúdios
    'Crescimento (%)': [0, 22.4, 25, 28, 67, 169],  # Crescimento percentual
    'Mercado (Bilhões USD)': [1.3, 1.4, 1.6, 1.9, 2.2, 2.6],  # Mercado em bilhões de dólares
    'Espectadores de eSports (Milhões)': [11, 13, 15, 17, 19, 22]  # Espectadores de eSports no Brasil
}

# Criação do DataFrame
df = pd.DataFrame(data)

# 1. Gráfico Interativo de Crescimento dos Estúdios de Jogos
fig_estudios = px.line(df, x='Ano', y='Estúdios de Jogos', title='Crescimento do Número de Estúdios de Jogos no Brasil (2017-2022)', 
                       markers=True)
fig_estudios.update_layout(xaxis_title='Ano', yaxis_title='Número de Estúdios')
fig_estudios.show()

# 2. Gráfico Interativo de Crescimento do Mercado
fig_mercado = px.bar(df, x='Ano', y='Mercado (Bilhões USD)', title='Crescimento do Mercado de Jogos no Brasil (2017-2022)', 
                     text='Mercado (Bilhões USD)')
fig_mercado.update_layout(xaxis_title='Ano', yaxis_title='Mercado (Bilhões USD)')
fig_mercado.show()

# 3. Gráfico 3D com o Crescimento dos Estúdios, Mercado e Espectadores
fig_3d = plt.figure(figsize=(10, 7))
ax = fig_3d.add_subplot(111, projection='3d')

ax.scatter(df['Ano'], df['Estúdios de Jogos'], df['Mercado (Bilhões USD)'], color='blue', s=100, label='Mercado de Jogos')
ax.set_xlabel('Ano')
ax.set_ylabel('Estúdios de Jogos')
ax.set_zlabel('Mercado (Bilhões USD)')
ax.set_title('Crescimento dos Estúdios e Mercado de Jogos no Brasil (2017-2022)')

plt.show()

# Gráfico interativo 3D com Plotly
fig_3d_interativo = go.Figure(data=[go.Scatter3d(
    x=df['Ano'],
    y=df['Estúdios de Jogos'],
    z=df['Mercado (Bilhões USD)'],
    mode='markers',
    marker=dict(
        size=12,
        color=df['Mercado (Bilhões USD)'],  # Cor representando o mercado
        colorscale='Viridis',
        opacity=0.8
    )
)])

fig_3d_interativo.update_layout(
    title="Crescimento 3D: Estúdios de Jogos, Mercado e Espectadores (2017-2022)",
    scene=dict(
        xaxis_title='Ano',
        yaxis_title='Estúdios de Jogos',
        zaxis_title='Mercado (Bilhões USD)'
    )
)

fig_3d_interativo.show()
