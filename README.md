**NASA web server log analysis using Hadoop/MapReduce**

  In this project I used Hadoop/MapReduce to analyse NASA web server log. I mainly performed 3 tasks. The mapper/reduce code is in the subdirectories with the command used to exucute them. Some task may have multiple mappers and reducers so run them in numerical order. Information about the data can be found [here](http://ita.ee.lbl.gov/html/contrib/NASA-HTTP.html).

* Task 1: Finding the most popular page of the Web server. (The one that appears most frequently in requests, regardless of command.)

* Task 2: Find the top 10 hosts that produced the most 404 HTTP errors.

* Task 3: Find the time difference between the first and the last visit for each host (if a host has visited the server only once than just print the timestamp of the visit) 

