from modules import storage as db

# Crea la struttura del db se non esiste già
db.init_db()

db.add_problem ( 'Problema 1', 'Descrizione 1', 'easy' )
db.get_user_solutions ( 'username' )
db.get_current_problem ( )