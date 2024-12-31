import urllib.parse
import urllib.request
from bs4 import BeautifulSoup

TTB_KEY = ""  # 알라딘 TTBKey

def fetch_monthly_bestsellers(year, month, output_dir="bestsellers"):
    import os
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    base_url = "http://www.aladin.co.kr/ttb/api/ItemList.aspx"
    
    # 4주 모두 조사
    for week in range(1, 5):
        params = {
            'ttbkey': TTB_KEY,
            'QueryType': 'Bestseller',
            'Year': year,
            'Month': month,
            'Week': week,
            'MaxResults': '10',
            'Start': '1',
            'SearchTarget': 'Book',
            'output': 'xml',
            'Version': '20131101'
        }
        url = f"{base_url}?{urllib.parse.urlencode(params)}"
        try:
            with urllib.request.urlopen(url) as response:
                xml_data = response.read()
            file_path = os.path.join(output_dir, f"{year}_{month:02d}_week{week}.xml")
            with open(file_path, "wb") as file:
                file.write(xml_data)
            print(f"Saved: {file_path}")
        except Exception as e:
            print(f"An error occurred for {year}-{month:02d}, Week {week}: {e}")

# Fetch data for 2024, all months
for month in range(1, 13):
    fetch_monthly_bestsellers(year=2024, month=month)