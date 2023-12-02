import yfinance as yf
import datetime as dt
from yahoo_fin.stock_info import *
from functions import Functions


class Stocks:
    #ticker varibale
    ticker = 'SPY' #We can search for any ticker using this variable
    current_price = round(get_live_price(ticker),2)

    #time varibales
    start_year = 2023
    start_day = 1
    start_month = 1
    start_hour = 9
    start_min = 30
    start_date = dt.datetime(start_year, start_month, start_day, start_hour, start_min)

    #These two variables set the times you want to plan for. earlier_time example spy930, later_time example spy1030.
    #This is so we can change the times in one location instead of changing the entire code
    #Note: If the current time is not past the time you would like, you will recieve an error. As this is pulling results from today as well.
    earlier_time = "09:30"
    later_time = "10:30"

    added_days = 2


    func = Functions()
    #-----------------------------------------coding time--------------------------------------------------------#


    # get historical market data
    yf_ticker = yf.Ticker(ticker)
    ticker_history = yf_ticker.history(interval="1h", start=start_date, end=dt.datetime.now())

    #reformatting the ticket_history for custom filters
    stock_history = func.format_stock_history(ticker_history)

    #Finding the difference of prices at certain times then entering those dif into a list
    diff_list = func.finding_dif_of_price(earlier_time, later_time, stock_history)

    #Finding the days where ticker dropped a dollar and enter those into a new list
    days_to_hold = func.find_days_where_ticker_dropped(diff_list, 1)

    #looping through the days_to_hold list to find a strategy
    results = func.holding_stategy(earlier_time, later_time, days_to_hold, added_days, stock_history)


    #-----------------------------------------printing time--------------------------------------------------------#

    print(f"Stock: {ticker}")
    print(f"Current Price: ${current_price}")
    print('---------------------------------------------')
    print(f"Amount of prices: {len(ticker_history)}")
    print(f'Amount of prices at 9:30: {len(stock_history["09:30"]["price"])}')
    print('---------------------------------------------')
    print('Amount of differences:', len(diff_list))
    print('Total trades:', len(days_to_hold))
    print('Wins:', results['wins'])
    print('Losses:', results['losses'])
    print(f'Winnings: ${round(float(results["wins_profit"]),2)}')
    print(f'Losings: ${round(float(results["lost_money"]),2)}')
    print(f'Biggest losing streak: {max(results["loss_streak"])}')
    print(f'Biggest wining streak: {max(results["win_streak"])}')
    print('Profits if bought last year with strat: $', round(float(results["wins_profit"] + results["lost_money"]),2))


