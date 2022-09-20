from flask import Blueprint, url_for, render_template, g
from werkzeug.utils import redirect
from market.models import Product, Order, OrderDetail
from gensim.models import word2vec
from gensim.models import KeyedVectors
from market.data import main_recomm
from market.data import main_noorder_recomm
import joblib

### 블루프린트의 별칭 url_for함수에 사용하게 될 것.
### url_prefix : 접두어
### __name__ 모듈명인 "main_views"로 인수가 전달됨.
bp=Blueprint('header_footer', __name__, url_prefix='/')

@bp.route('/')
def main():
    #### best 모델 : 공통
    product_top9 = main_recomm.rec_product(9)
    product_list = []
    for pro_9 in product_top9:
        products = Product.query.filter_by(product_name=pro_9).first()
        product_list.append(products)

    ### 로그인 시, 신규회원 / 기존회원을 위한 개인 추천 시스템 동작.
    if g.user:
        ### Order와 OrderDetail, Product 조인 : 주문목록 불러오기 위한 준비
        join_all=Order.query\
                .join(OrderDetail, Order.order_id==OrderDetail.order_id)\
                .join(Product, Product.product_id==OrderDetail.product_id)\
                .add_columns(Product.product_name)\
                .filter(Order.id==g.user.id)

        ### 회원의 주문목록 불러오기
        join_lists=[]
        for join in join_all:
            join_lists.append(join.product_name)

        if join_lists : ####### 주문목록이 있는경우 : 기존회원의 경우
            title = "It's for you"
            embedding_model = joblib.load('market/data/word2vec_pickle.pkl')
            model=embedding_model.wv.most_similar(positive=join_lists, topn=9)
            prod_reco_list=[]
            for m in model:
                product=Product.query.filter_by(product_name=m[0]).first()
                prod_reco_list.append(product)

            return render_template('html/header_footer/main.html', product_list=product_list,
                                                                    prod_reco_list=prod_reco_list,
                                                                    title=title)
        else : ### 주문목록이 없는경우 : 신규회원의 경우
            title="Hot Deal"
            ## vegetable 쪽 할인한다고 가정하고 제품 추천!
            product_vegi_9=main_noorder_recomm.rec_product(9)
            product_vegi_list = []
            for pro_9 in product_vegi_9:
                products = Product.query.filter_by(product_id=pro_9).first()
                product_vegi_list.append(products)
            return render_template('html/header_footer/main.html', product_list=product_list,
                                                                    prod_reco_list=product_vegi_list,
                                                                    title=title)

    else: #로그인 안했을때는 top9만 돌아가게 설정
        return render_template('html/header_footer/main.html', product_list=product_list)