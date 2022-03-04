from dash import Dash, dcc, html, Input, Output
import dash
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import dash_bootstrap_components as dbc
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd

GAMES = pd.read_csv('games_flat_xml_2012-2018.csv')
TV = pd.read_csv('TV_Ratings_onesheet.csv')

#Join 
DATA = GAMES.merge(TV,on='TeamIDsDate')


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],meta_tags=[
                  {"name": "viewport", "content": "width=device-width, initial-scale=1"}
                  ])


### creating the side bar menu
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 115,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}
# padding for the page content/links
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H1("Brand Recognition Metric", className="display-12"),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Stadium Attendance", href="/", active="exact"),
                dbc.NavLink("TV Viewership", href="/tv", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

### THIS IS FILLER FOR THE SIDE BAR MENU. CONTENT IS WHAT IS GOING TO BE SHOWED AFTER CLICKING SIDE BAR OPTION
content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)


app.layout = html.Div(children=[
    ### layout for the webpage title
    dbc.Card(
        dbc.CardBody([
            dbc.Row([
        html.H1(children='College Football Team Brand Recognition',style={'textAlign': 'center'}),

        html.Div(children='''
            Cole Felix, Jake Foard, Alex Cooper, & Kevin Bellefeuil
        ''',style={'textAlign': 'center'})])])),
    #### Div for the sidebar and content
    html.Div([dcc.Location(id="url"),
    sidebar,
    content])
])


###### THIS IS THE CALLBACK FOR THE SIDE BAR MENU
@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)

def render_page_content(pathname):
    
    if pathname == "/":
        ######## Place the content for stadium attendance here
        return [
                html.H1('Sales Count',
                        style={'textAlign':'center'}),
                dcc.Graph(id='bargraph',
                         figure=px.bar(retail, barmode='group', x='Company',
                         y='Sales'))
                ]
        #### Place content for tv viewership here
    elif pathname == "/tv":
        return [
                html.H1('Store Count',
                        style={'textAlign':'center'}),
                dcc.Graph(id='bargraph',
                         figure=px.bar(retail, barmode='group', x='Company',
                         y='Stores'))
                ]



if __name__ == '__main__':
    app.run_server(debug=True)
