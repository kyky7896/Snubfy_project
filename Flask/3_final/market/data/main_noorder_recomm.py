import random
import pandas as pd

def rec_product(n_items):
    data = pd.read_csv('market/data/category_data_test.csv')
    product_count = data['product_id'].value_counts().to_frame()
    product_count = product_count.reset_index().rename(columns = {"index":"product_id","product_id":"count","count":"category"})
    change_data = pd.merge(data, product_count, on = "product_id")
    df = change_data.drop(columns=['add_to_cart_order','department_id','order_id','user_id','eval_set',
                        'order_number','order_dow','order_hour_of_day','days_since_prior_order','aisle','department'], axis=1)
    df = df.drop_duplicates()
    final_df = df[(df['category'] == 'fresh vegetables organic')|(df['category'] == 'fresh vegetables')|(df['category'] == 'fresh fruits organic')|(df['category'] == 'fresh fruits')]
    data_top30 = list(set(final_df['product_id']))
    top_sample = random.sample(data_top30, k=n_items)
    return top_sample