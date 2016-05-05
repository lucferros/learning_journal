#python setup.py
#steves_hat_db development.ini
#PSHELL development.ini

from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker
from learning_journal.models import Entry

engine = engine_from_config(registry.settings, 'sqlalchemy.')
Session = sessionmaker(bind=engine)

session = Session()

# new_entry = Entry(title=<title>, body=<body>)
# session.add(new_entry)
# session.commit()

'''
In [7]: for x in range(10):
   ...:         new = Entry(title='myTitle {}'.format(x), body='myBody {}'.format(x))
   ...:         session.add(new)
   ...:

In [8]: session.commit()
2016-05-05 11:32:03,776 INFO  [sqlalchemy.engine.base.Engine:1192][MainThread] SELECT CAST('test plain returns' AS VARCHAR(60)) AS anon_1
2016-05-05 11:32:03,780 INFO  [sqlalchemy.engine.base.Engine:1193][MainThread] ()
2016-05-05 11:32:03,782 INFO  [sqlalchemy.engine.base.Engine:1192][MainThread] SELECT CAST('test unicode returns' AS VARCHAR(60)) AS anon_1
2016-05-05 11:32:03,786 INFO  [sqlalchemy.engine.base.Engine:1193][MainThread] ()
2016-05-05 11:32:03,789 INFO  [sqlalchemy.engine.base.Engine:646][MainThread] BEGIN (implicit)
2016-05-05 11:32:03,792 INFO  [sqlalchemy.engine.base.Engine:1097][MainThread] INSERT INTO entries (title, body, created, edited) VALUES (?, ?, ?, ?)
2016-05-05 11:32:03,796 INFO  [sqlalchemy.engine.base.Engine:1100][MainThread] ('myTitle 0', 'myBody 0', '2016-05-05 11:29:50.547910', '2016-05-05 11:29:50.547910')
2016-05-05 11:32:03,803 INFO  [sqlalchemy.engine.base.Engine:1097][MainThread] INSERT INTO entries (title, body, created, edited) VALUES (?, ?, ?, ?)
2016-05-05 11:32:03,806 INFO  [sqlalchemy.engine.base.Engine:1100][MainThread] ('myTitle 1', 'myBody 1', '2016-05-05 11:29:50.547910', '2016-05-05 11:29:50.547910')
2016-05-05 11:32:03,811 INFO  [sqlalchemy.engine.base.Engine:1097][MainThread] INSERT INTO entries (title, body, created, edited) VALUES (?, ?, ?, ?)
2016-05-05 11:32:03,815 INFO  [sqlalchemy.engine.base.Engine:1100][MainThread] ('myTitle 2', 'myBody 2', '2016-05-05 11:29:50.547910', '2016-05-05 11:29:50.547910')
2016-05-05 11:32:03,820 INFO  [sqlalchemy.engine.base.Engine:1097][MainThread] INSERT INTO entries (title, body, created, edited) VALUES (?, ?, ?, ?)
2016-05-05 11:32:03,824 INFO  [sqlalchemy.engine.base.Engine:1100][MainThread] ('myTitle 3', 'myBody 3', '2016-05-05 11:29:50.547910', '2016-05-05 11:29:50.547910')
2016-05-05 11:32:03,829 INFO  [sqlalchemy.engine.base.Engine:1097][MainThread] INSERT INTO entries (title, body, created, edited) VALUES (?, ?, ?, ?)
2016-05-05 11:32:03,833 INFO  [sqlalchemy.engine.base.Engine:1100][MainThread] ('myTitle 4', 'myBody 4', '2016-05-05 11:29:50.547910', '2016-05-05 11:29:50.547910')
2016-05-05 11:32:03,838 INFO  [sqlalchemy.engine.base.Engine:1097][MainThread] INSERT INTO entries (title, body, created, edited) VALUES (?, ?, ?, ?)
2016-05-05 11:32:03,841 INFO  [sqlalchemy.engine.base.Engine:1100][MainThread] ('myTitle 5', 'myBody 5', '2016-05-05 11:29:50.547910', '2016-05-05 11:29:50.547910')
2016-05-05 11:32:03,847 INFO  [sqlalchemy.engine.base.Engine:1097][MainThread] INSERT INTO entries (title, body, created, edited) VALUES (?, ?, ?, ?)
2016-05-05 11:32:03,851 INFO  [sqlalchemy.engine.base.Engine:1100][MainThread] ('myTitle 6', 'myBody 6', '2016-05-05 11:29:50.547910', '2016-05-05 11:29:50.547910')
2016-05-05 11:32:03,856 INFO  [sqlalchemy.engine.base.Engine:1097][MainThread] INSERT INTO entries (title, body, created, edited) VALUES (?, ?, ?, ?)
2016-05-05 11:32:03,860 INFO  [sqlalchemy.engine.base.Engine:1100][MainThread] ('myTitle 7', 'myBody 7', '2016-05-05 11:29:50.547910', '2016-05-05 11:29:50.547910')
2016-05-05 11:32:03,865 INFO  [sqlalchemy.engine.base.Engine:1097][MainThread] INSERT INTO entries (title, body, created, edited) VALUES (?, ?, ?, ?)
2016-05-05 11:32:03,869 INFO  [sqlalchemy.engine.base.Engine:1100][MainThread] ('myTitle 8', 'myBody 8', '2016-05-05 11:29:50.547910', '2016-05-05 11:29:50.547910')
2016-05-05 11:32:03,873 INFO  [sqlalchemy.engine.base.Engine:1097][MainThread] INSERT INTO entries (title, body, created, edited) VALUES (?, ?, ?, ?)
2016-05-05 11:32:03,877 INFO  [sqlalchemy.engine.base.Engine:1100][MainThread] ('myTitle 9', 'myBody 9', '2016-05-05 11:29:50.547910', '2016-05-05 11:29:50.547910')
2016-05-05 11:32:03,884 INFO  [sqlalchemy.engine.base.Engine:686][MainThread] COMMIT

In [9]:


In [9]: Entry.all()
2016-05-05 11:32:48,769 INFO  [sqlalchemy.engine.base.Engine:1192][MainThread] SELECT CAST('test plain returns' AS VARCHAR(60)) AS anon_1
2016-05-05 11:32:48,773 INFO  [sqlalchemy.engine.base.Engine:1193][MainThread] ()
2016-05-05 11:32:48,775 INFO  [sqlalchemy.engine.base.Engine:1192][MainThread] SELECT CAST('test unicode returns' AS VARCHAR(60)) AS anon_1
2016-05-05 11:32:48,779 INFO  [sqlalchemy.engine.base.Engine:1193][MainThread] ()
2016-05-05 11:32:48,781 INFO  [sqlalchemy.engine.base.Engine:646][MainThread] BEGIN (implicit)
2016-05-05 11:32:48,784 INFO  [sqlalchemy.engine.base.Engine:1097][MainThread] SELECT entries.id AS entries_id, entries.title AS entries_title, entries.body AS entries_body, entries.created AS entries_created, entries.edited AS entries_edited
FROM entries
2016-05-05 11:32:48,791 INFO  [sqlalchemy.engine.base.Engine:1100][MainThread] ()
Out[9]:
[<learning_journal.models.Entry at 0x209e6008278>,
 <learning_journal.models.Entry at 0x209e60082e8>,
 <learning_journal.models.Entry at 0x209e6008438>,
 <learning_journal.models.Entry at 0x209e60083c8>,
 <learning_journal.models.Entry at 0x209e6008358>,
 <learning_journal.models.Entry at 0x209e60084a8>,
 <learning_journal.models.Entry at 0x209e6008588>,
 <learning_journal.models.Entry at 0x209e6008630>,
 <learning_journal.models.Entry at 0x209e60086d8>,
 <learning_journal.models.Entry at 0x209e6008780>,
 <learning_journal.models.Entry at 0x209e6008828>]


In [11]: for row in Entry.all():
   ....:        print(row.id, row.title, row.body, row.created, row.edited)
   ....:
2016-05-05 11:35:10,894 INFO  [sqlalchemy.engine.base.Engine:1097][MainThread] SELECT entries.id AS entries_id, entries.title AS entries_title, entries.body AS entries_body, entries.created AS entries_created, entries.edited AS entries_edited
FROM entries
2016-05-05 11:35:10,902 INFO  [sqlalchemy.engine.base.Engine:1100][MainThread] ()
1 Title1 body1 2016-05-05 11:16:31.959780 2016-05-05 11:16:31.959780
2 myTitle 0 myBody 0 2016-05-05 11:29:50.547910 2016-05-05 11:29:50.547910
3 myTitle 1 myBody 1 2016-05-05 11:29:50.547910 2016-05-05 11:29:50.547910
4 myTitle 2 myBody 2 2016-05-05 11:29:50.547910 2016-05-05 11:29:50.547910
5 myTitle 3 myBody 3 2016-05-05 11:29:50.547910 2016-05-05 11:29:50.547910
6 myTitle 4 myBody 4 2016-05-05 11:29:50.547910 2016-05-05 11:29:50.547910
7 myTitle 5 myBody 5 2016-05-05 11:29:50.547910 2016-05-05 11:29:50.547910
8 myTitle 6 myBody 6 2016-05-05 11:29:50.547910 2016-05-05 11:29:50.547910
9 myTitle 7 myBody 7 2016-05-05 11:29:50.547910 2016-05-05 11:29:50.547910
10 myTitle 8 myBody 8 2016-05-05 11:29:50.547910 2016-05-05 11:29:50.547910
11 myTitle 9 myBody 9 2016-05-05 11:29:50.547910 2016-05-05 11:29:50.547910

In [12]:
'''