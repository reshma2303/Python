import pandas as pd
import numpy as np


def create_dataset(n_rows=5000):

    """
    5 columns
    :return:
    """
    np.random.seed(44)
    df = pd.DataFrame(index=np.arange(n_rows),
                      columns=['customer_per_day',
                               'site_id',
                               'merchandise_restock',
                               'fuel_restock',
                               'daily_revenue'])
    site_ids = ["001", "002", "A02", "B02", "003", "B03"]
    site_probabilities = [0.25, 0.15, 0.2, 0.04, 0.06,  0.3]
    print("site_probabilities sum: ", sum(site_probabilities))
    df['customer_per_day'] = np.random.randint(low=25, high=150, size=n_rows)
    df['site_id'] = np.random.choice(site_ids, p=site_probabilities, size=n_rows)
    df['merchandise_restock'] = np.random.choice(a=[0, 1], p=[0.25, 0.75], size=n_rows)
    df['fuel_restock'] = np.random.choice(a=[0,1], p=[0.1, 0.9], size=n_rows)
    df['daily_revenue'] = np.round(np.random.random(n_rows) * (5000-500) + 500, 2)



    def _add_state(row):
        if row['site_id'] in ["001", "B02"]:
            return "Rhode Island"
        elif row["site_id"] in ["002", "A02"]:
            return "Montana"
        else:
            return "Alabama"

    df['state'] = df.apply(lambda row: _add_state(row), axis=1)

    grouped_df = df.groupby(by=['state']).agg({'daily_revenue': sum}).reset_index()
    print(grouped_df)

    df['state_revenue_sum'] = df['daily_revenue'].groupby(df['state']).transform('sum')
    df['state_revenue_mean'] = df['daily_revenue'].groupby(df['state']).transform('mean')

    print("DataFrame Shape: ", df.shape)

    print("Site ID value counts\n")
    print(df.site_id.value_counts())

    print("State value counts\n")
    print(df.state.value_counts())

    print("DataFrame sample: \n")
    print(df.sample(10))



create_dataset()


