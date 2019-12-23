import shelve, re, os, datetime

# bre = re.compile(r'(\\d{1,2})-(\\d{1,2})')
d = datetime.date.today().day, datetime.date.today().month
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


def upcomming():
    c = datetime.date.today().month
    v = (c + 1 if c+1 < 13 else 1)
    lowest = min([int(i.split('-')[0]) for i in birthdays.values()])

    to_return = [(i + ' : ' + j) for (i,j) in birthdays.items() if int(j.split('-')[0]) == c
                 or int(j.split('-')[0]) == v
                 or int(j.split('-')[0]) == lowest]
    return to_return


x = False
while not x:
    usr = input('''\nEnter 'u' to print all upcoming birthdays 
      ||| Enter 's' to search for a particular name or month
      \n Enter 'a' to add 
      ||| Enter 'c' to change an entry ||| Enter 'q' to quit''')
    if usr == 'u':
        print(upcomming())
    if usr == 'q':
        x = True

birthdays.close()
quit()
