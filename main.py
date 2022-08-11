import requests
import pandas as pd
import json
import plotly.express as px
res = requests.post('http://127.0.0.1:8000/data', json={}).text
res = json.loads(res)
data = []
for town in res:
    for temp_data in res[town]:
        data.append((town, temp_data['temp'], temp_data['date']))
df = pd.DataFrame(data, columns=['Город', 'Температура', 'Дата'])
df = df.groupby('Город').mean()
print(list(df.index))
print(df['Температура'])
fig = px.bar(data_frame=df, title='Средняя температура', y='Температура')

fig.show()