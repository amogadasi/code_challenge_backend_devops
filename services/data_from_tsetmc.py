import redis
import requests
import json
from datetime import datetime
from time import sleep


redis_handle = redis.Redis(
    host='127.0.0.1', port=6379, encoding='utf-8', decode_responses=True)

stock_list = redis_handle.smembers('stock_list')

while True:
    time_str = datetime.now().strftime('%H:%M')
    for stock in stock_list:
        price_data = requests.get(
            f'http://cdn.tsetmc.com/api/ClosingPrice/GetClosingPriceInfo/{stock}', headers={'User-Agent': 'Chrome/112.0.0.0', 'Content-Type': 'application/json; charset=utf-8'})
        price_data = json.loads(price_data.text)['closingPriceInfo']
        print(
            f'Time: {time_str} - Stock: {stock} - Price: {price_data["pClosing"]}')

    sleep(60)
