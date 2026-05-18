import pandas as pd
import numpy as np
import os

# Ruta al CSV
CSV_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data E", "Amazon_BestSelling_Books_500.csv")

def get_dataframe():
    # Leer el CSV
    # Se añade errors='ignore' para evitar problemas de codificación si existieran
    df = pd.read_csv(CSV_PATH, encoding='utf-8')
    return df

def get_categorical_frequencies():
    """ Calcula frecuencias absolutas y relativas usando la columna Category """
    df = get_dataframe()
    # Frecuencia absoluta
    abs_freq = df['Category'].value_counts().reset_index()
    abs_freq.columns = ['label', 'absolute']
    
    # Frecuencia relativa
    total = len(df['Category'].dropna())
    abs_freq['relative'] = (abs_freq['absolute'] / total) * 100
    
    return abs_freq.to_dict(orient='records')

def get_continuous_frequencies(bins=10):
    """ Calcula frecuencias absolutas y acumuladas usando Price (USD) para el polígono """
    df = get_dataframe()
    
    # Limpiar y asegurar que sea numérico
    df['Price'] = pd.to_numeric(df['Price (USD)'], errors='coerce')
    df = df.dropna(subset=['Price'])
    
    # Crear intervalos (bins)
    counts, bin_edges = np.histogram(df['Price'], bins=bins)
    
    # Frecuencia acumulada
    cumulative = np.cumsum(counts)
    
    data = []
    for i in range(len(counts)):
        label = f"${bin_edges[i]:.2f} - ${bin_edges[i+1]:.2f}"
        data.append({
            "label": label,
            "midpoint": (bin_edges[i] + bin_edges[i+1]) / 2, # Para el polígono
            "absolute": int(counts[i]),
            "cumulative": int(cumulative[i])
        })
        
    return data

def get_statistics():
    """ Retorna Media, Mediana y Moda del Precio y Rating """
    df = get_dataframe()
    
    df['Price'] = pd.to_numeric(df['Price (USD)'], errors='coerce')
    df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
    
    stats = {}
    for col in ['Price', 'Rating']:
        s_data = df[col].dropna()
        if len(s_data) > 0:
            mean = s_data.mean()
            median = s_data.median()
            # La moda puede retornar múltiples valores, tomamos el primero
            modes = s_data.mode()
            mode = modes.iloc[0] if not modes.empty else None
            
            stats[col] = {
                "mean": round(mean, 2),
                "median": round(median, 2),
                "mode": round(mode, 2) if mode is not None else "N/A"
            }
            
    return stats

def get_raw_data(limit=20):
    """ Retorna una muestra de los datos para rellenar la tabla """
    df = get_dataframe()
    cols = ['Title', 'Author', 'Category', 'Price (USD)', 'Rating']
    res = df[cols].head(limit).fillna("N/A")
    return res.to_dict(orient='records')
