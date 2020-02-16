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
    ['passat perfet : nosaltres','hagim cantat'],
    ['passat perfet : vosaltres','hagiu cantat'],
    ['passat perfet : ells/elles','hagin cantat'],
    ['Imperfet : jo', 'cantes'],
    ['Imperfet : tu','cantessis'],
    ['Imperfet :ell/ella','cantes'],
    ['Imperfet : nosaltres','cantessim'],
    ['Imperfet : vosaltres','cantessiu'],
    ['Imperfet : ells/ellas','cantessin'],
    ['Passat plusquamperfet : jo', 'hagues cantat'],
    ['Passat plusquamperfet : tu','haguessis cantat'],
    ['Passat plusquamperfet : ell/ella','hagues cantat'],
    ['Passat plusquamperfet : nosaltres','haguessim cantat'],
    ['Passat plusquamperfet : vosaltres','haguessiu cantat'],
    ['passat plusquamperfet : ells/ellas','haguessin cantat'],
    ['Imperatiu', 'canta,canti,cantem,canteu,cantin'],
    ['Infinitiu','cantar'],
    ['infinitiu perfet','haver cantat'],
    ['gerundi','cantant'],
    ['gerundi perfet','havent cantat'],
    ['participi','cantat,cantada,cantats,cantades']
    ['present indicatiu : jo','canto']
    ['present indicatiu : tu','cantes']
    ['present indicatiu : ell/ella','canta']
    ['present indicatiu : nosaltres','cantem']
    ['present indicatiu : vosaltres','canteu']
    ['present indicatiu : ells,elles','canten']
    ['preterit imperfet indicatiu : jo','cantava']
    ['preterit imperfet indicatiu : tu','cantaves']
    ['preterit imperfet indicatiu : ell/ella','cantava']
    ['preterit imperfet indicatiu : nosaltres','cantavem']
    ['preterit imperfet indicatiu : vosaltres','cantaveu']
    ['preterit imperfet indicatiu : ells/elles','cantaven']
    ['passat simple : jo','canti']
    ['passat simple : tu','cantares']
    ['passat simple : ell/ella','canta']
    ['passat simple : nosaltres','cantarem']
    ['passat simple : vosaltres','cantareu']
    ['passat simple : ells/elles','cantaren']
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
