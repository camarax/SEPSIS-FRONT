import dash_bootstrap_components as dbc
from dash import html

def resultat(resultat):
    alert = dbc.Alert(
        [
            html.H4(f"Test {resultat['Prédiction']} à {resultat['Probalité']} %", className="alert-heading"),
            html.P(
                f"D'après des analyse, cet individu à un test positif avec une probalité de {resultat['Probalité']} %."
            ),
            html.Hr(),
            html.P(
                "Ce modèle fournit des prédictions probabilistes et il est recommandé de les faire évaluer par un professionnel compétent avant de prendre des décisions basées sur celles-ci! ",
                className="mb-0",
            ),
        ]
    )
    return alert