import json
import requests


class CurrencyCalculator:
    def __init__(self):
        self.main()
    
    def main(self):
        code = input()
        cache = dict()

        data = json.loads(requests.get(f"http://www.floatrates.com/daily/{'usd'}.json").content)
        for currency in data.keys():
            cache[currency.lower()] = {'usd': data[currency.lower()]["inverseRate"]}
        cache['usd'] = dict()

        data = json.loads(requests.get(f"http://www.floatrates.com/daily/{'eur'}.json").content)
        for currency in data.keys():
            cache[currency.lower()].update({'eur': data[currency.lower()]["inverseRate"]})

        cache2 = ['usd', 'eur']

        while True:
            currency_code = input()
            if currency_code != '':
                money = int(input())
                print("Checking the cache...")
                if currency_code.lower() in cache2:
                    print("Oh! It is in the cache!")
                    rate = cache[code.lower()][currency_code.lower()]
                else:
                    print("Sorry, but it is not in the cache!")
                    data = json.loads(requests.get(f"http://www.floatrates.com/daily/{currency_code}.json").content)
                    for currency in data.keys():
                        cache[currency.lower()].update({f'{currency_code.lower()}': data[currency.lower()]["inverseRate"]})
                    rate = data[code.lower()]["inverseRate"]
                    cache2.append(currency_code)
                print(f"You received {round(money * rate, 2)} {currency_code}.")
            else:
                break

currency_calculator = CurrencyCalculator()