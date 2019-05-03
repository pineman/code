import os
import sqlite3

DB = 'sqlite.db'

def create_table(db):
    db.execute('CREATE TABLE test (num INTEGER);')

    for i in range(1000):
        db.execute('INSERT INTO test VALUES (?)', (i, ))

    db.execute('ALTER TABLE test ADD COLUMN string TEXT DEFAULT "hello"')
    db.commit()


def print_table(db):
    for row in db.cursor().execute('SELECT num, string FROM test'):
        print(row)


def main():
    try:
        os.remove(DB)
    except:
        pass

    db = sqlite3.connect(DB)

    create_table(db)
    print_table(db)

    db.close()

if __name__ == '__main__':
    main()
