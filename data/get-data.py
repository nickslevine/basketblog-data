# functions for downloading box scores and season schedules from basketball-reference

from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import OutputType
import datetime
import pandas as pd
# last date: 2019-06-14

years = [2015, 2016, 2017, 2018, 2019]


def download_season_scores():
    for y in years:
        client.season_schedule(
            season_end_year=y, output_type=OutputType.CSV, output_file_path=f"season_{y}.csv")


def download_box_scores():
    d = datetime.date(2014, 10, 29)
    # response = client.team_box_scores(
    #     day=d.day, month=d.month, year=d.year)
    # df = pd.DataFrame(response)
    # df['Date'] = d.strftime("%Y-%m-%d")
    # d = d + datetime.timedelta(days=1)
    while d < datetime.date(2019, 6, 16):
        response = client.team_box_scores(
            day=d.day, month=d.month, year=d.year)
        try:
            df = pd.DataFrame(response)
            df['Date'] = d.strftime("%Y-%m-%d")
            df.to_csv(f'box_scores/{d.strftime("%Y-%m-%d")}.csv')
        except:
            print("whoops!")
        d = d + datetime.timedelta(days=1)
        print(d)


download_box_scores()
