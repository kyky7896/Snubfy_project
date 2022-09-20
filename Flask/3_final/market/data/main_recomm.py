import random
import pandas as pd
def rec_product(n_items):
    data=pd.read_csv('market/data/category_data_test.csv')
    product_count = data['product_name'].value_counts().to_frame()
    product_count = product_count.reset_index().rename(columns = {"index":"product_name","product_name":"count","count":"category"})

    change_data = pd.merge(data, product_count, on = "product_name")
    df = change_data.drop(columns=['add_to_cart_order','department_id','order_id','user_id','eval_set',
                               'order_number','order_dow','order_hour_of_day','days_since_prior_order','aisle','department'], axis=1)
    df = df.drop_duplicates()
    final_df = df.sort_values('count', ascending = False)
    best_reordered_model = final_df[final_df['reordered'] == 1]

    data_top30 = best_reordered_model['product_name']
    top30_product = data_top30.value_counts().head(30)
    top30_product_list = list(top30_product.index)
    top_sample = random.sample(top30_product_list, k=n_items)
    return top_sample
