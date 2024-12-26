# 💊 AI 약사 챗봇 서비스 💊
## SKN06-3rd-3team

## 팀 소개
## 삼쩜삼

![image](https://github.com/user-attachments/assets/a93de181-7b8f-48b1-8b76-62144617bf84)

| 김동훈 | 김승현 | 성은진 | 장예린 | 조하늘 |
|:--------------------:|:--------------------:|:--------------------:|:--------------------:|:--------------------:|
|<img width="100%" alt="스크린샷 2024-12-26 오후 4 33 51" src="https://github.com/user-attachments/assets/4c0c4e85-7bac-415e-9bb9-9c30d1d4ecc3" />|<img width="100%" alt="스크린샷 2024-12-26 오후 4 33 58" src="https://github.com/user-attachments/assets/0f87396c-d631-42e2-a4f0-3af2dbaa46d6" />  |<img width="100%" alt="스크린샷 2024-12-26 오후 4 34 17" src="https://github.com/user-attachments/assets/177f6c5e-1d34-44f3-8406-675a76864453" />|<img width="100%" alt="스크린샷 2024-12-26 오후 4 37 33" src="https://github.com/user-attachments/assets/5f979f3c-ff43-438b-85f8-407b9585fa63" />|<img width="100%" alt="스크린샷 2024-12-26 오후 4 31 59" src="https://github.com/user-attachments/assets/049bdda2-d041-4517-8047-5b731dae664c" />|
| 작은점| 점약사| 이어점| 마지막점| 큰점|

## ✍️ 프로젝트 개요
✔️ 개발 배경
- 최근 의약품 도매업계의 약국 공급 현황에 따르면, 비대면 활동의 증가로 인해 의료기관 방문 후 처방받는 의약품 수요는 감소했지만, 일반의약품 공급이 지속적으로 증가하고 있습니다.
- 사용자가 입력한 증상이나 상황, 약물정보를 바탕으로 의약품과 약국에 대한 정보를 함께 안내하는 **지능형 의료 상담 서비스**를 개발하고자 했습니다.

✔️ 개발 목적
사용자 맞춤형 정보제공
-데이터베이스 내에서 사용자가 입력한 정보에 따른 의약품 추천
-사용자 위치정보를 이용해 근처 약국 추천
실시간 상호작용
- 사용자의 추가 질문에 **실시간으로 답변**
- 새로운 증상이나 상황을 입력하면 즉시 재추천 

## 📝 주요 기능
✔️ 증상 기반 의약품 추천
- 사용자가 입력한 **증상을 기반**으로 적합한 약물 2가지를 추천 및 비교
- 부작용이 적고 복용이 간편한 약을 우선 추천

✔️ 약물 정보 제공
- 약의 효능, 복용법, 주의사항, 악화 시 대처방법을 함께 제공
- 각 정보를 **표로 제공**하여 가독성 향상
- 의약품에 대한 추가 정보 요청시 즉시 추가 정보 제공

✔️ 사용자 위치기반 약국 추천
- **사용자의 위치 정보**를 바탕으로 한 근처 약국 2곳을 추천
- 약국까지의 거리와 운영 시간, 전화번호 등의 정보 제공

✔️ 평가 및 피드백:
- LLM 기반 평가 도구를 사용하여 추천 시스템의 정확성, 신뢰도, 관련성을 평가.
- 주요 메트릭: 리콜(Recall), 정밀도(Precision), 충실도(Faithfulness), 답변 관련성(Answer Relevancy).

## 📊 기대 효과
- **사용자 경험 향상:** 빠르고 정확한 의약품 및 약국 정보 제공
- **안전성 강화:** 부작용 및 주의사항에 대한 명확한 안내
- **의료 리소스 절감:** 가벼운 증상에 대한 간단한 대응 가능
- **지속적 개선:** 사용자 피드백을 통해 추천 알고리즘 최적화

## 🔨 기술스택
<div>
<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/langchain-F7DF1E?style=for-the-badge&logo=langchain&logoColor=black">
<img src="https://img.shields.io/badge/openai-0769AD?style=for-the-badge&logo=openai&logoColor=black">
<img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white">
<img src="https://github.com/user-attachments/assets/c8cd01e7-6ce6-46db-8cc3-b13286829cf3" width="163" height="28"/>
</div>



## 상세내용

### 데이터 수집 및 전처리
---
- 공공데이터포털(www.data.go.kr) 에서 의약품개요정보, 의약품 회수 및 판매중지 정보, 서울시 약국 운영시간 정보 등 데이터 다운
- 데이터 로드 
 ```python3
   from langchain_community.document_loaders import TextLoader
   path = r'data/medicine.txt'

   # 1. loader 객체 생성
   loader = TextLoader(path, encoding='utf-8')
   # 2. loader를 이용해서 파일 읽어옴
   docs = loader.load()
```

#### 전처리
```
 오픈 API - https://www.data.go.kr/data/15075057/openapi.do 데이터 JSON 환경으로 가져와서 TXT 파일로 변환 (make_file.py 참고)
```        


### 사용 데이터
-  https://www.data.go.kr/data/15075057/openapi.do
-  https://www.data.go.kr/data/15098095/openapi.do
-  https://www.data.go.kr/data/15059114/openapi.do
-  https://data.seoul.go.kr/dataList/OA-20402/S/1/datasetView.do

### 벡터스토어 생성
```
# 문서 load and split
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100
)

docs = loader.load_and_split(splitter)
```

### RAG(Retrieval Augmented Generation) Chain 생성

  
## 챗봇 생성
-
## 성능 테스트
-





## 🪄향후 계획 및 개선점
### 1. 위치 안내 서비스
- 의약품 추천과 더불어 안전 상비의약품 판매가 가능한 편의점등의 위치 제공서비스
- 추천 의약품 재고가 있는 약국 정보 제공

### 2. 회수 판매 중지 정보 제공
- 기존 사용자가 가지고 있던 약에 대한 정보 제공.
- 현재 가지고 있는 약이 회수 및 판매 중지 제품일 경우 정보 제공


## 💭팀원 회고
김동훈
>
김승현
>
성은진
>
장예린
>
조하늘
> 팀원이 없다면 프로젝트가 진행이 안 됩니다. 감사합니다. 삼쩜삼 여러분. 


