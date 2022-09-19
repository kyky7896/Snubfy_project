from flask import Blueprint, render_template, request, redirect, session, flash, url_for,g
from market.models import Cart, Product, Member
from market.views.member_views import login_required
from market.data.user_nutrient import User_Nutrient as un
import datetime


bp = Blueprint('cart', __name__, url_prefix='/cart')

@bp.route('/mycart/', methods=['GET'])
@login_required
def mycart():
    cart_list=Cart.query.filter_by(id=g.user.id).order_by(Cart.cart_num.desc()).all()

    # user 1에 대한 영양소 정보
    # 추후 업데이트 예정
    user1 = un('Adults', 26, 'Female', 169, 55, 'Low Active', 0, 0)
    user1_n_prct = user1.nutrient_percent(245)
    user1_rec_prdc = user1.rec_product(245)

    # 상품 가격 계산
    price_list = []
    cart_prod_p = 0
    for item in cart_list:
        price_list.append(item.product.price * item.cart_amount)

    for price in range(len(price_list)):
            cart_prod_p += price_list[price]

    # 배송비 10$ 더한 총 가격 계산
    cart_prod_tot_p = cart_prod_p + 10

    return render_template('html/cart/cart.html', cart_list=cart_list,
                                                    user1_n_prct=user1_n_prct,
                                                    user1_rec_prdc=user1_rec_prdc,
                                                    cart_prod_p=cart_prod_p,
                                                    cart_prod_tot_p=cart_prod_tot_p)

@bp.route('/order_product/', methods=['GET'])
@login_required
def order_product():
    cart_list=Cart.query.filter_by(id=g.user.id).order_by(Cart.cart_num.desc()).all()

    # 상품 가격 계산
    price_list = []
    cart_prod_p = 0
    for item in cart_list:
        price_list.append(item.product.price * item.cart_amount)

    for price in range(len(price_list)):
        cart_prod_p += price_list[price]

    # 배송비 10$ 더한 총 가격 계산
    cart_prod_tot_p = cart_prod_p + 10

    return render_template('html/cart/order.html', cart_list=cart_list,
                                                   cart_prod_p=cart_prod_p,
                                                   cart_prod_tot_p=cart_prod_tot_p)

