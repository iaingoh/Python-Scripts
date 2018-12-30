# Python read csv scripts, with Pandas.
Inlcuded are some scripts i wrote which take csv files, read them, and organise them, or reorganise the data, either categorical or numerical.

### collections_Counter.py
- Opens a csv file(not included here due to its sensitive nature).
- Reads it via the csv reader.
- Loops through it.
- Counts the number of individual elements in each category via the collections library.

### dictionary_list_appendMethod.py
- A dictionary object with a key, value pair, the value being a list of numbers.
- Assign that particular dictionary key to a variable, that variable being a list, you can append to that variable.
- print the original dictionary object to see if it has been modified.
- It has.

### group_and_count_with_dictionaries.py
- First part:
    + A defined list of names.
    + A defined empty dictionary.
    + For each name's length, create a key of that length and append that name to its respective key.
- Second part:
    + With the default dict object, the number of repeated list element can be appended and counted easily.
- Third part:
    + Using Counter from collections.
    + Create a name list.
    + Plus the list into the Counter object and store it in a variable.
    + You can print the variable directly.
    + You can convert it to a dict object before printing.

### pandas-dataframes-counting-and-unique-values-noureddinSadawi.py
- raw_data is defined as a pandas dataframe. There is the key and value pairs. The values are lists of strings and integers.
- Accessing a pandas dataframe's column attribute, in this case, "city", i can count each unique value easily.

### parse_csv.py
- A simple csv file reader using Counter to counter the number of unique items in the csv file.
- For example, each category repeats itself, maybe several times, Counter assumes the low level work and counts how many times each category repeats. It returns a Counter object.

### reading_csv_files_in_Python.py
- Read the CSV file via pandas built in .read_csv() method.
- The get_group() was what i was looking for.
    + By first applying .groupby()
    + Then applying 

### removeDuplicate.py
- This script takes a unordered list as argument and removes duplicates in the list.
- The function returns a list without duplicates.
- I have hard coded a name list, and called the removeDupl function with it.
- The name list is without duplicates.



