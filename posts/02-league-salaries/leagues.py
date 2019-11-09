from collections import namedtuple
from dataclasses import dataclass


@dataclass
class League:
    teams: int
    games_per_team: int
    total_games: int
    players: int
    salary: int
    tv: int


nba = League(teams=30, games_per_team=82, total_games=439,
             players=10, tv=10, salary=10)
print(nba)
# League = namedtuple(
#     'League', ['teams', 'games_per_team', 'total_games', 'players', 'salary', 'tv'])

# nba = League(30, 82, 1230, 439, 7_800_000, 2_600_000_000)
# nba = League(teams=30, games_per_team=82, total_games=439,
#              players=10, salary=10, tv=10)
# print(nba.teams)

# nba = {
#     teams: 30,
#     games_per_team: 82,
#     total_games: 1230,
#     players: 439,
#     salary: 7_800_000,
#     tv: 2_600_000_000
# }
# mlb = {
#     teams: 30,
#     games_per_team: 162,
#     total_games: 2430,
#     players: 877,
#     salary: 4_500_000,
#     tv: 1_900_000_000

# }
# nfl = {
#     teams: 32,
#     games_per_team: 16,
#     total_games: 256,
#     players: 1696,
#     salary: 2_900_000,
#     tv: 6_500_000_000
# }
