from pathlib import Path

# throws IOError
def readUsersFromFile():
    l =[]
    users = dict()
    l.append(str(Path(__file__).parents[1]))
    l.append(r'\users.txt')
    filePath = ''.join(l)
    try:
        file = open(filePath, 'r')
    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))
        raise
    while True:
        email = file.readline()
        if email == '':
            break
        password = file.readline()
        if password == '':
            break
        newUser = {email: password}
        users.update(newUser)
    file.close()
    return users



