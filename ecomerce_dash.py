
import plotly.express as px
import pandas as pd
from dash import Dash, html, dcc

df = pd.read_csv('ecommerce_estatistica.csv')

#Histograma
fig1 = px.histogram(
    df,
    x='Preço',
    nbins=100,
    labels={'Preço':'Valor R$', 'count':'Quantidade'},
    title='Distribuição de Preço'
)
fig1.update_layout(yaxis_title='Quantidade de Produtos')

#Grafico de Disperção
fig2 = px.scatter(
    df,
    x='Preço',
    y='N_Avaliações',
    size='Nota',
    color='Gênero',
    title='Bolhas Preço vs Qtd'
)
fig2.show

#Mapa de Calor
corr = df[['Desconto', 'Nota']].corr()
fig7= px.imshow(
    corr,
    text_auto=True
)
fig7.show

#Barras Genero vs N_avaliações
fig3 = px.bar(
    df,
    x='Gênero',
    y='N_Avaliações',
    title='Gênero vs Numero de Avaliações'
)
fig3.show

#Pizza Top Marcas
top_marca = df['Marca'].value_counts().head(10).reset_index()
fig4 = px.pie(
    top_marca,
    values='count',
    names='Marca',
    title= 'Top Marcas'
)
fig4.show

#Dencidade
fig5 = px.violin(
    df,
    x='Desconto',
    title= 'Cuva de dencidade'
)
fig5.show

#Regreção
fig6 = px.scatter(
    df,
    x='Preço',
    y='Nota',
    trendline='ols',
    title='Região Linear:  Preço vs Notas'
)
fig6.show

#App
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Dashboard de E-commerce"), 
    dcc.Graph(figure=fig1),
    dcc.Graph(figure=fig2),
    dcc.Graph(figure=fig3),
    dcc.Graph(figure=fig4),
    dcc.Graph(figure=fig5),
    dcc.Graph(figure=fig6),
    dcc.Graph(figure=fig7)
])

app.run(debug=True, port=8050)