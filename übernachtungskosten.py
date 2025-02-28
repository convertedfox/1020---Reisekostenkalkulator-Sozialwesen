def übernachtungskosten_berechnen(distanz, anzahl_nächte) -> float:
    '''
    Diese Funktion berechnet die Übernachtungskosten für eine Reise.
    
    distanz: float,  Distanz zwischen Start- und Zielort
    anzahl_nächte: int, Anzahl der Übernachtungen
    return: float, Übernachtungskosten
    '''
    übernachtungskosten_pro_nacht = 95
    if distanz > 170:
        übernachtungskosten_pro_nacht = anzahl_nächte *übernachtungskosten_pro_nacht
    else:
        übernachtungskosten_pro_nacht = 0

    return übernachtungskosten_pro_nacht