
class Functions:
    def format_stock_history(self, stock_history): 
        new_dic_open = {} # place holder dic, will reformat this into the history dic
        new_dic_close = {}
        new_dic_high = {}
        new_dic_low = {}
        opening = stock_history['Open']
        closes = stock_history['Close']
        highs = stock_history['High']
        lows = stock_history['Low']
        # We can not loop through a timestamp so saved the timestamp as a string and entered it into a new dic to loop through
        for time, price in opening.items():
            new_dic_open[str(time)] = price
        for time, price in closes.items():
            new_dic_close[str(time)] = price
        for time, price in highs.items():
            new_dic_high[str(time)] = price
        for time, price in lows.items():
            new_dic_low[str(time)] = price

        history_dic = {
            "09:30": {
                'dates': [],
                'open': [],
                'close': [],
                'low': [],
                'high': [],
            },
            '09:45': {
                'dates': [],
                'open': [],
                'close': [],
                'low': [],
                'high': [],
            },
            '10:00': {
                'dates': [],
                'open': [],
                'close': [],
                'low': [],
                'high': [],
            },
            '10:15': {
                'dates': [],
                'open': [],
                'close': [],
                'low': [],
                'high': [],
            },
            "10:30": {
                'dates': [],
                'open': [],
                'close': [],
                'low': [],
                'high': [],
            },
            '10:45': {
                'dates': [],
                'open': [],
                'close': [],
                'low': [],
                'high': [],
            },
            '11:00': {
                'dates': [],
                'open': [],
                'close': [],
                'low': [],
                'high': [],
            },
            '11:15': {
                'dates': [],
                'open': [],
                'close': [],
                'low': [],
                'high': [],
            },
            "11:30": {
                'dates': [],
                'open': [],
                'close': [],
                'low': [],
                'high': [],
            },
            '11:45': {
                'dates': [],
                'open': [],
                'close': [],
                'low': [],
                'high': [],
            },
            '12:00': {
                'dates': [],
                'price': [],
                'low': [],
                'high': [],
            },
            '12:15': {
                'dates': [],
                'open': [],
                'close': [],
                'low': [],
                'high': [],
            },
            "12:30": {
                'dates': [],
                'open': [],
                'close': [],
                'low': [],
                'high': [],
            },
            "12:45": {
                'dates': [],
                'price': [],
                'low': [],
                'high': [],
            },
            "13:00": {
                'dates': [],
                'open': [],
                'close': [],
                'low': [],
                'high': [],
            },
            "13:15": {
                'dates': [],
                'open': [],
                'close': [],
                'low': [],
                'high': [],
            },
            "13:30": {
                'dates': [],
                'open': [],
                'close': [],
                'low': [],
                'high': [],
            },
            "13:45": {
                'dates': [],
                'open': [],
                'close': [],
                'low': [],
                'high': [],
            },
            "14:00": {
                'dates': [],
                'open': [],
                'close': [],
                'low': [],
                'high': [],
            },
            "14:15": {
                'dates': [],
                'open': [],
                'close': [],
                'low': [],
                'high': [],
            },
            "14:30": {
                'dates': [],
                'open': [],
                'close': [],
                'low': [],
                'high': [],
            },
            "14:45": {
                'dates': [],
                'open': [],
                'close': [],
                'low': [],
                'high': [],
            },
            "15:00": {
                'dates': [],
                'open': [],
                'close': [],
                'low': [],
                'high': [],
            },
            "15:15": {
                'dates': [],
                'open': [],
                'close': [],
                'low': [],
                'high': [],
            },
            "15:30": {
                'dates': [],
                'open': [],
                'close': [],
                'low': [],
                'high': [],
            }
        }

        # looping through the new dic and saving the dates and prices per key time
        for time, price in new_dic_open.items():
            for time1 in history_dic.keys():
                if time1 in time:
                    history_dic[time1]['dates'].append(time[0:10])
                    history_dic[time1]['open'].append(str(round(price, 2)))
        
        for time, price in new_dic_close.items():
            for time1 in history_dic.keys():
                if time1 in time:
                    history_dic[time1]['dates'].append(time[0:10])
                    history_dic[time1]['close'].append(str(round(price, 2)))
        
        for time, price in new_dic_high.items():
            for time1 in history_dic.keys():
                if time1 in time:
                    history_dic[time1]['dates'].append(time[0:10])
                    history_dic[time1]['high'].append(str(round(price, 2)))
        
        for time, price in new_dic_low.items():
            for time1 in history_dic.keys():
                if time1 in time:
                    history_dic[time1]['dates'].append(time[0:10])
                    history_dic[time1]['low'].append(str(round(price, 2)))
        
        return history_dic

    def finding_dif_of_price(self, earlier_time, later_time, history_dic):
        ###Returns a list of difference in price for given hours of a day
        diff_list = []
        for counter in range(len(history_dic[earlier_time]['open'])):
            dif = float(history_dic[earlier_time]['open'][counter]) - float(history_dic[later_time]['open'][counter])
            diff_list.append(round(float(dif), 2))
        return diff_list

    def find_days_where_ticker_dropped(self, diff_list, dollars):
        days_to_hold = []
        for days in range(len(diff_list)):
            if diff_list[days] <= -dollars:
                days_to_hold.append(days)
        return days_to_hold

    def holding_stategy(self, earlier_time, later_time, trades_found_list, added_days, history_dic):
        results = {
            'wins': 0,
            'losses': 0,
            'wins_profit': 0,
            'lost_money': 0,
            'loss_streak': [],
            'win_streak': [],
            'win_streak_counter': 0,
            'loss_steak_counter': 0,
        }
        later_time_prices = history_dic[later_time]['open']
        earlier_time_prices = history_dic[earlier_time]['open']

        for day in trades_found_list:
            try:
                dif = (round(float(later_time_prices[day + added_days]), 2) - round(float(earlier_time_prices[day]), 2))
                if float(dif) > 0.00:
                    results['wins_profit'] += dif * 100
                    results['wins'] += 1
                    results['win_streak_counter'] += 1

                    results['loss_streak'].append(results['loss_steak_counter'])
                    results['loss_steak_counter'] = 0
                else:
                    results['lost_money'] += dif - 150

                    results['loss_steak_counter'] += 1
                    results['losses'] += 1

                    results['win_streak'].append(results['win_streak_counter'])
                    results['win_streak_counter'] = 0
            except:
                pass

        return results

    
    #you can clean if you want lawl
    
    
    def double_bottom(self,stock_history, start_cash= 1000):
        start = start_cash
        tally =0
        profit=0
        loses = 0
        winnings = 0
        winners=[]
        trades_found=[]
        index_list=[]
        temp = stock_history['09:30']['open'][0]
        time = ['09:30','10:30','11:30','12:30','13:30','14:30','15:30']
        #loops through stock history and compares open 930 withsame day but at 1030 close price then stores the index val in index list
        try:
            for i in range(len(stock_history[time[0]]['open'])):
                if stock_history[time[0]]['open'][i] > stock_history[time[1]]['close'][i] and stock_history[time[0]]['open'][i] >= temp:
                    temp  = stock_history[time[0]]['open'][i]
                    index_list.append(i)
                else:
                    pass
        except:
            pass
        # loops through the index list and checks the price difference days after buy signal at 1030 open
        for i in index_list:
            try:
                total= float(stock_history['10:30']['close'][i])-float(stock_history['09:30']['open'][i+2])
                if total > 0.00:
                    # adds trade to list only if it profited more than 0 dollars in 2 days
                    trades_found.append(round(float(total),2)*60)
                else:
                    #just tallys up the loses
                    tally+=1
                    loses=loses + 120
            except:
                pass
        #loops through the trades that made profit and adds them all up and subracts for total winnings then subracts loses from wins to get profits
        for i in trades_found:
            winners.append(i)
            profit = profit + i 
        winnings = start + (profit-loses)    
        
        return round(float(winnings),2), loses, start, winners, tally
    
    