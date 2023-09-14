import pandas
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
pd.set_option('display.max_columns', None)

data = pd.read_excel('nba_player_data.xlsx')

## print(data.sample(10))

##print(data.shape)

data.drop(columns=['RANK', 'EFF'], inplace=True)
data['season_start_year'] = data['Year'].str[:4].astype(int)
data['TEAM'].replace(to_replace=['NOP', 'NOH'], value='NO', inplace=True)
data['Season_type'].replace('Regular%20Season', 'RS', inplace=True)

rs_df = data[data['Season_type'] == 'RS']
playoffs_df = data[data['Season_type'] == 'Playoffs']

total_cols = ['MIN','FGM','FGA','FG3M','FG3A','FTM','FTA',
              'OREB','DREB','REB','AST','STL','BLK','TOV','PF','PTS']

data_per_min = data.groupby(['PLAYER', 'PLAYER_ID', 'Year'])[total_cols].sum().reset_index()

print(data_per_min)

##NOT FINISHED

