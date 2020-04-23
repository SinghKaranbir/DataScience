from pandas import DataFrame, Series
import numpy as np

def create_dataframe():
    '''
    Creates a pandas dataframe called 'olympic_medal_count_df' containing the data from
    the table of 2014 Sochi winter olympics medal count.
    '''
    countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
                 'Netherlands', 'Germany', 'Switzerland', 'Belarus',
                 'Austria', 'France', 'Poland', 'China', 'Korea',
                 'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
                 'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
                 'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

    gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
    silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
    bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]
    # initialize the dictionary
    dict = {'country_name': Series(countries),
            'gold': Series(gold),
            'silver': Series(silver),
            'bronze': Series(bronze)}
    #Creates a 2 Column DataFrame using dictionary
    olympic_medal_count_df = DataFrame(dict)
    return olympic_medal_count_df


if __name__ == '__main__':
    olympic_medal_count_df = create_dataframe()
    print('Winter Olympics DataFrame is following')
    print(olympic_medal_count_df)
