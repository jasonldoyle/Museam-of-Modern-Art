import pandas as pd 
import seaborn as sns
import numpy as np 
import dash
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

artist_df = pd.read_csv("Artists.csv")
artwork_df = pd.read_csv("Artworks.csv")

artwork_df['painting_size'] = artwork_df['Height (cm)']* artwork_df['Width (cm)']
artwork_df['Date'] = artwork_df['Date'].replace('n.d.', '0')
artwork_df['Date'] = artwork_df['Date'].str.split('-').str[0]
artwork_df['Date'] = artwork_df['Date'].str.split('.').str[0]
artwork_df['Date'] = pd.to_numeric(artwork_df['Date'], errors='coerce')
artwork_df['decades'] = artwork_df['Date'] // 10 * 10
average_painting_size = artwork_df.groupby('decades', as_index=False)['painting_size'].mean()

top_three_artists = artwork_df['Artist'].value_counts().head(3).reset_index()
top_three_artists.columns = ['Artist', 'Count']
top_three_artists = artwork_df['Title'].value_counts().head(3).reset_index()
top_three_artists.columns = ['Title', 'Count']
top_medium = artwork_df['Medium'].value_counts().head(1).reset_index()
top_medium.columns = ['Medium', 'Count']
gender_counts = artwork_df['Gender'].value_counts().reset_index()
gender_counts.columns = ['Gender', 'Count']
top_classification = artwork_df['Medium'].value_counts().head(1).reset_index()
top_classification.columns = ['Medium', 'Count']