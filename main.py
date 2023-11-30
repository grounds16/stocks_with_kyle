import yfinance as yf
import datetime as dt

SPY = yf.Ticker('SPY')
start_year = 2023
start_day = 1
start_month = 1
start_hour = 9
start_min = 30
start_date = dt.datetime(start_year, start_month, start_day, start_hour, start_min)

# get historical market data
spy_2023_hist_1hr = SPY.history(interval="1h", start=start_date, end=dt.datetime.now())
print(f"Amount of prices: {len(spy_2023_hist_1hr)}")

new_dic = {}
spy_930 = []
spy_1030 = []
spy_1130 = []
spy_1230 = []
spy_1330 = []
spy_1430 = []
spy_1530 = []


time_list = ["09:30", "10:30", "11:30", "12:30", "13:30", "14:30", "15:30"]
opening = spy_2023_hist_1hr['Open']

#We can not loop through a time stamp so saved the time stamp as a string and entered it into a new dic to loop through
for time, price in opening.items():
    new_dic[str(time)] = price

#looping through the new dic and saving the prices per time
for time, price in new_dic.items():
    if time_list[0] in time:
        spy_930.append(price)
    if time_list[1] in time:
        spy_1030.append(price)
    if time_list[2] in time:
        spy_1130.append(price)
    if time_list[3] in time:
        spy_1230.append(price)
    if time_list[4] in time:
        spy_1330.append(price)
    if time_list[5] in time:
        spy_1430.append(price)
    if time_list[6] in time:
        spy_1530.append(price)
print(f'Amount of prices at 9:30: {len(spy_930)}')
print(f'Amount of prices at 10:30: {len(spy_1030)}')
print(f'Amount of prices at 11:30: {len(spy_1130)}')
print(f'Amount of prices at 12:30: {len(spy_1230)}')
print(f'Amount of prices at 1:30: {len(spy_1330)}')
print(f'Amount of prices at 2:30: {len(spy_1430)}')
print('---------------------------------------------')

#Finding the difference between 9:30 and 10:30 then entering those dif into a list
spy930_1030_difference = []
trades = []
for i in range(len(spy_930)):
    diff = spy_1030[i] - spy_930[i]
    spy930_1030_difference.append(diff)

#Finding the days where spy dropped a dollar from 9:30 to 10:30 and enter those into a new list
days_to_hold = []
for days in range(len(spy930_1030_difference)):
    if spy930_1030_difference[days] <= -1:
        trades.append(spy930_1030_difference[days])
        days_to_hold.append(days)

# print('difference: ', spy830_930_difference[0])
print('Amount of differences:', len(spy930_1030_difference))
print('Total trades:', len(trades))

#looping through the dif list to find a startegy
wins = 0
losses = 0
wins_profit = 0
lost_money = 0
loss_streak = []
win_streak = []
win_streak_counter = 0
loss_steak_counter = 0
added_days = 3

for day in days_to_hold:
    dif = (spy_1030[day+added_days]-spy_930[day])
    if float(dif) >= 1.00:
        wins_profit += dif * 100

        wins += 1
        win_streak_counter += 1

        loss_streak.append(loss_steak_counter)
        loss_steak_counter = 0
    else:
        lost_money += dif - 150

        loss_steak_counter += 1
        losses += 1

        win_streak.append(win_streak_counter)
        win_streak_counter = 0


print('Wins:', wins)
print('Losses:', losses)
print(f'Winnings: ${round(float(wins_profit),2)}')
print(f'Losings: ${round(float(lost_money),2)}')
print(f'Biggest losing streak: {max(loss_streak)}')
print(f'Biggest wining streak: {max(win_streak)}')
print('Profits if bought last year with strat: $', round(float(wins_profit + lost_money),2))


