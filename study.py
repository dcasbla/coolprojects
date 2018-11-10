import random

m = -1
score =0

exam = [
    ['Present', 'canti,cantis,canti,cantem,canteu,cantin'],
    ['Passat perfet', 'hagi cantat'],
    ['Imperfet', 'cantés'],
    ['Passat plusquamperfet', 'hagués cantat'],
    ['Imperatiu', 'canta'],
    ['Infinitiu','cantar'],
    ['infinitiu perfet','haver cantat'],
    ['gerundi','cantant'],
    ['gerundi perfet','havent cantat'],
    ['participi','cantat,cantada,cantats,cantades']
]

while(True):
    i = random.randint(0,len(exam)-1)
    value = exam[i][0]
    answer = exam[i][1]
    if (m != i):
        m = i
        print('Score: ' + str(score))
        x = input('quin es el '+ value + ': ')
        print('\n' * 10000)
        if answer == x:
            print ('correcte')
            score += 1
            if (score == 25):
                print('You mastered the verbs!!!!')
                break
        else:
            print ('Incorrecte, el ' + value + ' és: ' + answer)
            score = 0
