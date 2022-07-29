# Problem statement:
The court cases 1000 samples zip folder contains 1K html files on which you need to apply the searches.

# Terminal script: Written in any language and can be run from linux terminal.

You need to come up with a terminal script that does the following:
1.	Takes in search string 
a.	Person name
b.	Case type (Act under which case the case is registered)
2.	Finds first 5 files containing the string exactly
3.	List the filenames to carry out the next step
4.	Given a particular file, it is able to parse the HTML into structured format with proper field names

# Solution:
1. ...\court cases parsing\Code
	Contains .py file which is the program file
2. ...\court cases parsing\html 
	It contains the .html files given

# To Run:
Open the .py file from Step 1.
Set the path name in lines:-
	a. 12
	b. 13

# Once the path is set, run the program by giving input:-
1. In Linux system
	python Read_Parse.py
2. In Windows, open it with any python IDE
	F5 or click run opion
3. From Command prompt
	In code path file, python Read_Parse.py

# Input to Supply:-
    Enter 1 to get file names for
	Takes in search string 
	a.Person name
	b.Case type (Act under which case the case is registered)

    Enter 2 to parse .html file
	Given a particular file, it is able to parse the HTML into structured format with proper field names

    3 to exit
