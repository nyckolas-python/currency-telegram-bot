import datetime
from typing import NamedTuple, List, Dict
import pytz

#import db
#import exceptions

class Currency(Dict):
    # Add attr rateBuy and rateSell
    pass
    
def parse_currency_info(currency_info: list) -> Currency:
    # only a couple of (USD UAH) or (EUR UAH)
    usd_uah_rate = [curency for curency in currency_info if curency['currencyCodeA'] == 840 and curency['currencyCodeB'] == 980][0]
    #eur_uah_rate = [curency for curency in currency_info if curency['currencyCodeA'] == 978 and curency['currencyCodeB'] == 980][0]
    return Currency(usd_uah_rate)


# def add_today_currency(raw_message: str) -> Currency:
#     parsed_message = _parse_message(raw_message)
#     category = Categories().get_category(
#         parsed_message.category_text)
#     inserted_row_id = db.insert("expense", {
#         "amount": parsed_message.amount,
#         "created": _get_now_formatted(),
#         "category_codename": category["codename"],
#         "raw_text": raw_message
#     })
#     return Expense(amount=parsed_message.amount,
#                    category_name=category["name"])