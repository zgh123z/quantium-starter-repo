import dash
from dash import dcc, html, Input, Output
import pandas as pd

data = pd.read_csv("data/output.csv")
data["date"] = pd.to_datetime(data["date"])

PRICE_INCREASE_DATE = "2021-01-15"

app = dash.Dash(__name__)

app.layout = html.Div([

    # Header
    html.Div([
        html.H1("🍬 Pink Morsel Sales Visualiser",
                style={"margin": "0", "fontSize": "2rem", "fontWeight": "700", "color": "#fff"}),
        html.P("Soul Foods · Sales Analytics Dashboard",
               style={"margin": "6px 0 0", "color": "#f9c4d8", "fontSize": "0.95rem"})
    ], style={
        "background": "linear-gradient(135deg, #d63384 0%, #9b1d5a 100%)",
        "padding": "28px 40px",
        "boxShadow": "0 4px 16px rgba(214,51,132,0.3)"
    }),

    # Main content
    html.Div([

        # Info bar
        html.Div([
            html.Div([
                html.Span("📍 Filter by Region", style={"fontWeight": "600", "color": "#d63384", "fontSize": "1rem"}),
                html.P("Select a region to explore sales trends",
                       style={"margin": "2px 0 0", "color": "#888", "fontSize": "0.85rem"})
            ]),
            html.Div([
                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {"label": " 🌐  All Regions", "value": "all"},
                        {"label": " 🔵  North",        "value": "north"},
                        {"label": " 🟢  East",         "value": "east"},
                        {"label": " 🟠  South",        "value": "south"},
                        {"label": " 🔴  West",         "value": "west"},
                    ],
                    value="all",
                    inline=True,
                    inputStyle={"marginRight": "5px", "accentColor": "#d63384"},
                    labelStyle={
                        "marginRight": "18px",
                        "fontSize": "0.92rem",
                        "fontWeight": "500",
                        "color": "#444",
                        "cursor": "pointer"
                    }
                )
            ])
        ], style={
            "background": "#fff",
            "border": "1.5px solid #f0c0d8",
            "borderRadius": "14px",
            "padding": "20px 28px",
            "marginBottom": "22px",
            "display": "flex",
            "alignItems": "center",
            "justifyContent": "space-between",
            "flexWrap": "wrap",
            "gap": "14px",
            "boxShadow": "0 2px 8px rgba(214,51,132,0.08)"
        }),

        # Chart
        html.Div([
            dcc.Graph(
                id="sales-chart",
                config={"displayModeBar": False},
                style={"height": "480px"}
            )
        ], style={
            "background": "#fff",
            "borderRadius": "14px",
            "padding": "10px",
            "boxShadow": "0 2px 12px rgba(0,0,0,0.08)",
            "border": "1px solid #f0e0e8"
        }),

        # Footer note
        html.P(
            "📌 The dashed red line marks the Pink Morsel price increase on 15 January 2021.",
            style={
                "textAlign": "center",
                "color": "#aaa",
                "fontSize": "0.83rem",
                "marginTop": "18px"
            }
        )

    ], style={
        "maxWidth": "1100px",
        "margin": "0 auto",
        "padding": "30px 24px"
    })

], style={"background": "#fdf5f9", "minHeight": "100vh", "fontFamily": "'Segoe UI', Arial, sans-serif"})


@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(region):
    if region == "all":
        filtered = data.groupby("date")["sales"].sum().reset_index()
        chart_title = "Total Daily Sales — All Regions"
    else:
        filtered = data[data["region"] == region].groupby("date")["sales"].sum().reset_index()
        chart_title = f"Daily Sales — {region.capitalize()} Region"

    filtered = filtered.sort_values("date")

    return {
        "data": [{
            "x": filtered["date"],
            "y": filtered["sales"],
            "type": "line",
            "name": "Sales",
            "line": {"color": "#d63384", "width": 2.5},
            "fill": "tozeroy",
            "fillcolor": "rgba(214,51,132,0.07)"
        }],
        "layout": {
            "title": {"text": chart_title, "font": {"size": 17, "color": "#333"}},
            "xaxis": {
                "title": "Date",
                "gridcolor": "#f5e8ef",
                "linecolor": "#ddd"
            },
            "yaxis": {
                "title": "Total Sales ($)",
                "gridcolor": "#f5e8ef",
                "linecolor": "#ddd"
            },
            "plot_bgcolor": "#fff",
            "paper_bgcolor": "#fff",
            "shapes": [{
                "type": "line",
                "x0": PRICE_INCREASE_DATE,
                "x1": PRICE_INCREASE_DATE,
                "y0": 0, "y1": 1,
                "yref": "paper",
                "line": {"color": "red", "width": 2, "dash": "dash"}
            }],
            "annotations": [{
                "x": PRICE_INCREASE_DATE,
                "y": 0.97,
                "yref": "paper",
                "text": "Price Increase ↑",
                "showarrow": False,
                "xanchor": "left",
                "font": {"color": "red", "size": 12}
            }],
            "margin": {"l": 60, "r": 30, "t": 50, "b": 60},
            "hovermode": "x unified"
        }
    }


if __name__ == "__main__":
    app.run(debug=True)        id="sales-chart",
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
