class GestorFitxers:

    @staticmethod
    def filtrar_agricultura(
        df,
        country,
        region,
        crop,
        years,
    ):
        base_columns = [
            'Year',
            'Country',
            'Region',
            'Crop_Type',
            'Average_Temperature_C',
            'Adaptation_Strategies',
            'Economic_Impact_Million_USD',
            'Fertilizer_Use_KG_per_HA',
            'Pesticide_Use_KG_per_HA',
            'Irrigation_Access_%',
            'Crop_Yield_MT_per_HA'
        ]

        mask = (
            df['Year'].isin(years) &
            (df['Country'] == country) &
            (df['Region'] == region) &
            (df['Crop_Type'] == crop)
        )

        resultado = (
            df.loc[mask, base_columns]
              .sort_values(by='Year')
              .reset_index(drop=True)
        )

        return resultado

    def __str__(self):
        return "GestorFitxers: utilidad para filtrado de datos agrícolas"
