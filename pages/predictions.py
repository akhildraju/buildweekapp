# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer


df = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data")

col_names= ['symboling', 'normalized-losses','make', 'fuel-type', 'aspiration',  'num-of-doors',
            'body-style', 'drive-wheels', 'engine-location', 'wheel-base', 'length', 'width', 'height',
            'curb-weight','engine-type','num-of-cylinders','engine-size','fuel-system','bore','stroke','compression-ratio','horsepower','peak-rpm','citympg','highwaympg','price']
df.columns = col_names

df["citympg"] = pd.to_numeric(df.citympg, errors='coerce')
df["citympg"] = df.citympg.astype(float)

#Replace all ? to nan 
df[col_names] = df[col_names].replace({'?':np.nan})

# Replace pricae where there is no value to to mean value 
df["price"] = df.price.astype(float)
df['price'].fillna(df['price'].mean(), inplace = True)

df['num-of-doors'].fillna('4', inplace = True)
df["num-of-doors"].replace({"two": "2", "four": "4"}, inplace=True)
df['num-of-doors'] = df['num-of-doors'].astype('int8')

df['num-of-cylinders'].fillna('4', inplace = True)
df["num-of-cylinders"].replace({"two": "2", "four": "4", "five" :"5", "three":"3", "six" :"6", "eight":"8", "twelve":"12" }, inplace=True)
df['num-of-cylinders'] = df['num-of-cylinders'].astype('int8')

all_features= ['num-of-doors', 'wheel-base', 'length', 'width', 'height', 'curb-weight', 'num-of-cylinders','engine-size','bore','stroke','compression-ratio','horsepower','peak-rpm','citympg','highwaympg']

# Imports from this application
from app import app

drop_options = []
for str in all_features:
    drop_options.append({'label':str, 'value':str})

    # drop_options['label'] = str
    # drop_options['value'] = str

dcc.Dropdown(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montreal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    placeholder="Select a city",
)  




f1_drop = dcc.Dropdown(
        id='f1_name',
        options=drop_options,
        placeholder="Select first Feature",
        style={'color': 'black'}

    )

f1_value = dcc.Input(
    id='f1_value',
    placeholder='Feature 1 Value',
    type='text',
    value=''
)
f2_drop = dcc.Dropdown(
        id='f2_name',
        options=drop_options,
        placeholder="Select second Feature",
        style={'color': 'black'}
    )

f2_value = dcc.Input(
    id='f2_value',
    placeholder='Feature 2 Value',
    type='text',
    value=''
)
f3_drop = dcc.Dropdown(
        id='f3_name',
        options=drop_options,
        placeholder="Select third Feature",
        style={'color': 'black'}
    )

f3_value = dcc.Input(
    id='f3_value',
    placeholder='Feature 3 Value',
    type='text',
    value=''
)  

button = html.Div(
    [
        dbc.Button("Predict Car Price", id="predict-button", className="predict"),
        # html.Span(id="output-text", style={"vertical-align": "middle"}),
    ]
)

out_button = html.Div(
    [
        html.Span(id="output-text", style={"vertical-align": "middle"}),
    ]
)


# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions

            Select 3 Features to predict the pricae of  car

            """
        ),

        dcc.Markdown(
            """
            Select First Feature and It's value     
            """,
            style={"white-space": "pre"}
        ),

        f1_drop, 
        f1_value,
        
        dcc.Markdown(
            """
            Select Second Feature and It's value
            """,
            
            style={"white-space": "pre"}
        ),

        f2_drop, 
        f2_value,

        dcc.Markdown(
            """
            Select Third Feature and It's value
            """,
            style={"white-space": "pre"}
        ),

        f3_drop, 
        f3_value,

        button
        

    ],
    md=5,
)

column2 = dbc.Col(
    [
        out_button,
    ],
    md=3
)

@app.callback(
    Output("output-text", "children"), 
    [Input("predict-button", "n_clicks"), Input("f1_name", "value"),Input("f1_value", "value"),Input("f2_name", "value"),
    Input("f2_value", "value"), Input("f3_name", "value"), Input("f3_value", "value"), ]
)
def on_button_click(n, f1_name, f1_value, f2_name, f2_value, f3_name, f3_value):
    if n is not None and  n  >= 1:
        
        return "Predicted Car Price = $" + (predict(f1_name, f1_value, f2_name, f2_value, f3_name, f3_value))

layout = dbc.Row([column1, column2])


def predict(f1_name, f1_value, f2_name, f2_value, f3_name, f3_value):

    target = 'price'
    features = []
    values = []
    if f1_name is not None and f1_value is not None and len(f1_value) > 0:
        features.append(f1_name)
        values.append(int(f1_value))

    if f2_name is not None and f2_value is not None and len(f2_value) > 0:
        features.append(f2_name)
        values.append(int(f2_value))

    if f3_name is not None and f3_value is not None and len(f3_value) > 0:
        features.append(f3_name)
        values.append(int(f3_value))

    train, test = train_test_split(df, test_size=0.2)
    train, validate = train_test_split(train, test_size=0.2)

    # #getting the baseline
    y_train = train[target]
    y_validate = validate[target]
    baseline = y_train.value_counts()

    x_train = train[features]
    x_val   = validate[features]
    x_test  = test[features]

    y_train = train[target]
    y_val   = validate[target]

    linear_reg = LinearRegression()

    imputer = SimpleImputer()
    x_train_imputed = imputer.fit_transform(x_train)
    x_val_imputed = imputer.fit_transform(x_val)

    linear_reg.fit(x_train_imputed, y_train)
    linear_reg.predict(x_train_imputed)

    test_case = []
    test_case.append(values)
    predicted_value = linear_reg.predict(test_case)


    formatted_value = '%.2f' %  predicted_value[0]
    return formatted_value


