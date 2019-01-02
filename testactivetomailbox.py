foo = open('activeusersLDAP.txt', 'r')
bar = open('everymailboxplussize.txt', 'r')
f = open('everynonactivewithmailbox.txt', 'w')

activeUsers = []
allMailboxes = []

for each in foo:
    activeUsers.append(each)

for each in bar:
    allMailboxes.append(each)

for each in allMailboxes:
    if not each.split(',')[1] in activeUsers:
        f.write(each.split(',')[0] + '\t' + each.split(',')[1])

