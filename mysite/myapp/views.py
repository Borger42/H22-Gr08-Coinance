import pandas as pd
import requests
import plotly.graph_objects as go

from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import CreateUserForm

from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponse


API_key = '03QDMPDVX4N8GR4U'

#   https://medium.com/codex/alpha-vantage-an-introduction-to-a-highly-efficient-free-stock-api-6d17f4481bf
def get_monthly_data(symbol):
    api_key = '03QDMPDVX4N8GR4U'
    api_url = f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol={symbol}&apikey={api_key}'
    raw_df = requests.get(api_url).json()

    df = pd.DataFrame(raw_df[f'Monthly Adjusted Time Series']).T
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

    symbol = 'TSLA'

    data = get_monthly_data(symbol)
    graph = get_plot(data)

    #ts = TimeSeries(key=API_key)
    #data1 = ts.get_monthly_adjusted('AAPL')

    # html = data.to_html()
    html = "<h1>Yooooooooooooo<h1>"

    html = graph

    return HttpResponse(html)

def home (request):
    return render(request,'home.html',{})

def aboutus (request):
    return render(request,'aboutus.html',{})


def Actions (request, action):
    symbole = action.upper()
    data = get_monthly_data(symbole)
    graph = get_plot(data)
    return render(request,'Actions.html',{'symbole' : symbole, 'graph' : graph})

def contact (request):
    return render(request,'contact.html',{})


def team (request):
    return render(request,'team.html',{})

def loginPage (request): #https://jsfiddle.net/ivanov11/dghm5cu7/
    #if request.user.is_authenticated:
        #return redirect('home')
    #else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password is incorrect')

        context = {}
        return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def registerPage (request): #https://jsfiddle.net/ivanov11/hzf0jxLg/
    #if request.user.is_authenticated:
        #return redirect('home')
    #else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'register.html', context)

def search_bar(request):
    if request.method == "Post":
        searched = request.Post('searched')

        return render(request, 'search_bar.html', {'searched' :searched})

    else:
        return render(request, 'search_bar.html', {})

def resultat (request):
    if request.method =="Post":
        searched = request.Post['searched']

        return render(request,'search_bar.html',{})

    else:
        return render(request, 'search_bar.html', {})


