import pandas as pd 
import seaborn as sns
import numpy as np 
import dash
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

artist_df = pd.read_csv("Artists.csv")
artwork_df = pd.read_csv("Artworks.csv")

def combined_card_1(metrics, bg_colour="#2D2D2D", text_colour="#FFFFFF"):
    return html.Div(
        style={
            'backgroundColor': bg_colour,
            'color': text_colour, 
            'borderRadius': '15px',
            'padding': '20px',
            'width': '250px', 
            'boxShadow': '0px 4px 10px rgba(0, 0, 0, 0.5)',
            'margin': '5px',
            'border': '1px solid #444444',
            'fontFamily': 'Roboto, sans-serif'             
        },
        children=[
            html.H2('Dataset', style={'fontSize':'25px','marginTop': '0px' ,'marginBottom': '20px', 'color': '#858383'}),
            html.Div([
                html.P(f"Artists.csv Rows: {metrics['artist_num_feats']}"),
                html.P(f"Artworks.csv Rows: {metrics['artwork_num_feats']}", style={'margin': '10px 0'}),
                html.P(f"Memory: {metrics['memory']}"),
            ], style={'textAlign': 'left', 'fontSize': '16px'})
        ]
    )
def combined_card_2(metrics, bg_colour="#2D2D2D", text_colour="#FFFFFF"):
    return html.Div(
        style={
            'backgroundColor': bg_colour,
            'color': text_colour,
            'borderRadius': '15px',
            'padding': '20px',
            'width': '250px',
            'boxShadow': '0px 4px 10px rgba(0, 0, 0, 0.5)',
            'margin': '5px',
            'border': '1px solid #444444',
            'fontFamily': 'Roboto, sans-serif',
        },
        children=[
            html.H2('Artists', style={'fontSize': '25px','marginTop': '0px', 'marginBottom': '0px', 'color': '#858383', 'textAlign': 'center'}),
            html.Div([
                html.P(f"{metrics['num_artists']}"),
            ], style={'textAlign': 'center', 'fontSize': '35px', 'marginTop': '0px', 'marginBottom': '0px'})
        ]
    )

def combined_card_3(metrics, bg_color='#2D2D2D', text_colour='#FFFFFF'):
    return html.Div(
        style={
            'backgroundColor': bg_color,
            'color': text_colour,
            'borderRadius': '15px',
            'padding': '20px',
            'width': '250px',
            'boxShadow': '0px 4px 10px rgba(0, 0, 0, 0.5)',
            'margin': '5px',
            'border': '1px solid #444444',
            'fontFamily': 'Roboto, sans-serif',
        },
        children=[
            html.H2('Artworks', style={'fontSize': '25px','marginTop': '0px', 'marginBottom': '0px', 'color': '#858383', 'textAlign': 'center'}),
            html.Div([
                html.P(f"{metrics['num_artworks']}"),
        ], style = {'textAlign': 'center', 'fontSize': '35px', 'marginTop': '0px', 'marginBottom': '0px'})
    ]
)

def combined_card_4(metrics, bg_color= '#2D2D2D', text_colour='#FFFFFF'):
    return html.Div(
        style={
            'backgroundColor': bg_color,
            'color': text_colour,
            'borderRadius': '15px',
            'padding': '20px',
            'width': '250px',
            'boxShadow': '0px 4px 10px rgba(0, 0, 0, 0.5)',
            'margin': '5px',
            'border': '1px solid #444444',
            'fontFamily': 'Roboto, sans-serif',
        }, 
        children=[
            html.H2('Nationalities', style={'fontSize': '25px','marginTop': '0px', 'marginBottom': '0px', 'color': '#858383', 'textAlign': 'center'}),
            html.Div([
                html.P(f"{metrics['num_nationalities']}"),
        ], style = {'textAlign': 'center', 'fontSize': '35px', 'marginTop': '0px', 'marginBottom': '0px'})
    ]
)

def combined_card_5(metrics, bg_color= '#2D2D2D', text_colour='#FFFFFF'):
    return html.Div(
        style={
            'backgroundColor': bg_color,
            'color': text_colour,
            'borderRadius': '15px',
            'padding': '20px',
            'width': '250px',
            'boxShadow': '0px 4px 10px rgba(0, 0, 0, 0.5)',
            'margin': '5px',
            'border': '1px solid #444444',
            'fontFamily': 'Roboto, sans-serif',
        }, 
        children=[
            html.H2('Classifications', style={'fontSize': '25px','marginTop': '0px', 'marginBottom': '0px', 'color': '#858383', 'textAlign': 'center'}),
            html.Div([
                html.P(f"{metrics['num_classifications']}"),
        ], style = {'textAlign': 'center', 'fontSize': '35px', 'marginTop': '0px', 'marginBottom': '0px'})
    ]
)

artist_num_feats = "{:,}".format(len(artist_df))
artwork_num_feats = "{:,}".format(len(artwork_df))
memory = "72MB"
num_artists = "{:,}".format(len(artist_df))
num_artworks = "{:,}".format(artwork_df.ObjectID.nunique())
num_nationalities = artist_df.Nationality.nunique()
num_classifications = artist_df.Nationality.nunique()
