"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pathlib
import pandas as pd

def pregunta_03():
    """
    ¿Cuál es la cantidad de registros por cada letra de la columna `c1` del
    archivo `tbl0.tsv`?

    Rta/
    c1
    A     8
    B     7
    C     5
    D     6
    E    14
    Name: count, dtype: int64

    """
    current_dir = pathlib.Path(__file__).parent
    path = current_dir.parent / "files" / "input" / "tbl0.tsv"
    tbl0 = pd.read_csv(path, sep="\t")
    return tbl0["c1"].value_counts().sort_index()