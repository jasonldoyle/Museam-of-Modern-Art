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

average_painting_size = artwork_df.groupby('decades', as_index=False)['painting_size'].mean()
filtered_data = average_painting_size[average_painting_size['decades'] >= 1700]

T1fig1 = px.bar(
    filtered_data,
    x='decades',          
    y='painting_size',
    text='painting_size',     
    title="",  
    color='painting_size',     
    color_continuous_scale=px.colors.sequential.Viridis 
)

T1fig1.update_traces(
    texttemplate='%{text:.2f}', 
    textposition='outside',     
    marker=dict(opacity=0.8)    
)

T1fig1.update_layout(
    plot_bgcolor="#1E1E1E",      
    paper_bgcolor="#1E1E1E",    
    font=dict(color="#FFFFFF", size=14), 
    title=dict(font=dict(size=20, color="#00CED1"), x=0.5),
    xaxis=dict(
        title="Decade",     
        color="#FFFFFF",       
        gridcolor="#444444", 
        zeroline=False,
        ticklabelstandoff=20
    ),
    yaxis=dict(
        title="",   
        color="#FFFFFF",       
        showgrid=False          
    ),
    coloraxis_colorbar=dict(
        title="",  
        tickcolor="#FFFFFF",   
        titlefont=dict(color="#FFFFFF"), 
        bgcolor="#2D2D2D",      
        bordercolor="#444444",   
        borderwidth=1         
    )
)

artwork_df['DateAcquired'] = artwork_df['DateAcquired'].str.split('-').str[0]
artwork_df['DateAcquired'] = pd.to_numeric(artwork_df['DateAcquired'])
average_acquisitions_size = artwork_df.groupby('decades', as_index=False)['DateAcquired'].count()
filtered_DateAcquired_data = average_acquisitions_size[average_acquisitions_size['decades'] >= 1760]

T1fig2 = px.bar(
    filtered_DateAcquired_data,
    x='decades',              
    y='DateAcquired',     
    text='DateAcquired',      
    title="", 
    color='DateAcquired',   
    color_continuous_scale=px.colors.sequential.Viridis  
)


T1fig2.update_traces(
    texttemplate='%{text:.2f}', 
    textposition='outside',     
    marker=dict(opacity=0.8)    
)

T1fig2.update_layout(
    plot_bgcolor="#1E1E1E",      
    paper_bgcolor="#1E1E1E",    
    font=dict(color="#FFFFFF", size=14), 
    title=dict(font=dict(size=20, color="#00CED1"), x=0.5),
    xaxis=dict(
        title="Decade",     
        color="#FFFFFF",       
        gridcolor="#444444", 
        zeroline=False,
        ticklabelstandoff=20
    ),
    yaxis=dict(
        title="",   
        color="#FFFFFF",       
        showgrid=False          
    ),
    coloraxis_colorbar=dict(
        title="",  
        tickcolor="#FFFFFF",   
        titlefont=dict(color="#FFFFFF"), 
        bgcolor="#2D2D2D",      
        bordercolor="#444444",   
        borderwidth=1         
    )
)

top_classifications = artwork_df['Classification'].value_counts().head(5).reset_index()
top_classifications.columns = ['Classification', 'Count']

T1fig3 = px.bar(
    top_classifications,
    x='Classification',
    y='Count',
    text='Count',
    title="",
    color='Count',
    color_continuous_scale=px.colors.sequential.Viridis
)

T1fig3.update_traces(
    texttemplate='%{text:.0f}',
    textposition='outside',
    marker=dict(opacity=0.8)
)

T1fig3.update_layout(
    plot_bgcolor="#1E1E1E",
    paper_bgcolor="#1E1E1E",
    font=dict(color="#FFFFFF", size=14),
    title=dict(font=dict(size=40, color="#00CED1"), x=0.5),
    xaxis=dict(
        title="",
        color="#FFFFFF",
        gridcolor="#444444",
        zeroline=False,
        ticklabelstandoff=40
    ),
    yaxis=dict(
        title="",
        color="#FFFFFF",
        showgrid=False
    ),
    coloraxis_colorbar=dict(
        title="",
        tickcolor="#FFFFFF",
        titlefont=dict(color="#FFFFFF"),
        bgcolor="#2D2D2D",
        bordercolor="#444444",
        borderwidth=1
    ),
    height=600 
)

top_years = (artwork_df.groupby('DateAcquired').size().reset_index(name='Count').sort_values(by='Count', ascending=False).head(10))
top_years

yearly_counts = (artwork_df.groupby('DateAcquired').size().reset_index(name='Count').sort_values(by='DateAcquired'))

T1fig5 = px.bar(
    yearly_counts,
    x='DateAcquired',
    y='Count',
    text='Count',
    title="",
    color='Count',
    color_continuous_scale=px.colors.sequential.Viridis
)

T1fig5.update_traces(
    texttemplate='%{text:.0f}',
    textposition='outside',
    marker=dict(opacity=0.8)
)

T1fig5.update_layout(
    plot_bgcolor="#1E1E1E",
    paper_bgcolor="#1E1E1E",
    font=dict(color="#FFFFFF", size=14),
    title=dict(font=dict(size=40, color="#00CED1"), x=0.5),
    xaxis=dict(
        title="",
        color="#FFFFFF",
        gridcolor="#444444",
        zeroline=False,
        ticklabelstandoff=40
    ),
    yaxis=dict(
        title="",
        color="#FFFFFF",
        showgrid=False
    ),
    coloraxis_colorbar=dict(
        title="",
        tickcolor="#FFFFFF",
        titlefont=dict(color="#FFFFFF"),
        bgcolor="#2D2D2D",
        bordercolor="#444444",
        borderwidth=1
    ),
    height=600 
)
