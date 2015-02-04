import string
import random
import crypt
char_set = string.ascii_lowercase +string.ascii_uppercase + string.digits

users=["abdellatifdanba","arthurstomp","benvdstouwe","byran95","crist92","dionw","dutchneon","ejnijhof","hb117","herden","jan26th","jorisjbr","jurbraam94","lokkwanfoo","manuelbrand","martganzevles","matthiasmeerhof","penix","pindab0ter","piratninja","rachelswansen","robba024","royalclub","safirasuli","sanctuscoma","sebastianhilge","sjenk","sladebaumann","stijnno23","susie93","tomkaal","wesema"]

password=[]

print ">>>> BEGIN Python script"
print "---"

for user in users:
    pwd=''.join(random.sample(char_set*16, 16))
    password.append(pwd)
    ansiblePwd=crypt.crypt(pwd, "$1$SomeSalt$")
    print "- user: name=%s password=%s state=present shell=/bin/bash" % (user, ansiblePwd)

print "<<<<< End Python script"


i=0
for user in users:
    print user, password[i]
    i=i+1
