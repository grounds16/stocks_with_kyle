import yfinance as yf
import datetime as dt

#ticker varibales
ticker = 'AMZN' #We can search for any ticker using this variable
yf_ticker = yf.Ticker(ticker)

#time varibales
start_year = 2023
start_day = 1
start_month = 1
start_hour = 9
start_min = 30
start_date = dt.datetime(start_year, start_month, start_day, start_hour, start_min)
time_list = ["09:30", "10:30", "11:30", "12:30", "13:30", "14:30", "15:30"]
time_930 = []
time_1030 = []
time_1130 = []
time_1230 = []
time_1330 = []
time_1430 = []
time_1530 = []

#set times we want to search for during our algo
earlier_time = time_930
later_time = time_1030


#wins/losses varibables
wins = 0
losses = 0
wins_profit = 0
lost_money = 0
loss_streak = []
win_streak = []
win_streak_counter = 0
loss_steak_counter = 0

#trade varibales
added_days = 2
new_dic = {}
difference = []
trades = []
days_to_hold = []



print(f"Stock: {ticker}")
print('---------------------------------------------')

# get historical market data
ticker_history = yf_ticker.history(interval="1h", start=start_date, end=dt.datetime.now())
print(f"Amount of prices: {len(ticker_history)}")
opening = ticker_history['Open']

#We can not loop through a time stamp so saved the time stamp as a string and entered it into a new dic to loop through
for time, price in opening.items():
    new_dic[str(time)] = price

#looping through the new dic and saving the prices per time
for time, price in new_dic.items():
    if time_list[0] in time:
        time_930.append(price)
    if time_list[1] in time:
        time_1030.append(price)
    if time_list[2] in time:
        time_1130.append(price)
    if time_list[3] in time:
        time_1230.append(price)
    if time_list[4] in time:
        time_1330.append(price)
    if time_list[5] in time:
        time_1430.append(price)
    if time_list[6] in time:
        time_1530.append(price)
print(f'Amount of prices at 9:30: {len(time_930)}')
print(f'Amount of prices at 10:30: {len(time_1030)}')
print(f'Amount of prices at 11:30: {len(time_1130)}')
print(f'Amount of prices at 12:30: {len(time_1230)}')
print(f'Amount of prices at 1:30: {len(time_1330)}')
print(f'Amount of prices at 2:30: {len(time_1430)}')
print('---------------------------------------------')

#These two variables set the times you want to plan for. earlier_time example spy930, later_time example spy1030.
#This is so we can change the times in one location isntead of change the entire code
#Note: If the current time is not past the ticker time you would like, you will recieve an error.




#Finding the difference between 9:30 and 10:30 then entering those dif into a list
for i in range(len(earlier_time)):
    diff = later_time[i] - earlier_time[i]
    difference.append(diff)

#Finding the days where spy dropped a dollar from 9:30 to 10:30 and enter those into a new list
for days in range(len(difference)):
    if difference[days] <= -1:
        trades.append(difference[days])
        days_to_hold.append(days)

# print('difference: ', spy830_930_difference[0])
print('Amount of differences:', len(difference))
print('Total trades:', len(trades))

#looping through the days_to_hold list to find a startegy



for day in days_to_hold:
    try:
        dif = (later_time[day + added_days] - earlier_time[day])
        if float(dif) > 0.00:
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
    except:
        pass


print('Wins:', wins)
print('Losses:', losses)
print(f'Winnings: ${round(float(wins_profit),2)}')
print(f'Losings: ${round(float(lost_money),2)}')
print(f'Biggest losing streak: {max(loss_streak)}')
print(f'Biggest wining streak: {max(win_streak)}')
print('Profits if bought last year with strat: $', round(float(wins_profit + lost_money),2))


