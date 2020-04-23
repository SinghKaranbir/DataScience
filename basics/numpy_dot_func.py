from pandas import DataFrame, Series
import numpy as np
import create_data_frames as cdf

def points():
    '''Imagine a point system in which each country is awarded 4 points for each
    gold medal,  2 points for each silver medal, and one point for each
    bronze medal.

    Using the numpy.dot function, create a new dataframe called
    'olympic_points_df' that includes:
        a) a column called 'country_name' with the country name
        b) a column called 'points' with the total number of points the country
           earned at the Sochi olympics.
    '''
    olympic_medal_count_df = cdf.create_dataframe()

    points = np.dot(olympic_medal_count_df[['gold', 'silver', 'bronze']], [2,4,1])

    return DataFrame({'country_name': olympic_medal_count_df['country_name'],
                     'points': Series(points)
                     })

if __name__ == '__main__':
    points_df = points()
    print(points_df)
