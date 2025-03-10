from bs4 import BeautifulSoup
import requests
 
def scrape_stock_data(symbol, exchange):

    if exchange == 'NASDAQ':
        url = f"https://finance.yahoo.com/quote/{symbol}"
    elif exchange == 'NSE':
        url = f"https://finance.yahoo.com/quote/{symbol}.NS"
    
    headers        = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    response       = requests.get(url, headers=headers)
    soup           = BeautifulSoup(response.content, 'html.parser')

    current_price = soup.find("span", {"data-testid":"qsp-price"}).text
    price_changed = soup.find("span", {"data-testid":"qsp-price-change"}).text
    percentage_changed = soup.find("span", {"data-testid":"qsp-price-change-percent"}).text
    previous_close = soup.find("fin-streamer", {"data-field": "regularMarketPreviousClose"})['data-value']
    week_52_range  = soup.find("fin-streamer", {'data-field': 'fiftyTwoWeekRange'})['data-value']
    week_52_low, week_52_high = week_52_range.split(' - ')
    market_cap = soup.find("fin-streamer", {"data-field": "marketCap"})['data-value']
    pe_ratio = soup.find("fin-streamer", {"data-field":"trailingPE"})['data-value']
    # dividend_yield = soup.find("span", {"class":"value yf-1jj98ts"})
    
    # print(f"Current Price: {current_price},\nPrice_Changed: {price_changed},\nPercentage_Changed: {percentage_changed},\nPrevious Close: {previous_close},\nWeek_52_Range: {week_52_range},\nWeek_52_Low: {week_52_low},\nWeek_52_High: {week_52_high}")
    print('current_price :', current_price)
    print('price_changed :', price_changed)
    print('percentage_changed :', percentage_changed)
    print('previous_close :', previous_close)
    print('week_52_low :', week_52_low)
    print('week_52_high :', week_52_high)
    print('market_cap :', market_cap)
    print('pe_ratio :', pe_ratio)
    # print('dividend_yield :', dividend_yield)

scrape_stock_data('RHM.DE', 'NASDAQ')


