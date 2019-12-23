# Makes a shelve database of birthdays.txt, a list in format:
# 'First_Last 12-05'
# i.e December 5
# Updates the database on subsequent runs if any additions/changes
# to the original .txt
# Run on startup for quick update on upcomming birthdays

import shelve, re, os, datetime

# bre = re.compile(r'(\\d{1,2})-(\\d{1,2})')

birthdays = shelve.open('birthdays')

if 'birthdays.dir' not in os.listdir():
    print('Creating the birthday database...')

    original_b = open('birthdays.txt')
    line = original_b.readline().strip()
    while line != '':
        split = line.split()
        birthdays[split[0]] = split[1]
        line = original_b.readline().strip()
    original_b.close()
    print('Done!')
else:
    print('\nChecking for updates to the original bday file...')
    original_b = open('birthdays.txt')
    line = original_b.readline().strip()
    while line != '':
        split = line.split()
        if split[0] not in birthdays:
            birthdays[split[0]] = split[1]
            print('\nAdding: ', split)
        elif birthdays[split[0]] != split[1]:
            print('Changing '+split[0]+'s bday to: ', split[1])
            birthdays[split[0]] = split[1]

        line = original_b.readline().strip()
    original_b.close()

def upcomming():
    c = datetime.date.today().month
    v = (c + 1 if c+1 < 13 else 1)
    lowest = min([int(i.split('-')[0]) for i in birthdays.values()])

    to_return = [(i + ' : ' + j) for (i,j) in birthdays.items() if int(j.split('-')[0]) == c
                 or int(j.split('-')[0]) == v
                 or int(j.split('-')[0]) == lowest]
    return to_return


print('\n\t*** Upcoming Birthdays ***')
ok = upcomming()
for i in ok:
    print('\n'+'\t\t'+i)


birthdays.close()
quit()
