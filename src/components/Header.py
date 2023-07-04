import dash_bootstrap_components as dbc
from dash import Input, Output, State, html,  callback, ctx
from dash_bootstrap_components._components.Container import Container
import dash_mantine_components as dmc
from dash_iconify import DashIconify


# import des composants
from .stat import modal

PLOTLY_LOGO = "assets/logo.png"

search_bar = dbc.Row(
    [
        dbc.Col(
            dmc.Button(
                "Etat système",
                variant="outline",
                rightIcon=DashIconify(icon="simple-icons:statuspal"),
                color="orange",
                id="btn-health"
            ),
            width="auto",
        ),
    ],
    className="g-0 ms-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(dbc.NavbarBrand("MEDISCAN", className="ms-2")),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="#",
                style={"textDecoration": "none"},
            ),
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            dbc.Collapse(
                search_bar,
                id="navbar-collapse",
                is_open=False,
                navbar=True,
            ),
            modal,
        ], fluid=True,
       
    ),
    color="dark",
    dark=True,

)

# @callback(
#     Output("input-healt", "value"),
#     Input("btn-health", "n_clicks"),
# )
# def health(n_clicks):
#     if "btn-health" == ctx.triggered_id:
#         pass