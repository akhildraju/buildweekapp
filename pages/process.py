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


            Here is the distplot that shows the price of a car and number of models with that price. Here is the distplot that shows the price of a car and number of models with that price.This will be what I am predicting today. 
            I will be taking input for different features and just simply using them to predict the price of car.
  

            """
        ),
        html.Img(src=app.get_asset_url('distplot.png'), style={'height':'50%', 'width':'50%',  'display': 'flex', 
        'textAlign': 'center', 'align-items': 'center', 'justify-content': 'center'}),

        dcc.Markdown(
            """
            
            The dataset I selected had a lot of missing data or the data had been replaced with a “?”. 
            I had to cleanup my code to make it work.  
  
            """
        ),

        dcc.Markdown(
            """
            The accuracy score for my test set came in at 65% which would mean my predictive model correctly identified the price of 65% of cars in this dataset. 
            I wanted to take a deeper look into my dataset so I created a Shapley value plot to see what affect some of the bigger attributes were having on the graph.  
  
            """
        ),
        html.Img(src=app.get_asset_url('force_plot.png'), style={'height':'30%', 'width':'100%',  'display': 'flex'}),

        dcc.Markdown(
            """
            I wanted to see what features impact the price. Because of the shapley graph, number of cylinders  was heavily impacting the price outcome. 
            I wanted to take a better look at this correlation so I made a Seaborn plot comparing the number of cylinders to price as well as two other features (“horsepower”,”curb-weight”).  
  
            """
        ),
        html.Img(src=app.get_asset_url('multichart.png'), style={'height':'30%', 'width':'30%',  'display': 'flex', 
        'textAlign': 'center', 'align-items': 'center', 'justify-content': 'center'}),

        dcc.Markdown(
            """
            For me the hardest part about this project was just deciding between classification or regression when it came down to this dataset. 
            I found that in the end regression seemed to do better with the dataset as well as the target I selected (“price”). 
            Looking back I could have used a bigger dataset that could have given us a more accurate prediction. 
  
            """
        )

    ],
)

layout = dbc.Row([column1])