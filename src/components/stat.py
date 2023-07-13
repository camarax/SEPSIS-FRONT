import dash_bootstrap_components as dbc
from dash import Input, Output, State, html, callback, ctx
import requests
import time



modal = html.Div(
    [
        # dbc.Button("Open modal", id="open", n_clicks=0),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Health")),
                
                dbc.ModalBody([
                    html.Div(id="outout-healt")
                ]),
                dbc.ModalFooter(
                    dbc.Button(
                        "Close", id="close", className="ms-auto", n_clicks=0
                    )
                ),
            ],
            id="modal",
            is_open=False,
        ),
    ]
)


@callback(
    [
        Output("modal", "is_open"),
        Output("outout-healt", "children")
    ],

    [Input("btn-health", "n_clicks"), Input("close", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        # faire apel à l'api health
        headers = {'Content-Type': 'application/json',"Authorization":"lesecret"}
        start_time = time.time()
        response = requests.get("http://ec2-15-188-239-47.eu-west-3.compute.amazonaws.com:5000/health", headers=headers)
        response_time = "{:.2f}".format(time.time() - start_time)
        status = "Okay" if response.status_code == 200 else "Bad"
        return not is_open, html.P(f"Etat système : {status}, temps de réponse : {response_time} sc")
    return is_open, html.P("Etat système : Okay, temps de réponse : 0.02 sc")