from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from PIL import Image


GAMES = pd.read_csv('games_flat_xml_2012-2018.csv')
TV = pd.read_csv('TV_Ratings_onesheet.csv')

#Join 
DATA = GAMES.merge(TV,on='TeamIDsDate')

#cleaning data

# Getting the list of unique Home Team names
team_names = TV["Home Team"].unique()
other_team_index = np.isin(team_names, ["Alabama", "Tennessee"], invert = True)
# Creating an object for "options" in the dropdown menu.  It is all team names except Alabama and Tennessee (UT)
team_names_dict = [{'label' : tn, 'value': tn} for tn in team_names[other_team_index]]
tn_im=f"im_folder/tn.png"
al_im=f"im_folder/al.png"
asu_im=f"im_folder/asu.png"
ak_im=f"im_folder/ak.png"
aub_im=f"im_folder/aub.png"
byu_im=f"im_folder/byu.png"
cal_im=f"im_folder/cal.png"
ucf_im=f"im_folder/ucf.png"
clem_im=f"im_folder/clem.png"
duke_im=f"im_folder/duke.png"
fl_im=f"im_folder/fl.png"
fsu_im=f"im_folder/fsu.png"
fres_im=f"im_folder/fres.png"
uga_im=f"im_folder/uga.png"
gt_im=f"im_folder/gt.png"
hawaii_im=f"im_folder/hawaii.png"
hous_im=f"im_folder/hous.png"
ks_im=f"im_folder/ks.png"
uk_im=f"im_folder/uk.png"
latech_im=f"im_folder/latech.png"
lou_im=f"im_folder/lou.png"
lsu_im=f"im_folder/lsu.png"
mem_im=f"im_folder/mem.png"
mia_im=f"im_folder/mia.png"
mich_im=f"im_folder/mich.png"
miss_im=f"im_folder/miss.png"
ms_im=f"im_folder/ms.png"
missouri_im=f"im_folder/missouri.png"
nc_state_im=f"im_folder/nc_state.png"
nw_im=f"im_folder/northwestern.png"
nd_im=f"im_folder/notre_dame.png"
ok_im=f"im_folder/oklahoma.png"

im_dict={'alabama': al_im}




app = Dash(__name__)

app.layout = html.Div(children=[html.Div([
        html.Label('Choose a Team'),
        dcc.Dropdown(id='droppy',options= team_names_dict,style = {'width': '400px'})
    ]),
        html.Img(id='Image',src=Image.open(nw_im))
])

if __name__ == '__main__':
    app.run_server(debug=True,port=8054)



