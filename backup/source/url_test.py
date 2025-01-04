import requests
import pandas as pd
from pandas import json_normalize

key = "ttblej0931438001"
isbn = "K912934840"
url = f"https://www.aladin.co.kr/ttb/api/ItemLookUp.aspx?ttbkey={key}&itemIdType=ISBN&ItemId={isbn}&output=js&Version=20131101&OptResult=ebookList,usedList,reviewList,fileFormatList,c2binfo,packing,b2bSupply,subbarcode,cardReviewImgList,ratingInfo,bestSellerRank"

book_info=[]
response = requests.post(url)
response_json = response.json()
books = response_json.get('item',[])
for book in books:
    book_info.append(book)
    
df = json_normalize(book_info)
df = df.explode('subInfo.ebookList')
ebook_details = json_normalize(df['subInfo.ebookList'])
ebook_details = ebook_details.add_prefix('subInfo.ebookList.')
df = df.drop(columns=['subInfo.ebookList'])
df = pd.concat([df, ebook_details], axis=1)

# input_dir = "/Users/ez/study/devcourse/project2"
# output_csv_file = f"{input_dir}/test.csv"
# df.to_csv(output_csv_file, index=False, encoding="utf-8-sig")
# print(f"Updated CSV 파일 저장 완료: {output_csv_file}")