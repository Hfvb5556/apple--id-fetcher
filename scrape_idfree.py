import requests
from bs4 import BeautifulSoup
import json
import time

def scrape_apple_ids():
    url = "https://idfree.top"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        account_container = soup.find("div", {"id": "account-container"})
        
        if account_container:
            account_text = account_container.get_text().strip()
            # 假设页面格式是 "账号：xxx 密码：xxx"
            email = account_text.split("账号：")[1].split()[0]  # 提取邮箱
            password = account_text.split("密码：")[1].split()[0]  # 提取密码
            
            data = {
                "email": email,
                "password": password,
                "last_updated": time.strftime("%Y-%m-%d %H:%M:%S")
            }
            
            with open("apple_ids.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            print("成功抓取账号:", data)
        else:
            print("未找到账号信息")
    except Exception as e:
        print("抓取失败:", e)

if __name__ == "__main__":
    scrape_apple_ids()
