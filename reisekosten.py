import requests
import json
import time
from geopy.geocoders import Nominatim
import streamlit as st

@st.cache_data
def reisekosten_rechnen(startort, zielort, dienstort) -> float:
    '''
    Berechnet die Reisekosten von Startort zu Zielort.
    startort: str, Startort
    zielort: str, Zielort: Dort findet die Veranstaltung statt
    dienstort: str, Dienstort
    return: float, Reisekosten
    '''
    # Entfernung berechnen
    if zielort == dienstort:
        distance = 0
    else:
        distance = get_road_distance(startort, zielort)
    kosten = distance * 0.3
    return round(kosten, 0), distance

@st.cache_data
def get_road_distance(location1, location2) -> float:
    '''
    Berechnet die Entfernung zwischen zwei Orten.
    location1: str, Startort
    location2: str, Zielort
    return: float, Entfernung in km
    '''
    # Erst Koordinaten mit Nominatim ermitteln
    geolocator = Nominatim(user_agent="distance_calculator")
    
    location1_data = geolocator.geocode(location1)
    location2_data = geolocator.geocode(location2)
    
    coords1 = (location1_data.longitude, location1_data.latitude)
    coords2 = (location2_data.longitude, location2_data.latitude)
    
    # OSRM API-Anfrage für die Streckenberechnung
    url = f"http://router.project-osrm.org/route/v1/driving/{coords1[0]},{coords1[1]};{coords2[0]},{coords2[1]}?overview=false"
    
    response = requests.get(url)
    data = json.loads(response.text)
    
    # Entfernung in Metern umrechnen in Kilometer
    distance_km = data['routes'][0]['distance'] / 1000
    # Eine Sekunde warten um die API nicht zu überlasten
    time.sleep(2)
    return distance_km

if __name__ == "__main__":
    print(reisekosten_rechnen("Hamburg", "Berlin")) 