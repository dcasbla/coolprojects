import random
m = -1
score =0

exam = [
    ['Present : jo', 'canti'],
    ['present : tu','cantis'],
    ['present : ell/ella','canti'],
    ['present : nosaltres','cantem'],
    ['present : vosaltres','canteu'],
    ['present : ells/elles','cantin'],
    ['Passat perfet : jo', 'hagi cantat'],
    ['passat perfet : tu','hagis cantat'],
    ['passat perfet : ell/ella','hagi cantat'],
    ['passat perfet : nosaltres','hàgim cantat'],
    ['passat perfet : vosaltres','hàgiu cantat'],
    ['passat perfet : ells/elles','hagin cantat'],
    ['Imperfet : jo', 'cantés'],
    ['Imperfet : tu','cantessis'],
    ['Imperfet :ell/ella','cantés'],
    ['Imperfet : nosaltres','cantéssim'],
    ['Imperfet : vosaltres','cantéssiu'],
    ['Imperfet : ells/ellas','cantessin'],
    ['Passat plusquamperfet : jo', 'hagués cantat'],
    ['Passat plusquamperfet : tu','haguessis cantat'],
    ['Passat plusquamperfet : ell/ella','hagués cantat'],
    ['Passat plusquamperfet : nosaltres','haguéssim cantat'],
    ['Passat plusquamperfet : vosaltres','haguéssiu cantat'],
    ['passat plusquamperfet : ells/ellas','haguessin cantat'],
    ['Imperatiu', 'canta,canti,cantem,canteu,cantin'],
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
