# visualize_results.py

import pandas as pd
import matplotlib.pyplot as plt

# Load simulation log
df = pd.read_csv("patrol_simulation_log.csv")

# Plot risk over time
plt.figure(figsize=(10, 4))
plt.plot(df['step'], df['average_risk'], label='Avg Risk', color='orange')
plt.title("Average Zone Risk Over Time")
plt.xlabel("Step")
plt.ylabel("Risk Level")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("avg_risk_plot.png")
plt.show()

# Plot handled events
plt.figure(figsize=(10, 4))
plt.plot(df['step'], df['events_handled'], label='Events Handled', color='green')
plt.title("Cumulative Events Handled")
plt.xlabel("Step")
plt.ylabel("Event Count")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("events_handled_plot.png")
plt.show()
