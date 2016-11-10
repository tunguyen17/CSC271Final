create table students(
  ID varchar(50),
  first varchar(50) not null,
  last varchar(50) not null,
  year numeric(4,0) not null,
  primary key(ID)
);

create table visits(
  ID varchar(50),
  visit_date varchar(50), --YYYY-MM-DD
  visit_start varchar(50), --HH:MM
  show boolean not null, --If the student shows
  topic varchar(100) not null,
  note varchar(500),
  primary key(ID, visit_date, visit_start),
  foreign key(ID) references students
);

create table comments(
  ID varchar(50),
  visit_date varchar(50), --YYYY-MM-DD
  visit_start varchar(50), --HH:MM:SS.SSS
  comment_date varchar(50), ----YYYY-MM-DD
  comment_time varchar(50), --HH:MM:SS.SSS
  comments varchar(1000),
  observations varchar(1000),
  recommendations varchar(1000),
  primary key(ID, visit_date, visit_start, comment_date, comment_time),
  foreign key(ID) references students,
  foreign key(visit_date, visit_start) references visits ON UPDATE CASCADE -- automatic update when the visit_date and visit_start change
);
