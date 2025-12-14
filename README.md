# AI-Powered Dynamic Patrol Allocation System

This project is a proof-of-concept for an intelligent patrol management system that optimizes police patrol deployment across urban zones based on real-time traffic data, probabilistic risk modeling, and historical incident patterns. Designed initially for Dubai, the model can be adapted to other cities with dynamic road networks and varying risk zones.

## 🚀 Key Features

- 📊 **Probabilistic Risk Modeling** using TensorFlow Probability
- 🧠 **Bayesian Decision Making** with exploration vs. exploitation logic
- 🛰️ **Live Traffic Data Integration** via TomTom API
- 📍 **Zone-Based Patrol Simulation** with 50+ Dubai zones
- 🔁 **Real-Time Learning & Feedback Loop** (using Airtable)
- 🧭 **Multi-Vehicle Dynamic Routing** with MVT logic
- 📈 **Dashboard for Risk Heatmaps & Efficiency Metrics**

---

## 🧠 Technologies Used

| Component           | Technology                  |
|--------------------|-----------------------------|
| AI Framework       | TensorFlow Probability (TFP) |
| Data Storage       | Airtable (Live Updates)     |
| Traffic Data       | TomTom Maps API             |
| Visualization      | Matplotlib, Seaborn         |
| Backend Logic      | Python                      |
| Hosting (Optional) | Google Colab / Streamlit    |

---

## 🗺️ Project Flow

1. **Zone Risk Initialization**: Historical data and default risk values per zone
2. **Live Data Fetching**: Real-time traffic retrieved from TomTom API
3. **Bayesian Update**: Risk levels updated using live conditions
4. **Decision Algorithm**: Patrol actions determined using Multi-Armed Bandit logic
5. **Patrol Simulation**: Vehicle movement and coverage visualized per hour
6. **Efficiency Evaluation**: Metrics calculated (e.g., risk handled, patrol hit rate)

---

## 📌 Example Output

- 🔢 Zones considered: `50`
- 🚓 Patrols: `10`
- ⚠️ Risk Events Handled: `~13% efficiency` (P.O.C.)
- 📉 Dynamic dashboards for strategy visualization

---

## 📁 File Structure

```bash
📦 AI-Patrol-Manager
├── patrol_model.ipynb        # Main model with TensorFlow Probability
├── patrol_dashboard.ipynb    # Dashboard and graphs
├── zone_data.csv             # Zone information with base risk
├── README.md                 # Project overview
├── airtable_sync.py          # Airtable data integration
