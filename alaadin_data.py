import os
import json
import requests
import time
# 변수 설정
key = "ttbgland451437001"
QueryType = "Bestseller"
MaxResults = 10
Year = 2024

# 저장 디렉토리 설정
directory = "bestseller_data"
os.makedirs(directory, exist_ok=True)

# 데이터 요청 및 저장
for i in range(1, 13):
    for j in range(1, 5):
        Month = i
        Week = j
        url = f"http://www.aladin.co.kr/ttb/api/ItemList.aspx?ttbkey={key}&QueryType={QueryType}&MaxResults={MaxResults}&start=1&SearchTarget=Book&output=JS&Version=20131101&Year={Year}&Month={Month}&Week={Week}"

        # API 요청
        response = requests.get(url)

        if response.status_code == 200:
            try:
                # 응답을 JSON 형태로 변환
                response_json = response.json()

                # 파일 이름 생성
                file_name = f"{Year}_Month{Month}_Week{Week}.json"
                file_path = os.path.join(directory, file_name)

                # JSON 데이터를 파일로 저장
                with open(file_path, "w", encoding="utf-8") as file:
                    json.dump(response_json, file, ensure_ascii=False, indent=4)

                print(f"Saved data for Year: {Year}, Month: {Month}, Week: {Week} to {file_name}")
            except json.JSONDecodeError:
                print(f"Failed to decode JSON for Year: {Year}, Month: {Month}, Week: {Week}")
        else:
            print(f"Request failed for Year: {Year}, Month: {Month}, Week: {Week} with status code {response.status_code}")
        time.sleep(0.1)