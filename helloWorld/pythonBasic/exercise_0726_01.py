weight = input("몸무게는 얼마입니까? ")
isKg = False
kgFlg = input ("몸무게가 kg입니까? lbs입니까? ")
if kgFlg.find("kg") != -1:
    isKg = True

if isKg==True :
    print(str(weight)+"kg입니다.")
elif isKg==False :
    print(str(weight)+"lbs는 "+str(float(weight)/2.204623)+"kg입니다.")
