def std_weight(height, gender) :
    height_ = height*0.01
    if gender == "여자" :
        weight = round(height_*height_*21,2)
        print(f"키 {height} {gender}의 표준체중은 {weight}kg입니다")
    elif gender == "남자" : 
        weight = round(height_*height_*22,2)
        print(f"키 {height} {gender}의 표준체중은 {weight}kg입니다")


std_weight(175,"남자")  