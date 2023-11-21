# getAllStudents(): Retrieves and displays all records from the students table.
# addStudent(first_name, last_name, email, enrollment_date): Inserts a new student record into the students table.
# updateStudentEmail(student_id, new_email): Updates the email address for a student with the specified student_id.
# deleteStudent(student_id): Deletes the record of the student with the specified student_id.

import sys
import psycopg2

from postgresConfig import *


conn = psycopg2.connect(database = DATABASE_NAME, 
                        user = USER_NAME, 
                        host= HOST,
                        password = PASSWORD,
                        port = PORT)

def getAllStudents():
    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute a command: select all data from students table
    cur.execute("""SELECT * FROM students
                   ORDER BY student_id ASC""")
    
    #print table headers
    print(f"{'student_id':<12} {'first_name':<12} {'last_name':<12} {'email':<28} {'enrollment_date':<15}")
    print("------------------------------------------------------------------------------------")
    
    #fetch all data from previous command, parse then print. 
    rows = cur.fetchall()
    for row in rows:
        student_id, first_name, last_name, email, enrollment_date = row
        enrollment_date = enrollment_date.strftime("%Y-%m-%d")
        print(f"{student_id:<12} {first_name:<12} {last_name:<12} {email:<28} {enrollment_date:<15}")

    # Close cursor
    cur.close()

def addStudent(first_name, last_name, email, enrollment_date):
    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute a command: insert data into students table
    try:
        cur.execute(f"""INSERT INTO students (first_name, last_name, email, enrollment_date) 
                        VALUES('{first_name}','{last_name}','{email}','{enrollment_date}')""")
        # Make the changes to the database persistent
        conn.commit()
        print('Success!')

    except Exception as error:
        print("ERROR:", error)
    
    # Close cursor
    cur.close()
    
if __name__ == '__main__':
    args = sys.argv

    #Get cmd line arguments and pass them to the desired function
    globals()[args[1]](*args[2:])