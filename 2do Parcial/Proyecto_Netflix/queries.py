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
    tops = counts.head(10) # Reducido a 10 para que la gráfica se vea mejor
    
    # --- GRÁFICA ---
    # 1. Crear figura y eje
    fig, ax = plt.subplots(figsize=(8, 5))
    # 2. Dibujar gráfica de barras (X: Director, Y: Cantidad)
    ax.bar(tops['Director'], tops['Cantidad de Producciones'], color='skyblue')
    # 3. Textos y títulos
    ax.set_title('Top 10 Directores con más producciones')
    ax.set_xlabel('Director')
    ax.set_ylabel('Cantidad')
    # Rotar los nombres para que se puedan leer
    plt.xticks(rotation=45, ha='right')
    # 4. Ajustar el diseño
    fig.tight_layout()
    
    just = "Justificación: Identifica a los directores más recurrentes o exclusivos de Netflix, lo que ayuda a evaluar qué creadores garantizan un catálogo estable."
    return format_result(tops, just, fig)

def query_2_content_by_year_added():
    d = df.dropna(subset=['date_added']).copy()
    d['year_added'] = d['date_added'].dt.year.astype(int)
    pivot = pd.crosstab(d['year_added'], d['type']).reset_index()
    
    # --- GRÁFICA ---
    fig, ax = plt.subplots(figsize=(8, 5))
    # Dibujamos dos líneas, una para Películas y otra para Series
    ax.plot(pivot['year_added'], pivot.get('Movie', []), marker='o', label='Películas')
    ax.plot(pivot['year_added'], pivot.get('TV Show', []), marker='x', label='Series')
    
    ax.set_title('Contenido añadido por año')
    ax.set_xlabel('Año')
    ax.set_ylabel('Cantidad de títulos')
    ax.legend() # Mostrar qué color es qué cosa
    ax.grid(True) # Activar cuadrícula
    fig.tight_layout()
    
    just = "Justificación: Muestra el crecimiento de la plataforma comparando cuántas Películas vs Series se han añadido cada año, revelando la evolución de la estrategia de Netflix."
    return format_result(pivot, just, fig)

def query_3_pandemic_content_usa():
    d = df.dropna(subset=['date_added', 'country']).copy()
    d['year_added'] = d['date_added'].dt.year
    pandemic = d[(d['year_added'].isin([2020, 2021])) & (d['country'].str.contains('United States'))]
    res = pandemic[['title', 'type', 'year_added', 'director']]
    
    # Agrupamos para contar cuántas son de cada tipo en pandemia
    res_count = pandemic['type'].value_counts().reset_index()
    res_count.columns = ['Tipo', 'Cantidad']
    
    # --- GRÁFICA ---
    fig, ax = plt.subplots(figsize=(6, 4))
    # Gráfica de pastel (pie chart)
    ax.pie(res_count['Cantidad'], labels=res_count['Tipo'], autopct='%1.1f%%', colors=['#ff9999','#66b3ff'])
    ax.set_title('Películas vs Series en USA durante la Pandemia (2020-2021)')
    fig.tight_layout()
    
    just = "Justificación: Analiza el volumen de contenido estadounidense añadido durante los años fuertes de la pandemia (2020-2021) para entender la inyección de entretenimiento doméstico."
    return format_result(res, just, fig)

def query_4_top_genres():
    d = df.dropna(subset=['listed_in']).copy()
    d['genre_list'] = d['listed_in'].str.split(', ')
    exploded = d.explode('genre_list')
    genre_counts = exploded['genre_list'].value_counts().reset_index()
    genre_counts.columns = ['Género', 'Cantidad']
    tops = genre_counts.head(10)
    
    # --- GRÁFICA ---
    fig, ax = plt.subplots(figsize=(8, 5))
    # Gráfica de barras horizontales (barh) para que el texto largo quepa mejor
    ax.barh(tops['Género'][::-1], tops['Cantidad'][::-1], color='orange')
    ax.set_title('Top 10 Géneros más populares')
    ax.set_xlabel('Cantidad de títulos')
    fig.tight_layout()
    
    just = "Justificación: Revela en qué géneros invierte más Netflix (Comedias, Documentales, Drama, etc.) para abarcar su cuota de audiencia global (nichos)."
    return format_result(genre_counts.head(20), just, fig)

def query_5_movies_by_country():
    d = df[(df['type'] == 'Movie') & df['country'].notna()].copy()
    # Algunos títulos tienen varios países, contamos el primero por simplicidad
    d['main_country'] = d['country'].apply(lambda x: x.split(',')[0])
    counts = d['main_country'].value_counts().reset_index()
    counts.columns = ['País Principal', 'Cantidad de Películas']
    tops = counts.head(10)
    
    # --- GRÁFICA ---
    fig, ax = plt.subplots(figsize=(8, 5))
    # Gráfica de barras
    ax.bar(tops['País Principal'], tops['Cantidad de Películas'], color='lightgreen')
    ax.set_title('Top 10 Países productores de Películas')
    ax.set_ylabel('Cantidad de Películas')
    plt.xticks(rotation=45, ha='right')
    fig.tight_layout()
    
    just = "Justificación: Evalúa cuáles son los países con mayor peso de producción cinematográfica presente en la plataforma."
    return format_result(counts.head(15), just, fig)

def query_6_top_actors():
    d = df.dropna(subset=['cast']).copy()
    d['cast_list'] = d['cast'].str.split(', ')
    exploded = d.explode('cast_list')
    actor_counts = exploded['cast_list'].value_counts().reset_index()
    actor_counts.columns = ['Actor', 'Apariciones']
    tops = actor_counts.head(10)
    
    # --- GRÁFICA ---
    fig, ax = plt.subplots(figsize=(8, 5))
    # Barras horizontales invirtiendo el orden para que el mayor quede arriba ([::-1])
    ax.barh(tops['Actor'][::-1], tops['Apariciones'][::-1], color='purple')
    ax.set_title('Top 10 Actores con más apariciones')
    ax.set_xlabel('Cantidad de apariciones')
    fig.tight_layout()
    
    just = "Justificación: Análisis de 'estrellas'. Permite ver qué actores son un 'imán' de audiencias debido a su frecuente aparición en producciones originadas o compradas por Netflix."
    return format_result(actor_counts.head(20), just, fig)

def query_7_rating_distribution():
    d = df.groupby('rating').size().reset_index(name='Cantidad')
    d = d.sort_values('Cantidad', ascending=False).head(10)
    
    # --- GRÁFICA ---
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(d['rating'], d['Cantidad'], color='salmon')
    ax.set_title('Distribución de Clasificación (Ratings)')
    ax.set_xlabel('Clasificación')
    ax.set_ylabel('Cantidad')
    fig.tight_layout()
    
    just = "Justificación: Permite entender si Netflix está enfocado en adultos (TV-MA, R) o si las clasificaciones orientadas a jóvenes y niños tienen una cuota importante, delimitando al público objetivo."
    return format_result(d, just, fig)

def query_8_movie_duration_avg():
    d = df[(df['type'] == 'Movie') & df['duration'].notna()].copy()
    d['duration_min'] = d['duration'].str.replace(' min', '').astype(int)
    # Agrupar por año de lanzamiento desde 2000
    d = d[d['release_year'] >= 2000]
    avg_dur = d.groupby('release_year')['duration_min'].mean().round(1).reset_index()
    avg_dur.columns = ['Año de Lanzamiento', 'Duración Promedio (min)']
    
    # --- GRÁFICA ---
    fig, ax = plt.subplots(figsize=(8, 5))
    # Gráfica de línea (plot) marcando los puntos con 'o'
    ax.plot(avg_dur['Año de Lanzamiento'], avg_dur['Duración Promedio (min)'], marker='o', color='blue')
    ax.set_title('Duración Promedio de Películas desde 2000')
    ax.set_xlabel('Año de Lanzamiento')
    ax.set_ylabel('Duración (Minutos)')
    ax.grid(True)
    fig.tight_layout()
    
    just = "Justificación: Responde a la hipótesis de si las películas se han vuelto más cortas o más largas con el paso de las décadas recientes."
    return format_result(avg_dur, just, fig)

def query_9_top_tv_shows_seasons():
    d = df[(df['type'] == 'TV Show') & df['duration'].notna()].copy()
    # "1 Season", "2 Seasons"
    d['seasons'] = d['duration'].str.extract(r'(\d+)').astype(int)
    d = d.sort_values(by='seasons', ascending=False)
    res = d[['title', 'seasons', 'country', 'release_year']].head(10)
    
    # --- GRÁFICA ---
    fig, ax = plt.subplots(figsize=(8, 5))
    # Barras horizontales (barh)
    ax.barh(res['title'][::-1], res['seasons'][::-1], color='magenta')
    ax.set_title('Top 10 Series con Más Temporadas')
    ax.set_xlabel('Número de Temporadas')
    fig.tight_layout()
    
    just = "Justificación: Localiza las series con mayor persistencia (más temporadas), lo cual es crítico para la retención a largo plazo de usuarios."
    return format_result(res, just, fig)

def query_10_recent_vintage():
    # Películas muy viejas, pero apenas agregadas recientemente
    d = df.dropna(subset=['date_added']).copy()
    d['year_added'] = d['date_added'].dt.year.astype(int)
    vintage = d[(d['release_year'] <= 2000) & (d['year_added'] >= 2020)]
    res = vintage[['title', 'type', 'release_year', 'year_added', 'director']]
    
    counts = vintage['release_year'].value_counts().reset_index()
    counts.columns = ['Año Original', 'Cantidad Adquirida Reciente']
    counts = counts.sort_values('Año Original')
    
    # --- GRÁFICA ---
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(counts['Año Original'], counts['Cantidad Adquirida Reciente'], marker='o', color='teal')
    ax.set_title('Películas Vintage adquiridas recientemente (Por año original)')
    ax.set_xlabel('Año de Lanzamiento Original')
    ax.set_ylabel('Cantidad')
    ax.grid(True)
    fig.tight_layout()
    
    just = "Justificación: Analiza la estrategia de 'Clásicos'. Netflix adquiere licencias de años anteriores (vintage) e invierte para retener público nostálgico."
    return format_result(res.head(30), just, fig)

# Array a llamar desde la GUI
QUERIES = [
    ("Top 10 Directores", query_1_top_directors),
    ("Películas vs Series por Año", query_2_content_by_year_added),
    ("Contenido en Pandemia (USA)", query_3_pandemic_content_usa),
    ("Top 10 Géneros", query_4_top_genres),
    ("Producción de Películas por País", query_5_movies_by_country),
    ("Top 10 Actores", query_6_top_actors),
    ("Distribución por Clasificación", query_7_rating_distribution),
    ("Duración Promedio Películas", query_8_movie_duration_avg),
    ("Series con Más Temporadas", query_9_top_tv_shows_seasons),
    ("Clásicos adquiridos recientemente", query_10_recent_vintage),
]
