# Hadoop-and-Mapreduce-Cloudera

I've analyzed E-commerce data and webserver logs as part of [*"Introduction to Hadoop and Mapreduce"*] (https://www.udacity.com/course/intro-to-hadoop-and-mapreduce--ud617) Udacity course offered by Cloudera.

#Sales data analysis

-  Mapper and Reducer program to find the store with highest sales
-  Mapper and Reducer program to maximum product sale amount
-  Mapper and Reducer program to count number of products sold

# Webserver log analysis

- Mapper and Reducer program to find the number of web page hits
- Mapper and Reducer program to find the most popular web page (web page with highest number of hits)
- Mapper and Reducer program to find the IP address which issued most number of requests

# Execution

Mapper's output is sorted by Hadoop framework and then passed to Reducer. We can simulate the entire process on command line using the Unix sort utility in between the Mapper and Reducer

- cat testfile | ./mapper.py | sort | ./reducer.py
- cat logfile  | ./logfileipmapper.py | sort | ./logfileipreducer.py
