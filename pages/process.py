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
# column1 = dbc.Col(
#     [
#         dcc.Markdown(
#             """
#             I guess you could say I am a big car guy. Ever since I was growing up I always had a great fascination with cars. So when asked to do a data science project, I thought why not do it about a topic I really like?' 
#             So I started looking for datasets that contain cars. The dataset I used is from the UCI Machine Learning Repository (https://archive.ics.uci.edu/ml/datasets/Automobile) Before starting the notebook I took a look at the dataset and my initial thoughts were:
            
#             - There are many features that are not relevant for prediction such as ‘Make of the car’
#             - There are features that have direct impact on prediction such as Number of cylinders, HorsePower  
#             - This was  a very small dataset. I probably should have selected a dataset that has more data but I didn’t want to change at the last minute.


#             Here is the distplot that shows the price of a car and number of models with that price. Here is the distplot that shows the price of a car and number of models with that price.This will be what I am predicting today. 
#             I will be taking input for different features and just simply using them to predict the price of car.
  

#             """
#         ),
#         html.Img(src=app.get_asset_url('distplot.png'), style={'height':'50%', 'width':'50%',  'display': 'flex', 
#         'textAlign': 'center', 'align-items': 'center', 'justify-content': 'center'}),

#         dcc.Markdown(
#             """
            
#             The dataset I selected had a lot of missing data or the data had been replaced with a “?”. 
#             I had to cleanup my code to make it work.  
  
#             """
#         ),

#         dcc.Markdown(
#             """
#             The accuracy score for my test set came in at 65% which would mean my predictive model correctly identified the price of 65% of cars in this dataset. 
#             I wanted to take a deeper look into my dataset so I created a Shapley value plot to see what affect some of the bigger attributes were having on the graph.  
  
#             """
#         ),
#         html.Img(src=app.get_asset_url('force_plot.png'), style={'height':'30%', 'width':'100%',  'display': 'flex'}),

#         dcc.Markdown(
#             """
#             I wanted to see what features impact the price. Because of the shapley graph, number of cylinders  was heavily impacting the price outcome. 
#             I wanted to take a better look at this correlation so I made a Seaborn plot comparing the number of cylinders to price as well as two other features (“horsepower”,”curb-weight”).  
  
#             """
#         ),
#         html.Img(src=app.get_asset_url('multichart.png'), style={'height':'30%', 'width':'30%',  'display': 'flex', 
#         'textAlign': 'center', 'align-items': 'center', 'justify-content': 'center'}),

#         dcc.Markdown(
#             """
#             For me the hardest part about this project was just deciding between classification or regression when it came down to this dataset. 
#             I found that in the end regression seemed to do better with the dataset as well as the target I selected (“price”). 
#             Looking back I could have used a bigger dataset that could have given us a more accurate prediction. 
  
#             """
#         )

#     ],
# )

# layout = dbc.Row([column1])

column1 = dbc.Col(
    [
        html.H1(children="Process" ),

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
        html.Img(src=app.get_asset_url('distplot.png'), style={'height':'262px', 'width':'441px',  'display': 'flex', 
        'textAlign': 'center', 'align-items': 'center', 'justify-content': 'center'}),

        html.Pre(""" 
        
        """),

       dcc.Markdown(
            """
            
            The dataset I selected had a lot of missing data or the data had been replaced with a “?”. 
            I had to cleanup my code to make it work.  
  
            """
        ),

        html.Img(src=app.get_asset_url('cleanupcode.png'), style={'height':'347px', 'width':'1241px',  'display': 'flex'}),

        html.Pre("""    
        """),


        dcc.Markdown(
            """
            First I wanted to get my baseline metrics such as MAE since we had to use a regression model. MAE or Mean Absolute Error basically takes the difference between the actual value and the predicted value for that instance.  
  
            """
        ),
      
        html.Img(src=app.get_asset_url('code1.png'), style={'height':'111px', 'width':'486px',  'display': 'flex', 
        'textAlign': 'center', 'align-items': 'center', 'justify-content': 'center'}),


        html.Pre("""
        """),

        dcc.Markdown(
            """
            After using the code above on not only the train error, but the test and validation errors as well, I got that absolute mean errors for my train and test datasets (regression model) had shown to be $3180 and $3366. I also tested for the r^2 scores using the following code:
 
            """
        ),
      
        html.Img(src=app.get_asset_url('code2.png'), style={'height':'97px', 'width':'455px',  'display': 'flex', 
        'textAlign': 'center', 'align-items': 'center', 'justify-content': 'center'}),


        html.Pre("""
        """),

        dcc.Markdown(
            """
            R-squared is a statistical measure of how close the data are to the fitted regression line. And since this is a regression model it should perfectly showcase what we should expect the behavior of our train and test datasets to be. The r^2 scores I got for my train and test dataset were 0.6803897444390236 for train, and 0.3775318021597549 for my test.

            R-squared is always between 0 and 100%:  
            - 0% indicates that the model explains none of the variability of the response data around its mean.
            - 100% indicates that the model explains all the variability of the response data around its mean.
            
            In general, the higher the R-squared, the better the model fits your data. 

            """
        ),
      
        html.Pre("""
        """),

 
        dcc.Markdown(
            """
            With these metrics in mind, we can take a look at and see which features are driving the dataset towards a negative value and which are moving to a positive value. For this instance I made a Shapley plot
 
  
            """
        ),
        html.Img(src=app.get_asset_url('force_plot.png'), style={'height':'181px', 'width':'896px',  'display': 'flex'}),

        html.Pre("""    
        """),

        dcc.Markdown(
            """
            I wanted to see what features impact the price. I have created Permutaion Feature Importance to see the relationship between the selected features and my target column car price. I have used n_repeats=10 to randomly shuffle.      
  
            """
        ),
      
        html.Img(src=app.get_asset_url('permimp.png'), style={'height':'576px', 'width':'958px',  'display': 'flex', 
        'textAlign': 'center', 'align-items': 'center', 'justify-content': 'center'}),

        html.Pre("""
        """),

        dcc.Markdown(
            """
            Because of the shapley graph, number of cylinders  was heavily impacting the price outcome. 
            I wanted to take a better look at this correlation so I made a Seaborn plot comparing the number of cylinders to price as well as two other features (“horsepower”,”curb-weight”).  
            """
        ),
      
        html.Img(src=app.get_asset_url('multichart.png'), style={'height':'578px', 'width':'700px',  'display': 'flex', 
        'textAlign': 'center', 'align-items': 'center', 'justify-content': 'center'}),


        html.Pre("""
        """),

        html.H1(children="Example Prediction" ),

        dcc.Markdown(
            """
            Where the model succeeds/fails depends on the features. If given incorrect values it will give you an estimate that seems like an outlier when it comes to similar vehicles in that price range as well. If we take for example the 2020 q60 red sport 400 RWD (rear wheel drive), we can get a quick price estimate from google:

            """
        ),
      
        html.Img(src=app.get_asset_url('samplecar.png'), style={'height':'647px', 'width':'454px',  'display': 'flex', 
        'textAlign': 'center', 'align-items': 'center', 'justify-content': 'center'}),


        html.Pre("""
        """),

        dcc.Markdown(
            """
            When using the predictor and implementing some its features we get:

            """
        ),
      
        html.Img(src=app.get_asset_url('predct.png'), style={'height':'578px', 'width':'700px',  'display': 'flex', 
        'textAlign': 'center', 'align-items': 'center', 'justify-content': 'center'}),


        html.Pre("""
        """),

        dcc.Markdown(
            """
            Now of course, the code does not account for the twin turbocharged engine, the pricey leather and alcantara interior , nor the safety features this car comes with but it does estimate it within a very appropriate price range.   

            """
        ),


    ],
)

column_space = dbc.Col(
    [
        html.P(children='<br/>'),
    ],
)

column2 = dbc.Col(
    [
        html.Pre("""
        
        
        """),

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

row1= dbc.Row([column1])
row2= dbc.Row([column2])

row = html.Div(
    [
        dbc.Row([column1]),

    ]
)


layout = row