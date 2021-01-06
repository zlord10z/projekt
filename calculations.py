import math
import numpy as np

def calculateDistance(lat1, lat2, long1, long2):
    # Haversine formula

    r = 6378.137  # Earth Radius - 6378.137 km
    d = 0  # distanace

    p = math.pi / 180.0

    lat21 = ((lat2 - lat1) / 2) * p
    long21 = ((long2 - long1) / 2) * p
    lat1 = (lat1) * p
    lat2 = (lat2) * p

    ob_a = math.sin(lat21) ** 2
    ob_b = math.sin(long21) ** 2

    obl = math.sqrt(ob_a + math.cos(lat1) * math.cos(lat2) * ob_b)

    d = 2 * r * math.asin(obl)

    return d


def most_frequently_visited_place(list_lat, list_long):
    # srednia (wybranie lokalizacji ktorej zakazony byl najczesciej danego dnia i godziny tego dnia)
    average_lat = 0
    average_long = 0
    for i in range(len(list_lat)):
        average_lat += list_lat[i]
        average_long += list_long[i]

    if len(list_lat) != 0:
        average_lat = average_lat / len(list_lat)
        average_long = average_long / len(list_long)

    # dopasowanie elementu nabliżej średniej i wskazanie indeksu elementu w liscie
    index_lat = np.argmin(np.abs(np.array(list_lat) - average_lat))
    index_long = np.argmin(np.abs(np.array(list_long) - average_long))
    return [index_lat, index_long]
