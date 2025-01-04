import os
import pandas as pd
import json

# JSON 파일 디렉토리와 CSV 파일 저장 디렉토리 설정
json_directory = "bestseller_data"  # JSON 파일이 저장된 디렉토리
csv_directory = "bestseller_csv"  # CSV 파일을 저장할 디렉토리
os.makedirs(csv_directory, exist_ok=True)

# JSON 파일을 순회하며 CSV 파일로 변환
for file_name in os.listdir(json_directory):
    if file_name.endswith(".json"):
        json_file_path = os.path.join(json_directory, file_name)
        csv_file_path = os.path.join(csv_directory, file_name.replace(".json", ".csv"))

        try:
            # JSON 파일 읽기
            with open(json_file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
            
            # JSON 데이터를 Pandas DataFrame으로 변환
            if "item" in data:
                df = pd.json_normalize(data["item"])  # 'item' 키의 데이터를 DataFrame으로 변환
                
                # 추가 메타데이터를 DataFrame에 추가 (Year, Month, Week)
                df["Year"] = data.get("Year")
                df["Month"] = data.get("Month")
                df["Week"] = data.get("Week")
                
                # DataFrame을 CSV 파일로 저장
                df.to_csv(csv_file_path, index=False, encoding="utf-8-sig")  # CSV 파일의 인코딩은 UTF-8-SIG로 설정
                print(f"Converted {file_name} to {csv_file_path}")
            else:
                print(f"Key 'item' not found in {file_name}. Skipping...")
        except Exception as e:
            print(f"Failed to process {file_name}: {e}")
