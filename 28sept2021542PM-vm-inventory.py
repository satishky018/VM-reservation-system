#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Machine:
    """A sample Employee class"""

    def __init__(self, ip, username, password, avalible, owner):
        self.ip = ip
        self.username = username
        self.password = password
        self.avalible = avalible
        self.owner    = owner


# In[13]:


import sqlite3
#from employee import Employee

conn = sqlite3.connect('server.db')

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS machine (
            ip varchar,
            username text,
            password text,
          avalible boolean,
            owner null
          )""")


def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO machine VALUES (:ip, :username, :password, :avalible, :owner)", {'ip': emp.ip, 'username': emp.username, 'password': emp.password, 'avalible': emp.avalible, 'owner': emp.owner})


def get_emps_by_avalible(avalible):
    c.execute("SELECT * FROM machine WHERE avalible=:avalible", {'avalible': avalible})
    return c.fetchall()

def get_emps_by_ip(ip):
    c.execute("SELECT * FROM machine WHERE ip=:ip", {'ip': ip})
    return c.fetchall()


def update_pay(ip, avalible, owner):
    with conn:
        c.execute("""UPDATE machine SET avalible = :avalible, owner = :owner
                    WHERE ip = :ip""",
                  {'ip': ip, 'avalible': avalible, 'owner': owner})


#def remove_emp(emp):
#    with conn:
#        c.execute("DELETE from employees WHERE first = :first AND last = :last",
#                  {'first': emp.first, 'last': emp.last})

emp_1 = Machine('192.168.1.2', 'satish', 'satish-password', 1, '' )
emp_2 = Machine('192.168.1.3', 'tim', 'tim-password', 1, '' )
emp_3 = Machine('192.168.1.4', 'sera', 'sera-password', 1, '' )
emp_4 = Machine('192.168.1.5', 'dan', 'dan-password', 1, '' )
emp_5 = Machine('192.168.1.6', 'scot', 'scot-password', 1, '' )

if c.execute("SELECT * FROM machine").fetchone():
             print("data alrady exixt")
else:
             insert_emp(emp_1)
             insert_emp(emp_2)
             insert_emp(emp_3)
             insert_emp(emp_4)
             insert_emp(emp_5)


#emps = get_emps_by_avalible('0')
#print(get_emps_by_avalible('0'))
#print(get_emps_by_ip('192.168.1.2'))
#update_pay('192.168.1.2', 0, 'sky')
#remove_emp(emp_1)

emps = get_emps_by_avalible(1)
print(emps)

#conn.close()


# In[12]:


import paramiko
while True:
    x = input('''please write "new" for request for new machine or write "return" to return the machine
''')
    if x == "new":
        emps = get_emps_by_avalible('1')
        if len(emps) == 0:
            print ("no vm left try after some time.")
        else:
            i = input('enter your name: ')
            j = list(emps[0])
            #print(get_emps_by_avalible('0'))
            k=emps[0]
            print(i + " " + "your machine ip is"+"=" + j[0] + " " + "username is" + "=" + j[1] + " " + "password is" + "=" + j[2] )
            update_pay(k[0], 0, i)
    elif x == "return":
        retip = input('please enter machine ip: ')
        try:
            emps = get_emps_by_ip(retip)
            #emps = list(emps[0])
            #print(emps)
        except:
            print("enter valid ip")
            continue
        k=emps[0]
        update_pay(k[0], 1, '')
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(emps[0], 22, emps[1], emps[2])
            stdin, stdout, stderr = ssh.exec_command('rm -rf /tmp')
            lines = stdout.readlines()
            print(lines)
        except:
            print ("Unabele to conenct to the server")
    else:
        print("plesae provide valid response")


# In[ ]:


i=('192.168.1.2', 'satish', 'satish-password', 1, '')
print(i[0])


# In[ ]:




