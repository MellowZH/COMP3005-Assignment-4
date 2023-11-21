# COMP3005-Assignment-4
SETUP:
1. In postgres, create a new database
2. Open postgresConfig.py and change the variables according to your postgres settings
3. Open a comand prompt into the root of the project
4. run `python init.py`

The database should now be initialized with a student table and some entries.

APPLICATION:
There are 4 operations that can be preformed. They are executed by the following functions inside of operations.py
1. getAllStudents(): Retrieves and displays all records from the students table.
2. addStudent(first_name, last_name, email, enrollment_date): Inserts a new student record into the students table.
3. updateStudentEmail(student_id, new_email): Updates the email address for a student with the specified student_id.
4. deleteStudent(student_id): Deletes the record of the student with the specified student_id.

To run one of these operations, simply run `python operations.py {function} {args}`
