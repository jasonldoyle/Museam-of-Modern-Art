import pandas as pd 
import seaborn as sns
import numpy as np 
import dash
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

artist_df = pd.read_csv("Artists.csv")
artwork_df = pd.read_csv("Artworks.csv")



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
