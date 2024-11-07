This file provides a summary of the project, setup instructions, and guidance on running the scripts.

___________________________________________________________________________________________________________________________________________

--->Student Management System with MySQL

This repository contains two Python scripts that work with a MySQL database to manage student information and attendance records.
___________________________________________________________________________________________________________________________________________
--->Requirements

-->MySQL Database: Install and set up MySQL on your local machine or server.
-->Python 3: Ensure you have Python 3 installed.
-->MySQL Connector for Python: Install using: pip install mysql-connector-python
___________________________________________________________________________________________________________________________________________

--->Overview of Scripts

--->1. `Students_entry.py`

This script allows you to:
- Create a table to store student information.
- Enter and store details for each student (roll number, name, section, and class).
- The script will loop, allowing continuous input of new students until you exit.

--->Table Schema

The table `name_of_table` created by this script has the following fields:

- `roll_no`: Integer (3)
- `name`: Varchar (20)
- `section`: Char (7)
- `class`: Integer (2)

--->2. `Attandance.py`

This script allows you to:
- Create a table for a specific day's attendance.
- Prompt the user to enter attendance details for each student.
- Automatically fetch and update attendance status (Present/Absent) based on user input.

--->Table Schema

Each day's attendance table will be named `dayX` where X is the day number (e.g., `day1`, `day2`). The table includes the following fields:

- `roll_no`: Integer (3)
- `name`: Varchar (20)
- `status`: Varchar (7) (either "Present" or "Absent")
___________________________________________________________________________________________________________________________________________
--->Setup Instructions

1. Set up MySQL Database and User

   Log in to your MySQL console and create a database: CREATE DATABASE name_of_the_database;

   Replace `"name_of_the_database"` in the scripts with the actual name of your database.

2. Edit the Scripts

   Update the following fields in both scripts:
   -Database Name: Replace `"name_of_the_database"` with your MySQL database name.
   -Password: Replace `"your password here"` with your MySQL password.

3. Run the Scripts

   - Run `Students_entry.py` to add students to the database.
   - Run `Attandance.py` to record attendance for a specific day. 
___________________________________________________________________________________________________________________________________________
--->Usage

--->Running `Students_entry.py`

1. Launch the script.
2. Enter the details for each student (roll number, name, section, class).
3. After each entry, you can choose to continue or exit by pressing 'X'.

--->Running `Attandance.py`

1. Launch the script.
2. Enter the day number to create a table for that specific day's attendance.
3. Input each student’s roll number and attendance status (Present/Absent).
4. The status is saved for each student in the corresponding day's table.
___________________________________________________________________________________________________________________________________________
--->License

This project is licensed under the MIT License.
___________________________________________________________________________________________________________________________________________
--->Author

MD SAAD ANSARI
