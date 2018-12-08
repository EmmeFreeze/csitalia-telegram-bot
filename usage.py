from modules import storage as db

# Crea la struttura del db se non esiste già
db.init_db()

db.add_problem ( 'Problema 1', 'Descrizione 1', 'easy' )
db.get_current_problem ( )
db.add_solution ( 'informaticage', 'Ansi C99', 'http:\\solution.com\tuna', 26 )
print ( db.get_user_solutions ( 'informaticage' ) )