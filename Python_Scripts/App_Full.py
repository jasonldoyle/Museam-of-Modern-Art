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

T2fig1 = px.pie(
    gender_counts,
    names='Gender',            
    values='Count',             
    title="",  
    color='Gender',     
    color_discrete_sequence=px.colors.sequential.Viridis  
)

T2fig1.update_layout(
    plot_bgcolor="#1E1E1E",      
    paper_bgcolor="#1E1E1E",
    font=dict(color="#FFFFFF", size=14),  
    title=dict(font=dict(size=40, color="#00CED1"), x=0.5) 
)

artist_df['lifespan'] = (artist_df['EndDate'])-(artist_df['BeginDate'])

def clean_deaths(value):
    if len(str(value)) > 3:
        return None  
        
    if value < 18:
        return None
        
    return value  

artist_df['lifespan'] = artist_df['lifespan'].apply(clean_deaths)

avg_age = (artist_df.groupby('lifespan').size().reset_index(name='Count').sort_values(by='lifespan'))

T2fig2 = px.bar(
    avg_age,
    x='lifespan',
    y='Count',
    text='Count',
    title="",
    color='Count',
    color_continuous_scale=px.colors.sequential.Viridis
)

T2fig2.update_traces(
    texttemplate='%{text:.0f}',
    textposition='outside',
    marker=dict(opacity=0.8)
)

T2fig2.update_layout(
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


avg_birth = (artist_df.groupby('BeginDate').size().reset_index(name='Count').sort_values(by='BeginDate'))

avg_birth = avg_birth[avg_birth['BeginDate'] >= 1730]

T2fig3 = px.bar(
    avg_birth,
    x='BeginDate',
    y='Count',
    text='Count',
    title="",
    color='Count',
    color_continuous_scale=px.colors.sequential.Viridis
)

T2fig3.update_traces(
    texttemplate='%{text:.0f}',
    textposition='outside',
    marker=dict(opacity=0.8)
)

T2fig3.update_layout(
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


avg_death = (artist_df.groupby('EndDate').size().reset_index(name='Count').sort_values(by='EndDate'))

avg_death = avg_death[avg_death['EndDate'] >= 1795]

T2fig4 = px.bar(
    avg_death,
    x='EndDate',
    y='Count',
    text='Count',
    title="",
    color='Count',
    color_continuous_scale=px.colors.sequential.Viridis
)

T2fig4.update_traces(
    texttemplate='%{text:.0f}',
    textposition='outside',
    marker=dict(opacity=0.8)
)

T2fig4.update_layout(
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


artist_df.Nationality.value_counts().iloc[100:]

nationality_to_country = {
    "American": "United States",
    "German": "Germany",
    "British": "United Kingdom",
    "French": "France",
    "Italian": "Italy",
    "Japanese": "Japan",
    "Swiss": "Switzerland",
    "Dutch": "Netherlands",
    "Russian": "Russia",
    "Austrian": "Austria",
    "Canadian": "Canada",
    "Brazilian": "Brazil",
    "Spanish": "Spain",
    "Mexican": "Mexico",
    "Argentine": "Argentina",
    "Polish": "Poland",
    "Swedish": "Sweden",
    "Danish": "Denmark",
    "Chinese": "China",
    "Belgian": "Belgium",
    "Czech": "Czech Republic",
    "Israeli": "Israel",
    "Chilean": "Chile",
    "Venezuelan": "Venezuela",
    "South African": "South Africa",
    "Cuban": "Cuba",
    "Colombian": "Colombia",
    "Finnish": "Finland",
    "Australian": "Australia",
    "Hungarian": "Hungary",
    "Indian": "India",
    "Norwegian": "Norway",
    "Peruvian": "Peru",
    "Croatian": "Croatia",
    "Korean": "South Korea",
    "Irish": "Ireland",
    "Uruguayan": "Uruguay",
    "Turkish": "Turkey",
    "Scottish": "United Kingdom",  
    "Romanian": "Romania",
    "Serbian": "Serbia",
    "Haitian": "Haiti",
    "Slovenian": "Slovenia",
    "New Zealander": "New Zealand",
    "Ukrainian": "Ukraine",
    "Puerto Rican": "Puerto Rico",
    "Iranian": "Iran",
    "Nigerian": "Nigeria",
    "Greek": "Greece",
    "Native American": "United States",
    "Icelandic": "Iceland",
    "Egyptian": "Egypt",
    "Portuguese": "Portugal",
    "Canadian Inuit": "Canada",
    "Lebanese": "Lebanon",
    "Slovak": "Slovakia",
    "Guatemalan": "Guatemala",
    "Moroccan": "Morocco",
    "Ecuadorian": "Ecuador",
    "Congolese": "Democratic Republic of the Congo",
    "Bosnian": "Bosnia and Herzegovina",
    "Georgian": "Georgia",
    "Taiwanese": "Taiwan",
    "Vietnamese": "Vietnam",
    "Kenyan": "Kenya",
    "Czechoslovakian": "Czechoslovakia", 
    "Pakistani": "Pakistan",
    "Bangladeshi": "Bangladesh",
    "Zimbabwean": "Zimbabwe",
    "Palestinian": "Palestine",
    "Bulgarian": "Bulgaria",
    "Filipino": "Philippines",
    "Macedonian": "North Macedonia",
    "Senegalese": "Senegal",
    "Thai": "Thailand",
    "Bolivian": "Bolivia",
    "Panamanian": "Panama",
    "Nicaraguan": "Nicaragua",
    "Luxembourger": "Luxembourg",
    "Malaysian": "Malaysia",
    "Albanian": "Albania",
    "Algerian": "Algeria",
    "Malian": "Mali",
    "Sudanese": "Sudan",
    "Ghanaian": "Ghana",
    "Lithuanian": "Lithuania",
    "Welsh": "United Kingdom", 
    "Latvian": "Latvia",
    "Singaporean": "Singapore",
    "English": "United Kingdom",
    "Salvadoran": "El Salvador",
    "Cameroonian": "Cameroon",
    "Kyrgyz": "Kyrgyzstan",
    "Iraqi": "Iraq",
    "Tunisian": "Tunisia",
    "Catalan": "Spain",  
    "Emirati": "United Arab Emirates",
    "Namibian": "Namibia",
    "Syrian": "Syria",
    "Trinidad and Tobagonian": "Trinidad and Tobago",
    "Costa Rican": "Costa Rica",
    "Paraguayan": "Paraguay",
    "Bahamian": "Bahamas",
    "Mozambican": "Mozambique",
    "Estonian": "Estonia",
    "Azerbaijani": "Azerbaijan",
    "Ethiopian": "Ethiopia",
    "South Korean": "South Korea",
    "Sri Lankan": "Sri Lanka",
    "Sierra Leonean": "Sierra Leone",
    "Caribbean": "Caribbean Region",
    "Hunkpapa Lakota": "United States",  # Native American nation
    "Burkinabé": "Burkina Faso",
    "Indonesian": "Indonesia",
    "Ivatan": "Philippines",  # Indigenous group in the Philippines
    "Nepali": "Nepal",
    "Beninese": "Benin",
    "Afghan": "Afghanistan",
    "Persian": "Iran",
    "Coptic": "Egypt",  # Religious/ethnic group in Egypt
    "Sahrawi": "Western Sahara",
    "Ugandan": "Uganda",
    "Kuwaiti": "Kuwait",
    "Cambodian": "Cambodia",
    "Ivorian": "Ivory Coast",
    "Cypriot": "Cyprus",
    "Jamaican American": "United States",  # Mixed identity, categorized to the U.S.
    "Tanzanian": "Tanzania",
    "Yugoslav": "Former Yugoslavia",  # Historical country
    "Oneida": "United States",  # Native American nation
}
artist_df["Country"] = artist_df["Nationality"].map(nationality_to_country)

nationality_counts = artist_df['Country'].value_counts().reset_index()
nationality_counts.columns = ['Country', 'Count']

T2fig5 = px.choropleth(
    nationality_counts,
    locations='Country',  
    locationmode='country names',  
    color='Count',  
    hover_name='Country',
    title="",
    color_continuous_scale=px.colors.sequential.Blues,  
    height=600 

)

T2fig5.update_layout(
    plot_bgcolor="#1E1E1E",  
    paper_bgcolor="#1E1E1E", 
    font=dict(color="#FFFFFF", size=14), 
    title=dict(font=dict(size=40, color="#00CED1"), x=0.5),  
    coloraxis_colorbar=dict(
        title="",
        tickcolor="#FFFFFF",
        titlefont=dict(color="#FFFFFF"),
        bgcolor="#2D2D2D",
        bordercolor="#444444",
        borderwidth=1,

    )
)


top_countries = artist_df['Country'].value_counts().head(5).reset_index()
top_countries.columns = ['Country', 'Count']
T1fig6 = px.bar(
    top_countries,
    x='Country',
    y='Count',
    text='Count',
    title="",
    color='Count',
    color_continuous_scale=px.colors.sequential.Viridis
)

T1fig6.update_traces(
    texttemplate='%{text:.0f}',
    textposition='outside',
    marker=dict(opacity=0.8)
)

T1fig6.update_layout(
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