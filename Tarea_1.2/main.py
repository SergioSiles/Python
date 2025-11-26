# Importamos las librerías necesarias
import pandas as pd
import numpy as np
import re

# Cargamos el archivo CSV original con datos sucios
df = pd.read_csv("personas_sucio.csv")

# Eliminamos filas completamente vacías
df = df.dropna(how='all')

# Normalizar nombres: 
# - Convertimos a texto
# - Quitamos espacios en blanco
# - Ponemos la primera letra en mayúscula y el resto en minúscula
df["nombre"] = df["nombre"].astype(str).str.strip().str.title()

# Convertimos las edades a formato numérico
# - Forzamos a número
# - Calculamos la media de la columna edad
# - Sustituimos los NaN por la media
# - Convertimos las edades a enteros
df["edad"] = pd.to_numeric(df["edad"], errors="coerce")
edad_media = df["edad"].mean(skipna=True)
df["edad"] = df["edad"].fillna(edad_media)
df["edad"] = df["edad"].astype(int)

# Convertimos todas las ciudades a MAYÚSCULAS
df["ciudad"] = df["ciudad"].astype(str).str.strip().str.upper()

# Validamos los emails
# - Eliminamos espacios
# - Comprobamos si cumplen el formato
# - Si no es valido, lo sustituimos por desconocido@correo.com
df["email"] = df["email"].astype(str).str.strip()
df["email"] = df["email"].apply(lambda x: x if re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", x) else np.nan)
df["email"] = df["email"].fillna("desconocido@correo.com")

# Formateamos las fechas al formato DD/MM/AAAA
# - Convertimos a tipo fecha
# - Las convertimos a texto con formato día/mes/año
# - Sustituimos las vacías por una fecha por defecto
df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce")
df["fecha"] = df["fecha"].dt.strftime("%d/%m/%Y")
df["fecha"] = df["fecha"].fillna("01/01/2000")

# Guardamos el nuevo CSV limpio
df.to_csv("personas_limpio.csv", index=False)
