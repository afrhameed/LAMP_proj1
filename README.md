# LAMP_proj1

This project uses linux bash, python, mysql and php to do the following:

Bash:
Stock values are read from a website by first converting html to xhtml 
Python:
Then, using XML DOM, the xhtml file's stock information is extracted and
fed into a table using mysql connector with python

This process is repeated every minute for an hour using Bash

Finally, the php script generates a stock information table from mysql.
The table is sortable, and the sorting is done on the server side.
