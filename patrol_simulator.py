import pandas as pd
import numpy as np
from utils.patrol_utils import compute_patrol_score
from utils.live_traffic import fetch_tomtom_traffic

class PatrolUnit:
    def __init__(self, id, start_zone):
        self.id = id
        self.current_zone = start_zone
        self.route_history = [start_zone]

    def move_to(self, next_zone):
        self.current_zone = next_zone
        self.route_history.append(next_zone)

class PatrolSimulation:
    def __init__(self, zones_csv, num_patrols=10, api_key=None):
        self.zones_df = pd.read_csv(zones_csv)
        self.num_patrols = num_patrols
        self.patrols = []
        self.api_key = api_key
        self.zone_scores = self.zones_df[['Zone ID', 'Base Risk']].copy()
        self.zone_scores['Updated Risk'] = self.zone_scores['Base Risk']
        self.init_patrols()

    def init_patrols(self):
        start_zones = np.random.choice(self.zones_df['Zone ID'], self.num_patrols, replace=False)
        self.patrols = [PatrolUnit(i, zone) for i, zone in enumerate(start_zones)]

    def update_zone_risks(self):
        for i, row in self.zones_df.iterrows():
            if self.api_key:
                traffic = fetch_tomtom_traffic(self.api_key, row['Latitude'], row['Longitude'])
                if traffic:
                    traffic_factor = (traffic['currentSpeed'] / traffic['freeFlowSpeed']) if traffic['freeFlowSpeed'] > 0 else 1
                    confidence_weight = traffic['confidence']
                    new_risk = compute_patrol_score(row['Base Risk'], traffic_factor, confidence_weight)
                    self.zone_scores.loc[i, 'Updated Risk'] = new_risk
            else:
                noise = np.random.normal(0, 0.3)
                self.zone_scores.loc[i, 'Updated Risk'] = row['Base Risk'] + noise

    def assign_patrols(self):
        assigned_zones = set()
        for patrol in self.patrols:
            available = self.zone_scores[~self.zone_scores['Zone ID'].isin(assigned_zones)]
            if available.empty:
                continue
            next_zone = available.sort_values('Updated Risk', ascending=False).iloc[0]['Zone ID']
            patrol.move_to(next_zone)
            assigned_zones.add(next_zone)

    def run_simulation(self, steps=5):
        for step in range(steps):
            print(f"\n--- Step {step + 1} ---")
            self.update_zone_risks()
            self.assign_patrols()
            self.print_patrols()

    def print_patrols(self):
        for patrol in self.patrols:
            print(f"Patrol #{patrol.id} moved to zone: {patrol.current_zone}")

if __name__ == "__main__":
    sim = PatrolSimulation("zone_data.csv", num_patrols=10, api_key=None)  # Replace with your TomTom API key if available
    sim.run_simulation(steps=5)
