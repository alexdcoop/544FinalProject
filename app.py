from turtle import home
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
from datetime import date, datetime

#GAMES = pd.read_csv(r'C:\Users\kevin\OneDrive\Documents\BZAN_544_Decision_Support\f_project\544FinalProject\games_flat_xml_2012-2018.csv') 
#TV = pd.read_csv(r'C:\Users\kevin\OneDrive\Documents\BZAN_544_Decision_Support\f_project\544FinalProject\TV_Ratings_onesheet.csv')  
GAMES = pd.read_csv('games_flat_xml_2012-2018.csv')
gcolumnsWeWant = ['homename','visname','date','attend']
GAMES = GAMES[gcolumnsWeWant]

TV = pd.read_csv('TV_Ratings_onesheet.csv')
tvcolumnsWeWant = ['Home Team', 'Visitor Team', 'Date', 'VIEWERS', 'Network']
TV = TV[tvcolumnsWeWant]


#Define Home team Labels for our dropdown
gamesUHomeDict = [{'label' : tn, 'value': tn} for tn in np.unique(GAMES.homename)]
TVUHomeDict = [{'label' : tn, 'value': tn} for tn in np.unique(TV['Home Team'])]

#Get years
GAMES['year'] = [datetime.strptime(date, '%m/%d/%Y').year for date in GAMES.date]
gYears = np.unique(GAMES['year'])
gDict = [{'label' : tn, 'value': tn} for tn in gYears]

TV['year'] = [datetime.strptime(date, '%m/%d/%Y').year for date in TV.Date]
tvYears = np.unique(TV['year'])
tvDict = [{'label' : tn, 'value': tn} for tn in tvYears]



app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],meta_tags=[
                  {"name": "viewport", "content": "width=device-width, initial-scale=1"}
                  ])
app.config.suppress_callback_exceptions=True

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
            html.H4("Home Team"),
            #Home team dropdown
            dcc.Dropdown(id='homeTeam', placeholder="Select Home Team" ,options=gamesUHomeDict),
            #Year dropdown
            html.H4('Year'),
            dcc.RadioItems(id='year',options=gDict),
            #GRAPH
            dcc.Graph(id='graph'),
            #TABLE
            html.Table(id='Table',children = [],className='table table-striped')]
                
        #### Place content for tv viewership here
    elif pathname == "/tv":
        return [
            #Home team dropdown
            html.H4("Home Team"),
            dcc.Dropdown(id='homeTeam', placeholder="Select Home Team" ,options=TVUHomeDict),
            #Year dropdown
            html.H4('Year'),
            dcc.RadioItems(id='year',options=tvDict),
            #GRAPH
            dcc.Graph(id='graph'),

            #PIE CHART FOR NETWORK AND TITLE
            html.Div([html.H4('Network Share',style={'textAlign': 'center'}),dcc.Graph(id='pie')]),
            
            #TABLE
            html.Table(id='Table',children = [],className='table table-striped')]

#THIS IS THE CALLBACK FOR TABLE
@app.callback(
    Output("Table", "children"),
    Input("homeTeam", 'value'),
    [Input("url", "pathname")],
    Input('year', 'value')
)
def update_table(value,pathname,year):
    #create the table
    tableChildren = create_table(value, pathname,year)
    return tableChildren


# THIS IS THE CALLBACK FOR THE PLOT
@app.callback(
    Output('graph', 'figure'),
    Input('year', 'value'),
    Input('homeTeam', 'value'),
    [Input("url", "pathname")]
)
def update_graph(year, homeTeam, pathname):
    #create the graph
    data = create_graph(year,homeTeam, pathname)
    
    title = "{homeTeam} {y}".format(homeTeam = 'All teams' if homeTeam is None else homeTeam, y = 'Attendance' if pathname == '/' else 'Viewership')
    
    fig = dict({
        "data": [data],
        "layout": {"title": {"text": title}}
    })
    
    return fig

### creating the graph
def create_graph(year, homeTeam, pathname):
    #Make X and Y
    if pathname == '/':
        Data = GAMES
        if year is not None:
            #subset year
            Data = Data[Data['year'] == year]
        
        if homeTeam is None:
            #Get all
            X=Data.date
            Y=Data.attend
        else:
            #subset hometeam
            X = Data[Data.homename == homeTeam].date
            Y = Data[Data.homename == homeTeam].attend
           
    elif pathname == '/tv':
        Data = TV
        if year is not None:
            #subset year
            Data = Data[Data['year'] == year]
        
        if homeTeam is None:
            #Get all
            X=Data.Date
            Y=Data.VIEWERS
        else:
            #subset hometeam
            X = Data[Data['Home Team'] == homeTeam].Date
            Y = Data[Data['Home Team'] == homeTeam].VIEWERS
    else:
        print('ERROR CREATING TABLE')
        
    DATA = dict(
        type = "scatter",
        mode = "markers",
        x=X,
        y=Y,
        hovertemplate= ' %{y} <br> Date: %{x} ',
        name=homeTeam,
        marker=dict(
            color='rgb(255,130,0)',
            opacity=.6,
            size = 7    
    ))
    return DATA

#THIS IS THE CALLBACK FOR THE PIE CHART
@app.callback(
    Output('pie', 'figure'),
    Input('year', 'value'),
    Input('homeTeam', 'value')
)
## creating the pie chart

def pie_chart(year,homeTeam):
    Data = TV
    if year is not None:
        Data = Data[Data['year'] == year] 
    if homeTeam is not None:
        Data=Data[Data['Home Team'] == homeTeam]       
    fig2 = px.pie(Data, values=('VIEWERS'), names='Network', color='Network',
        color_discrete_map={'ABC':'grey',
                            'CBS':'royalblue',
                            'ESPN':'red',
                            'ESPN2':'cyan',
                            'ESPNU':'yellow',
                        "ESPNews":'purple' })
    return fig2



### creating the table
def create_table(homeTeam, pathname, year):
    if pathname == '/':
        if homeTeam is not None:
            DATA = GAMES[GAMES.homename == homeTeam]
        else:
            DATA = GAMES
    elif pathname == '/tv':
        if homeTeam is not None:
            DATA = TV[TV['Home Team'] == homeTeam]
        else:
            DATA = TV
    else:
        print('ERROR CREATING TABLE')
        
    #Subset year
    if year is not None:
        DATA = DATA[DATA['year'] == year]
        
    tableChildren = [
            html.Thead([
                html.Tr([html.Th(col) for col in DATA.columns])
                ]),
            html.Tbody([
                html.Tr([
                    html.Td(DATA.iloc[i][col]) for col in DATA.columns
                ]) for i in range(len(DATA))
            ])
            ]
    
    return tableChildren

if __name__ == '__main__':
    app.run_server(debug=True)
