from sqlite4 import SQLite4
from scrap import scrap

db = SQLite4("banco.db")
db.connect()

def start():
    db.create_table('prod', ['id', 'name', 'preco', 'description'])
    print('crio a tabela')

def db_add(produtos):
    for i in produtos:
        db.insert('prod', {'id': i, 'name': produtos[i][0], 'preco': produtos[i][1], 'description': produtos[i][2]})
    return print('itens adicionado com sucesso')

def que():
    return db.select("prod")

def deletar():
    db.delete('prod', '1 == 1')
    return print('tabela "prod" deletada')

# deletar()
start()
db_add(scrap())
que()
# db.disconnect()