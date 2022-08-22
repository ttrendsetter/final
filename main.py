import requests
import pandas as pd
import json
import datetime
import plotly.express as px
print("""Please input start date and end date format YYYY-MM-DD (from today for a week ahead)""")
start_date = (input('input values or press enter if you want use default value: ')
              or datetime.datetime.now().date())
end_date = (input('input values or press enter if you want use default value: ')
            or start_date + datetime.timedelta(days=7))
req = {'start_date': str(start_date), 'end_date': str(end_date)}
res = requests.post('http://127.0.0.1:8000/data', json=req).text
res = json.loads(res)
data = []
for town in res:
    for temp_data in res[town]:
        data.append((town, temp_data['temp'], temp_data['date']))
df = pd.DataFrame(data, columns=['Город', 'Температура', 'Дата'])
# print(df)
df = df.groupby('Город').mean()
# print(list(df.index))
#
# print(df['Температура'])

fig = px.bar(data_frame=df,
             title=f'Средняя температура c {start_date} по {end_date}', y='Температура')

fig.show()