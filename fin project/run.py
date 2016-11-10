import sqlite3
import logging

class database(object):
    #constructor for the database object
    #the input is a database
    def __init__(self, db):
        #connect to db
        self.con = sqlite3.connect(db)

        #crusor object allow people to execute commands
        self.cur = self.con.cursor()

    #################   STUDENTS   #################
    #Insertion
    def insStudent(self, ID, first, last, year):
        #data holder
        data = [ID, first, last, year]
        #execute to update data
        try:
            #proccess data and insert new data into the database
            self.cur.execute('insert into students values(?,?,?,?)', data)
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
            #Unsuccessful update, rollback to earlier commit
            self.con.rollback()

    #Deletion
    def delStudent(self, ID):
        data = [ID]
        try:
            self.cur.execute('delete from students where ID = ?', data)
            self.con.commit()
        except sqlite3.IntegrityError, value:
            logging.warning(value)
            self.con.rollback()

    #################   VISITS   #################

    #Insertion
    def insVisit(self, ID, visit_date, visit_start, show, topic, note):
        #data holder
        data = [ID, visit_date, visit_start, show, topic, note]
        #execute to update data
        try:
            self.cur.execute('insert into visits values(?,?,?,?,?,?)', data)
            self.con.commit()
        except sqlite3.IntegrityError, value:
            logging.warning(value)
            self.con.rollback()

    #Deletion
    def delVisit(self, ID, visit_date, visit_start):
        data = [ID, visit_date, visit_start]
        try:
            self.cur.execute('delete from visits where (ID = ?) and (visit_date = ?) and (visit_start = ?)', data)
            self.con.commit()
        except sqlite3.IntegrityError, value:
            logging.warning(value)
            self.con.rollback()


    #################   DATABASE HANDELING   #################
    #method to close the connection with database
    def close(self):
        self.con.close()

### MAIN ###
def main():
    db = database('database/cup.db')
    #db.insStudent('tanguyen17', 'Tu', 'Nguyen', 2017)
    #db.delStudent('tanguyen17')
    #db.insVisit('tanguyen17', '2016-11-13', '09:00', 1, 'Time Management', 'Nothing special')
    #db.delVisit('tanguyen17', '2016-11-13', '09:00')
    db.cur.execute('select * from visits')

    for i in db.cur:
        print i
    ############################################################
    db.close()

#execute the main method
if __name__ == '__main__':
    main()
