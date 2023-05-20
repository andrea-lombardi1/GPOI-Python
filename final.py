"""Script che crea un'applicazione Dash che mostra un grafico a barre interattivo."""
from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px

app = Dash(title="Andrea Lombardi - GPOI Python", update_title="Caricamento...")


app.layout = html.Div([
    html.H1('PERSONE CHE HANNO SUBITO UN INFORTUNIO SUL LUOGO DI LAVORO NEL 2020'),
    html.H4('Dati ISTAT'),
    dcc.Dropdown(
        id="dropdown",
        options=["Nazionalità", "Italia", "Età"],
        value="Nazionalità",
        clearable=False,
        style={'width': '50%', 'margin': 'auto'}
    ),
    dcc.Graph(id="graph", style={'height': '80vh'}),
], style={'margin': 'auto', 'textAlign': 'center', 'fontFamily': 'arial', 'color': 'black'})


@app.callback(
    Output("graph", "figure"),
    Input("dropdown", "value"))
def update_bar_chart(value):
    """Funzione che aggiorna il grafico a barre in base al valore selezionato nella dropdown"""
    d_f = pd.read_csv(f"data/{value}.csv")
    fig = px.bar(d_f, x="Sesso", y="Valore", color=value, barmode="group", text_auto=True)
    return fig


app.run_server(port=8080)
