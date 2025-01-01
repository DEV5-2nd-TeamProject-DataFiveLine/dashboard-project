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

def fetch_item_data(url, query, errors, isbn, month, week, index):
    try:
        query.update({'ItemId':isbn})
        query_text = parse.urlencode(query,encoding='UTF-8',doseq=True)
        con = url + "?" + query_text
        res = requests.get(con)
        res.raise_for_status() # HTTP 에러 발생 시 예외 처리

        res_json = res.json()
        if 'item' in res_json:
            return res_json['item'][0]
        else:
            errors.append({
                'month':month,
                'week':week,
                'index':index,
                'isbn':isbn,
                'error':"item key is missing in response."
            })
            
    except requests.exceptions.RequestException as e:
        errors.append({'isbn':isbn,"error": str(e)})

def loop_isbn(start_month, end_month, start_week, end_week, json_file, item_path, query, url):
    merged_data = {}
    errors = []
    for month in tqdm(range(start_month, end_month+1)):
        for week in range(start_week, end_week+1):
            if str(month) not in merged_data:
                merged_data[str(month)] = {}
            merged_list = []
            
            for index, item in enumerate(json_file.get(str(month), {}).get(str(week), [])):
                isbn = item.get('isbn13')
                if not isbn:
                    errors.append({
                        'month': month,
                        'week': week,
                        'index': index,
                        'error': "Missing ISBN."
                    })
                    continue

                data = fetch_item_data(url, query, errors, isbn, month, week, index)
                if data:
                    merged_list.append(data)

                time.sleep(random.uniform(0.3,1))

            merged_data[str(month)][str(week)] = merged_list

    write_json(merged_data,item_path)

    if errors:
        error_log_path = item_path.replace('.json', '_errors.json')
        write_json(errors, error_log_path)
        print(f"Errors encountered. Check the log file: {error_log_path}")
    else:
        print("All requests processed successfully.")

api_path = os.path.join(os.getcwd(),"API.env")
load_dotenv(api_path)
api_key = os.getenv("Aladdin_KEY")

query_item ={
    'ttbkey' : api_key, 
    'itemIdType':'ISBN',
	'output':'js', 
	'Version':'20131101',
    'OptResult':'ebookList,usedList,fileFormatList,c2binfo,packing,b2bSupply,subbarcode,cardReviewImgList,ratingInfo,bestSellerRank'
}

url_item = "http://www.aladin.co.kr/ttb/api/ItemLookUp.aspx"

best_path = 'c:/Users/Yeojun/Aladdin/bestseller.json'
json_file = read_json(best_path)

item_path = 'c:/Users/Yeojun/Aladdin/itemLookUp.json'

loop_isbn(1, 12, 1, 4, json_file, item_path, query_item, url_item)



