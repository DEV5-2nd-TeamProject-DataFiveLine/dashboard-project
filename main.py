from aladin_data import get_bestseller
from request_product_info import get_bookInfo
from bestseller_convert_to_parquet import convert_bestseller_json_to_parquet as b_parquet
from bestseller_convert_to_csv import convert_bestseller_json_to_csv as b_csv
from product_info_csv import convert_product_info_json_to_csv as p_csv
from product_info_parquet import convert_product_info_json_to_parquet as p_parquet

def main():
    # 설정할 매개변수
    key = ""  # API 키를 여기에 입력하세요
    QueryType = "Bestseller"  # 옵션: "NewRelease", "Bestseller", "Bestseller_Month", "Bestseller_Year"
    MaxResults = 50  # 최대 결과 개수 (1000 ~ 10000)
    Year = 2024  # 베스트셀러 목록 연도

    # 출력 디렉터리 정의
    bestSeller_json_directory = "bestseller_data"
    bestSeller_parquet_directory = "bestseller_parquet"
    bestSeller_csv_directory = "bestseller_csv"

    productInfo_json_directory = "product_info"
    productInfo_parquet_directory = "product_info_parquet"
    productInfo_csv_directory = "product_info_csv"

    # 베스트셀러 데이터 가져오기 및 JSON 저장
    get_bestseller(key, QueryType, MaxResults, Year)
    
    # 책 정보 가져오기 및 JSON 저장
    get_bookInfo(key)


    # 베스트셀러 JSON을 Parquet와 CSV로 변환
    b_parquet(bestSeller_json_directory, bestSeller_parquet_directory)
    b_csv(bestSeller_json_directory, bestSeller_csv_directory)
    
    # 제품 정보 JSON을 Parquet와 CSV로 변환
    p_parquet(productInfo_json_directory, productInfo_parquet_directory)
    p_csv(productInfo_json_directory, productInfo_csv_directory)

if __name__ == "__main__":
    main()
