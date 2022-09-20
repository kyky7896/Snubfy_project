from market import db
from flask import Blueprint, url_for, render_template, flash, session, request, g
from market.member_form import LoginForm, SignupForm
from market.models import Member, Order
from werkzeug.utils import redirect
from werkzeug.security import generate_password_hash
from flask_login import logout_user
# @login_required적용을 위한 import
# from pybo.views.auth_views import login_required
import functools

bp=Blueprint('member', __name__, url_prefix='/member')

@bp.route('/login/', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        error = None
        member = Member.query.filter_by(id=form.id.data).first()

        if not member:
            error = "존재하지 않는 사용자입니다."

        if error is None:
            session.clear()
            session['member_id'] = member.id
            return redirect(url_for('header_footer.main'))
        flash(error)

        db.session.flush()
    return render_template('html/member/login.html', form=form)

#로그아웃 기능
@bp.route('/logout/')
def logout_page():
    session.clear()
    flash("로그아웃이 완료되었습니다")
    # 특정 주소로 접속. 주소에서 데이터를 처리하는 과정만 거치고 결과를 보여주거나 응용할 때 사용
    return redirect(url_for('header_footer.main'))

# 회원가입
#### 연동 나중에 확인하기
@bp.route('/signup/', methods = ['GET', 'POST'])
def signup():
    form = SignupForm()
    # 사용자가 submit 버튼을 눌렀는지 확인용
    # 유효성 검사 : 회원가입 조건을 충족하는지
    if request.method == 'POST' and form.validate_on_submit():
        print(form.id.data,"받아오나")
        member = Member.query.filter_by(id = form.id.data).first()
        print(member)
        if not member:
            print("회원가입해라!")
            # 회원가입에 필요한 인수
            member_to_create = Member(name = form.name.data,
                                      id = form.id.data,
                                      pwd = generate_password_hash(form.pwd.data),   # password.setter로 넘어가 비밀번호를 암호로 decode한 후 저장
                                      gender = form.gender.data,
                                      rnum = form.rnum.data,
                                      phnum = form.phnum.data,
                                      address1 = form.address_1.data,
                                      address2 = form.address_2.data,
                                      email = form.email.data,
                                      admin = form.admin.data)
            print("create",member_to_create)
            db.session.add(member_to_create)
            db.session.commit()
            db.session.close()


            # 다른 페이지로 넘어감
            # 연결되는 url을 하드코딩하는 것은 좋지 않기 때문에 route 자체를 url 자리에 넣어줌
            return redirect(url_for('member.login'))

        else: #사용자
            flash("이미 존재하는 사용자입니다.")
            return

    return render_template('html/member/signup.html', form=form)


# 이 에너테이션이 적용된 함수는 라우팅 함수보다 항상 먼저 실행됨
@bp.before_app_request
def load_logged_in_user():
    user_id=session.get('member_id')
    if user_id is None:
        #g는 플라스크 컨텍스트 변수
        g.user=None
    else:
        # session 변수에 user_id값이 있으면 db에서 사용자 조회해서 g.user에 저장
        # 이러면 세션을 조사할 필요가 없고. g.user에 값이 있는지 확인하면 됨.
        g.user=Member.query.get(user_id) #user의 객체가 저장됨.

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(*args, **kwargs):
        if g.user is None:
            # get인 경우에 원래 가려던 페이지로 다시 찾아갈수 있도록
            # 로그인 페이지에 next파라미터 전달
            _next=request.url if request.method =='GET' else ''
            return redirect(url_for('member.login', next=_next))
        return view(*args, **kwargs)
    return wrapped_view


@bp.route('/mypage/myorder/', methods=['GET'])
@login_required
def myorder():
    order_list=Order.query.filter_by(id=g.user.id).order_by(Order.order_id.desc()).all()
    print(order_list)
    if not order_list:
        error="주문내역이 없습니다."
        return render_template('html/member/mypage_orderlist.html', order_list=order_list , error=error)
    return render_template('html/member/mypage_orderlist.html', order_list=order_list)

@bp.route('/mypage/myorder/<int:order_num>/', methods=['GET'])
@login_required
def myorderdetail(order_num):
    orders=Order.query.get_or_404(order_num)
    return render_template('html/member/mypage_orderdetail.html', orders=orders)
