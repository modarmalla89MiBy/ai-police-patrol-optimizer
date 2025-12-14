# patrol_model.py

import numpy as np
import pandas as pd
import tensorflow_probability as tfp
import tensorflow as tf
from scipy.spatial.distance import cdist

tfd = tfp.distributions

class PatrolModel:
    def __init__(self, zone_file, num_patrols=10):
        self.zone_df = pd.read_csv(zone_file)
        self.num_zones = len(self.zone_df)
        self.num_patrols = num_patrols
        self.init_probabilistic_model()

    def init_probabilistic_model(self):
        base_risks = self.zone_df['Base Risk'].values
        self.base_risks = tf.convert_to_tensor(base_risks, dtype=tf.float32)
        self.zone_ids = self.zone_df['Zone ID'].tolist()
        self.current_risk = tfd.Normal(loc=self.base_risks, scale=1.0).sample()

    def update_risks_with_live_data(self, traffic_weights):
        self.current_risk += tf.convert_to_tensor(traffic_weights, dtype=tf.float32)

    def choose_patrol_zones(self):
        sorted_indices = tf.argsort(self.current_risk, direction='DESCENDING')
        selected = sorted_indices[:self.num_patrols]
        return [self.zone_ids[i] for i in selected.numpy()]

    def compute_efficiency(self, handled_risks):
        total_risk = tf.reduce_sum(self.current_risk)
        handled_total = tf.reduce_sum(handled_risks)
        return float(handled_total / total_risk * 100)

# Example usage:
if __name__ == "__main__":
    model = PatrolModel("zone_data.csv", num_patrols=10)
    traffic = np.random.normal(loc=1.0, scale=0.2, size=model.num_zones)
    model.update_risks_with_live_data(traffic)
    patrol_zones = model.choose_patrol_zones()
    print("Zones to Patrol:", patrol_zones)
