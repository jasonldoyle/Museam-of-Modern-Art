import pandas as pd 
import seaborn as sns
import numpy as np 
import dash
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

artist_df = pd.read_csv("Artists.csv")
artwork_df = pd.read_csv("Artworks.csv")

from cards import combined_card_1, combined_card_2, combined_card_3, combined_card_4, combined_card_5, artist_num_feats, artwork_num_feats, memory, num_artists, num_artworks, num_nationalities, num_classifications
from Tab1 import T1fig1, T1fig2, T1fig3, T1fig5
from Tab2 import T2fig1, T2fig2, T2fig3, T2fig4, T2fig5, T1fig6
from Tab3 import top_three_artists, top_medium, gender_counts, top_classification, top_classification

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
def classify_only_male(gender):
    if not isinstance(gender, str):  
        return gender
    gender = gender.lower()  
    if "male" in gender and "female" not in gender:  
        return "Male"
    return gender  
artwork_df['Gender'] = artwork_df['Gender'].apply(classify_only_male)

def classify_only_male(gender):
    if not isinstance(gender, str):  
        return gender
    if "female" in gender:  
        return "Female"
    return gender  
artwork_df['Gender'] = artwork_df['Gender'].apply(classify_only_male)

def classify_only_male(gender):
    if not isinstance(gender, str):  
        return gender
    if "()" in gender:  
        return "Unkown"
    return gender  
artwork_df['Gender'] = artwork_df['Gender'].apply(classify_only_male)

def classify_only_male(gender):
    if not isinstance(gender, str):  
        return "Other"  
    if "Male" in gender or "Female" in gender or "Unkown" in gender:  
        return gender
    return "Other" 
artwork_df['Gender'] = artwork_df['Gender'].apply(classify_only_male)

gender_counts = artwork_df['Gender'].value_counts().reset_index()
gender_counts.columns = ['Gender', 'Count']

app = dash.Dash(__name__)
server = app.server
app.layout = html.Div(
    style={
        'backgroundColor': '#1E1E1E',  
        'color': '#FFFFFF',           
        'fontFamily': 'Arial, sans-serif',
        'padding': '20px',
    },
    children=[
        html.H1(
            "Museum of Modern Art", 
            style={'textAlign': 'center', 'color': '#00CED1', 'fontSize': '50px'}
        ),
        dcc.Tabs(
            style={
                'backgroundColor': '#2D2D2D',
                'color': '#FFFFFF',
                'border': '1px solid #3E3E3E',
                'fontSize': '16px',
                'padding': '10px',
            },
            children=[
                # Tab 1: About the Museum
                dcc.Tab(
                    label="About the Museum",
                    style={
                        'backgroundColor': '#2D2D2D',
                        'border': '1px solid #3E3E3E',
                        'color': '#FFFFFF',
                        'padding': '10px',
                        'fontWeight': 'bold',
                    },
                    selected_style={
                        'backgroundColor': '#444444',
                        'border': '1px solid #00CED1',
                        'color': '#00CED1',
                        'padding': '10px',
                        'fontWeight': 'bold',
                    },
                    children=[
                        html.Div([
                            html.Div(
                                style={
                                    'display': 'flex',
                                    'justifyContent': 'center',
                                    'alignItems': 'center',
                                    'flexWrap': 'nowrap',
                                    'gap': '20px',
                                    'marginBottom': '30px',
                                },
                                children=[
                                    combined_card_1(metrics={
                                        "artist_num_feats": artist_num_feats,
                                        "artwork_num_feats": artwork_num_feats,
                                        "memory": memory,
                                    }),
                                    combined_card_2(metrics={"num_artists": num_artists}),
                                    combined_card_3(metrics={"num_artworks": num_artworks}),
                                    combined_card_4(metrics={"num_nationalities": num_nationalities}),
                                    combined_card_5(metrics={"num_classifications": num_classifications}),
                                ]
                            ),
                            html.Div(
                                style={
                                    'display': 'grid',
                                    'gridTemplateColumns': 'repeat(2, 1fr)',
                                    'gap': '20px',
                                    'margin': '20px',
                                },
                                children=[
                                    html.Div([
                                        html.H3(
                                            "Average Painting Sizes (cm) by Decade", 
                                            style={'textAlign': 'center', 'color': '#00CED1'}
                                        ),
                                        dcc.Graph(figure=T1fig1, style={'backgroundColor': '#1E1E1E'})
                                    ]),
                                    html.Div([
                                        html.H3(
                                            "Average Acquisitions by Decade", 
                                            style={'textAlign': 'center', 'color': '#00CED1'}
                                        ),
                                        dcc.Graph(figure=T1fig2, style={'backgroundColor': '#1E1E1E'})
                                    ]),
                                    html.Div([
                                        html.H3(
                                            "Top 5 Classifications", 
                                            style={'textAlign': 'center', 'color': '#00CED1'}
                                        ),
                                        dcc.Graph(figure=T1fig3, style={'backgroundColor': '#1E1E1E'})
                                    ]),
                                    html.Div([
                                        html.H3(
                                            "Acquisitions over the Years", 
                                            style={'textAlign': 'center', 'color': '#00CED1'}
                                        ),
                                        dcc.Graph(figure=T1fig5, style={'backgroundColor': '#1E1E1E'})
                                    ])
                                ]
                            )
                        ])
                    ]
                ),
                # Tab 2: Insights
                dcc.Tab(
                    label="Insights",
                    style={
                        'backgroundColor': '#2D2D2D',
                        'border': '1px solid #3E3E3E',
                        'color': '#FFFFFF',
                        'padding': '10px',
                        'fontWeight': 'bold',
                    },
                    selected_style={
                        'backgroundColor': '#444444',
                        'border': '1px solid #00CED1',
                        'color': '#00CED1',
                        'padding': '10px',
                        'fontWeight': 'bold',
                    },
                    children=[
                        html.Div(
                            style={
                                'backgroundColor': '#1E1E1E',
                                'padding': '20px',
                                'borderRadius': '10px',
                                'boxShadow': '0px 4px 10px rgba(0, 0, 0, 0.5)',
                            },
                            children=[
                                html.H1(
                                    "",
                                    style={
                                        'textAlign': 'center',
                                        'color': '#00CED1',
                                        'marginBottom': '20px'
                                    }
                                ),
                                html.Div(
                                    style={
                                        'display': 'grid',
                                        'gridTemplateColumns': 'repeat(2, 1fr)',
                                        'gap': '20px',
                                        'marginTop': '20px',
                                    },
                                    children=[
                                        html.Div([
                                            html.H3(
                                                "Gender Pie",
                                                style={
                                                    'textAlign': 'center',
                                                    'color': '#00CED1',
                                                    'marginBottom': '10px'
                                                }
                                            ),
                                            dcc.Graph(figure=T2fig1, style={'backgroundColor': '#1E1E1E'})
                                        ]),
                                        html.Div([
                                            html.H3(
                                                "Map of Artists Origins",
                                                style={
                                                    'textAlign': 'center',
                                                    'color': '#00CED1',
                                                    'marginBottom': '10px'
                                                }
                                            ),
                                            dcc.Graph(figure=T2fig5, style={'backgroundColor': '#1E1E1E'})
                                        ]),
                                        html.Div([
                                            html.H3(
                                                "Average Lifespan",
                                                style={
                                                    'textAlign': 'center',
                                                    'color': '#00CED1',
                                                    'marginBottom': '10px'
                                                }
                                            ),
                                            dcc.Graph(figure=T2fig2, style={'backgroundColor': '#1E1E1E'})
                                        ]),
                                        html.Div([
                                            html.H3(
                                                "Count of Countries",
                                                style={
                                                    'textAlign': 'center',
                                                    'color': '#00CED1',
                                                    'marginBottom': '10px'
                                                }
                                            ),
                                            dcc.Graph(figure=T1fig6, style={'backgroundColor': '#1E1E1E'})
                                        ]),
                                        html.Div([
                                            html.H3(
                                                "Births",
                                                style={
                                                    'textAlign': 'center',
                                                    'color': '#00CED1',
                                                    'marginBottom': '10px'
                                                }
                                            ),
                                            dcc.Graph(figure=T2fig3, style={'backgroundColor': '#1E1E1E'})
                                        ]),
                                        html.Div([
                                            html.H3(
                                                "Deaths",
                                                style={
                                                    'textAlign': 'center',
                                                    'color': '#00CED1',
                                                    'marginBottom': '10px'
                                                }
                                            ),
                                            dcc.Graph(figure=T2fig4, style={'backgroundColor': '#1E1E1E'})
                                        ]),
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                # Tab 3: Artists by Decade
                dcc.Tab(
    label="Throughout the Decades",
    style={
        'backgroundColor': '#2D2D2D',
        'border': '1px solid #3E3E3E',
        'color': '#FFFFFF',
        'padding': '10px',
        'fontWeight': 'bold',
    },
    selected_style={
        'backgroundColor': '#444444',
        'border': '1px solid #00CED1',
        'color': '#00CED1',
        'padding': '10px',
        'fontWeight': 'bold',
    },
    children=[
        html.Div([
            html.H1("", style={'textAlign': 'center', 'color': '#00CED1'}),
            
            # Decade Slider
            dcc.Slider(
                id='decade-slider',
                min=1760,
                max=2020,
                step=10,
                marks={i: str(i) for i in range(1760, 2030, 10)},
                value=1920,
                tooltip={"placement": "bottom", "always_visible": True}
            ), 

# Graphs
html.Div([
    dcc.Graph(id='fig-top-artists'),
    dcc.Graph(id='fig-top-titles')
], style={'display': 'flex', 'justifyContent': 'space-around', 'alignItems': 'center'}),

html.Div([
    dcc.Graph(id='fig-top-medium'),
    dcc.Graph(id='fig-gender-counts')
], style={'display': 'flex', 'justifyContent': 'space-around', 'alignItems': 'center'}),
        ])
    ]
),
            ]
        )
    ]
)
@app.callback(
    [
        Output('fig-top-artists', 'figure'),
        Output('fig-top-titles', 'figure'),
        Output('fig-top-medium', 'figure'),
        Output('fig-gender-counts', 'figure')
    ],
    [Input('decade-slider', 'value')]
)
def update_figures(selected_decade):
    # Filter data by selected decade
    filtered_df = artwork_df[artwork_df['decades'] == selected_decade]

    # Top 3 Artists
    filtered_artists = filtered_df['Artist'].value_counts().head(3).reset_index()
    filtered_artists.columns = ['Artist', 'Count']
    fig_top_artists = px.bar(
        filtered_artists,
        x='Artist',
        y='Count',
        text='Count',
        title=f"Top 3 Artists ({selected_decade})",
        color='Count',
        color_continuous_scale='Viridis'
    )
    fig_top_artists.update_traces(texttemplate='%{text:.0f}', textposition='outside')
    fig_top_artists.update_layout(
        title_x=0.5,
        font=dict(size=14, color="#FFFFFF"),
        paper_bgcolor="#1E1E1E",
        plot_bgcolor="#1E1E1E"
    )

    # Top 3 Titles
    filtered_titles = filtered_df[filtered_df['Title'] != 'Untitled']  
    filtered_titles = filtered_titles['Title'].value_counts().head(3).reset_index()
    filtered_titles.columns = ['Title', 'Count'] 
    fig_top_titles = px.bar(
        filtered_titles,
        x='Title',
        y='Count',
        text='Count',
        title=f"Top 3 Titles ({selected_decade})",
        color='Count',
        color_continuous_scale='Viridis'
    )
    fig_top_titles.update_traces(texttemplate='%{text:.0f}', textposition='outside')
    fig_top_titles.update_layout(
        title_x=0.5,
        font=dict(size=14, color="#FFFFFF"),
        paper_bgcolor="#1E1E1E",
        plot_bgcolor="#1E1E1E"
    )

    # Top Medium
    filtered_medium = filtered_df['Medium'].value_counts().head(1).reset_index()
    filtered_medium.columns = ['Medium', 'Count']
    fig_top_medium = px.bar(
        filtered_medium,
        x='Medium',
        y='Count',
        text='Count',
        title=f"Most Common Medium ({selected_decade})",
        color='Count',
        color_continuous_scale='Viridis'
    )
    fig_top_medium.update_traces(texttemplate='%{text:.0f}', textposition='outside')
    fig_top_medium.update_layout(
        title_x=0.5,
        font=dict(size=14, color="#FFFFFF"),
        paper_bgcolor="#1E1E1E",
        plot_bgcolor="#1E1E1E"
    )

    # Gender Distribution (Pie Chart)
    filtered_gender_counts = filtered_df['Gender'].value_counts().reset_index()
    filtered_gender_counts.columns = ['Gender', 'Count']
    fig_gender_counts = px.pie(
        filtered_gender_counts,
        names='Gender',
        values='Count',
        title=f"Gender Distribution ({selected_decade})"
    )
    fig_gender_counts.update_traces(textinfo='none')
    fig_gender_counts.update_layout(
        title_x=0.5,
        font=dict(size=14, color="#FFFFFF"),
        paper_bgcolor="#1E1E1E",
        plot_bgcolor="#1E1E1E"
    )

    return fig_top_artists, fig_top_titles, fig_top_medium, fig_gender_counts


if __name__ == '__main__':
    app.run_server(debug=True)