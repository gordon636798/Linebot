# LINE BOT 教學

## LINE BOT介紹
- line@
- linebot

![](https://i.imgur.com/G2UPIwi.png)

----
## 環境設定
1. 進入連結複製中間的CDOE 存為.py檔放在桌面
https://github.com/line/line-bot-sdk-python
2. 註冊ngrok(測試用linebot webhook)
https://ngrok.com/
下載出來是一個ZIP壓縮檔，把裡面的EXE放到桌面
3. python3環境
- pip install flask
- pip install line-bot-sdk
---
## 建立LINEBOT
**1. 建立Providers**
![](https://i.imgur.com/nAAgSif.png)
**2. 選擇Messaging API(linebot服務)**
![](https://i.imgur.com/l2DAnbM.png)
**3. optional選項可不填**
![](https://i.imgur.com/k5nj7wP.png)
**4. 加個好友**
![](https://i.imgur.com/4pbv5cs.png)
**5. 進入LINE Offical Account Manager後台管理**
https://www.linebiz.com/tw/login/
![](https://i.imgur.com/XqIJgom.png)
**7. 進入聊天設定**
![](https://i.imgur.com/R9HRF6a.png)
![](https://i.imgur.com/ZOn6DkQ.png =400x)
**6. 選擇「聊天」選項**
![](https://i.imgur.com/0hRoCys.png)

## 聊天模式
- 再次點選聊天就可以與使用者在後台進行一對一聊天
![](https://i.imgur.com/zpxONa5.png)
![](https://i.imgur.com/x8RiiMu.png)

---
## 自動回復訊息
1. 回到右上角點選「設定」
![](https://i.imgur.com/QPbaibV.png)
2. 點選「回應設定」
![](https://i.imgur.com/VyQtVak.png)
3. 選擇「智慧聊天」
![](https://i.imgur.com/1AZPWst.png)

4. 回到主頁點選「自動回應訊息」
![](https://i.imgur.com/RiS85RK.png)
5. 選擇「建立」
![](https://i.imgur.com/IiZxIby.png)
6. 設定關鍵字和回應文字 接著儲存變更
![](https://i.imgur.com/w1wKjKE.png)
7. 結果
![](https://i.imgur.com/elvSCgZ.png)


---
## 建立AI回復訊息 5/15新增功能
1. 一般問題回復
![](https://i.imgur.com/zPiC1Va.png)
![](https://i.imgur.com/SQA25yA.png)
2. 基本資訊回復
![](https://i.imgur.com/G23AQWD.png)
3. 點選開啟並設定回復的話後點選右上角「儲存」
![](https://i.imgur.com/kjogEQ6.png)
![](https://i.imgur.com/U8mFRYm.png)


-----
- 其他範例
![](https://i.imgur.com/oJOYzQF.png)
![](https://i.imgur.com/tTaBU9M.png)

- 圖文選單
![](https://i.imgur.com/cw0a10e.png)
- 圖中有四格選選項
![](https://i.imgur.com/kziBjhH.png =300x)
A: 擺飾
B: 點擊後進入GOOGLE MAP
C: 點擊後問機器人 營業時間
D: 點擊後進入官網

---
## 聊天機器人模式
- 有時候LINE的後台功能不夠你滿足客戶需求
    - 爬蟲
    - 抽卡機
    - 其他玩具...
- 剛剛設定的功能部分無法使用
    - 聊天室![](https://i.imgur.com/sZnmpqE.png)
    - AI自動回復![](https://i.imgur.com/irMJorM.png)
- 剩下自動回復功能正常
![](https://i.imgur.com/GqTh73u.png)

1. 回到回應設定畫面，照畫面中設定
![](https://i.imgur.com/pvlsjr2.png) 進階設定中的「自動回應訊息」若啟用，則前面設定的功能就可以繼續使用，但不包含AI回復。

2. 回到LINE Developers(注意這裡的後台管理網頁跟前面不一樣，前面是LINE Offical Account Manager)
https://developers.line.biz/console/channel/1654251856/basics

![](https://i.imgur.com/YKH6dc7.png)

3. Basic settings 往下滑有一組 Channel secret
![](https://i.imgur.com/jRqNes3.png)

4. 選MessagingAPI 往下點issue Channel access token
![](https://i.imgur.com/gOITTVh.png)
![](https://i.imgur.com/G9HAeRw.png)

5. 修改範例程式 第15.16行處 把前面兩項資訊貼進去後存檔
![](https://i.imgur.com/x4n8mcG.png)

6. 打開兩個Command line(命令提示字元)
- 第一個CMD
    ```
    >cd Desktop
    >python app.py
    
     * Serving Flask app "app" (lazy loading)
     * Environment: production
       WARNING: This is a development server. Do not use it in a production deployment.
       Use a production WSGI server instead.
     * Debug mode: off
     * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
    ```
- 第二個CMD
    ```
    >cd Desktop
    >ngrok http 5000
    
    ngrok by @inconshreveable                                                                                                                          (Ctrl+C to quit)
    Session Status                online
    Account                        (Plan: Free)
    Update                        update available (version 2.3.35, Ctrl-U to update)
    Version                       2.3.34
    Region                        United States (us)
    Web Interface                 http://127.0.0.1:4040
    Forwarding                    http://a7e4a9d0.ngrok.io -> http://localhost:5000
    Forwarding                    https://a7e4a9d0.ngrok.io -> http://localhost:5000

    Connections                   ttl     opn     rt1     rt5     p50     p90 
                                  0       0       0.00    0.00    0.00    0.00 

    ```
以上為成功執行的畫面 

### 3. 設定Webhook 把第二個視窗的的forwarding的網址後面加入/callback，記得把Use webhook打開
![](https://i.imgur.com/PccZa1h.png)

### 4. 成功運作畫面 (官方範例)
![](https://i.imgur.com/rdaRzRR.png)

## 新增聊天機器人功能

主要改動的CODE在涵式 **def handlemessage(event)**
```
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))
```
### 1. 新增關鍵字回復 
```
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text =='你老師':
        message = TextSendMessage(text='許政穆老師')
        line_bot_api.reply_message(event.reply_token, message)
```
把原本的涵式的程式碼刪掉用以上程式替代
![](https://i.imgur.com/CVReggI.png)

### 2. 新增關鍵字回復圖片

```
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage 
    #這裡家一個ImageSendMessage
)
```
```
# 複製放在 handle_message 的程式下面

    elif event.message.text =='學校':
        url = request.url_root +'static/tmp/test/' + 'test.png'
        url = url.replace('http','https')
        print(url)
        message = ImageSendMessage(url,url)
        line_bot_api.reply_message(event.reply_token, message)
```

資料夾結構
根據FLASK的設定，你需要另外建立static/tmp的資料夾，把會需要上傳的檔案放進去
```
root
│  app.py         
│             
├─static       
│  └─tmp        
│      └─test   
│              test.png
```

![](https://i.imgur.com/vmCzv5o.png)

### 3. 新增關鍵字回復 FlexSendMessage

- 準備好回復格式
https://developers.line.biz/flex-simulator/
把裡面的json存起來跟app.py放一起
```
root    
│  app.py   
│  test.json  
│                                                           
├─static                                                   
│  └─tmp                                                   
│      └─test                                               
│              test.png 
```


```
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, FlexSendMessage
    #這裡再增加一個FlexSendMessage
    
    import json #另外新增json lib
)
```
```
#app.py新增部分
    elif event.message.text == '學校資訊':
        f = json.load(open('./test.json'))
        print(f)
        flex_message = FlexSendMessage(
        alt_text='hello',
            contents=f
        )
        line_bot_api.reply_message(event.reply_token, flex_message)
```

![](https://i.imgur.com/ph6vDmU.png)

### 4. 很多時候 Linebot 會結合爬蟲
```
# 爬蟲的程式碼 把此程式碼與app.py一起放
import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.ncyu.edu.tw/csie/itemize_list.aspx?site_content_sn=58775'
res = requests.get(url, timeout =130)
print(res)
soup = BeautifulSoup(res.text,'html.parser')

tags = soup.find_all('a',href=re.compile('sn=58775'), limit = 4)

for tag in tags[:]:
    print(tag.text)

```
```
# app.py新增部分
    elif event.message.text == '公告':
        import spider
        tags = spider.tags
        
        messages = []
        for tag in tags:
            messages.append(TextSendMessage(text=tag.text))
        line_bot_api.reply_message(event.reply_token, messages)
```

![](https://i.imgur.com/fDtyyut.png)






