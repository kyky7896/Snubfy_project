
from flask import Blueprint, render_template, request, url_for, g, flash
from werkzeug.utils import redirect, secure_filename
import os

from market import db
from market.models import Recipe, RecipeIngredient, Ingredient
# @login_required적용을 위한 import
from market.views.member_views import login_required

bp=Blueprint('recipe', __name__, url_prefix='/recipe')

@bp.route('/list/')
def recipe_list():
    recipe_list=Recipe.query.order_by(Recipe.recipe_id.asc()).all()[0:12]
    return render_template('html/recipe/recipe_list.html', recipe_list=recipe_list)

@bp.route('/detail/<int:recipe_id>')
def recipe_detail(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)

    return render_template('html/recipe/recipe_detail.html', recipe=recipe)