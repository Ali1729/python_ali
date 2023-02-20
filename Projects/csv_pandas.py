# A search script to search a set of csv files and generates an output csv file. How the script operates will be controlled by a config file. 

# Get all the files from the search directory. The files in the search directory will all have the same format (same columns).

# Each record is searched in ordered of column then keyword until a match is found. Once there is a match in a record then no more searching in that record. That record is added to the output file. If no match, record is skipped.

# The output file will have two additional columns at the beginning of the record. Matched Column (MC), Matched Keyword (MK). So we know exactly were the match was found and what the match is.

# A keyword can be one word or multiple words. For example. If a keyword is "look here" the search is looking for the exact match of "look here". The search should NOT be case sensitive.

# The output file should have the timestamp appended to the file name.

# Notes: Some of these files are very big so should be able to handle large files. And the CSV files sometimes have different formats so need to be able to handle different formats of CSV files and output to standard format.

# For example
# ====
# Search File
# Name   Phone     Note       Email 
# Dave     513          bud         b@b.com
# bud       612          do not     x@x.com
# Jan        612         how to     bud@c.com
# Ned       6122       wow        try@now.com
# Budd     6122       now         at@ncom

# Search in columns 1, 2,4
# Search for keywords = "bud, 612, try@now.com"

# Result file
# MC        MK        Name   Phone    Note       Email 
# Name    bud       Bud      612         do not     x@x.com
# Phone   612        Jan       612        how to     bud@c.com
# Ned       6122       wow        try@now.com

# Config File
# Search_Directory = "/dir/"
# Output_Directory = "/dir2/"
# Search_Keywords = "HR,DEI, Diversity, Human Resources"
# Search_Columns = "2,5"
# OutputFile = search_results_name+TIMESTAMP