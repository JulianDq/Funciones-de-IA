import pandas as pd
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

DATASET_PATH = os.path.join(os.path.dirname(__file__), "data", "netflix_titles.csv")

def load_data():
    try:
        df = pd.read_csv(DATASET_PATH)
        # Limpieza básica
        df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return pd.DataFrame()

df = load_data()

def format_result(result_df, justificacion, fig=None):
    # Asegurar que no pasamos más de 100 filas para no trabar el UI
    if len(result_df) > 100:
        result_df = result_df.head(100)
    
    # Convertir a listas para el treeview
    columns = list(result_df.columns)
    rows = result_df.fillna("N/A").values.tolist()
    return columns, rows, justificacion, fig

# ------------- CONSULTAS -------------

def query_1_top_directors():
    d = df[df['director'].notna()].copy()
    counts = d['director'].value_counts().reset_index()
    counts.columns = ['Director', 'Cantidad de Producciones']
    tops = counts.head(15)
    
    just = "Justificación: Identifica a los directores más recurrentes o exclusivos de Netflix, lo que ayuda a evaluar qué creadores garantizan un catálogo estable."
    return format_result(tops, just)

def query_2_content_by_year_added():
    d = df.dropna(subset=['date_added']).copy()
    d['year_added'] = d['date_added'].dt.year.astype(int)
    pivot = pd.crosstab(d['year_added'], d['type']).reset_index()
    
    just = "Justificación: Muestra el crecimiento de la plataforma comparando cuántas Películas vs Series se han añadido cada año, revelando la evolución de la estrategia de Netflix."
    return format_result(pivot, just)

def query_3_pandemic_content_usa():
    d = df.dropna(subset=['date_added', 'country']).copy()
    d['year_added'] = d['date_added'].dt.year
    pandemic = d[(d['year_added'].isin([2020, 2021])) & (d['country'].str.contains('United States'))]
    res = pandemic[['title', 'type', 'year_added', 'director']]
    
    just = "Justificación: Analiza el volumen de contenido estadounidense añadido durante los años fuertes de la pandemia (2020-2021) para entender la inyección de entretenimiento doméstico."
    return format_result(res, just)

def query_4_top_genres():
    d = df.dropna(subset=['listed_in']).copy()
    d['genre_list'] = d['listed_in'].str.split(', ')
    exploded = d.explode('genre_list')
    genre_counts = exploded['genre_list'].value_counts().reset_index()
    genre_counts.columns = ['Género', 'Cantidad']
    
    just = "Justificación: Revela en qué géneros invierte más Netflix (Comedias, Documentales, Drama, etc.) para abarcar su cuota de audiencia global (nichos)."
    return format_result(genre_counts.head(20), just)

def query_5_movies_by_country():
    d = df[(df['type'] == 'Movie') & df['country'].notna()].copy()
    # Algunos títulos tienen varios países, contamos el primero por simplicidad
    d['main_country'] = d['country'].apply(lambda x: x.split(',')[0])
    counts = d['main_country'].value_counts().reset_index()
    counts.columns = ['País Principal', 'Cantidad de Películas']
    
    just = "Justificación: Evalúa cuáles son los países con mayor peso de producción cinematográfica presente en la plataforma."
    return format_result(counts.head(15), just)

def query_6_top_actors():
    d = df.dropna(subset=['cast']).copy()
    d['cast_list'] = d['cast'].str.split(', ')
    exploded = d.explode('cast_list')
    actor_counts = exploded['cast_list'].value_counts().reset_index()
    actor_counts.columns = ['Actor', 'Apariciones']
    
    just = "Justificación: Análisis de 'estrellas'. Permite ver qué actores son un 'imán' de audiencias debido a su frecuente aparición en producciones originadas o compradas por Netflix."
    return format_result(actor_counts.head(20), just)

def query_7_rating_distribution():
    d = df.groupby('rating').size().reset_index(name='Cantidad')
    d = d.sort_values('Cantidad', ascending=False)
    
    just = "Justificación: Permite entender si Netflix está enfocado en adultos (TV-MA, R) o si las clasificaciones orientadas a jóvenes y niños tienen una cuota importante, delimitando al público objetivo."
    return format_result(d, just)

def query_8_movie_duration_avg():
    d = df[(df['type'] == 'Movie') & df['duration'].notna()].copy()
    d['duration_min'] = d['duration'].str.replace(' min', '').astype(int)
    # Agrupar por año de lanzamiento desde 2000
    d = d[d['release_year'] >= 2000]
    avg_dur = d.groupby('release_year')['duration_min'].mean().round(1).reset_index()
    avg_dur.columns = ['Año de Lanzamiento', 'Duración Promedio (min)']
    
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(avg_dur['Año de Lanzamiento'], avg_dur['Duración Promedio (min)'], marker='o', linestyle='-', color='b')
    ax.set_title('Duración Promedio de Películas desde 2000')
    ax.set_xlabel('Año')
    ax.set_ylabel('Duración en Minutos')
    ax.grid(True)
    fig.tight_layout()
    
    just = "Justificación: Responde a la hipótesis de si las películas se han vuelto más cortas o más largas con el paso de las décadas recientes."
    return format_result(avg_dur, just, fig)

def query_9_top_tv_shows_seasons():
    d = df[(df['type'] == 'TV Show') & df['duration'].notna()].copy()
    # "1 Season", "2 Seasons"
    d['seasons'] = d['duration'].str.extract(r'(\d+)').astype(int)
    d = d.sort_values(by='seasons', ascending=False)
    res = d[['title', 'seasons', 'country', 'release_year']].head(15)
    
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.barh(res['title'][::-1], res['seasons'][::-1], color='m')
    ax.set_title('Top 15 Series con Más Temporadas')
    ax.set_xlabel('Temporadas')
    fig.tight_layout()
    
    just = "Justificación: Localiza las series con mayor persistencia (más temporadas), lo cual es crítico para la retención a largo plazo de usuarios."
    return format_result(res, just, fig)

def query_10_recent_vintage():
    # Películas muy viejas, pero apenas agregadas recientemente
    d = df.dropna(subset=['date_added']).copy()
    d['year_added'] = d['date_added'].dt.year.astype(int)
    vintage = d[(d['release_year'] <= 2000) & (d['year_added'] >= 2020)]
    res = vintage[['title', 'type', 'release_year', 'year_added', 'director']]
    
    just = "Justificación: Analiza la estrategia de 'Clásicos'. Netflix adquiere licencias de años anteriores (vintage) e invierte para retener público nostálgico."
    return format_result(res.head(30), just)

# Array a llamar desde la GUI
QUERIES = [
    ("Top 15 Directores", query_1_top_directors),
    ("Películas vs Series por Año", query_2_content_by_year_added),
    ("Contenido en Pandemia (USA)", query_3_pandemic_content_usa),
    ("Top 20 Géneros", query_4_top_genres),
    ("Producción de Películas por País", query_5_movies_by_country),
    ("Top 20 Actores", query_6_top_actors),
    ("Distribución por Clasificación", query_7_rating_distribution),
    ("Duración Promedio Películas", query_8_movie_duration_avg),
    ("Series con Más Temporadas", query_9_top_tv_shows_seasons),
    ("Clásicos adquiridos recientemente", query_10_recent_vintage),
]
