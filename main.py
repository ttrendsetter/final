import requests
import pandas as pd
import json
import plotly
res = requests.post('http://127.0.0.1:8000/data', json={}).text
res = json.loads(res)
data = []
for town in res:
    for temp_data in res[town]:
        data.append((town, temp_data['temp'], temp_data['date']))
df = pd.DataFrame(data, columns=['Город', 'Температура', 'Дата'])
print(df.groupby('Город').mean())