import yfinance as yf
import datetime as dt
from yahoo_fin.stock_info import *


#ticker varibale
ticker = 'SPY' #We can search for any ticker using this variable
current_price = round(get_live_price(ticker),2)
new_dic = {}

earlier_time = "09:30"
later_time = "10:30"
start_year = 2023
start_day = 1
start_month = 1
start_hour = 9
start_min = 30
start_date = dt.datetime(start_year, start_month, start_day, start_hour, start_min)
yf_ticker = yf.Ticker(ticker)
ticker_history = yf_ticker.history(interval="1h", start=start_date, end=dt.datetime.now())
opening = ticker_history['Open']

for time, price in opening.items():
    new_dic[str(time)] = price
time_dic = {
            "09:30": {
                'dates': [],
                'price': []
            },
            '09:45': {
                'dates': [],
                'price': []
            },
            '10:00': {
                'dates': [],
                'price': []
            },
            '10:15': {
                'dates': [],
                'price': []
            },
            "10:30": {
                'dates': [],
                'price': []
            },
            '10:45': {
                'dates': [],
                'price': []
            },
            '11:00': {
                'dates': [],
                'price': []
            },
            '11:15': {
                'dates': [],
                'price': []
            },
            "11:30": {
                'dates': [],
                'price': []
            },
            '11:45': {
                'dates': [],
                'price': []
            },
            '12:00': {
                'dates': [],
                'price': []
            },
            '12:15': {
                'dates': [],
                'price': []
            },
            "12:30": {
                'dates': [],
                'price': []
            },
            "12:45": {
                'dates': [],
                'price': []
            },
            "13:00": {
                'dates': [],
                'price': []
            },
            "13:15": {
                'dates': [],
                'price': []
            },
            "13:30": {
                'dates': [],
                'price': []
            },
            "13:45": {
                'dates': [],
                'price': []
            },
            "14:00": {
                'dates': [],
                'price': []
            },
            "14:15": {
                'dates': [],
                'price': []
            },
            "14:30": {
                'dates': [],
                'price': []
            },
            "14:45": {
                'dates': [],
                'price': []
            },
            "15:00": {
                'dates': [],
                'price': []
            },
            "15:15": {
                'dates': [],
                'price': []
            },
            "15:30": {
                'dates': [],
                'price': []

            }
        }

for time, price in new_dic.items():
    for time1 in time_dic.keys():
        if time1 in time:
            time_dic[time1]['dates'].append(time[0:10])
            time_dic[time1]['price'].append(str(round(price, 2)))
diff_list= []
for counter in range(len(time_dic[earlier_time]['price'])):
    dif = round(float(time_dic[earlier_time]['price'][counter]), 2) - round(float(time_dic[later_time]['price'][counter]), 2)
    diff_list.append(round(float(dif), 2))

print(earlier_time)
print(time_dic[earlier_time]['dates'])
print(diff_list)


