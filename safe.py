import os
from subprocess import call,Popen
import sqlite3
import sys
import getpass




crypass="amiya_frost"


db="password.db"
#fold="private"
def databasechecker():

    if os.path.exists("./Private")and os.path.isfile(db):
        print "please fill the form"
        passwordchecker()
    else:
        process=Popen(['cmd.exe','/c mkdir Private '])
        firsttimepass()


def firsttimepass():
    #decrypt(getKey(), db)
    try:
        db_conn = sqlite3.connect(db)
        print 'enter first time values'
        c = db_conn.cursor()
        c.execute("create table holderpass (name1 TEXT NOT NULL ,pass1 TEXT NOT  NULL )")
        db_conn.commit()
        os.system('cls')
        name = raw_input("please enter the name:")
        pass1 = raw_input("please enter the password :")
        if (name != None) and (pass1 != None):
            c.execute("INSERT INTO holderpass VALUES (?,?)", (name, pass1))

        firstp()
    except:
        print "well done"

    db_conn.commit()





def passwordchecker():
    #decrypt(getKey(), db)
    db_conn = sqlite3.connect(db)
    c = db_conn.cursor()
    c.execute("select * from holderpass")
    k=c.fetchall()
    m=str(k[0][0])
    l=str(k[0][1])
    #print k ,m,l
    db_conn.close()

    def iner():
        na = raw_input("enter the name:")
        #pa = raw_input("enter the password:")
        pa=getpass.getpass(prompt="enter the password:")
        att=["+s","+h"]
        att2=['-s','-h']
        #print k
        if (na == m) and (pa == l):
            call(["attrib"]+att2+["Private"])
            def z():
                s = raw_input("want to lock the folder type yes:")
                if (s == 'yes') or (s == 'yes'):
                    call(["attrib"] + att + ["Private"])
                    out()
                else:
                    print "wrong input"
                    z()
            z()



        else:
            print  "wrong password"
            iner()

    iner()


def out():
    #encrypt(getKey(), db)
    att = ['+s', '+h']
    call(["attrib"] + att + [db])
    print "process has been successful"


def firstp():
    att = ['+s', '+h']
    #att2 = ['-s', '-h']
    a=raw_input("want to lock the folder type yes:")
    if (a == 'yes') or (a == 'yes'):
        call(["attrib"] + att + ["Private"])
        call(["attrib"] + att + [db])
        out()



#code added




#code end

if __name__=="__main__":
    try:
        os.system('cls')
        databasechecker()
    except:
        print "error:",sys.exc_info()[0]
