import requests

api_url = 'https://api.coingecko.com/api/v3/exchange_rates'

try:
    response = requests.get(api_url)
    # print(response.text)
    response.raise_for_status()
    response_data=response.json()
    btc_to_usd_exchange_rate = response_data['rates']['usd']['value']
    print(btc_to_usd_exchange_rate)

    while True:
        try:
            num_of_btc_user_has = float(input('How many BitCoin do you have that you check the exchange rate of? '))
            break
        except ValueError:
            print('That is not a number... Please try again!')

    print(f'{num_of_btc_user_has} BTC is ${btc_to_usd_exchange_rate*num_of_btc_user_has:,.2f} USD')
except Exception as e:
    print(e)
    print("the request did not complete correctly")