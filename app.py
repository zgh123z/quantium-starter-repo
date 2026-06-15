import dash
from dash import dcc, html
import pandas as pd
import glob

# --- Load and combine all CSV files ---
files = glob.glob("data/daily_sales_data_*.csv")
dfs = []
for f in files:
    df = pd.read_csv(f)
    dfs.append(df)

data = pd.concat(dfs, ignore_index=True)

# Keep only pink morsel rows
data = data[data["product"] == "pink morsel"].copy()

# Clean price column (remove $) and calculate sales
data["price"] = data["price"].str.replace("$", "", regex=False).astype(float)
data["sales"] = data["price"] * data["quantity"]

# Group by date
daily = data.groupby("date")["sales"].sum().reset_index()
daily.columns = ["date", "sales"]
daily = daily.sort_values("date")

# --- Build the Dash App ---
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualiser",
            style={"textAlign": "center", "fontFamily": "Arial", "color": "#d63384"}),

    dcc.Graph(
        id="sales-chart",
        figure={
            "data": [{
                "x": daily["date"],
                "y": daily["sales"],
                "type": "line",
                "name": "Daily Sales",
                "line": {"color": "#d63384"}
            }],
            "layout": {
                "title": "Daily Sales of Pink Morsel Over Time",
                "xaxis": {"title": "Date"},
                "yaxis": {"title": "Total Sales ($)"},
                "plot_bgcolor": "#fff",
                "paper_bgcolor": "#fff"
            }
        }
    )
], style={"maxWidth": "960px", "margin": "0 auto", "padding": "20px"})

if __name__ == "__main__":
    app.run(debug=True)
