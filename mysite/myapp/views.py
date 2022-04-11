import pandas as pd
import requests
import plotly.graph_objects as go
from django.shortcuts import render

from django.http import HttpResponse


API_key = '03QDMPDVX4N8GR4U'

#   https://medium.com/codex/alpha-vantage-an-introduction-to-a-highly-efficient-free-stock-api-6d17f4481bf
def get_monthly_data(symbol):
    api_key = '03QDMPDVX4N8GR4U'
    api_url = f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol={symbol}&apikey={api_key}'
    raw_df = requests.get(api_url).json()

    df = pd.DataFrame(raw_df[f'Monthly Time Series']).T
    df = df.rename(
        columns={'1. open': 'open', '2. high': 'high', '3. low': 'low', '4. close': 'close', '5. volume': 'volume'})
    for i in df.columns:
        df[i] = df[i].astype(float)
    df.index = pd.to_datetime(df.index)
    df = df.iloc[::-1]
    return df

def get_plot(data):
    figure = go.Figure(
        data=[
            go.Candlestick(
                x=data.index,
                open=data['open'],
                high=data['high'],
                low=data['low'],
                close=data['close']
            )
        ]
    )

    graph = figure.to_html()

    return graph

def index(request): # http://127.0.0.1:8000

    symbol = 'AAPL'

    data = get_monthly_data(symbol)
    graph = get_plot(data)

    #ts = TimeSeries(key=API_key)
    #data1 = ts.get_monthly_adjusted('AAPL')

    # html = data.to_html()
    html = "<h1>Yooooooooooooo<h1>"
    html = html+graph

    return HttpResponse(html)

def home (request):
    return render(request,'home.html',{})

def aboutus (request):
    return render(request,'aboutus.html',{})


def currency (request):
    return render(request,'Currency.html',{})

def contact (request):
    return render(request,'contact.html',{})

def login (request):
    return render(request,'login.html',{})

def register (request):
    return render(request,'register.html',{})