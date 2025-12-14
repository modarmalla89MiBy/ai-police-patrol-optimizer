# train_model.py

from patrol_model import run_simulation
from utils.patrol_utils import calculate_efficiency
import pandas as pd

# Load zone data
zone_df = pd.read_csv('zone_data (1).csv')

# Run simulation (example setup)
results = run_simulation(
    zone_data=zone_df,
    num_patrols=10,
    total_steps=100,
    exploration_rate=0.3
)

# Display basic result summary
print("\n--- Simulation Summary ---")
print(f"Events Handled: {results['events_handled']}")
print(f"Total Events: {results['total_events']}")
print(f"Efficiency: {calculate_efficiency(results['events_handled'], results['total_events'])}%")

# Optionally save results
pd.DataFrame(results['log']).to_csv('patrol_simulation_log.csv', index=False)
