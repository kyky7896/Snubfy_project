from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField, IntegerField, SubmitField, SelectField,RadioField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
from market.models import Member

class ProductForm(FlaskForm):
    product_name=StringField('product_name', validators=[DataRequired()])
    price=IntegerField('price', validators=[DataRequired()])
    detail=StringField('detail', validators=[DataRequired()])
    image=StringField('image', validators=[DataRequired()])
    cart_num=SelectField('cart_num', choices=[(1, 'snacks'),(2, 'dairy eggs'),(3, 'frozen'),(4, 'beverages'),
                                              (5, 'pantry'),(6, 'produce'),(7, 'bakery'),(8, 'canned goods'),
                                              (9, 'dry goods pasta'),(10, 'deli'),(11, 'breakfast'),(12, 'meat seafood'),
                                              (13, 'babies'),(14, 'international'),(15, 'alcohol'),(16, 'personal care'),
                                              (17, 'bulk')] ,validators=[DataRequired()], coerce=int)

#class CartForm(FlaskForm):


class LoginForm(FlaskForm):
    id = StringField('사용자이름', validators=[DataRequired()])
    pwd = PasswordField('비밀번호', validators=[DataRequired()])

# 회원가입 form
class SignupForm(FlaskForm):

    # 회원가입시 id가 겹치면 생기는 IntegrityError 해결 -> id가 겹칠 시 처리방법
    # id를 입력하면, FlaskForm이 StringField 내의 id를 모두 검사 -> validation 조건을 확인 -> 중복 여부 판단
    # def validate_id(self, id_to_check):
    #     # 같은 id가 이미 존재
    #     id = Member.query.filter_by(id=id_to_check.data).first()
    #     if id:
    #         raise ValidationError('이미 존재하는 ID입니다.')
    #
    # def validate_rnum(self, rnum_to_check):
    #     # 같은 주민번호가 이미 존재
    #     rnum = Member.query.filter_by(rnum=rnum_to_check.data).first()
    #     if rnum:
    #         raise ValidationError('이미 등록된 주민번호입니다.')
    #
    # def validtae_phnum(self, phnum_to_check):
    #     phnum = Member.query.filter_by(phnum=phnum_to_check.data).first()
    #     if phnum:
    #         raise ValidationError('이미 존재하는 전화번호입니다.')
    #
    # def validate_email(self, email_to_check):
    #     email = Member.query.filter_by(email=email_to_check.data).first()
    #     if email:
    #         raise ValidationError('이미 존재하는 메일입니다.')


    id = StringField('id', validators=[Length(min=2, max=20), DataRequired()])
    pwd = PasswordField('pwd', validators=[Length(min=3), DataRequired()])   # 만들 패스워드
    # 올바르게 입력했는지 확인용, pwd1과 일치하는지 확인
    pwdcheck = PasswordField('pwdcheck',validators=[EqualTo('pwd'), DataRequired()])
    name = StringField('name')
    gender = StringField('gender')
    address_1=StringField('address_1')
    address_2=StringField('address_2')
    rnum = StringField('rnum')
    phnum = StringField('phnum')
    email = EmailField('email', validators=[Email(), DataRequired()])
    gender = RadioField('gender', choices=[('female','gender'),('male','gender')], default='male')
    admin = RadioField('admin', choices=[('administer','admin'),('member','admin')], default='member')
    # submit = SubmitField(label='Create Account')   # 작성한 개인정보 제출
