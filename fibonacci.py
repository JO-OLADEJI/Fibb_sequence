def fibb(term):
    first, second = 0, 1
    if int(term) > 0 and int(term) <= 2:
        return term
    elif int(term) < 0:
        print('Negative terms in a Fibonacci Sequence don\'t exist')
        return term
    else:
        for i in range((int(term) -2)):
            answer = second + first
            temp = second
            second = answer
            first = temp
        return answer
print('Enter Exit to cancel...')
while True:
    term = input('Enter the number of Term: ').capitalize()
    if term == 'Exit':
        break
    if term[-1] == '1':
        ending = 'st'
    elif term[-1] == '2':
        ending = 'nd'
    elif term[-1] == '3':
        ending = 'rd'
    else:
        ending = 'th'
    try:
        print('The ' + str(term) + ending + ' Term of a Fibonacci Sequence is ' + str(fibb(term)))
    except:
        print('Error: Invalid Input')
bye = input()
