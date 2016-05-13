# WeatherDataAnalysisUsingMapReduce
Analyze weather data station wise

Weather Data Analysis using Map reduce:
Project was executed on the Oracle VirtualBox using the Hadoop instance provided by cloudera.
Two code files: mapper1.py and reducer1.py
Data: weather.txt
Please refer original.png for the format of original file.
 
Since the original file for weather is about 252MB in size, I have attached a weather.txt file that has a few records from the entire file.
The header part of the original file is removed for convenience of processing in the mapper1.py
Columns of our interest are STN, YEARMODA, TEMP
Since we are gauging weather conditions, we are calculating the average temperature of each station(STN) for each month.
The key will be the station ID (which is STN) + month(which is the 5th and 6th character of the YEARMODA column values).The value will be temperature(TEMP)
To get an idea about the mapper processing, please run the MapperOutput.py file which is in the code folder.
The key and value set will be created in the mapper and provided to the reducer for consolidating the results as per the key.

Please refer output.png for the output of the execution.
 

The above output shows the average temperature of each station for month 02. Since the weather.txt file consisted of records belonging to 02 month, the output is as above.




