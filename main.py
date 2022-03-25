import tkinter as tk
import logging
from connectors.binance import BinanceFuturesClient

logger = logging.getLogger()

logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.INFO)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

if __name__ == '__main__':
    binance = BinanceFuturesClient('68e55dfa88c4175b5dedc866635e28ea412ed8e633b3d16e1d3eccd93878656f',
'503a6fc5ebf601856533693ec83034970266fc39a2c9c71ea09f9f5fa222ae52', True)

    print(binance.get_balances())

    root = tk.Tk()

    root.mainloop()

