"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pathlib
import pandas as pd

def pregunta_01():
    """
    ¿Cuál es la cantidad de filas en la tabla `tbl0.tsv`?

    Rta/
    40

    """
    current_dir = pathlib.Path(__file__).parent
    path = current_dir.parent / "files" / "input" / "tbl0.tsv"
    tbl0 = pd.read_csv(path, sep="\t")
    return tbl0.shape[0]