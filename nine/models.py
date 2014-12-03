from django.db import models
import csv
import datetime
from datetime import date

# Create your models here.

class square():
    pass
#    a = GET['a']
#    b = request.GET(b)
#    c = request.GET(c)
#    summa = a + b + c

class Heroes():
    def __init__(self, filename):
        self.persons = []
        fp = open(filename,"rb")
    
        with fp as csvfile:
            n = 0
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in reader:
                if n > 0:
                    if row[4] != '':
                        user = Person(row[0], row[1], row[2], row[3], row[4])
                    else:
                        user = Person(row[0], row[1], row[2], row[3])
                    self.persons.append(user)
                n += 1


    def get_hero(self, nickname):
        for person in self.persons:
            if person.nickname == nickname:
                return person
        return None

class Person(object):
    def __init__(self, ident, surname, name, bdata, nickname=None):
        self.ident = ident
        self.surname = surname
        self.name = name
        dt = bdata.split("-")
        #print 'bdata', bdata
        #print 'dt', dt
        birth_date = datetime.date(int(dt[0]), int(dt[1]), int(dt[2]))
        self.birth_date = birth_date
        if nickname is not None:
            self.nickname = nickname
        else:
            self.nickname = ''
