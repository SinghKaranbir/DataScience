import numpy as np
import create_data_frames as cdf


def get_average_medal_count():
    '''
    Get the average count medals within gold, silver, bronze winning countries
    '''
    olympic_medal_count_df = cdf.create_dataframe()
    avg_medal_count = olympic_medal_count_df[['gold', 'silver', 'bronze']].apply(np.mean)

    return avg_medal_count

if __name__ == '__main__':
    avg_medal_count = get_average_medal_count()
    print(avg_medal_count)
