import requests
import pandas as pd
import numpy as np

def make_request():
    base_url = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync"

    query = """
    SELECT pl_name, ra, dec, sy_dist, pl_orbper, pl_rade, pl_bmasse, pl_eqt,
        st_teff, st_rad, pl_orbsmax
    FROM ps
    WHERE pl_rade > 0.5 AND pl_rade < 2.0
    AND pl_eqt > 200 AND pl_eqt < 400
    ORDER BY sy_dist ASC
    """

    params = {
        "query": query,
        "format": "json"
    }
    
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)

        df['pl_radius_m'] = df['pl_rade'] * 6.371e6   # Raio em metros (raio da Terra)

        return df
    else:
        print("Erro na solicitação:", response.status_code)
        return None