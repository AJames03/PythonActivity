# _Comma Separated Values (CSV)_
---

#### What is CSV?
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; A Comma Separated Values (CSV) file is a plain text file that contains a list of data. These files are often used for exchanging data between different applications. For example, databases and contact managers often support CSV files.

#### Codes with Python
---
##### STEP 1:
- Create a Folder
- ***Example:*** csv
##### STEP 2:
- Create a file name 
- ***Example:*** csv_test.py
##### STEP 3:
- Inside the csv_test.py file, import the csv
```md
import csv
```
##### STEP 4:
- Type with open() as file:
-- **with open()** is used to handle file operations efficiently and safely. It ensures that the file is properly closed after its block is executed, even if an error occurs.
- ***Clustering-Quiz-Record.csv*** is the file of csv which you created.
- **mode="r"** → Opens the file in read mode, meaning the file is opened for reading, and an error will occur if the file does not exist.
-- **Different Modes in `open()`** 
 
| Mode | Description |
|------|------------|
| `"r"` | Read mode (default); opens file for reading, errors if the file does not exist. |
| `"w"` | Write mode; creates a new file or overwrites existing content. |
| `"a"` | Append mode; writes to the end of the file without erasing existing content. |
| `"r+"` | Read & Write mode; does not erase content, errors if the file does not exist. |
| `"w+"` | Read & Write mode; overwrites existing content or creates a new file. |
| `"a+"` | Read & Append mode; reads & writes to the end of the file. |
| `"rb"` | Read binary mode, for non-text files like images. |
| `"wb"` | Write binary mode. |
| `"ab"` | Append binary mode. |

- **newline=''** → Ensures that newline characters are handled correctly, which is useful when working with CSV files to prevent extra blank lines.
- **encoding="utf-8"** → Specifies that the file should be read using UTF-8 encoding, which supports a wide range of characters.
- **Common Encoding Types**

| Encoding | Description |
|----------|------------|
| `utf-8` | Universal encoding, supports most languages, widely used. |
| `ascii` | Supports only basic English characters (A-Z, a-z, 0-9). |
| `latin-1` | Used for Western European languages, does not support all characters. |
| `utf-16` | Used for some Windows files, stores characters in 2 bytes. |
| `utf-32` | Uses 4 bytes per character, making it larger in size. |
***Example:***
```md
with open('Clustering-Quiz-Record.csv', mode="r", newline='', encoding="utf-8") as file:
```

##### STEP 5:
```md
reader = csv.reader(file)
```
**1. reader**
-
- It is a variable name

**2. csv**
-
- This refers to the CSV module, which is a built-in Python module used to read and write CSV (Comma-Separated Values) files.
```md
import csv
```

**3. csv.reader()**
-
- This creates a reader object that allows you to iterate over rows in the CSV file.
- Each row is returned as a list of values, automatically splitting values based on the default delimiter (comma ,).

**4. file**
-
- The file is from the **as file**
```
with open('Clustering-Quiz-Record.csv', mode="r", newline='', encoding="utf-8") as file:
```
##### STEP 6:
- The for loop is needed for this to loop all the data inside the csv file.
```md
for row in reader:
        print(row)
```
- **for** - is a looping statement
- **row** - is a variable name
- **in**
-- The in keyword is used in a for loop to iterate over an iterable (e.g., a list, tuple, dictionary, file, or CSV reader).
-- It means "for each item in the iterable, do something."
- **reader** - is from the variable **reader** = csv.reader(file).
- **print(row)** - is used to print all data from our csv file which is *Clustering-Quiz-Record.csv*

## About
---
**Author:** Aron James L. Betinol
**Developer:** Aron James L. Betinol
**Programming Language:** Python
**Date of Published:** March 5, 2025

