import pandas as pd

df = pd.read_csv('dataset/nyc_weather.csv')

# print(df.head())

# print(df['EST'])

# print(df['EST'][0])

# print(df[['EST','DewPoint','Humidity']])

# print(df['Temperature'].max())

# print(df['EST'][df['Events'] == 'Rain'] )

# df['Manoj'] = df['Temperature'] + 10
# print(df[['Manoj', 'Temperature']])

df['WindSpeedMPH'] = df['WindSpeedMPH'].fillna(0)

print(df['WindSpeedMPH'].mean())






