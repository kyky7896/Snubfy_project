from market.data.rec_nutrient import rec_EER, rec_carbonhydrate, rec_protein, rec_water, rec_vita_a, rec_vita_b6, rec_vita_b12, rec_vita_c, rec_vita_d, rec_ca, rec_mg, rec_na, rec_cl, rec_p, rec_k
import numpy as np
import pymysql


# 수정해야할 정보
conn_db = pymysql.connect(
    user = 'root',
    passwd = '12345678',
    host = '127.0.0.1',
    db = 'market',
    charset = 'utf8'
)

cursor = conn_db.cursor(pymysql.cursors.DictCursor)

class User_Nutrient:
    def __init__(self, state, period, sex, height, weight, activity, trimester = 0, postpartum = 0):
        self.state = state
        self.period = period
        self.sex = sex
        self.height = height
        self.weight = weight
        self.activity = activity
        self.trimester = trimester
        self.postpartum = postpartum

    #권장 섭취 영양소 계산호출
    def get_nutrient(self):

        energy = rec_EER(self.state, self.period, self.sex, self.height, self.weight, self.activity, self.trimester, self.postpartum) #칼로리 ( = 탄수화물(g) * 4 + 단백질(g) * 4 + 지방(g) * 9)
        carbohd = rec_carbonhydrate(self.state, self.period, self.trimester, self.postpartum) #탄수화물
        protein = rec_protein(self.state, self.period, self.weight, self.trimester, self.postpartum) #단백질
        water = rec_water(self.state, self.period, self.sex, self.weight, self.trimester, self.postpartum) #물
        vit_a = rec_vita_a(self.state, self.period, self.sex, self.trimester, self.postpartum) #비타민 A
        vit_b6 = rec_vita_b6(self.state, self.period, self.sex, self.trimester, self.postpartum) #비타민 B-6
        vit_b12 = rec_vita_b12(self.state, self.period, self.trimester, self.postpartum) #비타민 B-12
        vit_c = rec_vita_c(self.state, self.period, self.sex, self.trimester, self.postpartum) #비타민 C
        vit_d = rec_vita_d(self.state, self.period, self.trimester, self.postpartum) #비타민 D
        ca = rec_ca(self.state, self.period, self.trimester, self.postpartum) #칼슘
        na = rec_na(self.state, self.period, self.trimester, self.postpartum) #나트륨
        p = rec_p(self.state, self.period, self.trimester, self.postpartum) #인
        k = rec_k(self.state, self.period, self.trimester, self.postpartum) #칼륨
        cl = rec_cl(self.state, self.period, self.trimester, self.postpartum) #염소
        mg = rec_mg(self.state, self.period, self.sex, self.trimester, self.postpartum) #마그네슘

        return np.array([energy, carbohd, protein, water, vit_a, vit_b6, vit_b12, vit_c, vit_d, ca, na, p, k, cl, mg])

    #############################################################################

    def nutrient_percent(self, user_id): # 유저의 권장 섭취량과 유저의 id를 받아 장바구니에 담긴 상품의 영양소를 array로 넣는다.
        #user_nut에는 Class 호출시 만든 유저의 정보(예를 들면 user1 = User_Nutrient('Adults', 32, 'Male', 169, 55, 'Low Active', 0, 0))를 변수로 한 user1.get_nutrient()를 기입
        #user_id에는 sql DB에서 가져올 유저의 id

        #유저의 id로 카트에 담긴 상품의 영양소 정보 끌어오기 프로시저로 만들어봄..
        #-----------------------------------------
        # DROP PROCEDURE IF EXISTS cart_nutrient;

        # DELIMITER $$
        # CREATE PROCEDURE cart_nutrient (
        #     IN user_id INT)
        # BEGIN
        #     SELECT nutrient.* FROM nutrient
        #     JOIN product ON nutrient.product_id=product.product_id
        #     JOIN cart ON cart.product_id=product.product_id
        #     WHERE cart.id = user_id;
        # END $$
        # DELIMITER ;

        # CALL cart_nutrient(112108);
        #-------------------------------------------

        qry = '''
                 SELECT * FROM nutrient
                    INNER JOIN product ON  nutrient.product_id=product.product_id
                    INNER JOIN cart ON cart.product_id=product.product_id
                    WHERE cart.id = {};
        '''.format(user_id)

        # qry = "CALL cart_nutrient({});"
        cursor.execute(qry)

        result = cursor.fetchall()

        cart_nut = []

        for r in result:# p_id, energy, carbohd, sugar, protein, fat, water, va, vb6, vb12, vc, vd, ca, na, p, k, cl, mg
            cart_nut.append(np.array([r['energy'], r['carbohd'], r['protein'], r['water']/1000, r['vit_a'], r['vit_b6'], r['vit_b12'], r['vit_c'], r['vit_d']/40, r['ca'], r['na']/1000, r['p'], r['k']/1000, r['cl']/1000, r['mg']]))

        #카트에 담긴 영양소의 합을 계산
        cart_nut = sum(cart_nut)
 
        diff_nu = self.get_nutrient() - cart_nut #유저의 권장 영양소와 카트에 담긴 상품의 영양소 차이
        percent_nu = (diff_nu/self.get_nutrient()) * 100 #유저 권장 영양소 백분율
        
        per_energy = round(percent_nu[0], 1)
        per_carbohd = round(percent_nu[1], 1)
        per_protein = round(percent_nu[2], 1)
        per_water = round(percent_nu[3], 1)
        per_vita = round(percent_nu[4], 1)
        per_vitb6 = round(percent_nu[5], 1)
        per_vitb12 = round(percent_nu[6], 1)
        per_vitc = round(percent_nu[7], 1)
        per_vitd = round(percent_nu[8], 1)
        per_ca = round(percent_nu[9], 1)
        per_na = round(percent_nu[10], 1)
        per_p = round(percent_nu[11], 1)
        per_k = round(percent_nu[12], 1)
        per_cl = round(percent_nu[13], 1)
        per_mg = round(percent_nu[14], 1)

        return np.array([per_energy, per_carbohd, per_protein, per_water, per_vita, per_vitb6, per_vitb12, per_vitc, per_vitd, per_ca, per_na, per_p, per_k, per_cl, per_mg])

    #############################################################################
    # 유저의 아이디와 권장 영양소의 부족한 양(퍼센트) 정보를 가져와 상품을 추천해줌.
    def rec_product(self, user_id):
        #per_nu는 각 영양소의 부족한 정도(퍼센트 정보) np.array로 받아옴
        #예를 들면, user1.nutrient_percent(user_id)

        percent_nu = self.nutrient_percent(user_id)

        nu = ['energy', 'carbohd', 'protein', 'water', 'vit_a', 'vit_b6', 'vit_b12', 'vit_c', 'vit_d', 'ca', 'na', 'p', 'k', 'cl', 'mg']

        cond = ''

        for idx in range(len(percent_nu)):
            if percent_nu[idx] > 0:
                if cond != '':
                    cond += ' AND '
                    cond += nu[idx] + '!= 0'
                else:
                    cond += nu[idx] + '!= 0'

        qry = '''
        SELECT * FROM product A WHERE A.product_id IN (SELECT B.product_id FROM nutrient B WHERE B.{});
        '''.format(cond)

        cursor.execute(qry)

        result = cursor.fetchmany(9)

        return result