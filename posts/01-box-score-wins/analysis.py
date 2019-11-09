import pandas as pd
df = pd.read_csv('merged.csv')

stats = 'assists,attempted_field_goals,attempted_free_throws,attempted_three_point_field_goals,blocks,defensive_rebounds,made_field_goals,made_free_throws,made_three_point_field_goals,minutes_played,offensive_rebounds,personal_fouls,steals,team,turnovers,field_goal_pct,three_point_pct,free_throw_pct,assists_per_fg'.split(
    ',')


def get_winner(row):
    if row['home_team_score'] > row['away_team_score']:
        return 'home'
    else:
        return 'away'


home_away = {
    'home': 'away',
    'away': 'home'
}

counts = {}
for s in stats:
    counts[s] = 0

df['winner'] = df.apply(lambda row: get_winner(row), axis=1)

for k, row in df.iterrows():
    winner = row['winner']
    for s in stats:
        if row[f'{s}_{winner}'] > row[f'{s}_{home_away[winner]}']:
            counts[s] += 1
count_df = pd.DataFrame.from_dict(
    counts, orient='index', columns=['value'])
count_df['prc'] = count_df['value'] / len(df)
count_df.sort_values(by='value').to_csv('results.csv')
