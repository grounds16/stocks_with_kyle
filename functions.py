class Functions:
    def format_stock_history(self, stock_history):
        new_dic = {}  # place holder dic, will reformat this into the history dic
        opening = stock_history['Open']

        # We can not loop through a timestamp so saved the timestamp as a string and entered it into a new dic to loop through
        for time, price in opening.items():
            new_dic[str(time)] = price
        history_dic = {
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

        # looping through the new dic and saving the dates and prices per key time
        for time, price in new_dic.items():
            for time1 in history_dic.keys():
                if time1 in time:
                    history_dic[time1]['dates'].append(time[0:10])
                    history_dic[time1]['price'].append(str(round(price, 2)))
        return history_dic

    def finding_dif_of_price(self, earlier_time, later_time, history_dic):
        ###Returns a list of difference in price for given hours of a day
        diff_list = []
        for counter in range(len(history_dic[earlier_time]['price'])):
            dif = float(history_dic[earlier_time]['price'][counter]) - float(history_dic[later_time]['price'][counter])
            diff_list.append(round(float(dif), 2))
        return diff_list

    def find_days_where_ticker_dropped(self, diff_list, dollars):
        days_to_hold = []
        for days in range(len(diff_list)):
            if diff_list[days] <= -dollars:
                days_to_hold.append(days)
        return days_to_hold

    def holding_stategy(self, earlier_time, later_time, days_to_hold_list, added_days, history_dic):
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
        later_time_prices = history_dic[later_time]['price']
        earlier_time_prices = history_dic[earlier_time]['price']

        for day in days_to_hold_list:
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
