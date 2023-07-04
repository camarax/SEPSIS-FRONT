import dash_bootstrap_components as dbc
from dash import Input, Output, State, html, callback, ctx
from dash_bootstrap_components._components.Container import Container
import dash_mantine_components as dmc
from dash_iconify import DashIconify
import requests
import json


# Import des composants

from .resultat import resultat


body =  dbc.Container([
    dbc.Row([
        dbc.Col([
            
            dbc.Row([
                # Left
                dbc.Col([  
                    dbc.Row([dbc.Col([
                        dmc.Center([
                            dmc.Text(
                                "Scan Sepsis",
                                variant="gradient",
                                gradient={"from": "red", "to": "yellow", "deg": 45},
                                style={"fontSize": 50},
                            )
                        ])
                    ])]),
                    dbc.Row([dbc.Col([
                        dmc.Text(
                            "Diagnostic du prélevement sanguin",
                            style={"fontSize": 15},
                        )
                    ])]),
                    html.Br(),
                    dbc.Row([
                        # Form gauche
                        dbc.Col([
                            dmc.TextInput(label="PRG :", type="number", id="input-prg"),
                            dmc.TextInput(label="PL:", type="number", id="input-pl"),
                            dmc.TextInput(label="PR:", type="number", id="input-pr"),
                            dmc.TextInput(label="SK:", type="number", id="input-sk"),
                        ]),
                        # Form droite
                        dbc.Col([
                            dmc.TextInput(label="TS:", type="number", id="input-ts"),
                            dmc.TextInput(label="M11:", type="number", id="input-m11"),
                            dmc.TextInput(label="BD12:", type="number", id="input-bd12"),
                            dmc.TextInput(label="AGE:", type="number", id="input-age"),

                        ])
                    ]),
                    dbc.Row([
                        dbc.Col([
                            dmc.TextInput(label="INSSURANCE:", type="number", id="input-inssurance"),
                        ])
                    ]),
                    html.Br(),
                    # Row botton
                    dbc.Row([
                        dbc.Col([
                            dmc.Button(
                                "PRÉDDIRE",
                                variant="gradient",
                                gradient={"from": "indigo", "to": "cyan"},
                                fullWidth=True,
                                id="btn-predict"
                            ),
                        ]),

                        dbc.Col([
                            dmc.Button(
                                "ANNULER",
                                variant="gradient",
                                gradient={"from": "orange", "to": "red"},
                                fullWidth=True,
                                id="btn-cancel"
                            )
                        ])
                    ])
                ],width={"size":"5"}),

                # Right
                dbc.Col([
                    dmc.Center([
                        dmc.Text(
                            "Résultat",
                            variant="gradient",
                            gradient={"from": "Green", "to": "yellow", "deg": 45},
                            style={"fontSize": 35},
                        ),
                    ]),
                    dmc.Center([
                        html.Div(id="output-predict"),
                    ]),
                ], id="right-block")



            ])
        ])
    ],id="row-body")
])


@callback(
    Output("output-predict", "children"),
    [
        Input("btn-predict", "n_clicks"),
        Input("input-prg", "value"),
        Input("input-pl", "value"),
        Input("input-pr", "value"),
        Input("input-sk", "value"),
        Input("input-ts", "value"),
        Input("input-m11", "value"),
        Input("input-bd12", "value"),
        Input("input-age", "value"),
        Input("input-inssurance", "value"),
    ],
)
def predict(n_clicks,value_prg,value_pl,value_pr,value_sk,value_ts,value_m11,value_bd12,value_age,value_inssurance):
    if "btn-predict" == ctx.triggered_id:
        data = {
            "PRG" : value_prg,
            "PL" : value_pl,
            "PR" : value_pr,
            "SK" : value_sk,
            "TS" : value_ts,
            "M11" : value_m11,
            "BD12" : value_bd12,
            "Age" : value_age,
            "Insurance" : value_inssurance
        }
        if any(value == "" for value in data.values()):
            error = dmc.Alert("Veillez renseignez tous les champs avant de cliquer sur le bouton prédire. Merci !!!", title="Erreur!", color="red"),
            return error
        else:
            # faire appel à l'api
            data_float = {cle: float(value) for cle, value in data.items()}
            headers = {'Content-Type': 'application/json',"Authorization":"lesecret"}
            response = requests.post("http://127.0.0.1:5000/predict", json=data_float, headers=headers).json()
            return resultat(response)

@callback(
    [
        Output("input-prg", "value"),
        Output("input-pl", "value"),
        Output("input-pr", "value"),
        Output("input-sk", "value"),
        Output("input-ts", "value"),
        Output("input-m11", "value"),
        Output("input-bd12", "value"),
        Output("input-age", "value"),
        Output("input-inssurance", "value"),
    ],

    Input("btn-cancel", "n_clicks"),
    prevent_initial_call=True
)
def cancel(n_clicks):
    if "btn-cancel" == ctx.triggered_id:
        return "","","","","","","","",""
