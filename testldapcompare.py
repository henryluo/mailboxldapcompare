import threading, time, sys
import ldap

def wrapper(func, args, res):
    res.append(func(*args))

res = []
str1 = "."

con = ldap.initialize('ldap://ldapIPAddress')

ldap_base = 'dc=example,dc=com'
query = '(objectclass=OrgPerson)'
#result = con.search_s(ldap_base, ldap.SCOPE_SUBTREE)

#Start extracting info from LDAP
print "Querying information from LDAP"
t = threading.Thread(target=wrapper, args=(con.search_s, (ldap_base, ldap.SCOPE_SUBTREE,), res))
t.start()
while t.is_alive():
    sys.stdout.write('\r'+str1)
    sys.stdout.flush()
    time.sleep(.5)
    str1 = str1 + "."
    t.join(0.2)
print "Done\n"

#Writing compared queried information to a file
print "Comparing Files"
activeusersLDAP = []

for dn, entry in res[0]:
    if 'uid' in entry:
        activeusersLDAP.append(entry['uid'][0])

bar = open('everymailboxplussize.txt', 'r')
f = open('everynonactivewithmailbox.txt', 'w')

allMailboxes = []

for each in bar:
    allMailboxes.append(each)

for each in allMailboxes:
    if not each.split(',')[1].rstrip() in activeusersLDAP:
        f.write(each.split(',')[0] + '\t' + each.split(',')[1])

bar.close()
f.close()
