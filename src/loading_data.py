import pandas as pd
import requests

def load_tickers_from_website(
        url="https://www.bankier.pl/inwestowanie/profile/quote.html?symbol=WIG",
        headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
                "Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7"
            }):
    """
    Pobiera listę spółek z tabeli na stronie Bankier.pl.

    Kolumna Ticker_yf zawiera listę tickerów odpowiednią dla nazewnictwa przez yfinance.
    """

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status() 
        tables = pd.read_html(response.text, decimal=',', thousands=' ')

        if len(tables) > 0:
            df = tables[0]
            print("Pobrano pomyślnie")
            df['Ticker_yf'] = df['Ticker'] + ".WA"
            return df
        else:
            print("Nie znaleziono żadnej tabeli na stronie.")
            return None

    except Exception as e:
        print(f"Wystąpił błąd: {e}")
        return None


def load_tickers_from_file(filepath = r'data\WIG_ticker_list.csv', **kwargs):
    """
    Ładuje tabelę z pliku CSV i przygotowuje je dla Yahoo Finance.
    Kolumna Ticker powinna zawierać tickery spółek w tabeli

    Kolumna Ticker_yf zawiera listę tickerów odpowiednią dla nazewnictwa przez yfinance
    """
    try:
        df = pd.read_csv(filepath, sep = ';')
        df['Ticker_yf'] = df['Ticker'] + ".WA"
        print('Pobrano pomyślnie')
        return df
    
    except FileNotFoundError:
        print('Nie znaleziono pliku')
        return None
    
    except Exception as e:
        print(f"Wystąpił błąd: {e}")
        return None        