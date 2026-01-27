import math
from typing import List, Tuple
import pandas as pd

Point = Tuple[float, float]  # (latitude, longitude)

EARTH_RADIUS_M = 6_371_000

def haversine_distance(p1: Point, 
                       p2: Point) -> float:
    """
    Compute distance in meters between two GPS coordinates using Haversine formula.
    """
    lat1, lon1 = p1
    lat2, lon2 = p2

    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)

    a = math.sin(dphi / 2) ** 2 + \
        math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return EARTH_RADIUS_M * c


def match_closest(source_points: List[Point],
                  target_points: List[Point],) -> List[Tuple[Point, Point, float]]:
    """
    For each point in source_points, find the closest point in target_points.
    
    Returns list of (source_point, closest_target_point, distance_meters)
    """
    if not target_points:
        raise ValueError("target_points must not be empty")

    matches = []

    for sp in source_points:
        closest = min(
            target_points,
            key=lambda tp: haversine_distance(sp, tp)
        )
        distance = haversine_distance(sp, closest)
        matches.append((sp, closest, distance))

    return matches

def get_geo_coordinates(file: str) -> pd.DataFrame: 
    """
    Reads a CSV file and returns a set of geo coordinates
    """
    df = pd.read_csv(file)
    df_trimmed = df[["full_address","street_number","street_name","zip_code",
                     "neighborhood","public_works_district","city_council_district",
                     "fire_district","police_district","ward","precinct",
                     "latitude", "longitude"]].copy()

    return df_trimmed