"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    import pandas as pd
    import re

    with open("files/input/clusters_report.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    lines = [line.rstrip() for line in lines if line.strip() and not line.startswith("-")]
    start_idx = next(i for i, line in enumerate(lines) if re.match(r"^\s*\d+\s", line))
    data_lines = lines[start_idx:]

    clusters = []
    current = ""

    for line in data_lines:
        if re.match(r"^\s*\d+\s", line):
            if current:
                clusters.append(current.strip())
            current = line.strip() 
        else:
            current += " " + line.strip()
    if current:
        clusters.append(current.strip())

    data = []
    for c in clusters:
        
        parts = re.split(r"\s{2,}", c, maxsplit=3)
        
        cluster = int(parts[0])
        cantidad = int(parts[1])
        porcentaje = float(parts[2].replace(" %", "").replace(",", "."))
        
        palabras = parts[3] if len(parts) > 3 else ""
        data.append([cluster, cantidad, porcentaje, palabras])

    df = pd.DataFrame(
        data,
        columns=[
            "cluster",
            "cantidad_de_palabras_clave",      
            "porcentaje_de_palabras_clave",     
            "principales_palabras_clave",       
        ],
    )

    df["principales_palabras_clave"] = (
        df["principales_palabras_clave"]
        .str.replace(r"\s+", " ", regex=True)     
        .str.replace(r",\s*", ", ", regex=True)   
        .str.strip()                              
        .str.replace(r"\.$", "", regex=True)     
    )

    return df




