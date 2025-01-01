import requests
from urllib import parse
import json
import os
from tqdm import tqdm
import time
import random
from dotenv import load_dotenv


def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)
    
def write_json(data,file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def bestsellerAPI(url, query, startmonth,endmonth,startweek,endweek, output_path, delay_range=(0.3, 1)):
    merged_data = {}
    errors = []

    for m in tqdm(range(startmonth,endmonth+1), desc="Processing months"):
        query.update({'Month':str(m)})
        for w in range(startweek,endweek+1):
            query.update({'Week':str(w)})

            try:
                # 쿼리 문자열 생성 및 요청
                query_text = parse.urlencode(query,encoding='UTF-8',doseq=True)
                con = url + "?" + query_text
                res = requests.get(con)

                # JSON 데이터 처리
                res_json = res.json()
                if 'item' in res_json:
                    if str(m) not in merged_data:
                        merged_data[str(m)] = {}
                    merged_data[str(m)][str(w)] = res_json['item']
                else:
                    errors.append({"month": m, "week": w, "error": "Invalid response structure"})
            except requests.exceptions.RequestException as e:
                # 에러 발생 시 로그 저장
                errors.append({"month": m, "week": w, "error": str(e)})

            time.sleep(random.uniform(*delay_range))

    write_json(merged_data,output_path)
    if errors:
        # 에러 로그 저장
        error_log_path = output_path.replace('.json', '_errors.json')
        write_json(errors, error_log_path)
        print(f"Errors encountered. Check the log file: {error_log_path}")
    else:
        print("All requests processed successfully.")

api_path = os.path.join(os.getcwd(),"API.env")
load_dotenv(api_path)
api_key = os.getenv("Aladdin_KEY")

query ={
    'ttbkey' : api_key, 
	'QueryType' : 'Bestseller', 
    'SearchTarget':'Book', 
	'MaxResults':'50', 
	'start':'1', 
	'output':'js', 
	'Version':'20131101',
    'Year':'2024',
    'Month':'1',
    'Week':'1'
}

url = "http://www.aladin.co.kr/ttb/api/ItemList.aspx"

output_path = 'c:/Users/Yeojun/Aladdin/bestseller.json'

bestsellerAPI(url, query, 1, 12, 1, 4, output_path)