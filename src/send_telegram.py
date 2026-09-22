import json, os, urllib.request, urllib.parse

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

with open("docs/state.json", encoding="utf-8") as f:
    state = json.load(f)

lines = ["📊 트라이팟 오늘의 신호"]
for k, v in state.items():
    lines.append(f"{k}: {v}")
text = "\n".join(lines)

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
data = urllib.parse.urlencode({"chat_id": CHAT_ID, "text": text}).encode()
urllib.request.urlopen(url, data=data)
