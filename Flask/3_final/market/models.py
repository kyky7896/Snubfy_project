# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.schema import FetchedValue
from market import db

class Cart(db.Model):
    __tablename__ = 'cart'

    cart_num = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.ForeignKey('member.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    cart_date = db.Column(db.DateTime, server_default=db.FetchedValue())
    product_id = db.Column(db.ForeignKey('product.product_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    cart_amount = db.Column(db.Integer, nullable=False)

    member = db.relationship('Member', primaryjoin='Cart.id == Member.id')


class Member(db.Model):
    __tablename__ = 'member'

    id = db.Column(db.String(20, 'utf8_unicode_ci'), primary_key=True)
    pwd = db.Column(db.String(255, 'utf8_unicode_ci'), nullable=False)
    name = db.Column(db.String(20, 'utf8_unicode_ci'), nullable=False)
    rnum = db.Column(db.String(20, 'utf8_unicode_ci'), nullable=False, unique=True)
    gender = db.Column(db.String(20, 'utf8_unicode_ci'), nullable=False)
    address1 = db.Column(db.Text(collation='utf8_unicode_ci'), nullable=False)
    address2 = db.Column(db.Text(collation='utf8_unicode_ci'), nullable=False)
    phnum = db.Column(db.String(20, 'utf8_unicode_ci'), nullable=False, unique=True)
    email = db.Column(db.String(50, 'utf8_unicode_ci'), unique=True)
    admin = db.Column(db.String(20, 'utf8_unicode_ci'), nullable=False)


class Nutrient(db.Model):
    __tablename__ = 'nutrient'

    product_id = db.Column(db.ForeignKey('product.product_id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
    energy = db.Column(db.Float, server_default=db.FetchedValue())
    carbohd = db.Column(db.Float, server_default=db.FetchedValue())
    sugar = db.Column(db.Float, server_default=db.FetchedValue())
    protein = db.Column(db.Float, server_default=db.FetchedValue())
    fat = db.Column(db.Float, server_default=db.FetchedValue())
    water = db.Column(db.Float, server_default=db.FetchedValue())
    vit_a = db.Column(db.Float, server_default=db.FetchedValue())
    vit_b6 = db.Column(db.Float, server_default=db.FetchedValue())
    vit_b12 = db.Column(db.Float, server_default=db.FetchedValue())
    vit_c = db.Column(db.Float, server_default=db.FetchedValue())
    vit_d = db.Column(db.Float, server_default=db.FetchedValue())
    ca = db.Column(db.Float, server_default=db.FetchedValue())
    na = db.Column(db.Float, server_default=db.FetchedValue())
    p = db.Column(db.Float, server_default=db.FetchedValue())
    k = db.Column(db.Float, server_default=db.FetchedValue())
    cl = db.Column(db.Float, server_default=db.FetchedValue())
    mg = db.Column(db.Float, server_default=db.FetchedValue())

    ####### 수정함 ########
    # product = db.relationship('Product', primaryjoin='Nutrient.product_id == Product.product_id', back_populates='nutrient')


class OrderDetail(db.Model):
    __tablename__ = 'order_detail'

    order_detail_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.ForeignKey('orders.order_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    pamount = db.Column(db.Integer, nullable=False)
    product_id = db.Column(db.ForeignKey('product.product_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    reorder = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())

    # order = db.relationship('Order', primaryjoin='OrderDetail.order_id == Order.order_id')
    product = db.relationship('Product', primaryjoin='OrderDetail.product_id == Product.product_id', backref='order_detail')


class Order(db.Model):
    __tablename__ = 'orders'

    order_id = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.ForeignKey('member.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    card_com = db.Column(db.String(30, 'utf8_unicode_ci'), nullable=False)
    card_num = db.Column(db.Integer, nullable=False)
    ex_date = db.Column(db.String(10, 'utf8_unicode_ci'), nullable=False)

    #추가
    order_detail = db.relationship('OrderDetail', primaryjoin='OrderDetail.order_id == Order.order_id', backref='order')
    member = db.relationship('Member', primaryjoin='Order.id == Member.id')

    def __repr__(self):
        return "<Order('%s', '%s', '%s', '%s','%s')>" % (self.order_id, self.id, self.card_com, self.card_num, self.card_num)


class Product(db.Model):
    __tablename__ = 'product'

    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.Text(collation='utf8_unicode_ci'), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    detail = db.Column(db.Text(collation='utf8_unicode_ci'), nullable=False)
    image = db.Column(db.Text(collation='utf8_unicode_ci'), nullable=False)
    ingred_id = db.Column(db.ForeignKey('ingredients.ingred_id', ondelete='CASCADE', onupdate='CASCADE'), index=True)

    #추가
    categories = db.relationship('Category', primaryjoin='Product.product_id==Category.product_id', backref='product')
    nutrient=db.relationship('Nutrient', primaryjoin='Nutrient.product_id == Product.product_id', backref='product')
    ingredient=db.relationship('Ingredient', primaryjoin='Ingredient.ingred_id == Product.ingred_id', backref='product')
    cart = db.relationship('Cart', primaryjoin='Product.product_id==Cart.product_id', backref='product')

    def __repr__(self):
        return "<Product('%s', '%s', '%d', '%s','%s')>" % (self.product_id, self.product_name, self.price, self.detail, self.image)

class Category(Product):
    __tablename__ = 'category'

    cart_num = db.Column(db.Integer, nullable=False)
    aisle_id = db.Column(db.Integer, nullable=False)
    aisle = db.Column(db.String(50, 'utf8_unicode_ci'), nullable=False)
    department = db.Column(db.String(50, 'utf8_unicode_ci'), nullable=False)
    category = db.Column(db.String(50, 'utf8_unicode_ci'), nullable=False)
    product_id = db.Column(db.ForeignKey('product.product_id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)

class Recipe(db.Model):
    __tablename__ = 'recipe'

    recipe_id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.Text(collation='utf8_unicode_ci'), nullable=False)
    minutes = db.Column(db.Integer, nullable=False)
    steps = db.Column(db.Text(collation='utf8_unicode_ci'), nullable=False)
    recipe_image = db.Column(db.Text(collation='utf8_unicode_ci'))

class RecipeIngredient(db.Model):
    __tablename__ = 'recipe_ingredient'

    re_in_num = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.ForeignKey('recipe.recipe_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    ingred_id = db.Column(db.ForeignKey('ingredients.ingred_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)

    ingred = db.relationship('Ingredient', primaryjoin='RecipeIngredient.ingred_id == Ingredient.ingred_id', backref='recipe_ingredients')
    recipe = db.relationship('Recipe', primaryjoin='RecipeIngredient.recipe_id == Recipe.recipe_id', backref='recipe_ingredients')

class Ingredient(db.Model):
    __tablename__ = 'ingredients'

    ingred_id = db.Column(db.Integer, primary_key=True)
    ingred_name = db.Column(db.String(50, 'utf8_unicode_ci'), nullable=False)

