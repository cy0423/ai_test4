import requests  # 請求工具
from bs4 import BeautifulSoup  # 解析工具
import time  # 用來暫停程式

stock = ["1101", "2330"]

for i in range(len(stock)):  # 迴圈依序爬股價
    # 現在處理的股票
    stockid = stock[i]

    # 網址塞入股票編號
    url = "https://tw.stock.yahoo.com/quote/" + stockid + ".TW"

    # 發送請求
    r = requests.get(url)

    # 解析回應的 HTML
    soup = BeautifulSoup(r.text, 'html.parser')

    # 定位股價
    price_tag = soup.find('span', class_=[
        "Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)",
        "Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c)",
        "Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)"
    ])

    if price_tag:
        price = price_tag.getText()  # 獲取股價
        # 回報的訊息 (可自訂)
        message = f"股票 {stockid} 即時股價為 {price}"

        # 用 telegram bot 回報股價
        token = "7790673273:AAHB-NqyZ5DDmIG1rGQyunRTb1A7ws7MMk8"  # bot token
        chat_id = "7449832652"  # 使用者 id

        # bot 送訊息
        url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
        requests.get(url)

    else:
        print(f"未找到股票 {stockid} 的價格。")

    # 每次都停 3 秒
    time.sleep(3)
