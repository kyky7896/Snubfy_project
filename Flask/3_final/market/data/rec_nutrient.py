# 권장 칼로리 (대상의 성장 상태(유아, 청소년 등), 연령, 성별, 키, 몸무게, 활동성, 임신 기간, 수유기간)
def rec_EER(state, period, sex, height, weight, activity, trimester = 0, postpartum = 0):
    # Kcal
    #영유아기

    if (state == 'Infants') or (state == 'Young Children'):
        #개월별로 나누어 계산
        if 0 <= period <= 3:
            eer = (89 * weight - 100) + 175
        elif 4 <= period <= 6:
            eer = (89 * weight - 100) + 56
        elif 7 <= period <= 12:
            eer = (89 * weight - 100) + 22
        elif 13 <= period <= 35:
            eer = (89 * weight - 100) + 20

    #아동, 청소년기        
    elif (state == 'Children') or (state == 'Adolescents'):
        if sex == 'Male':
            #활동성 지수
            if activity == 'Sedentary':
                pa = 1
            elif activity == 'Low Active':
                pa = 1.13
            elif activity == 'Active':
                pa = 1.26
            elif activity == 'Very Active':
                pa = 1.42

            ## 칼로리
            if 3 <= period <= 8:
                eer = 88.5 - (61.9 * period) + pa * ((26.7 * weight) + (903 * height/100)) + 20
            else:
                eer = 88.5 - (61.9 * period) + pa * ((26.7 * weight) + (903 * height/100)) + 25

        elif sex == 'Female':
            #활동성 지수
            if activity == 'Sedentary':
                pa = 1
            elif activity == 'Low Active':
                pa = 1.16
            elif activity == 'Active':
                pa = 1.31
            elif activity == 'Very Active':
                pa = 1.56

            ## 칼로리
            if 3 <= period <= 8:
                eer = 135.3 - (30.8 * period) + pa * ((10 * weight) + (934 * height/100)) + 20
            else:
                eer = 135.3 - (30.8 * period) + pa * ((10 * weight) + (934 * height/100)) + 20   

            #임산부
            if trimester == 1: #3개월
                eer = eer
            elif trimester == 2: #6개월
                eer += 340 
            elif trimester == 3: #9개월
                eer += 452
            
            #수유기간
            if 0 <= postpartum <= 6:
                eer += 330
            elif 7 <= postpartum <= 12:
                eer += 400

    #성인
    elif state == 'Adults':
        if sex == 'Male':
            #활동성 지수
            if activity == 'Sedentary':
                pa = 1
            elif activity == 'Low Active':
                pa = 1.11
            elif activity == 'Active':
                pa = 1.25
            elif activity == 'Very Active':
                pa = 1.48

            ## 칼로리
            eer = 662 - (9.53 * period) + pa * ((15.91 * weight) + (539.6 * height/100))

        elif sex == 'Female':
            #활동성 지수
            if activity == 'Sedentary':
                pa = 1
            elif activity == 'Low Active':
                pa = 1.12
            elif activity == 'Active':
                pa = 1.27
            elif activity == 'Very Active':
                pa = 1.45

            ## 칼로리
            eer = 662 - (6.91 * period) + pa * ((9.36 * weight) + (726 * height/100))
            
            #임산부
            if trimester == 1: #3개월
                eer = eer
            elif trimester == 2: #6개월
                eer += 340 
            elif trimester == 3: #9개월
                eer += 452

            #수유기간
            if 0 <= postpartum <= 6:
                eer += 330
            elif 7 <= postpartum <= 12:
                eer += 400
            
    return round(eer, 1)


##################################################################
def rec_carbonhydrate(state, period, trimester = 0, postpartum = 0): #탄수화물, 설탕 모두 포함
    # g
    #영유아기
    if (state == 'Infants') or (state == 'Young Children'):
        #개월별로 나누어 계산
        if 0 <= period <= 6:
            carbonhd = 60
        elif 7 <= period <= 12:
            carbonhd = 95
        elif period > 12:
            carbonhd = 130

    #아동, 청소년기        
    elif (state == 'Children') or (state == 'Adolescents'):
        carbonhd = 130

        #임산부
        if trimester != 0: 
            carbonhd = 175
        
        if postpartum != 0:
            carbonhd = 210

    #성인
    elif state == 'Adults':
        carbonhd = 130         
        #임산부
        if trimester != 0: 
            carbonhd = 175
        
        if postpartum != 0:
            carbonhd = 210


    return round(carbonhd, 1)

##################################################################

def rec_protein(state, period, weight, trimester = 0, postpartum = 0):
    # g
    #영유아기
    if (state == 'Infants') or (state == 'Young Children'):
        #개월별로 나누어 계산
        if 0 <= period <= 6:
            protein = 1.52 * weight 
        elif 7 <= period <= 12:
            protein = 1.2 * weight 
        elif period <= 35:
            protein = 1.05 * weight 

    #아동, 청소년기        
    elif (state == 'Children') or (state == 'Adolescents'):
        if 3 <= period <= 8:
            protein = 0.95 * weight
        elif 9 <= period <= 13:
            protein = 0.95 * weight 
        elif 14 <= period <= 18:
            protein = 0.85 * weight
        
        #임산부
        if trimester != 0: 
            protein = 1.1 * weight
        
        #수유기간
        if postpartum != 0:
            protein = 1.3 * weight

    #성인
    elif state == 'Adults':
        protein = 0.85 * weight
            
        #임산부
        if trimester != 0: 
            protein = 1.1 * weight
        
        #수유기간
        if postpartum != 0:
            protein = 1.3 * weight
            
    return round(protein, 1)

##################################################################

def rec_water(state, period, sex, weight, trimester = 0, postpartum = 0):
    # L
    #영유아기
    if (state == 'Infants') or (state == 'Young Children'):
        #개월별로 나누어 계산
        if 0 <= period <= 6:
            water = 0.7 
        elif 7 <= period <= 12:
            water = 0.8 
        elif 13 <= period <= 35:
            water = 1.3

    #아동, 청소년기        
    elif (state == 'Children') or (state == 'Adolescents'):
        if 3 <= period <= 8:
            water = 1.7
        elif 9 <= period <= 13:
            if sex == 'Male':
                water = 2.4
            else:
                water = 2.1
        elif 14 <= period <= 18:
            if sex == 'Male':
                water = 3.3
            else:
                water = 2.3
        
        #임산부
        if trimester != 0: 
            water = 3
        
        #수유기간
        if postpartum != 0:
            water = 3.8

    #성인
    elif state == 'Adults':
        if sex == 'Male':
            water = 3.7
        else:
            water = 2.7
            
        #임산부
        if trimester != 0: 
            water = 3
        
        #수유기간
        if postpartum != 0:
            water = 3.8
            
    return round(water, 1)

##################################################################

def rec_vita_a(state, period, sex, trimester = 0, postpartum = 0):
    # ug (microgram)
    #영유아기
    if (state == 'Infants') or (state == 'Young Children'):
        #개월별로 나누어 계산
        if 0 <= period <= 6:
            vit_a = 400 
        elif 7 <= period <= 12:
            vit_a = 500 
        elif 13 <= period <= 35:
            vit_a = 300

    #아동, 청소년기        
    elif (state == 'Children') or (state == 'Adolescents'):
        if 3 <= period <= 8:
            vit_a = 400
        elif 9 <= period <= 13:
            if sex == 'Male':
                vit_a = 600
            else:
                vit_a = 600
        elif 14 <= period <= 18:
            if sex == 'Male':
                vit_a = 900
            else:
                vit_a = 700
        
        #임산부
        if trimester != 0: 
            vit_a = 750
        
        #수유기간
        if postpartum != 0:
            vit_a = 1200

    #성인
    elif state == 'Adults':
        if sex == 'Male':
            vit_a = 900
        else:
            vit_a = 700
            
        #임산부
        if trimester != 0: 
            vit_a = 770
        
        #수유기간
        if postpartum != 0:
            vit_a = 1300
            
    return round(vit_a, 1)

##################################################################

def rec_vita_b6(state, period, sex, trimester = 0, postpartum = 0):
    #mg  
    #영유아기
    if (state == 'Infants') or (state == 'Young Children'):
        #개월별로 나누어 계산
        if 0 <= period <= 6:
            vit_b6 = 0.1 
        elif 7 <= period <= 12:
            vit_b6 = 0.3 
        elif 13 <= period <= 35:
            vit_b6 = 0.5

    #아동, 청소년기        
    elif (state == 'Children') or (state == 'Adolescents'):
        if 3 <= period <= 8:
            vit_b6 = 0.6
        elif 9 <= period <= 13:
            if sex == 'Male':
                vit_b6 = 1.0
            else:
                vit_b6 = 1.0
        elif 14 <= period <= 18:
            if sex == 'Male':
                vit_b6 = 1.3
            else:
                vit_b6 = 1.2
        
        #임산부
        if trimester != 0: 
            vit_b6 = 1.9
        
        #수유기간
        if postpartum != 0:
            vit_b6 = 2.0

    #성인
    elif state == 'Adults':
        if sex == 'Male':
            if 19 <= period <= 30:
                vit_b6 = 1.3
            elif period >= 30:
                vit_b6 = 1.7
        else:
            if 19 <= period <= 30:
                vit_b6 = 1.3
            elif period >= 30:
                vit_b6 = 1.5
            
        #임산부
        if trimester != 0: 
            vit_b6 = 1.9
        
        #수유기간
        if postpartum != 0:
            vit_b6 = 2.0
            
    return round(vit_b6, 1)

##################################################################

def rec_vita_b12(state, period, trimester = 0, postpartum = 0):
    #ug (microgram)  
    #영유아기
    if (state == 'Infants') or (state == 'Young Children'):
        #개월별로 나누어 계산
        if 0 <= period <= 6:
            vit_b12 = 0.4 
        elif 7 <= period <= 12:
            vit_b12 = 0.5 
        elif 13 <= period <= 35:
            vit_b12 = 0.9

    #아동, 청소년기        
    elif (state == 'Children') or (state == 'Adolescents'):
        if 3 <= period <= 8:
            vit_b12 = 1.2
        elif 9 <= period <= 13:
            vit_b12 = 1.8
        elif 14 <= period <= 18:
            vit_b12 = 2.4
        
        #임산부
        if trimester != 0: 
            vit_b12 = 1.9
        
        #수유기간
        if postpartum != 0:
            vit_b12 = 2.0

    #성인
    elif state == 'Adults':
        vit_b12 = 2.4
            
        #임산부
        if trimester != 0: 
            vit_b12 = 2.6
        
        #수유기간
        if postpartum != 0:
            vit_b12 = 2.8
            
    return round(vit_b12, 1)

##################################################################

def rec_vita_c(state, period, sex, trimester = 0, postpartum = 0):
    #mg  
    #영유아기
    if (state == 'Infants') or (state == 'Young Children'):
        #개월별로 나누어 계산
        if 0 <= period <= 6:
            vit_c = 40
        elif 7 <= period <= 12:
            vit_c = 50 
        elif 13 <= period <= 35:
            vit_c = 15

    #아동, 청소년기        
    elif (state == 'Children') or (state == 'Adolescents'):
        if 4 <= period <= 8:
            vit_c = 25
        elif 9 <= period <= 13:
            vit_c = 45
        elif 14 <= period <= 18:
            if sex == "Male":
                vit_c = 75
            else:
                vit_c = 65
        
        #임산부
        if trimester != 0: 
            vit_c = 80
        
        #수유기간
        if postpartum != 0:
            vit_c = 115

    #성인
    elif state == 'Adults':
        if sex == 'Male':
            vit_c = 90
        else:
            vit_c = 75

        #임산부
        if trimester != 0: 
            vit_c = 85
        
        #수유기간
        if postpartum != 0:
            vit_c = 120
            
    return round(vit_c, 1)

##################################################################

def rec_vita_d(state, period, trimester = 0, postpartum = 0):
    #ug  (microgram)
    #영유아기
    if (state == 'Infants') or (state == 'Young Children'):
        #개월별로 나누어 계산
        if 0 <= period <= 12:
            vit_d = 25
        elif 13 <= period <= 35:
            vit_d = 50

    #아동, 청소년기        
    elif (state == 'Children') or (state == 'Adolescents'):
        if 3 <= period <= 18:
            vit_d = 50

    #성인
    elif state == 'Adults':
        vit_d = 50
            
    return round(vit_d, 1)

##################################################################

def rec_ca(state, period, trimester = 0, postpartum = 0):
    #mg
    #영유아기
    if (state == 'Infants') or (state == 'Young Children'):
        #개월별로 나누어 계산
        if 0 <= period <= 6:
            ca = 210
        elif 7 <= period <= 12:
            ca = 270
        elif 13 <= period <= 35:
            ca = 500

    #아동, 청소년기        
    elif (state == 'Children') or (state == 'Adolescents'):
        if 4 <= period <= 8:
            ca = 800
        elif 9 <= period <= 18:
            ca = 1300
        
        #임신기간
        if trimester != 0: 
            ca = 1300
        
        #수유기간
        if postpartum != 0:
            ca = 1300

    #성인
    elif state == 'Adults':
        if 19 <= period <= 50:
            ca = 1000
        elif period >= 51:
            ca = 1200

        #임신기간
        if trimester != 0: 
            ca = 1000
        
        #수유기간
        if postpartum != 0:
            ca = 1000
            
    return round(ca, 1)


##################################################################

def rec_mg(state, period, sex, trimester = 0, postpartum = 0):
    #mg 
    #영유아기
    if (state == 'Infants') or (state == 'Young Children'):
        #개월별로 나누어 계산
        if 0 <= period <= 6:
            mg = 30
        elif 7 <= 75 <= 12:
            mg = 75
        elif 13 <= period <= 35:
            mg = 80

    #아동, 청소년기        
    elif (state == 'Children') or (state == 'Adolescents'):
        if 4 <= period <= 8:
            mg = 130
        elif 9 <= period <= 13:
            mg = 240
        elif 14 <= period <= 18:
            if sex == 'Male':
                mg = 410
            else:
                mg = 360
        
        #임신기간
        if trimester != 0: 
            mg = 400
        
        #수유기간
        if postpartum != 0:
            mg = 360

    #성인
    elif state == 'Adults':
        if 19 <= period <= 30:
            if sex == "Male":
                mg = 400
            else:
                mg = 420

            #임신기간
            if trimester != 0:
                mg = 350
            #수유기간
            if postpartum != 0:
                mg = 310

        elif period >= 31:
            if sex == "Male":
                mg = 420
            else:
                mg = 320

            #임신기간
            if trimester != 0: 
                mg = 360
            
            #수유기간
            if postpartum != 0:
                mg = 320
            
    return round(mg, 1)

##################################################################

def rec_na(state, period, trimester = 0, postpartum = 0):
    #g 
    #영유아기
    if (state == 'Infants') or (state == 'Young Children'):
        #개월별로 나누어 계산
        if 0 <= period <= 6:
            na = 0.12
        elif 7 <= 75 <= 12:
            na = 0.37
        elif 13 <= period <= 35:
            na = 1.0

    #아동, 청소년기        
    elif (state == 'Children') or (state == 'Adolescents'):
        if 4 <= period <= 8:
            na = 1.2
        elif 9 <= period <= 18:
            na = 1.5

    #성인
    elif state == 'Adults':
        if 19 <= period <= 50:
            na = 1.5

        elif 51 <= period <= 70:
            na = 1.3

        elif period > 70:
            na = 1.2
            
    return round(na, 1)

##################################################################

def rec_cl(state, period, trimester = 0, postpartum = 0):
    #g 
    #영유아기
    if (state == 'Infants') or (state == 'Young Children'):
        #개월별로 나누어 계산
        if 0 <= period <= 6:
            na = 0.18
        elif 7 <= 75 <= 12:
            na = 0.57
        elif 13 <= period <= 35:
            na = 1.5

    #아동, 청소년기         
    elif (state == 'Children') or (state == 'Adolescents'):
        if 4 <= period <= 8:
            na = 1.9
        elif 9 <= period <= 18:
            na = 2.3

    #성인
    elif state == 'Adults':
        if 19 <= period <= 50:
            na = 2.3

        elif 51 <= period <= 70:
            na = 2.0

        elif period > 70:
            na = 1.8
            
    return round(na, 1)

##################################################################

def rec_p(state, period, trimester = 0, postpartum = 0):
    #mg  
    #영유아기
    if (state == 'Infants') or (state == 'Young Children'):
        #개월별로 나누어 계산
        if 0 <= period <= 6:
            p = 100
        elif 7 <= period <= 12:
            p = 275 
        elif 13 <= period <= 35:
            p = 460

    #아동, 청소년기        
    elif (state == 'Children') or (state == 'Adolescents'):
        if 4 <= period <= 8:
            p = 400
        elif 9 <= period <= 18:
            p = 1250

    #성인
    elif state == 'Adults':
        p = 700
            
    return round(p, 1)


##################################################################

def rec_k(state, period, trimester = 0, postpartum = 0):
    #mg  
    #영유아기
    if (state == 'Infants') or (state == 'Young Children'):
        #개월별로 나누어 계산
        if 0 <= period <= 6:
            k = 0.4
        elif 7 <= period <= 12:
            k = 0.7 
        elif 13 <= period <= 35:
            k = 3.0

    #아동, 청소년기        
    elif (state == 'Children') or (state == 'Adolescents'):
        if 4 <= period <= 8:
            k = 3.8
        elif 9 <= period <= 13:
            k = 4.5
        elif 14 <= period <= 18:
            k = 4.7

        if postpartum != 0:
            k = 5.1

    #성인
    elif state == 'Adults':
        k = 4.7

        if postpartum != 0:
            k = 5.1
            
    return round(k, 1)

##################################################################

