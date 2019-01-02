#
# Testing sort on the first variable and number

import re, operator, argparse

# Argument parser section
parser = argparse.ArgumentParser(description='Get arguments for mods.')
parser = argparse.ArgumentParser()
parser.add_argument('--count', type=int, help='Number of mailboxes to display. Default is 40.', default=40)
args = parser.parse_args()

f = open("everymailboxsize.txt", "r")
message = f.read()
messagearray = message.split('\n')[:-1]
message_dict = {}

f.close()

for each in messagearray:
    if 'G' in each.split('\t')[0]:
        message_dict[each.split('\t')[1].split('/')[2]] = float(re.sub("[^0-9.]", "", each.split('\t')[0]))

count = 0
for k,v in sorted(message_dict.iteritems(), key=operator.itemgetter(1), reverse=True):
    if count > args.count:
        break
    print '{0}\t{1}GB\t{2}'.format(count,int(round(v)), k)
    count = count + 1

f = open("everymailbox.txt", "w")
b = open("everymailboxplussize.txt", "w")

for each in messagearray:
    f.write(each.split('\t')[1].split('/')[2] + '\n')
    b.write(each.split('\t')[0] + ',' + each.split('\t')[1].split('/')[2] + '\n')

f.close()
b.close()
