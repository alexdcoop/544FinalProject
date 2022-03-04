from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np


GAMES = pd.read_csv('games_flat_xml_2012-2018.csv')
TV = pd.read_csv('TV_Ratings_onesheet.csv')

#Join 
DATA = GAMES.merge(TV,on='TeamIDsDate')

app = Dash(__name__)

app.layout = html.Div(children=[])

if __name__ == '__main__':
    app.run_server(debug=True)
