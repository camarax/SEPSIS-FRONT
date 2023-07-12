from dash import Dash, html, dcc, Output, Input,no_update
import dash_bootstrap_components as dbc

# Import des composants
from components.Header import navbar
from components.Body import body


app = Dash(name='sepsisApi',external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    navbar,
    body,
])


if __name__ == '__main__':
    
    app.run_server(debug=True, port=8080)
