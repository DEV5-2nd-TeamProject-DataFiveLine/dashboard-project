import os
import pandas as pd
import json

# JSON 파일 디렉토리와 Parquet 파일 저장 디렉토리 설정
json_directory = "bestseller_data"  # JSON 파일이 저장된 디렉토리
parquet_directory = "bestseller_parquet"  # Parquet 파일을 저장할 디렉토리
os.makedirs(parquet_directory, exist_ok=True)

# JSON 파일을 순회하며 Parquet 파일로 변환
for file_name in os.listdir(json_directory):
    if file_name.endswith(".json"):
        json_file_path = os.path.join(json_directory, file_name)
        parquet_file_path = os.path.join(parquet_directory, file_name.replace(".json", ".parquet"))

        try:
            # JSON 파일 읽기
            with open(json_file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
            
            # JSON 데이터를 Pandas DataFrame으로 변환
            df = pd.json_normalize(data["item"])  # 'item' 키의 데이터를 DataFrame으로 변환
            
            # 추가 메타데이터를 DataFrame에 추가 (Year, Month, Week)
            df["Year"] = data.get("Year")
            df["Month"] = data.get("Month")
            df["Week"] = data.get("Week")
            
            # DataFrame을 Parquet 파일로 저장
            df.to_parquet(parquet_file_path, index=False, engine="pyarrow")
            print(f"Converted {file_name} to {parquet_file_path}")
        except Exception as e:
            print(f"Failed to process {file_name}: {e}")
