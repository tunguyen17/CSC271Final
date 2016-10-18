import sqlite3
import logging

class database(object):
    def __init__(self, db):
        #connect to db
        self.con = sqlite3.connect(db)

        #crusor object allow people to execute commands
        self.cur = self.con.cursor()

    def insStudent(self, ID, first, last, year, major=None, minor=None):
        data = [ID, first, last, year, major, minor]
        try:
            self.cur.execute('insert into students values(?,?,?,?,?,?)', data)
            #commit the new name to the database
            self.con.commit()
        except sqlite3.IntegrityError, value:
            #print out the value
            logging.warning(value)
            '''
                There are two types of IntegrityError
                    UNIQUE : duplication of primary key
                    NOT NULL: when input a None into the input of a none null attribute
            '''
            #rollback to earlier commit
            self.con.rollback()

    def delStudent(ID):
        data = ID
        try:
            self.cur.execute('delete from students ')

    #method to close the connection with database
    def close(self):
        self.con.close()

#main method
def main():
    db = database('database/cup.db')
    db.insStudent('tanguyen17', 'Tu', 'Nguyen', 2017, 'Math', 'Comp. Sci.')
    db.cur.execute('select * from students')

    for i in db.cur:
        print i
    ############################################################
    db.close()

#execute the main method
if __name__ == '__main__':
    main()
