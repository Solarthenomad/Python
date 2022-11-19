class House:
    # 매물 초기화 : 위치, 건물 종류, 매물 종류, 가격, 준공년도
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    # 매물 정보 표시
    def show_detail(self):
        
        print(f"{self.location} 아파트 {self.deal_type} {self.price} {self.completion_year}")
        

house = []
house1 = House("강남", "아파트", "매매", "10억", "2010년")
house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
house3 = House("송파", "빌라", "월세", "500/50", "2000년")

house.append(house1)
house.append(house2)
house.append(house3)
count = len(house)

print(f"총 {count}대의 매물이 있습니다. ") #클래스 내부에서 정의하면 총 3대의 매물이 있습니다가 3번 나옴
for h in house:
    h.show_detail()