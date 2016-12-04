'''
DATABASE library for the interaction with the database

class database
- used for setting up connection with the database
- used for fletching, adding and updating data

methods
STUDENTS SCHEMA
insStudent
delStudent

VISITS SCHEMA
insVisit
delVisit

COMMENTS SCHEMA
insComment
delComment
'''

import sqlite3
import logging
import time, datetime #this is for creating a new time stamp

class Database(object):
    #################   CONSTRUCTOR   #################
    #the input is a database
    def __init__(self, db):
        '''
        CONSTRUCTOR
        input:
        - db: location of the .db file

        Fields:
        - con : the connection to the database
        - cur : crusor object
        - relation : a list of relations of the database
        - meta : containing the metadata of each relation schema
        '''
        ### CONNECT TO DB ####
        self.con = sqlite3.connect(db)
        #crusor object allow people to execute commands
        self.cur = self.con.cursor()

        ### DATABASE ATTRIBUTE METADATA ####
        #Name of the relations
        self.relations = ['students', 'visits', 'comments']
        #Meta data of each relations
        self.meta = {'students': self.cur.execute('PRAGMA table_info("students")').fetchall(),\
                    'visits': self.cur.execute('PRAGMA table_info("visits")').fetchall(),\
                    'comments': self.cur.execute('PRAGMA table_info("comments")').fetchall(),}

    #################   DATABASE HANDELING   #################
    #method to close the connection with database
    def close(self):
        self.con.close()

    #fletch all data from table r
    def fetchData(self, r):
        'fletch everything from relation r'
        if r in self.relations: #checking if the input is a valid table
            return self.cur.execute('select * from {}'.format(r)).fetchall()
        else:
            pass

    #################   STUDENTS   #################
    #Insertion
    def insStudent(self, ID, first, last, year, note):
        'Insert a new student. Inputs ID, first, last, year'

        #data holder
        data = [ID, first, last, year, note]

        #execute to update data
        try:
            #proccess data and insert new data into the database
            self.cur.execute('insert into students values(?,?,?,?,?)', data)
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
            #raise exception for the GUI
            raise Exception(value)

    #Find visit
    def findStudent(self, ID):
        #execute to update data
        try:
            return self.cur.execute('select * from students where (ID = ?)', [ID]).fetchall()
        except sqlite3.IntegrityError, value:
            logging.warning(value)
            #raise exception for the GUI
            raise Exception(value)

    #Find All IDs
    def idList(self):
        #execute to update data
        try:
            return self.cur.execute('select ID from students').fetchall()[0]
        except sqlite3.IntegrityError, value:
            logging.warning(value)
            #raise exception for the GUI
            raise Exception(value)


    #Deletion
    def delStudent(self, ID):
        'Student deletions. Input ID'

        data = [ID]
        try:
            self.cur.execute('delete from students where ID = ?', data)
            self.con.commit()
        except sqlite3.IntegrityError, value:
            logging.warning(value)
            #Unsuccessful update, rollback to earlier commit
            self.con.rollback()
            #raise exception for the GUI
            raise Exception(value)

    #################   VISITS   #################

    #Insertion
    def insVisit(self, ID, visit_date, visit_start, show, topic, note, comments, observations, recommendations):
        #data holder
        data = [ID, visit_date, visit_start, show, topic, note, comments, observations, recommendations]
        #execute to update data
        try:
            self.cur.execute('insert into visits values(?,?,?,?,?,?,?,?,?)', data)
            self.con.commit()
        except sqlite3.IntegrityError, value:
            logging.warning(value)
            self.con.rollback()
            #raise exception for the GUI
            raise Exception(value)

    #Find visit
    def findVisit(self, keys):
        #data holder
        data = keys
        #execute to update data
        try:
            return self.cur.execute('select * from visits where (ID = ?) and (visit_date = ?) and (visit_start = ?)', data).fetchall()
        except sqlite3.IntegrityError, value:
            logging.warning(value)
            #raise exception for the GUI
            raise Exception(value)

    #update visit
    def updateVisit(self, ID, visit_date, visit_start, show, topic, note, comments, observations, recommendations):
        #data holder

        keys = [ID, visit_date, visit_start]

        data = [show, topic, note, comments, observations, recommendations]
        dataCol = ["show", "topic", "note", "comments", "observations", "recommendations"]
        """
        #execute to update data
        try:
            #Consider "visit_date" and "visit_start" because they are in primary key
            if visit_date:
                self.cur.execute('update visits\
                                  set visit_date = \
                                  where (ID = ?) and (visit_date = ?) and (visit_start = ?)', keys)

            for i in range(len(data)):
                if data[i]:

        except sqlite3.IntegrityError, value:
            logging.warning(value)
            #raise exception for the GUI
            raise Exception(value)
            """
    #Deletion
    def delVisit(self, ID, visit_date, visit_start):
        data = [ID, visit_date, visit_start]
        try:
            self.cur.execute('delete from visits where (ID = ?) and (visit_date = ?) and (visit_start = ?)', data)
            self.con.commit()
        except sqlite3.IntegrityError, value:
            logging.warning(value)
            self.con.rollback()
            #raise exception for the GUI
            raise Exception(value)

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
            #raise exception for the GUI
            raise Exception(value)

    #Deletion
    def delComment(self, ID, visit_date, visit_start, comment_date, comment_time):
        data = [ID, visit_date, visit_start, comment_date, comment_time]
        try:
            self.cur.execute('delete from comments where (ID = ?) and (visit_date = ?) and (visit_start = ?) and (comment_date = ?) and (comment_time = ?)' , data)
            self.con.commit()
        except sqlite3.IntegrityError, value:
            logging.warning(value)
            self.con.rollback()
            #raise exception for the GUI
            raise Exception(value)

    #Time Stamp
    def getTimeStamp(self):
        return datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')


#Only execute the main menthod if the file is run directly
if __name__ == '__main__':
    db = Database('database/cup.db')
    #db.insStudent('tanguyen17', 'Tu', 'Nguyen', 2017)
    #db.delStudent('tanguyen17')
    #db.insVisit('tanguyen17', '2016-11-13', '09:00', 1, 'Time Management', 'Nothing special')
    #db.delVisit('tanguyen17', '2016-11-13', '09:00')
    #db.insComment('tanguyen17', '2016-11-13', '09:00', '2016-11-13', '10:00', 'Good', 'ok', 'Nothing special')
    #db.delComment('tanguyen17', '2016-11-13', '09:00', '2016-11-13', '10:00')
    print db.findVisit("tanguyen17", "2016-9-20", "10:29")
    print db.getTimeStamp()
    for i in db.cur:
        print i
    ############################################################
    db.close()
