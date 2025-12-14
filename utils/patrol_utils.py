# utils/patrol_utils.py

import numpy as np
import math

def calculate_reward(base_risk, traffic_delay):
    """
    Combines risk and delay into a single reward metric.
    Higher risk and lower delay = higher reward.
    """
    return base_risk / (1 + traffic_delay)

def select_next_zone(probabilities):
    """
    Selects next patrol zone using probabilistic sampling.
    """
    zones = list(probabilities.keys())
    weights = np.array(list(probabilities.values()))
    weights = weights / weights.sum()  # Normalize to sum to 1
    return np.random.choice(zones, p=weights)

def update_risk_with_traffic(base_risk, traffic_factor):
    """
    Updates base risk using a traffic congestion factor.
    """
    return base_risk * (1 + traffic_factor)

def calculate_efficiency(events_detected, total_events):
    """
    Calculates patrol efficiency as percentage.
    """
    return round(100 * events_detected / total_events, 2) if total_events > 0 else 0

def compute_patrol_score(base_risk, traffic_factor, confidence):
    """
    Compute adjusted patrol score based on base risk, traffic, and confidence level.
    
    Parameters:
        base_risk (float): Historical risk value (1–10)
        traffic_factor (float): Ratio of current speed / free flow speed (< 1 = congestion)
        confidence (float): Confidence in traffic data (0–1)
        
    Returns:
        float: Adjusted score, rounded between 1 and 10
    """
    adjusted = base_risk * (1 + (1 - traffic_factor)) * confidence
    return round(min(max(adjusted, 1), 10), 2)

def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Compute the Haversine distance (in km) between two geographic points.
    
    Parameters:
        lat1, lon1 (float): Coordinates of point 1
        lat2, lon2 (float): Coordinates of point 2
    
    Returns:
        float: Distance in kilometers
    """
    R = 6371  # Earth radius in km
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2)**2 + \
        math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c

