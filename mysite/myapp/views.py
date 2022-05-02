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


def get_weekly_data(symbol):
    api_key = '03QDMPDVX4N8GR4U'
    api_url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol={symbol}&apikey={api_key}'
    raw_df = requests.get(api_url).json()

    df = pd.DataFrame(raw_df[f'Weekly Adjusted Time Series']).T
    df = df.rename(
        columns={'1. open': 'open', '2. high': 'high', '3. low': 'low', '4. close': 'close', '5. volume': 'volume'})
    for i in df.columns:
        df[i] = df[i].astype(float)
    df.index = pd.to_datetime(df.index)
    df = df.iloc[::-1]
    return df

def get_daily_data(symbol):
    api_key = '03QDMPDVX4N8GR4U'
    api_url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}'
    raw_df = requests.get(api_url).json()

    df = pd.DataFrame(raw_df[f'Time Series (Daily)']).T
    df = df.rename(
        columns={'1. open': 'open', '2. high': 'high', '3. low': 'low', '4. close': 'close', '5. volume': 'volume'})
    for i in df.columns:
        df[i] = df[i].astype(float)
    df.index = pd.to_datetime(df.index)
    df = df.iloc[::-1]
    return df


def recherche_par_mot_cle(mot_cle):
    api_key = '03QDMPDVX4N8GR4U'
    api_url = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={mot_cle}&apikey={api_key}'
    raw_df = requests.get(api_url).json()
    df = pd.DataFrame(raw_df['bestMatches'])
    df = df.rename(
        columns={'1. symbol': 'symbol',
                 '2. name': 'name',
                 '3. type': 'type',
                 '4. region': 'region',
                 '5. marketOpen': 'marketOpen',
                 '6. marketClose': 'marketClose',
                 '7. timezone': 'timezone',
                 '8. currency': 'currency',
                 '9. matchScore': 'matchScore'})
    return df


def resultat_to_html(df):
    html = ''
    for index, row in df.iterrows():
        html += f'<h1> <a href="/actions/{row["symbol"]}">{row["name"]} : {row["symbol"]}    {row["region"]}    {row["currency"]}</a><h1>\n'
    return html


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


def index(request):  # http://127.0.0.1:8000

    symbol = 'TSLA'

    data = get_monthly_data(symbol)
    graph = get_plot(data)

    # ts = TimeSeries(key=API_key)
    # data1 = ts.get_monthly_adjusted('AAPL')

    # html = data.to_html()
    # html = "<h1>Yooooooooooooo<h1>"

    html = graph

    return HttpResponse(html)


def home(request):
    return render(request, 'home.html', {})


def aboutus(request):
    return render(request, 'aboutus.html', {})


def ActionsDaily(request, action):
    symbole = action.upper()
    data = get_daily_data(symbole)
    graph = get_plot(data)
    return render(request, 'Actions.html', {'symbole': symbole, 'graph': graph})


def ActionsWeekly(request, action):
    symbole = action.upper()
    data = get_weekly_data(symbole)
    graph = get_plot(data)
    return render(request, 'Actions.html', {'symbole': symbole, 'graph': graph})


def ActionsMonthly(request, action):
    symbole = action.upper()
    data = get_monthly_data(symbole)
    graph = get_plot(data)
    return render(request, 'Actions.html', {'symbole': symbole, 'graph': graph})


def contact(request):
    return render(request, 'contact.html', {})


def team(request):
    return render(request, 'team.html', {})


def loginPage(request):  # https://jsfiddle.net/ivanov11/dghm5cu7/
    if request.user.is_authenticated:
        return redirect('home')
    else:
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


def registerPage(request):  # https://jsfiddle.net/ivanov11/hzf0jxLg/
    if request.user.is_authenticated:
        return redirect('home')
    else:
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


def userPage(request):
    products =Product.objects.all()
    context = {'products':products}
    return render(request, 'user.html', context)


def get_data_now(symbol):
    api_key = '03QDMPDVX4N8GR4U'
    api_url=f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}'
    raw_df = requests.get(api_url).json()

    df = pd.DataFrame(raw_df[f'Global Quote']).T
    df = df.rename(
        columns={'2. open': 'open', '3. high': 'high', '4. low': 'low', '5. price': 'price', '6. volume': 'volume'})
    for i in df.columns:
        df[i] = df[i].astype(float)
    df.index = pd.to_datetime(df.index)
    df = df.loc['open':'volume']

    return df.to_html()


def search_bar(request):
    if request.method == "Post":
        searched = request.Post('searched')

        return render(request, 'search_bar.html', {'searched': searched})

    else:
        return render(request, 'search_bar.html', {})


def resultat(request):
    if request.method == "Post":
        searched = request.Post['searched']

        return render(request, 'search_bar.html', {})

    else:
        return render(request, 'search_bar.html', {})


def search_page(request, mot_cle):
    data = recherche_par_mot_cle(mot_cle)
    resultats = resultat_to_html(data)
    return render(request, 'Search_page.html', {'mot_cle': mot_cle, 'resultats': resultats})
