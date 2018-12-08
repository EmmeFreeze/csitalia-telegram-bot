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
    solution_url VARCHAR ( 1024 ) NOT NULL, \
    programming_language VARCHAR ( 255 ), \
    problem_id INT, \
    FOREIGN KEY ( problem_id ) REFERENCES problem ( id ), \
    PRIMARY KEY ( id ) ); " )

def get_current_problem ( ):
  sql = "SELECT id, pname, pdescription, pdifficulty, pdatetime FROM problem;"
  mycursor.execute(sql)
  current_problem = mycursor.fetchall()

  return current_problem

def get_user_solutions ( username ):
    sql = "SELECT \
    pname,\
    pdescription, \
    username, \
    solution_url,\
    sdatetime, \
    programming_language\
    FROM problem INNER JOIN solution \
    ON problem.id = solution.problem_id WHERE USERNAME LIKE " + "'%" + username + "%'"

    mycursor.execute(sql)
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

def add_solution ( username, programming_language, solution_url, problem_id ):
  sql = "INSERT INTO solution ( username, \
    programming_language, \
    solution_url, \
    problem_id, \
    sdatetime ) \
    VALUES ( %s, %s, %s, %s, NOW() );"

  val = ( username, programming_language, solution_url, problem_id )
  mycursor.execute(sql, val)
