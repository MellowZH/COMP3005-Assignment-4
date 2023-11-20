import psycopg2


conn = psycopg2.connect(database = "COMP3005A4", 
                        user = "", 
                        host= 'localhost',
                        password = "",
                        port = 5432)