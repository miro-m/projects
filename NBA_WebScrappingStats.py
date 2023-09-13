import pandas as pd
import requests
pd.set_option('display.max_columns', None)
import time
import numpy as np

test_url =  'https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=Totals&Scope=S&Season=2012-13&SeasonType=Regular%20Season&StatCategory=PTS'
req = requests.get(url=test_url).json()

print(req)

table_headers = req['resultSet']['headers']

print(pd.DataFrame(req['resultSet']['rowSet'], columns=table_headers))


df_cols = ['Year', 'Season_type'] + table_headers
df = pd.DataFrame(columns=df_cols)
pd.DataFrame(columns=df_cols)
season_types = ['Regular%20Season', 'Playoffs']
years = ['2012-13', '2013-14', '2014-15', '2015-16', '2016-17', '2017-18', '2018-19', '2019-20', '2020-21','2021-22']

headers = {'Accept': '*/*', 'Origin': 'https://www.nba.com', 'Accept-Encoding': 'gzip, deflate, br', 'Host': 'stats.nba.com',
           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15',
           'Accept-Language': 'en-CA,en-US;q=0.9,en;q=0.8','Referer': 'https://www.nba.com/', 'Connection': 'keep-alive'}

begin_loop = time.time()
for y in years:
    for s in season_types:
        api_url = 'https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=Totals&Scope=S&Season='+y+'&SeasonType='+s+'&StatCategory=PTS'
        req = requests.get(url=api_url).json()
        temp_df1 = pd.DataFrame(req['resultSet']['rowSet'], columns=table_headers)
        temp_df2 = pd.DataFrame({'Year': [y for i in range(len(temp_df1))],
                                 'Season_type': [s for i in range(len(temp_df1))]})

        temp_df3 = pd.concat([temp_df2, temp_df1], axis=1)
        df = pd.concat([df, temp_df3], axis=0, ignore_index=True)
        print(f'Finished scraping data for the {y} and {s}.')
        lag = np.random.uniform(low=2, high=3)
        print(f'...waiting {round(lag, 1)} seconds')
        time.sleep(lag)

print(f'Process completed! Total run time:{round((time.time() - begin_loop)/60, 2)}')
df.to_excel('nba_player_data.xlsx', index=False)
