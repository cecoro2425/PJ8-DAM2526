from abc import ABC, abstractmethod
from GestorFitxers import GestorFitxers
import pandas as pd


# =======================
# Clase abstracta
# =======================

class AnalisisBase(ABC):
    def __init__(self, df, country, region, crop, years):
        self.country = country
        self.region = region
        self.crop = crop
        self.years = years

        self.df = GestorFitxers.filtrar_agricultura(
            df,
            country,
            region,
            crop,
            years
        )

    @abstractmethod
    def analizar(self):
        pass

    @abstractmethod
    def graficar(self):
        pass

    def __str__(self):
        return f"Análisis agrícola en {self.country} - {self.region} ({self.crop})"

    def __eq__(self, other):
        return (
            isinstance(other, AnalisisBase) and
            self.country == other.country and
            self.region == other.region and
            self.crop == other.crop and
            self.years == other.years
        )


# =======================
# Análisis climático
# =======================

class AnalisisClimatico(AnalisisBase):

    def analizar(self):
        return self.df[['Average_Temperature_C']].describe()

    def graficar(self):
        self.df.plot(
            x='Year',
            y='Average_Temperature_C',
            title=f"Temperatura media - {self.country}"
        )

    def __str__(self):
        return f"Análisis Climático [{self.country} - {self.crop}]"


# =======================
# Análisis socioeconómico
# =======================

class AnalisisSocioeconomico(AnalisisBase):

    def analizar(self):
        return self.df[
            ['Economic_Impact_Million_USD', 'Crop_Yield_MT_per_HA']
        ].corr()

    def graficar(self):
        self.df.plot(
            x='Year',
            y='Economic_Impact_Million_USD',
            title=f"Impacto económico - {self.country}"
        )

    def __str__(self):
        return f"Análisis Socioeconómico [{self.country} - {self.region}]"


# =======================
# Clase principal
# =======================

class ProyectoAgricola:
    def __init__(self, ruta_csv):
        self.df = pd.read_csv(ruta_csv)
        self.analisis = []

    def crear_analisis_climatico(self, country, region, crop, years):
        analisis = AnalisisClimatico(
            self.df,
            country,
            region,
            crop,
            years
        )
        self.analisis.append(analisis)
        return analisis

    def crear_analisis_socioeconomico(self, country, region, crop, years):
        analisis = AnalisisSocioeconomico(
            self.df,
            country,
            region,
            crop,
            years
        )
        self.analisis.append(analisis)
        return analisis

    def __str__(self):
        return f"Proyecto agrícola con {len(self.analisis)} análisis"

    def __eq__(self, other):
        return (
            isinstance(other, ProyectoAgricola) and
            self.df.equals(other.df)
        )
