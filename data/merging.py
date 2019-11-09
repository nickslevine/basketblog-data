# merge box scores and results

import pandas as pd
import datetime


def get_date(s):
    d = str(s)[0:10]
    h = str(s)[11:13]
    fields = list(map(int, d.split('-')))
    date_object = datetime.date(fields[0], fields[1], fields[2])
    if int(h) < 10:
        return (date_object - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    else:
        return d


all_box_scores = pd.read_csv('all_box_scores.csv')
nba_scores = pd.read_csv('nba_scores.csv')
nba_scores['Date'] = nba_scores['start_time'].apply(lambda x: get_date(x))
all_box_scores['team'] = all_box_scores['team'].apply(
    lambda x: ' '.join(x.split('.')[1].split('_')))


merged = nba_scores.merge(all_box_scores, left_on=[
                          'Date', 'home_team'], right_on=['Date', 'team'], how='inner')
merged = merged.merge(all_box_scores, left_on=['Date', 'away_team'], right_on=[
                      'Date', 'team'], how='inner', suffixes=['_home', '_away'])


# df1 = all_box_scores.merge(
#     nba_scores, left_on=['Date', 'team'], right_on=['Date', 'home_team'], how='inner')
# df2 = all_box_scores.merge(
#     nba_scores, left_on=['Date', 'team'], right_on=['Date', 'away_team'], how='inner')
# combined = pd.concat([df1, df2])
# print(len(combined))
# combined.to_csv('combined.csv')
merged.to_csv('merged.csv')
