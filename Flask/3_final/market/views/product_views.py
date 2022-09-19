
from flask import Blueprint, render_template, request, url_for, g, flash
from werkzeug.utils import redirect, secure_filename
import os

from market import db, app
from market.models import Product, Category
from market.member_form import ProductForm
# @login_required적용을 위한 import
from market.views.member_views import login_required
# 추천상품
from market.data.product_recomm import recommend_product
import pandas as pd

bp=Blueprint('product', __name__, url_prefix='/product')

category_set=['snacks', 'dairy eggs', 'frozen','beverages',
'pantry','produce','bakery','canned goods','dry goods pasta','deli', 'breakfast', 'meat seafood',
 'babies', 'international', 'alcohol', 'personal care','bulk']

@bp.route('/create/', methods=['GET','POST'])
@login_required
def create():
    form=ProductForm()
    if request.method =='POST':
        f=request.files['image']
        fn=secure_filename(f.filename)
        # 동일한 파일명이 있을때
        if os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], fn)) :
            fn_split = fn.split('.')  # .jpg뒤에 0, 1이 붙지 않기위해 파싱
            # 이미지 저장
            _ = 0
            while os.path.isfile(app.config['UPLOAD_FOLDER'] + fn): #같은 파일명을 찾아서
                fn = fn_split[0] + '_' + str(_) + '.' + fn_split[1]
                _ += 1
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], fn))
        #동일한 파일명 없을때는 그냥 저장해주기
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], fn))
        print(form.product_name.data, "//" , form.price.data, "//", form.detail.data, "//", secure_filename(f.filename))

        param={'product_name': form.product_name.data,
         'price': form.price.data,
         'detail': form.detail.data,
         'image': secure_filename(f.filename),
         'cart_num':form.cart_num.data}
        # 프로시저 mysql에 직접 불러서 사용
        db.session.execute("call user_proc_1(:product_name, :price, :detail, :image, :cart_num)", param)
        db.session.commit()
        return redirect(url_for('header_footer.main'))
    return render_template('html/product/product_create.html', form=form,
                                                                category_set=category_set)

@bp.route('/list/<int:cart_num>')
def _list(cart_num):
    # 카테고리에서 10개만 필터링함
    category=Category.query.filter_by(cart_num=cart_num).order_by(Category.aisle_id.asc())[0:9]
    small_cat=Category.query.filter_by(cart_num=cart_num).group_by(Category.aisle_id).order_by(Category.aisle_id.asc())
    return render_template('html/product/product_list.html', category=category, small_cat=small_cat)

@bp.route('/list/<int:cart_num>/<int:aisle_id>')
def aisle_list(cart_num, aisle_id):
    if aisle_id != 'None':
        category = Category.query.filter_by(cart_num=cart_num, aisle_id=aisle_id)[0:9] # .order_by(Category.product_id.asc())[0:9]
        small_cat = Category.query.filter_by(cart_num=cart_num).group_by(Category.aisle_id).order_by(Category.aisle_id.asc())
    return render_template('html/product/product_list.html', category=category, small_cat=small_cat)

@bp.route('/detail/<int:product_id>')
def detail(product_id):
    product=Product.query.get_or_404(product_id)
    #함께 구매한 제품
    recomm_product=recommend_product(product_id)
    product_list=[]
    for product_id in recomm_product:
        prod=Product.query.filter_by(product_id=product_id).first()
        product_list.append(prod)
    return render_template('html/product/product_detail.html', product=product, recomm_product=product_list)

@bp.route('/update/<int:product_id>', methods=['GET','POST'])
@login_required
def update(product_id):
    product=Product.query.get_or_404(product_id)
    prev_image=product.image # 이전 파일명 저장
    category=Category.query.get_or_404(product_id)
    if g.user.admin != 'administer':
        flash('수정 권한이 없습니다.')
        return redirect(url_for('product.detail', product_id=product_id))
    if request.method == 'POST':
        form=ProductForm()
        if form.validate_on_submit():
            form.populate_obj(product)
            f = request.files['image']
            fn = secure_filename(f.filename) # 있는경우 = 사진을 바꾸려고 한 경우임
            ##### 이미지 수정시 로직
            ##### 1. 이미지 그대로 나뒀을때 => 수정하지 않겠다는 뜻 (데이터 수정하지 않음)
            ##### 2. 이미지 바꾼경우        => 1) 기존 이미지를 동일한 걸로 바꿈 : 삭제하고 기존 업로드처럼 진행
                                                ## create에서 중복파일이 없게끔 _01 붙여서 저장했기 때문에 삭제가능.
            #####                              2) 새로운 이미지 업로드 : 삭제하고 기존 업로드로 진행
            if fn: # 이미지가 넘어온경우 = 이미지 바꾼경우임
                # 이미지 바꾼경우 : 이전이랑 다른 이미지 인데도 동일한 파일명이 있는경우 : 이전파일 삭제후 새파일저장

                os.remove(app.config['UPLOAD_FOLDER'] + secure_filename(prev_image)) # 이전 파일을 삭제하고
                f.save(os.path.join(app.config['UPLOAD_FOLDER'] + fn)) # 새로운 파일을 다시 저장한다
                # product 수정
                product=Product.query.filter_by(product_id=product_id).first()
                product.product_name=form.product_name.data
                product.detail=form.detail.data
                product.price=form.price.data
                product.image=secure_filename(fn)
                # 다른 테이블(cate)에 있는 카테고리넘버 수정 : on update cascade로 자동수정되지않나?
                category=Category.query.filter_by(product_id=product_id).first()
                category.cart_num=form.cart_num.data
                db.session.commit()
                db.session.close()

        else: # 이미지는 수정하지 않겠다는 경우 : 현상유지
            # product 수정
            product = Product.query.filter_by(product_id=product_id).first()
            product.product_name = form.product_name.data
            product.detail = form.detail.data
            product.price = form.price.data
            # 다른 테이블(cate)에 있는 카테고리넘버 수정
            category=Category.query.filter_by(product_id=product_id).first()
            category.cart_num=form.cart_num.data
            db.session.commit()
            db.session.close()
        return redirect( url_for('product.detail', product_id=product_id))
    else:
        form=ProductForm(obj=product)
    return render_template('html/product/product_update.html', form=form,
                                                                product=product,
                                                                category=category,
                                                                category_set=category_set)

@bp.route('/delete/<int:product_id>')
@login_required
def delete(product_id):
    product=Product.query.get_or_404(product_id)
    if g.user.admin != 'administer':
        flash('삭제 권한이 없습니다')
        return redirect(url_for('product.detail', product_id=product_id))
    db.session.delete(product)
    db.session.commit()
    db.session.close()
    return redirect(url_for('header_footer.index'))