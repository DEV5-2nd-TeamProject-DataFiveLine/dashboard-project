import requests
import json
import pandas as pd

key = ""
year = "2024"

bestseller_data = []

for month in range(1, 2):
    for week in range(1, 2):
        week_names = ["첫째주", "둘째주", "셋째주", "넷째주"]
        week_name = week_names[week - 1]
        print(f"[{year}년 {month}월 {week_name}]")
        url = f"http://www.aladin.co.kr/ttb/api/ItemList.aspx?ttbkey={key}&QueryType=Bestseller&Year={year}&Month={month}&Week={week}&Results=10&start=1&SearchTarget=Book&output=js&Version=20131101"

        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            try:
                response_json = response.json()
                items = response_json.get("item", [])

                if not items:
                    print("  Bestseller 목록이 존재하지 않습니다.")
                else:
                    for item in items:
                        # 년, 월, 주 데이터 추가
                        item['year'] = year
                        item['month'] = month
                        item['week'] = week

                        bestseller_data.append(item)
            except json.JSONDecodeError as e:
                print("  JSONDecodeError:", e)
                print("  응답 내용:", response.text)
        else:
            print(f"  Error: {response.status_code}")
            print(f"  응답 내용: {response.text}")


df = pd.DataFrame(bestseller_data)

# subInfo 필드 제거(비어있는 필드여서 parquet파일로 저장 불가)
df = df.drop(columns=['subInfo'])

# 데이터 저장
output_dir = "/Users/ez/study/devcourse/project2/data"
parquet_file = f"{output_dir}/bestseller_{year}.parquet"
df.to_parquet(parquet_file, index=False)
print(f"Parquet 파일 저장 완료: {parquet_file}")