import sys
import psycopg2

from postgresConfig import *

# Open a connection to the postgres database using parameters from config file
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
    
    # Print table headers
    print(f"{'student_id':<12} {'first_name':<12} {'last_name':<12} {'email':<28} {'enrollment_date':<15}")
    print("------------------------------------------------------------------------------------")
    
    # Fetch all data from previous command, parse then print. 
    rows = cur.fetchall()
    for row in rows:
        student_id, first_name, last_name, email, enrollment_date = row
        enrollment_date = enrollment_date.strftime("%Y-%m-%d")
        print(f"{student_id:<12} {first_name:<12} {last_name:<12} {email:<28} {enrollment_date:<15}")

    # Close cursor and communication with the database
    cur.close()
    conn.close()

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
    
    # Close cursor and communication with the database
    cur.close()
    conn.close()

def updateStudentEmail(student_id, new_email):
    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute a command: modify a students email
    try:
        cur.execute(f"""UPDATE students 
                        SET email = '{new_email}' 
                        WHERE student_id = {student_id}""")
        # Make the changes to the database persistent
        conn.commit()
        print('Success!')

    except Exception as error:
        print("ERROR:", error)
    
    # Close cursor and communication with the database
    cur.close()
    conn.close()

def deleteStudent(student_id):
    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute a command: delete student from database
    try:
        cur.execute(f"""DELETE from students 
                        WHERE student_id = {student_id}""")
        # Make the changes to the database persistent
        conn.commit()
        print('Success!')

    except Exception as error:
        print("ERROR:", error)
    
    # Close cursor and communication with the database
    cur.close()
    conn.close()
    
if __name__ == '__main__':
    args = sys.argv

    # Get cmd line arguments and pass them to the desired function
    globals()[args[1]](*args[2:])