# File: utils/patrol_utils.py

import numpy as np

def calculate_reward(base_risk, traffic_delay):
    """
    Combines risk and delay into a single reward metric.
    Higher risk and lower delay = higher reward.
    """
    return base_risk / (1 + traffic_delay)

def select_next_zone(probabilities):
    """
    Selects next patrol zone using probabilistic sampling
    """
    zones = list(probabilities.keys())
    weights = np.array(list(probabilities.values()))
    weights = weights / weights.sum()  # normalize
    return np.random.choice(zones, p=weights)

def update_risk_with_traffic(base_risk, traffic_factor):
    """
    Simple function to combine historical risk and traffic data.
    """
    return base_risk * (1 + traffic_factor)

def calculate_efficiency(events_detected, total_events):
    """
    Calculates patrol efficiency (hit rate).
    """
    return round(100 * events_detected / total_events, 2) if total_events > 0 else 0
