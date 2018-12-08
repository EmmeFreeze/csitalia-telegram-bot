import mysql.connector

# EDIT THIS TO CONFIGURE MYSQL
mydb = mysql.connector.connect(
    host="sql2.freemysqlhosting.net",
    user="sql2269110",
    passwd="rW7*xZ8*"
)

mycursor = mydb.cursor()

def init_db ( ):
  # CREATES DATABASE
  mycursor.execute ( "CREATE DATABASE IF NOT EXISTS sql2269110;" )

  # UNCOMMENT IF IT WONT CREATE DB
  mycursor.execute ( "USE sql2269110; " )

  # CREATES TABLE problem
  mycursor.execute ( "CREATE TABLE IF NOT EXISTS problem ( \
    id INT NOT NULL AUTO_INCREMENT, \
    pname VARCHAR ( 255 ) NOT NULL, \
    pdescription VARCHAR ( 512 ),\
    pdatetime DATETIME, \
    pdifficulty ENUM( 'easy', 'medium', 'hard', 'advanced' ), \
    PRIMARY KEY ( id ) );" )

  # CREATES TABLE solution
  mycursor.execute ( "CREATE TABLE IF NOT EXISTS solution ( \
    id INT NOT NULL AUTO_INCREMENT, \
    username VARCHAR ( 255 ) NOT NULL, \
    sdatetime DATETIME, \
    programming_language VARCHAR ( 255 ), \
    problem_id INT, \
    FOREIGN KEY ( problem_id ) REFERENCES problem ( id ), \
    PRIMARY KEY ( id ) ); " )

def get_current_problem ( ):
  sql = "SELECT pname, pdescription, pdifficulty, pdatetime FROM problem;"
  mycursor.execute(sql)
  current_problem = mycursor.fetchall()

  return current_problem

def get_user_solutions ( username ):
    sql = "SELECT \
    pname,\
    pdescription, \
    username, \
    sdatetime, \
    programming_language\
    FROM problem INNER JOIN solution \
    ON problem.id = solution.problem_id WHERE username='%s';"

    val = ( username )
    mycursor.execute(sql, val)
    user_solutions = mycursor.fetchall()

    return user_solutions

def add_problem ( name, description, difficulty ):
  sql = "INSERT INTO problem ( pname, \
    pdescription, \
    pdifficulty,\
    pdatetime ) \
    VALUES ( %s, %s, %s, NOW() );"

  val = ( name, description, difficulty )
  mycursor.execute(sql, val)

# Crea db se non esiste
init_db ()

print ( add_problem ( "Problema test", "testing problem 2", "easy" ) )
print ( get_current_problem ( ) )
print ( get_user_solutions ( 'informaticage' ) )