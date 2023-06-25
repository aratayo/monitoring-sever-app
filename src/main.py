from fastapi import FastAPI
# import requests

app = FastAPI()

@app.get("/")
def read_root():
  return {"Hello": "World"}

# url1 = "https://group-manager.nutfes.net"  #GM2
# url2 = "http://seeds.nutfes.net" #seeds
# url3 = "http://finansu.nutfes.net" #FinanSu

# response1 = requests.get(url1)
# response2 = requests.get(url2)
# response3 = requests.get(url3)

# print("ステータスコード:", response1.status_code)  # ステータスコードを出力する
# print("ステータスコード:", response2.status_code)  # ステータスコードを出力する
# print("ステータスコード:", response3.status_code)  # ステータスコードを出力する

