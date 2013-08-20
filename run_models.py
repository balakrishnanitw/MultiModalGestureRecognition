from models import movement_interval
from pandas import DataFrame
import pandas as pd
import numpy as np
from postprocessing import pad_smooth


def train_audio_models(train_on, predict_on):
    pass


def train_movement_model_and_merge_on_audio_interval(train_on, predict_on,
        path_to_audio_intervals, path_to_movement_model_with_audio_interval):


    df_out = movement_interval(train_on=train_on, predict_on=predict_on)
    df_out = df_out.groupby('sample_id').apply(pad_smooth, window_len=11)

    middle = pd.read_csv(path_to_audio_intervals, header=None, skiprows=1)
    middle = middle.ix[:, [0, 2]]
    middle.columns = ['sample_id', 'frame']
    middle_probs = pd.merge(middle, df_out, how='left', on=['sample_id', 'frame'])
    middle_probs = middle_probs.drop(['sample_id', 'frame', 0, 'movement'], axis=1)

    middle_probs.to_csv(path_to_movement_model_with_audio_interval, index=False)


def extract_audio_intervals_from_movement_model():
    pass


def merge_models():
    pass


def create_prediction_file():
    pass


if __name__ == '__main__':

    #leaderboard model settings
    predict_on = ['validation1_lab', 'validation2_lab', 'validation3_lab']
    train_on = ['training1', 'training2', 'training3', 'training4']
    path_to_audio_intervals = 'Submission_table_t1234_v123.csv'
    path_to_movement_model_with_audio_interval =\
            'movement_probs_added_' + path_to_audio_intervals

    train_movement_model_and_merge_on_audio_interval(train_on, predict_on,
            path_to_audio_intervals, path_to_movement_model_with_audio_interval)

    # parameter estimation settings
    predict_on = ['training2', 'validation2_lab']
    train_on = ['training1', 'training3', 'training4', 'validation1_lab', 'validation3_lab']
    path_to_audio_intervals = 'Submission_table_t134v13_t2v2.csv'
    path_to_movement_model_with_audio_interval =\
            'movement_probs_added_' + path_to_audio_intervals

    train_movement_model_and_merge_on_audio_interval(train_on, predict_on,
            path_to_audio_intervals, path_to_movement_model_with_audio_interval)

    # test set model
    #train_on = ['training1', 'training2', 'training3', 'training4', 
    #        'validation1_lab', 'validation2_lab', 'validation3_lab']
    #predict_on = ['test1', 'test2', 'test3', 'test4', 'test5', 'test6']


    #train_audio_models(train_on, predict_on, path_to_audio_intervals)
