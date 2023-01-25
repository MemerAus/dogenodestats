# Script to pull DOGE price from Binance 
# Ensure you save this in the same folder where the stats.py lives (OLED_Stats)
#someone else could probably build this into the stats.py code but this worked so its what I did :D

# Import libraries
import json
import requests
  
# defining key/request url
key = "https://api.binance.com/api/v3/ticker/price?symbol=DOGEUSDT"
  
# requesting data from url
data = requests.get(key)  
data = data.json()
print(f"DOGE price: {data['price']}")
