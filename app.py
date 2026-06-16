import dash
from dash import dcc, html
import pandas as pd

data = pd.read_csv("data/output.csv")

daily = data.groupby("date")["sales"].sum().reset_index()
daily = daily.sort_values("date")

PRICE_INCREASE_DATE = "2021-01-15"

app = dash.Dash(__name__)

app.layout = html.Div([

    html.H1(
        "Pink Morsel Sales Visualiser",
        style={
            "textAlign": "center",
            "fontFamily": "Arial",
            "color": "#d63384",
            "paddingTop": "30px"
        }
    ),

    html.P(
        "Daily sales of Pink Morsels over time. The red dashed line marks the price increase on 15 Jan 2021.",
        style={
            "textAlign": "center",
            "fontFamily": "Arial",
            "color": "#666",
            "marginBottom": "10px"
        }
    ),

    dcc.Graph(
        id="sales-chart",
        figure={
            "data": [
                {
                    "x": daily["date"],
                    "y": daily["sales"],
                    "type": "line",
                    "name": "Daily Sales",
                    "line": {"color": "#d63384", "width": 2}
                }
            ],
            "layout": {
                "title": "Total Daily Sales Over Time",
                "xaxis": {"title": "Date"},
                "yaxis": {"title": "Total Sales ($)"},
                "plot_bgcolor": "#fff",
                "paper_bgcolor": "#fff",
                "shapes": [
                    {
                        "type": "line",
                        "x0": PRICE_INCREASE_DATE,
                        "x1": PRICE_INCREASE_DATE,
                        "y0": 0,
                        "y1": 1,
                        "yref": "paper",
                        "line": {
                            "color": "red",
                            "width": 2,
                            "dash": "dash"
                        }
                    }
                ],
                "annotations": [
                    {
                        "x": PRICE_INCREASE_DATE,
                        "y": 1,
                        "yref": "paper",
                        "text": "Price Increase (15 Jan 2021)",
                        "showarrow": False,
                        "xanchor": "left",
                        "font": {"color": "red", "size": 12}
                    }
                ]
            }
        },
        style={"height": "550px"}
    )

], style={"maxWidth": "1100px", "margin": "0 auto", "padding": "20px"})

if __name__ == "__main__":
    app.run(debug=True)
