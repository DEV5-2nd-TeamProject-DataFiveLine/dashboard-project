import pandas as pd
import requests
import os
from pandas import json_normalize

key = ""

# 기존 데이터 파일 로드
input_dir = "/Users/ez/study/devcourse/project2/data"
parquet_file = f"{input_dir}/bestseller_2024.parquet"
output_parquet_file = f"{input_dir}/book_lookup.parquet"

df = pd.read_parquet(parquet_file)
book_data = []

for idx, row in df.iterrows():
    isbn = row['isbn']
    if pd.isna(isbn) or isbn == "": 
        print(f"Skipping row {idx}, ISBN is missing.")
        continue

    url = f"https://www.aladin.co.kr/ttb/api/ItemLookUp.aspx?ttbkey={key}&itemIdType=ISBN&ItemId={isbn}&output=js&Version=20131101&OptResult=ebookList,usedList,reviewList,fileFormatList,c2binfo,packing,b2bSupply,subbarcode,cardReviewImgList,ratingInfo,bestSellerRank"
    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            response_json = response.json()
            items = response_json.get("item",[])

            for item in items:
                book_data.append(item)
        else:
            print(f"API Error for ISBN {isbn}: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed for ISBN {isbn}: {e}")
    print(f"row {idx} completed successfully")

# 데이터 평탄화
df = json_normalize(book_data)
df = df.explode('subInfo.ebookList')

# 'subInfo.ebookList' 평탄화
ebook_details = json_normalize(df['subInfo.ebookList'])
ebook_details = ebook_details.add_prefix('subInfo.ebookList.')

# index 재설정
df = df.reset_index(drop=True)
ebook_details = ebook_details.reset_index(drop=True)
print(df.index.is_unique)
print(ebook_details.index.is_unique)

# 기존데이터와 'subInfo.ebookList' 결합
df = df.drop(columns=['subInfo.ebookList'])
df = pd.concat([df, ebook_details], axis=1)

# 데이터 저장
df.to_parquet(output_parquet_file, index=False)
print(f"Parquet 파일 저장 완료: {output_parquet_file}")