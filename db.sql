CREATE DATABASE IF NOT EXISTS csitaly;

USE csitaly;

CREATE TABLE IF NOT EXISTS problem ( 
    id INT NOT NULL AUTO_INCREMENT,
    pname VARCHAR ( 255 ) NOT NULL,
    pdescription VARCHAR ( 512 ),
    pdatetime DATETIME DEFAULT NOW(),
    pdifficulty ENUM( 'easy', 'medium', 'hard', 'advanced' ),
    
    PRIMARY KEY ( id )
);

CREATE TABLE IF NOT EXISTS solution ( 
    id INT NOT NULL AUTO_INCREMENT,
    username VARCHAR ( 255 ) NOT NULL,
    sdatetime DATETIME DEFAULT NOW(),
    programming_language VARCHAR ( 255 ),

    -- Reference on problem
    problem_id INT,
    FOREIGN KEY (problem_id) REFERENCES problem ( id ),
    PRIMARY KEY ( id )
);