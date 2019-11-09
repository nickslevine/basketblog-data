import pandas as pd
import altair as alt

font = 'Times New Roman'
df = pd.read_csv('results.csv')
df['label'] = df[df.columns[0]]
df = df[~df.label.isin(['minutes_played', 'team'])]
df['middle'] = .5
bars = alt.Chart(df, title='How often in a game the team with more points has more of each stat (2015-2019)').mark_bar(color='#303030').encode(
    y=alt.Y('label:N', sort = alt.EncodingSortField(field='prc', op='sum', order='descending'), title=None),
    x=alt.X('prc:Q', axis=alt.Axis(format=".0%"), scale=alt.Scale(domain=[0,1]), title=None)
)
rule = alt.Chart(df).mark_rule(color='orange').encode(
  x = 'middle:Q'
)
(bars+rule).properties(width=600, height=350).configure_axis(labelFont = font, labelFontSize=14).configure_title(font=font, fontSize=16, fontWeight='normal').save('../../../basketblog/static/img/01_box_score_winners.svg')