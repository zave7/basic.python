# --- Faker : 테스트용 더미 데이터를 생성할 때 사용하는 라이브러리

## Faker 설치
### $ pip install Faker

from faker import Faker

## current_country : 현재 설정된 나라 반환
Faker().current_country() # United States, 기본값

## name : 이름 더미 데이터 반환
Faker().name() # Mary Flynn, 영어 이름 반환
Faker("ko-KR").name() # 최지우, 한글 이름 반환

## address : 주소 더미 데이터 반환
Faker("ko-KR").address() # 제주특별자치도 음성군 영동대225거리 (윤서이이동)

## postcode : 우편번호 반환
## country : 국가명 반환
## company : 회사명 반환
## job : 직업명 반환
## phone_number : 휴대폰 번호 반환
## email : 이메일 주소 반환
## user_name : 사용자명 반환
## pyint : 임의의 숫자 반환
## ipv4_private : IP 주소 반환
## text : 임의의 문장 (한글 임의의 문장은 catch_phrase)
## color_name : 색상명 반환