import sqlite3
import logging

class Database(object):
    #################   CONSTRUCTOR   #################
    #the input is a database
    def __init__(self, db):
        ### CONNECT TO DB ####
        self.con = sqlite3.connect(db)
        #crusor object allow people to execute commands
        self.cur = self.con.cursor()

        ### DATABASE ATTRIBUTE METADATA ####
        self.relations = ['students', 'visits', 'comments']

        self.meta = {'students': self.cur.execute('PRAGMA table_info("students")').fetchall(),\
                    'visits': self.cur.execute('PRAGMA table_info("visits")').fetchall(),\
                    'comments': self.cur.execute('PRAGMA table_info("comments")').fetchall(),}

    #################   DATABASE HANDELING   #################
    #method to close the connection with database
    def close(self):
        self.con.close()

    def fetchData(self, r):
        if r in self.relations: #checking if the input is a valid table
            return self.cur.execute('select * from {}'.format(r)).fetchall()
        else:
            pass

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
            raise Exception('Error!! Already Exists')

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

    #################   COMMENTS   #################

    #Insertion
    def insComment(self, ID, visit_date, visit_start, comment_date, comment_time, comments, observations, recommendations):
        #data holder
        data = [ID, visit_date, visit_start, comment_date, comment_time, comments, observations, recommendations]
        #execute to update data
        try:
            self.cur.execute('insert into comments values(?,?,?,?,?,?,?,?)', data)
            self.con.commit()
        except sqlite3.IntegrityError, value:
            logging.warning(value)
            self.con.rollback()

    #Deletion
    def delComment(self, ID, visit_date, visit_start, comment_date, comment_time):
        data = [ID, visit_date, visit_start, comment_date, comment_time]
        try:
            self.cur.execute('delete from comments where (ID = ?) and (visit_date = ?) and (visit_start = ?) and (comment_date = ?) and (comment_time = ?)' , data)
            self.con.commit()
        except sqlite3.IntegrityError, value:
            logging.warning(value)
            self.con.rollback()


### MAIN ###
def main():
    db = Database('database/cup.db')
    #db.insStudent('tanguyen17', 'Tu', 'Nguyen', 2017)
    #db.delStudent('tanguyen17')
    #db.insVisit('tanguyen17', '2016-11-13', '09:00', 1, 'Time Management', 'Nothing special')
    #db.delVisit('tanguyen17', '2016-11-13', '09:00')
    #db.insComment('tanguyen17', '2016-11-13', '09:00', '2016-11-13', '10:00', 'Good', 'ok', 'Nothing special')
    #db.delComment('tanguyen17', '2016-11-13', '09:00', '2016-11-13', '10:00')
    db.cur.execute('select * from comments')

    for i in db.cur:
        print i

    ############################################################
    db.close()

#Only execute the main menthod if the file is run directly
if __name__ == '__main__':
    main()
