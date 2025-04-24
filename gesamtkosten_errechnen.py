import os
import pandas as pd
import streamlit as st
from reisekosten import reisekosten_rechnen
from übernachtungskosten import übernachtungskosten_berechnen

@st.cache_data
def gesamtkosten_errechnen(startort, dienstort) -> pd.DataFrame:
    '''
    Diese Funktion geht errechnet für einen Dozenten und seinen Startort ein Dataframe mit allen Kosten, die für jeden Standort anfallen.
    '''

    spalten = ["Veranstaltungsort", "Reisekosten", "Übernachtungskosten", "Mietkosten", "Gesamtkosten"]
    standorte = pd.read_csv(os.path.join("data", "standorte.csv"))
    
    ergebnisse = []
    
    for standort in standorte["name"]:
        reisekosten, distanz = reisekosten_rechnen(startort, standort, dienstort)
        # print(startort, standort, reisekosten)
        übernachtungskosten = übernachtungskosten_berechnen(distanz, 3)
        mietkosten = standorte[standorte["name"] == standort]["raummiete_pro_tag"].values
        gesamtkosten = reisekosten + übernachtungskosten + mietkosten
        ergebnisse.append([standort, reisekosten, übernachtungskosten, mietkosten, gesamtkosten])
    
    kostentabelle = pd.DataFrame(ergebnisse, columns=spalten)
    return kostentabelle

if __name__ == "__main__":
    print(gesamtkosten_errechnen("Heidelberg"))