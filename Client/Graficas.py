import pandas as pd
import plotly.graph_objs as go

# Carga los datos
df = pd.read_csv('datos.csv')

# Crea un gráfico de barras
data = [go.Bar(x=df['mes'], y=df['ventas'])]
layout = go.Layout(title='Ventas por mes')
fig = go.Figure(data=data, layout=layout)

# Guarda el gráfico en un archivo HTML
fig.write_html('grafica.html')
