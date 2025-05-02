# 🚲 YouBike 空位查詢 Line Bot

這是一個使用 Python + Flask 開發的 Line Bot，可以查詢台北市各行政區的 YouBike 即時空位資訊。  
用戶只要在 Line 上輸入區名（例如：大安、中山），就會回傳該區所有站點的可停車位數。

## 🔧 功能介紹

- ✅ 查詢即時 YouBike 站點空位
- ✅ 支援輸入行政區名，如：信義、中山、大安...
- ✅ 透過 Line Bot 回覆使用者結果
- ✅ 部署於 Render 雲端平台
- ✅ 使用 GitHub 版本控制
- ✅ 使用 `.env` 保護敏感憑證

## 📦 專案結構

```
youbike-linebot/
├── app.py
├── .env (需自行建立)
├── requirements.txt
├── Procfile
└── README.md
```

## ⚙️ 使用說明

1. 安裝相依套件：
```
pip install -r requirements.txt
```

2. 建立 `.env` 檔案，內容如下：
```
LINE_CHANNEL_ACCESS_TOKEN=你的 access token
LINE_CHANNEL_SECRET=你的 channel secret
```

3. 執行：
```
python app.py
```

## ☁️ Render 部署方式

1. Push 專案到 GitHub
2. 前往 [https://render.com](https://render.com) 建立新 Web Service
3. 輸入 Start Command：`python app.py`
4. 設定環境變數與 Webhook 即可

## 📡 資料來源

台北市 YouBike 即時資料 API  
https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json
