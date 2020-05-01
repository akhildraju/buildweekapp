# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
            I guess you could say I am a big car guy. Ever since I was growing up I always had a great fascination with cars. So when asked to do a data science project, I thought why not do it about a topic I really like?' 
            So I started looking for datasets that contain cars. The dataset I used is from the UCI Machine Learning Repository (https://archive.ics.uci.edu/ml/datasets/Automobile) Before starting the notebook I took a look at the dataset and my initial thoughts were:
            
            - There are many features that are not relevant for prediction such as ‘Make of the car’
            - There are features that have direct impact on prediction such as Number of cylinders, HorsePower  
            - This was  a very small dataset. I probably should have selected a dataset that has more data but I didn’t want to change at the last minute.


            Here is the distplot that shows the price of a car and number of models with that price. I chose price as a target.  

            """
        ),
        html.Img(src=app.get_asset_url('distplot.png'), style={'height':'50%', 'width':'50%',  'display': 'flex', 
        'textAlign': 'center', 'align-items': 'center', 'justify-content': 'center'}),

    ],
)

layout = dbc.Row([column1])