from alaadin_data import get_bestseller
from request_product_info import get_bookInfo

def main():
    key = "ttblej0931438001"
    QueryType = "Bestseller"  # "NewRelease", "Bestseller", "Bestseller_Month", "Bestseller_Year"
    MaxResults = 50  # 1000 ~ 10000
    Year = 2023

    # bestseller_data.json 파일에 bestseller_data를 저장
    get_bestseller(key, QueryType, MaxResults, Year)

    # product_info.json 파일에 product_info를 저장
    get_bookInfo(key)