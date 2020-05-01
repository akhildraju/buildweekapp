# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import base64


# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Esimate Price of Cars based on other features

            Based on the existing data, you can predict the price of a car based on features like horsepower 
            etc.   

            """
        ),
        dcc.Link(dbc.Button('Estimate', color='primary'), href='/predictions')
    ],
    md=4,
)


import pandas as pd
import numpy as np

df = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data")

col_names= ['symboling', 'normalized-losses','make', 'fuel-type', 'aspiration',  'num-of-doors',
            'body-style', 'drive-wheels', 'engine-location', 'wheel-base', 'length', 'width', 'height',
            'curb-weight','engine-type','num-of-cylinders','engine-size','fuel-system','bore','stroke','compression-ratio','horsepower','peak-rpm','citympg','highwaympg','price']
df.columns = col_names
df.loc[df['price'] == '?'] = np.nan
df["price"] = df.price.astype(float)
df['price'].fillna(df['price'].mean(), inplace = True)

target = 'price'
fig = px.histogram(df[target], x="price",   labels={'price':'Price of the Car', 'y':'Total Count'})
fig.update_layout(
    title="Car Model Prices",
    xaxis_title="Car Prices (USD)",
    yaxis_title="Model Count",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#7f7f7f"
    )
)


image_filename = 'main1.png' # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read())


# gapminder = px.data.gapminder()
# fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
#            hover_name="country", log_x=True, size_max=60)

# column2 = dbc.Col(
#     [
#         dcc.Graph(figure=fig),
#     ]
# )

column2 = dbc.Col(
    [
        html.Img(src=app.get_asset_url('main.png'), style={'height':'100%', 'width':'50%'})
    ]
)

layout = dbc.Row([column1, column2])