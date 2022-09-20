from sklearn.metrics.pairwise import cosine_similarity
import itertools
import pandas as pd
import numpy as np
import random


def recommend_product(p):
    data = pd.read_csv('market/data/category_data_test.csv')
    case1_data = data.drop(
        columns=['add_to_cart_order', 'reordered', 'aisle_id', 'department_id', 'product_name', 'order_id',
                 'department',
                 'category', 'eval_set', 'order_number', 'order_dow', 'order_hour_of_day', 'days_since_prior_order'],
        axis=1)

    # 상품과 함께 구매했던 다른 상품 list로 만들기
    user_list = list(data[data['product_id'] == p]['user_id'])
    product_pay_list = []
    for i in user_list:
        product_pay_list.append(list((case1_data[case1_data['user_id'] == i]['product_id'])))
        product_list = list(itertools.chain.from_iterable(product_pay_list))

    if len(product_pay_list) != 0:  # 기존에 있는 제품일 경우에는
        df_list = sorted(set(product_list))  # 상품과 함께 구매했던 다른 상품 df형식으로 만들고
        df = pd.DataFrame(columns=['product_id', 'user_id', 'aisle'])
        for i in range(len(df_list)):
            df = df.append(pd.DataFrame(case1_data[case1_data['product_id'] == df_list[i]]))

        # 상품간 유사도 측정
        user_matrix_product = pd.crosstab(df.user_id, df.product_id)
        user_matrix_product_t = user_matrix_product.transpose()
        sim_data = cosine_similarity(user_matrix_product_t)
        index = np.where(user_matrix_product_t.index == p)[0][0]
        similar_aisle = sorted(list(enumerate(sim_data[index])), key=lambda x: x[1], reverse=True)[1:10]

        # best-seller 모델 구현
        def rec_product(n_items):
            product_count = data['product_id'].value_counts().to_frame()
            product_count = product_count.reset_index().rename(
                columns={"index": "product_id", "product_id": "count", "count": "category"})
            change_data = pd.merge(data, product_count, on="product_id")
            df = change_data.drop(columns=['add_to_cart_order', 'department_id', 'order_id', 'user_id', 'eval_set',
                                           'order_number', 'order_dow', 'order_hour_of_day', 'days_since_prior_order',
                                           'aisle', 'department'], axis=1)
            df = df.drop_duplicates()
            final_df = df.sort_values('count', ascending=False).head(58)
            data_top30 = list(set(final_df['product_id']))
            top_sample = random.sample(data_top30, k=9)
            return top_sample

        # 최종 상품 추천
        brr = []
        for i in similar_aisle:
            brr.append(user_matrix_product_t.index[i[0]])
        # 만약 추천 갯수가 9개 이하일 경우는 BEST-SELLER 모델에서 추천하도록 코드 구현
        if len(brr) < 9:
            brr.append(int(''.join([(str(n)) for n in rec_product(9 - len(brr))])))
        return brr

    else:  # 새로운 제품일 경우에는
        def rec_long_tail(n_items):  # long-tail 제품 추천
            product_count = data['product_id'].value_counts().to_frame()
            product_count = product_count.reset_index().rename(
                columns={"index": "product_id", "product_id": "count", "count": "category"})
            change_data = pd.merge(data, product_count, on="product_id")
            df = change_data.drop(columns=['add_to_cart_order', 'department_id', 'order_id', 'user_id', 'eval_set',
                                           'order_number', 'order_dow', 'order_hour_of_day', 'days_since_prior_order',
                                           'aisle', 'department'], axis=1)
            df = df.drop_duplicates()
            final_df = df.sort_values('count', ascending=True).head(52)
            data_long30 = list(set(final_df['product_id']))
            tail_sample = random.sample(data_long30, k=n_items)
            return tail_sample

        return rec_long_tail(9)