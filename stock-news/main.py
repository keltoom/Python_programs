import requests
from datetime import date, timedelta
from twilio.rest import Client

yesterday = str(date.today() - timedelta(days=1))
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
api_key = "OY817746SRRKUAHN"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
news_api_key = "0aa0888ee852418b94bc929b1cfadd75"

account_sid = "AC5c4eca0bbc1692c37bad943e5bfeac4b"
auth_token = "19039cb1af8e4e35597d2c766930fdc6"

# STEP 1: Using https://www.alphavantage.co/documentation/#daily

# yesterday's closing stock price

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": api_key,
}
response = requests.get(STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

# the day before yesterday's closing stock price
before_yesterday_data = data_list[1]
before_yesterday_closing_price = before_yesterday_data["4. close"]
print(before_yesterday_closing_price)

# the positive difference between 1 and 2
difference = float(yesterday_closing_price) - float(before_yesterday_closing_price)
up_down = None
if difference < 0:
    up_down = "🔻"
else:
    up_down = "🔺"
print(difference)

percentage_difference = round((difference / float(yesterday_closing_price)) * 100)
print(f'per: {percentage_difference}')

if abs(percentage_difference) >= 0:
    # use the News API to get articles related to the COMPANY_NAME.
    params = {
        "qInTitle": STOCK_NAME,
        "from": yesterday,
        "sortBy": "popularity ",
        "apiKey": news_api_key,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=params)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]
    # create a list that contains the first 3 articles.
    first_articles = articles[:3]

    # STEP 3: Use twilio.com/docs/sms/quickstart/python
    # to send a separate message with each article's title and description to your phone number.

    articles_list = [{
                         f"{STOCK_NAME}: {up_down}{percentage_difference}%\nHeadline: {article['title']} \nDescription: "
                         f"{article['description']}"}
                     for article in first_articles]
    # Send each article as a separate message via Twilio.

    client = Client(account_sid, auth_token)
    for article in articles_list:
        message = client.messages.create(
            body=article,
            from_='+1 947 333 4519',
            to='+213 xxx xx xx xx'
        )

        print(message.status)
