import random
from datetime import datetime

import MetaTrader5 as mt5
import pandas as pd

if not mt5.initialize(login="your_login", server="your_server",password="your_password"):
    print("initialize() failed, error code =",mt5.last_error())
    quit()

pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 500)
pd.set_option('display.width', 2000)

symbol = "your_symbol"
symbol_info = mt5.symbol_info(symbol)
if symbol_info is None:
    print(symbol, "not found, can not call order_check()")
    mt5.shutdown()
    quit()


if not symbol_info.visible:
    print(symbol, "is not visible, trying to switch on")
    if not mt5.symbol_select(symbol, True):
        print("symbol_select({}}) failed, exit", symbol)
        mt5.shutdown()
        quit()

for i in range(20):
    lot = round(random.uniform(0.01, 1), 2)
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot,
        "type": mt5.ORDER_TYPE_BUY,
        "magic": 234000,
        "comment": "python script open",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_FOK,
    }

    # send a trading request
    result = mt5.order_send(request)
    # check the execution result
    print(f"1. order_send(): {symbol}")
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print(f"2. order_send failed, retcode={result.retcode}")
        # request the result as a dictionary and display it element by element
        result_dict = result._asdict()
        for field in result_dict.keys():
            print(f"   {field}={result_dict[field]}")
            # if this is a trading request structure, display it element by element as well
            if field == "request":
                traderequest_dict = result_dict[field]._asdict()
                for tradereq_filed in traderequest_dict:
                    print(f"       traderequest: {tradereq_filed}={traderequest_dict[tradereq_filed]}")
        print("shutdown() and quit")
        mt5.shutdown()
        quit()

    print("2. order_send done, ", result)
    print("   opened position with POSITION_TICKET={}".format(result.order))

positions_total=mt5.positions_total()
if positions_total>0:
    print("Total positions=",positions_total)
else:
    print("Positions not found")
print(mt5.positions_get())

# for i in range(1):
#     lot = 0.1
#     request = {
#         "action": mt5.TRADE_ACTION_DEAL,
#         "symbol": symbol,
#         "volume": lot,
#         "type": mt5.ORDER_TYPE_SELL,
#         "magic": 234000,
#         "comment": "python script open",
#         "type_time": mt5.ORDER_TIME_GTC,
#         "type_filling": mt5.ORDER_FILLING_FOK,
#     }
#
#
#     # send a trading request
#     result = mt5.order_send(request)
#     # check the execution result
#     print(f"1. order_send(): {symbol}")
#     if result.retcode != mt5.TRADE_RETCODE_DONE:
#         print(f"2. order_send failed, retcode={result.retcode}")
#         # request the result as a dictionary and display it element by element
#         result_dict = result._asdict()
#         for field in result_dict.keys():
#             print(f"   {field}={result_dict[field]}")
#             # if this is a trading request structure, display it element by element as well
#             if field == "request":
#                 traderequest_dict = result_dict[field]._asdict()
#                 for tradereq_filed in traderequest_dict:
#                     print(f"       traderequest: {tradereq_filed}={traderequest_dict[tradereq_filed]}")
#         print("shutdown() and quit")
#         mt5.shutdown()
#         quit()
#
#     print("2. order_send done, ", result)
#     print(f"   opened position with POSITION_TICKET={result.order}")


# from_date=datetime(2023,10,12)
# to_date=datetime(2023,10,14)
# history_deals=mt5.history_deals_total(from_date, to_date)
# if history_deals>0:
#     print("Total history deals=",history_deals)
# else:
#     print("Deals not found in history")


# get deals for symbols whose names contain neither "EUR" nor "GBP"
# deals = mt5.history_deals_get(from_date, to_date, group="USDJPY")
# if deals == None:
#     print("No deals, error code={}".format(mt5.last_error()))
# elif len(deals) > 0:
#     # display these deals as a table using pandas.DataFrame
#     df=pd.DataFrame(list(deals),columns=deals[0]._asdict().keys())
#     df['time'] = pd.to_datetime(df['time'], unit='s')
#     print(df)
# print("")

mt5.shutdown()
