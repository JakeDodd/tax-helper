import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

data = pd.read_csv("test.csv")

app = Dash(__name__)

fig = px.pie(data, values="amount", names="category", title="Taxes")

app.layout = html.Div(
    children=[
        html.H1(children="Analysis of Tax Distribution"),
        dcc.Graph(
            figure=fig
        ),
       ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
