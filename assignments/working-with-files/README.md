# 📘 Assignment: Working with Files in Python

## 🎯 Objective

Learn how to read from and write to files using Python's built-in `open()` function. You will practice persisting data between program runs, processing text line by line, and working with CSV data without external libraries.

## 📝 Tasks

### 🛠️	Read a Text File

#### Description
Open an existing text file and print its contents to the console, processing it line by line.

#### Requirements
Completed program should:

- Open the file `notes.txt` using `open()` with the appropriate read mode.
- Read and print each line of the file, stripping any trailing newline characters.
- Use a `with` statement to ensure the file is properly closed after reading.
- Example output (given a file with two lines):
  ```
  Line 1: Hello, world!
  Line 2: Python file I/O is useful.
  ```

### 🛠️	Write and Append to a Text File

#### Description
Write new content to a file, then append additional lines without overwriting the original content.

#### Requirements
Completed program should:

- Create (or overwrite) a file called `output.txt` and write at least three lines to it using `open()` in write mode (`'w'`).
- Reopen the same file in append mode (`'a'`) and add at least one more line.
- Read `output.txt` back and print all its contents to verify the result.
- Example final contents of `output.txt`:
  ```
  Name: Alice
  Age: 17
  Subject: Computer Science
  Note: Appended after initial write.
  ```

### 🛠️	Process a CSV File Without Libraries

#### Description
Read a CSV file manually using Python's built-in string methods to parse and display structured data.

#### Requirements
Completed program should:

- Open `students.csv` (provided as starter data) using `open()` in read mode.
- Skip the header row and parse each remaining row by splitting on commas.
- Print each student's name and grade in a formatted string. Example:
  ```
  Alice - Grade: A
  Bob - Grade: B
  Charlie - Grade: A
  ```
- Calculate and print the total number of students found in the file.
