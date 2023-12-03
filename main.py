import yfinance as yf
import datetime as dt
from yahoo_fin.stock_info import *
from functions import Functions

class Stocks:
    #index number testing
    index_number = 0

    #ticker varibale
    start_cash = 1000
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
    #turn this into a script that pulls data on the 15 min chart in 30 day intervals and saves to new list and store it to the dict greg made
    #then we can make functions off the 15min script to change to 30min, 1hr, 2hr etc but we cant get data under 15 min if we can pull from 5 min that would be wild might try
    
       
    ticker_history = yf_ticker.history(interval="1h", start=start_date, end=dt.datetime.now())
    
    #reformatting the ticket_history for custom filters
    stock_history = func.format_stock_history(ticker_history)
    
    #Finding the difference of prices at certain times then entering those dif into a list
    diff_list = func.finding_dif_of_price(earlier_time, later_time, stock_history)

    #Find when stock price on 1hr makes new high and new low store both 
    #(low is lowest point on 1hr chart followed by hitting a previous high and coming back down to the previous low or making new highs but then returning to recent low)
    double_bottom_strategy = func.double_bottom(stock_history, start_cash) 
  
    #Finding the days where ticker dropped a dollar and enter those into a new list
    trades_found = func.find_days_where_ticker_dropped(diff_list, 1)

    #looping through the trades_found list to find a strategy
    results = func.holding_stategy(earlier_time, later_time, trades_found, added_days, stock_history)


    #-----------------------------------------printing time--------------------------------------------------------#
    print(f'Starting cash: {start_cash}')
    print(f"Stock: {ticker}")
    print(f"Current Price: ${current_price}")
    print('---------------------------------------------')
    print(f"Amount of prices: {len(ticker_history)}")
    print(f'total days: {len(stock_history["09:30"]["open"])} item in list at index {index_number}, high: {stock_history["09:30"]["high"][index_number]} low: {stock_history["09:30"]["low"][index_number]}, open: {stock_history["09:30"]["open"][index_number]}, close: {stock_history["09:30"]["close"][index_number]}')
    print('---------------------------------------------')
    print("Total amount of days that could've be traded:", len(diff_list))
    print('Total trades found:', len(trades_found))
    print('Wins:', results['wins'])
    print('Losses:', results['losses'])
    print(f'Winnings: ${round(float(results["wins_profit"]),2)}')
    print(f'Losings: ${round(float(results["lost_money"]),2)}')
    print(f'Biggest losing streak: {max(results["loss_streak"])}')
    print(f'Biggest wining streak: {max(results["win_streak"])}')
    print('Profits/loses: $', round(float(results["wins_profit"] + results["lost_money"]),2))
    print(f'Double bottom : winnings ${double_bottom_strategy[0]}, loses: $-{double_bottom_strategy[3]}, start: ${start_cash}')
    print(f'Double bottom : biggest winning streak: {double_bottom_strategy[2]}, biggest losing streak: {double_bottom_strategy[1]}, max amount of money lost before winning: ${double_bottom_strategy[3]}')