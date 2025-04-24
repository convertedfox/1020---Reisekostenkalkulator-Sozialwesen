import streamlit as st
import os
import pandas as pd
from gesamtkosten_errechnen import gesamtkosten_errechnen

## Daten laden
@st.cache_data
def load_data():
    dozenten = pd.read_csv(os.path.join("data", "dozenten.csv"))
    standorte = pd.read_csv(os.path.join("data", "standorte.csv"))
    blockstrukturen = ["2 Tage, dann 3 Tage"]
    return dozenten, standorte, blockstrukturen

st.title("Kostenkalkulator Sozialwesen 🚗")

# Daten laden
dozenten, standorte, blockstrukturen = load_data()

# Standorte auswählen
st.markdown("### Infos zur Veranstaltung")
blöcke = st.selectbox("Wie sind die Blöcke der Veranstaltung strukturiert?", blockstrukturen)
# Dozenten auswählen
st.markdown("### Dozentenauswahl")
dozent = st.selectbox("Dozent", dozenten["Name"].values)
st.write(dozenten[dozenten["Name"] == dozent])
# Kostenkalulation
st.markdown("### Kostenkalkulation")
st.write("Heimatort: " + dozenten[dozenten["Name"] == dozent]["heimatort"].values[0])

# Gesamtkosten berechnen
gesamtkosten = gesamtkosten_errechnen(dozenten[dozenten["Name"] == dozent]["heimatort"].values[0], dozenten[dozenten["Name"] == dozent]["dienstort"].values[0] )
st.write(gesamtkosten)
minimum = float(gesamtkosten["Gesamtkosten"].min())
bester_standort=gesamtkosten[gesamtkosten["Gesamtkosten"] == minimum]["Veranstaltungsort"].values[0]
## Ergebbnisse
st.markdown("### Ergebnisse")
st.write("Die niedrigsten Gesamtkosten wären " + str(minimum) + " € am Standort " + bester_standort + "!")