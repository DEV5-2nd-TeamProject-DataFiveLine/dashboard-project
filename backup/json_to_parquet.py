import os
import pandas as pd
import json

# JSON 파일이 저장된 디렉토리
json_directory = "rating_info_Data"
# Parquet 파일 저장 디렉토리
parquet_directory = "rating_info_Parquet"
os.makedirs(parquet_directory, exist_ok=True)

# 디렉토리 내 모든 JSON 파일 처리
for file_name in os.listdir(json_directory):
    if file_name.endswith(".json"):
        json_file_path = os.path.join(json_directory, file_name)
        

        # JSON 파일 읽기
        with open(json_file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        
        # JSON 데이터를 데이터프레임으로 변환
        try:
            df = pd.json_normalize(data)  # JSON 구조를 펼쳐 데이터프레임으로 변환
            
            # Parquet 파일 이름 설정
            parquet_file_name = file_name.replace(".json", ".parquet")
            parquet_file_path = os.path.join(parquet_directory, parquet_file_name)
            
            # Parquet 파일 저장
            df.to_parquet(parquet_file_path, engine="pyarrow", index=False)
            print(f"Converted {file_name} to {parquet_file_name}")
        except Exception as e:
            print(f"Failed to convert {file_name}: {e}")
