
Project Description (Happy Journey!):

1.WeatherPy:

- The code randomly generates a series of latitude and longitudinal values.

- It then uses the citypy library to get the cities corresponding to those latitude and longitudinal values.

- Weather API is then used to get the temprature, Humidity, Cloudiness, Wind speed corresponding to those cities.

-  Analysis is then performed on the impact of latitude on temp, cloudiness, wind sppeed, Humidity.

2.VaccationPy

- The code subsets the data generated from the above steps, by only selectng cities with ideal weather conditions (i.e 70 < temp < 80, wind speed < 10%, cloudiness = 0 etc )

- It then uses the Google places API, to get the list of hotels that are within 5000 m radius (i.e. 3miles) of thosee cities.

- The results are then plotted on a goggle Heat Map, with weather condition along with the hotel name.


Note:

In order to replicate the results in my code, avoid running the api calls for weather.

After importing the packages & libraries, Run the code from cell 38 in the WeatherPy.ipynb jupyter notebook.

Enter your API keys in the api_keys.py file.




