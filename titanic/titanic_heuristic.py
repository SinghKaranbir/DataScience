import pandas as pd
import numpy as np


def gender_based_heuristic():
    '''
    Heuristic based on the gender of the passenger. In this heuristic, if passenger
    is female then she survived else passenger didn't survive
    '''
    predictions = {}
    titanic_df = pd.read_csv('data/titanic_data.csv')
    for _, passenger in titanic_df.iterrows():
        passenger_id = passenger['PassengerId']
        # Gender Based heuristic
        if passenger['Sex'] == 'female':
            predictions[passenger_id] = 1
        else:
            predictions[passenger_id] = 0

    return predictions


def complex_heuristic():
    '''
    Heuristic based on gender, social class and age of the passenger.
    If the passenger is female or passenger is of higher class and less than 18 then
    passenger survived else he/she was died
    '''
    predictions = {}
    titanic_df = pd.read_csv('data/titanic_data.csv')
    for _, passenger in titanic_df.iterrows():
        passenger_id = passenger['PassengerId']
        # Two or more attribute based heuristic
        if passenger['Sex'] == 'female' or (passenger['Pclass'] == 1 and passenger['Age'] < 18):
            predictions[passenger_id] = 1
        else:
            predictions[passenger_id] = 0

    return predictions


def analyze(predictions):
    '''
    Analyze the accuracy of the heuristic based on the data set
    '''

    titanic_df = pd.read_csv('data/titanic_data.csv')

    survival_series = titanic_df['Survived'][titanic_df['Sex'] == 'female']
    values = list(predictions.values())

    actual_survivals = survival_series.sum()
    predicted_survivals = sum(values)

    print('Predicted Survivals: {}'.format(predicted_survivals))
    print('Actual Survivals: {}'.format(actual_survivals))
    percent = (actual_survivals / predicted_survivals) * 100
    rounded_percent = round(percent, 2)
    print('Accuracy of Heuristics {}%'.format(rounded_percent))


if __name__ == '__main__':
    print('For gender based heuristics:')
    predictions = gender_based_heuristic()
    analyze(predictions)

    print('For two or more attribute based heuristic:')
    predictions = complex_heuristic()
    analyze(predictions)
