import math
from twilio.rest import Client

import requests
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"


STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = 
NEWS_API_KEY = 
TWILIO_SID = 
TWILIO_AUTH_TOKEN = 

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").



STOCK_ENDPOINTS = f'https://www.alphavantage.co/query'
# url1 = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey={STOCK_API_KEY}'
stock_params = {
"function":"TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "outputsize" : "compact",
    "apikey": STOCK_API_KEY
}

news_params = {
    'q':COMPANY_NAME,
    "apiKey":NEWS_API_KEY
}
response = requests.get(STOCK_ENDPOINTS,params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]
# print(data_list)
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data['4. close']
print(yesterday_closing_price)


day_before_yesterday = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday['4. close']
print(day_before_yesterday_closing_price)

diff = abs(float(yesterday_closing_price)-float(day_before_yesterday_closing_price))
print(diff)


diff_percent = round(diff/float(yesterday_closing_price)*100)


up_down = None
if diff_percent > 5:
    up_down = '🔺'
else:
    up_down = '🔻'
    response=requests.get(NEWS_ENDPOINT,news_params)
    news_articles = response.json()['articles']


    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 







    three_articles = news_articles[:3]
    # print(three_articles)
    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 


    formatted_list = [ f'{STOCK_NAME}: {up_down}{diff_percent} \nHeadline: {article["title"]} \nBrief: {article["description"]} ' for article in news_articles]
    print(formatted_list)


#TODO 9. - Send each article as a separate message via Twilio.
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

#Optional TODO: Format the message like this:
    for article in formatted_list:
        message = client.messages.create(
            body=article,
            from_='',
            to=''
        )
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

