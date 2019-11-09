# combine data files into single csvs
import pandas as pd
import os


def combine_season_scores():
    df = pd.read_csv('season_2015.csv')
    df['season_end_year'] = 2015
    # df['season_end_year'] = 2015
    years = [2016, 2017, 2018, 2019]
    for y in years:
        temp = pd.read_csv(f'season_{y}.csv')
        temp['season_end_year'] = y
        df = pd.concat([df, temp])
    df.to_csv('nba_scores.csv')


def combine_box_scores():
    dfs = []
    for f in os.listdir('box_scores'):
        dfs.append(pd.read_csv(f'box_scores/{f}'))
    all_scores = pd.concat(dfs)
    all_scores['field_goal_pct'] = all_scores['made_field_goals'] / \
        all_scores['attempted_field_goals']
    all_scores['three_point_pct'] = all_scores['made_three_point_field_goals'] / \
        all_scores['attempted_three_point_field_goals']
    all_scores['free_throw_pct'] = all_scores['made_free_throws'] / \
        all_scores['attempted_free_throws']
    all_scores['assists_per_fg'] = all_scores['assists'] / \
        all_scores['made_field_goals']
    all_scores.to_csv('all_box_scores.csv')


combine_box_scores()
