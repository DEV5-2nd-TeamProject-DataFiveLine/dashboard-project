<img width="1541" alt="image" src="https://github.com/user-attachments/assets/9f84e586-505c-4859-a434-6672fef83fc9" /># DashBoard-Project
## 분석배경 및 목표

1. **도서 시장 동향 분석**: 
    - 베스트셀러 목록 분석을 통해 선호하는 책의 장르, 주제, 저자 등을 파악할 수 있음
    - 현 시점의 독서 트렌드와 사회적 관심사를 알 수 있음
    - 어떤 유형의 도서가 잘 팔리고 있는지, 도서 시장의 변화를 예측할 수 있음
2. **마케팅 전략 개발**
    - 베스트셀러 데이터를 분석하여 인기 있는 책의 마케팅 전략을 수립
    - 이를 바탕으로 비슷한 책을 출간하려는 출판사 혹은 저자에게 유용한 정보를 제공할 수 있음
3. **사회적/문화적 변화 분석**
    - 베스트셀러 목록은 때로 사회적, 정치적 또는 문화적 변화를 반영함
    - 분석을 통해 독자의 관심을 가지는 문제 혹은 이슈를 파악할 수 있음
4. **독자 리뷰 분석**
    - 리뷰의 집계를 통해 해당 도서에 대한 독자들의 객관적인 의견을 파악할 수 있음
5. **독서 성향 및 인사이트 제공**
    - 독서 데이터를 통해 사람들의 독서 성향, 선호도 등을 파악
    - 파악한 데이터를 바탕으로 독자에게 맞춤형 추천 시스템을 제공할 수 있음

---

## **데이터 소스**

1. **국내외 온라인 서점 API**: 판매량, 가격, 리뷰, 평점.

---

## **주요 기능**

1. **도서 분야별 판매 동향**: 분야별 판매량 및 월별 추이 시각화.
2. **베스트셀러 및 신간 분석**: 판매량 및 평점 비교

### **기술 스택**

- **Language**: Python, SQL
- **Cloud**: AWS S3, Snowflake
- **ETL Tools**: pandas
- **API**: Aladin API
- **BI Tool**: Superset (Preset)

1.	**데이터 수집**

- 알라딘 API를 이용해 주별 베스트셀러 JSON 데이터 확보
- 알라딘 API, ISBN번호를 이용해 개별 도서 정보 JSON 데이터 확보

2.	**데이터 전처리**

- pandas를 이용해 CSV, Parquet 파일로 변환
- 결측치 처리 및 중복 데이터 제거.
- 도서 카테고리 통합 및 매핑.

3.	**데이터 웨어하우스 설계 및 적재**

- Snowflake에 데이터 적재
- CSV, Parquet 파일 기반 ERD설계 및 테이블 생성
- 테이블 설계
    - 베스트 셀러 데이터를 기준으로 도서정보 테이블 설계
    - ISBN13을 PK로 지정
    - ISBN13을 외래키로 이용하여 SubInfo 테이블 설계 ( 포장정보, 판매정보 ,리뷰정보, 랭킹정보, 전자책정보, 중고책 정보, 중고 매입 정보)
    - 각 SubInfo 의 ID를 PK로 지정
    - 시리즈 ID와 카테고리 ID를 외래키로 사용하는 시리즈, 카테고리 테이블 작성

4.	**데이터 분석**

- 월별 및 카테고리별 판매량 분석 수행.
- 평점과 리뷰 수를 기반으로 인기 도서 분석 진행.

5.	**시각화**

- 분야별 판매량과 월별 추이 시각화
- 베스트셀러와 신간 도서의 비교 차트를 Superset에서 구성.

## ERD
<img width="705" alt="image" src="https://github.com/user-attachments/assets/7a105798-b576-4629-868d-ac8be0e5cb66" />

## 시스템 아키텍처

<img width="701" alt="image" src="https://github.com/user-attachments/assets/e6648b17-15be-4ac9-8326-e2c7ba1fe117" />


# 전체 대시보드

---

본 프로젝트는 국내 도서 판매 사이트 중 유일하게 API를 제공하는 알라딘 도서의 데이터를 활용하였습니다.

수집된 데이터를 분석하여 대시보드 설계 방안을 구상한 결과, **대시보드의 주요 목적**에 따라 **관리자용 대시보드**와 **사용자용 대시보드**로 나누어 제작하는 것이 효과적이라고 판단하였습니다.

**관리자용 대시보드**는 도서 판매량 및 매출 데이터를 중심으로 **영업 전략 수립과 마케팅 활동**에 기여할 수 있는 정보를 제공하는 데 초점을 맞추었습니다.

**사용자용 대시보드**는 인기 도서와 고객들이 참고할만한 정보를 시각적으로 전달함으로써 **도서 선택과 구매 의사결정을 지원**하는 것을 목적으로 설계했습니다.

<img width="1541" alt="image" src="https://github.com/user-attachments/assets/8a5dba41-0343-49e6-b24c-459608170169" />


▲ 관리자용 대시보드

![image](https://github.com/user-attachments/assets/9159784a-75b2-40b4-b18b-6dabf325780c)


▲ 사용자용 대시보드
 	
 
## 🙌 Branch Naming Convention

| 이름 | 규칙 | 설명 | 분기점 | 병합점 |
|---|---|---|---|---|
| main | `main` | 배포 가능한 최종 상태의 브랜치 | - | develop |
| develop | `develop` | 기능 개발을 위한 분기 및 병합 지점으로 사용하는 브랜치 | main | feat |
| hotfix | `hotfix/v<hotfix-version>` | 서비스 중 긴급 수정 건에 대한 처리 | main | main, develop |
| feat | `feat/<feature-name>` | 기능 개발 브랜치 | develop | develop |
| refactor | `refactor/<feature-name>` | 리팩토링 브랜치 | develop | develop |

<details>
<summary>예시</summary>
<div markdown="1">

- <이름>/<기능설명>-#<이슈번호> 의 형식으로 작성
- 브랜치명은 kebab-case를 따름
- 예) feat/create-login-#3

</div>
</details>

## 🙌 Commit Message Convention

| 머릿말           | 설명                                                     |
| ---------------- | ------------------------------------------------------|
| feat             | 새로운 기능 추가                                          |
| fix              | 버그 수정                                               |
| design           | UI 디자인 변경                                           |
| !BREAKING CHANGE | 커다란 API 변경                                          |
| !HOTFIX          | 코드 포맷 변경, 세미 콜론 누락, 코드 수정이 없는 경우             |
| refactor         | 프로덕션 코드 리팩토링(기능은 그대로 유지)                      |
| comment          | 주석 추가 및 변경                                         |
| docs             | 문서 수정                                               |
| test             | 테스트 추가, 테스트 리팩토링(기능은 그대로 유지)                 |
| setting          | 패키지 설치, 개발 설정                                     |
| chore            | 빌드 테스트 업데이트, 패키지 매니저를 설정하는 경우(기능은 그대로 유지)|
| rename           | 파일 혹은 폴더명을 수정(기능은 그대로 유지)                     |
| remove           | 파일 삭제(기능은 그대로 유지)                                |

<details>
<summary>예시</summary>
<div markdown="1">

- 양식: <머릿말>: <제목> - #<이슈번호> 의 형식으로 작성
- 예시: feat: 로그인 기능 추가 - #3

</div>
</details>
