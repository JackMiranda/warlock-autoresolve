from numpy.random import randint
from sys import stdout
import time

FACE = {
   1 : [
' ┏━━━━━━━┓ ',
' ┃       ┃ ',
' ┃   ◆   ┃ ',
' ┃       ┃ ',
' ┗━━━━━━━┛ '
],
   2 : [
' ┏━━━━━━━┓ ',
' ┃ ◆     ┃ ',
' ┃       ┃ ',
' ┃     ◆ ┃ ',
' ┗━━━━━━━┛ '
],
   3 : [
' ┏━━━━━━━┓ ',
' ┃ ◆     ┃ ',
' ┃   ◆   ┃ ',
' ┃     ◆ ┃ ',
' ┗━━━━━━━┛ '
],
   4 : [
' ┏━━━━━━━┓ ',
' ┃ ◆   ◆ ┃ ',
' ┃       ┃ ',
' ┃ ◆   ◆ ┃ ',
' ┗━━━━━━━┛ '
],
   5 : [
' ┏━━━━━━━┓ ',
' ┃ ◆   ◆ ┃ ',
' ┃   ◆   ┃ ',
' ┃ ◆   ◆ ┃ ',
' ┗━━━━━━━┛ '
],
   6 : [
' ┏━━━━━━━┓ ',
' ┃ ◆   ◆ ┃ ',
' ┃ ◆   ◆ ┃ ',
' ┃ ◆   ◆ ┃ ',
' ┗━━━━━━━┛ '
]}

"""
  09 skill      11 skill
 ┏━━━━━━━┓  │  ┏━━━━━━━┓ 
 ┃ ◆   ◆ ┃  │  ┃ ◆   ◆ ┃ 
 ┃   ◆   ┃  │  ┃       ┃  
 ┃ ◆   ◆ ┃  │  ┃ ◆   ◆ ┃  
 ┗━━━━━━━┛  │  ┗━━━━━━━┛  
 ┏━━━━━━━┓  │  ┏━━━━━━━┓ 
 ┃ ◆   ◆ ┃  │  ┃ ◆   ◆ ┃ 
 ┃   ◆   ┃  │  ┃   ◆   ┃  
 ┃ ◆   ◆ ┃  │  ┃ ◆   ◆ ┃  
 ┗━━━━━━━┛  │  ┗━━━━━━━┛  
   Roll:    │     Roll:
    10      │      09
            │
       Player hit!
            │
   ┌──┐     │     ┌──┐
   │██│     │     |█ |
   │██│     │     |██|
   │██│     │     |██|
   │██│     │     |██|
   │██│     │     |██|
   │██│     │     |██|
   │██│     │     |██|
   │██│     │     |██|
   │██│     │     |██|
   │██│     │     |██|
   │██│     │     |██|
   │██│     │     |██|
  Player    │    Monster
    24      │      23
 
     MONSTER DEFEATED 
""" 

def staminaBar(fill):
    segs = []
    for _ in range(12):
        if fill <= 0:
            segs.append('   │  │   ')
        elif fill == 1:
            segs.append('   │█ │   ')
        else:
            segs.append('   │██│   ')
        fill -= 2
    segs.append('   ┌──┐   ')
    return segs[::-1]

def printBars(playerStamina, monsterStamina):
    sep = ['  │  ' for _ in range(13)]
    for line in list(zip(staminaBar(playerStamina),sep,staminaBar(monsterStamina))):
        for seg in line:
            stdout.write(seg)
        stdout.write('\n')
    print('  Player    │    Monster')
    print('    {}      │      {}\n'.format(str(playerStamina).zfill(2),str(monsterStamina).zfill(2)))
    return


def printPair(l, r):
   sep = [' │ ',' │ ',' │ ',' │ ',' │ ']
   for line in list(zip(FACE[l],sep,FACE[r])):
       for seg in line:
           stdout.write(seg)
       stdout.write('\n')
   return

def printRolls(playerRoll, monsterRoll,playerSkill,monsterSkill):
    tl,bl = playerRoll
    tr,br = monsterRoll
    printPair(tl,tr)
    printPair(bl,br)
    print('   Roll:    │     Roll:')
    print(' {}+{}={}   │   {}+{}={}'.format(
            str(tl+bl).zfill(2),
            str(playerSkill).zfill(2),
            str(tl+bl+playerSkill).zfill(2),
            str(tr+br).zfill(2),
            str(monsterSkill).zfill(2),
            str(tr+br+monsterSkill).zfill(2)
        )
    )
    return

def roll():
    return randint(1,7)

def flushAndReset():
    stdout.flush()
    for _ in range(34):
        stdout.write('\033[A\r')

def printBoard(playerRoll,playerStamina,playerSkill,monsterRoll,monsterStamina,monsterSkill,hitText,defeatedText):
    flushAndReset()
    print('  {} skill      {} skill'.format(str(playerSkill).zfill(2),str(monsterSkill).zfill(2)))
    printRolls(playerRoll,monsterRoll,playerSkill,monsterSkill)
    print('            │')
    print('       {}'.format(hitText))
    print('            │')
    printBars(playerStamina,monsterStamina)
    print('     {}'.format(defeatedText))
    return

def rollAnimation(playerRoll,playerStamina,playerSkill,monsterRoll,monsterStamina,monsterSkill,hitText,defeatedText):
    for _ in range(6):
        randPlayerRoll  = roll(),roll()
        randMonsterRoll = roll(),roll()
        printBoard(randPlayerRoll,playerStamina,playerSkill,randMonsterRoll,monsterStamina,monsterSkill,'    ...      ',defeatedText)
        print('')
        time.sleep(0.12)
    return

def printStep(playerRoll,playerStamina,playerSkill,monsterRoll,monsterStamina,monsterSkill,hitText,defeatedText):
    printBoard(playerRoll,playerStamina,playerSkill,monsterRoll,monsterStamina,monsterSkill,hitText,defeatedText)
    input('       Continue...')
    if playerStamina > 0 and monsterStamina > 0:
        rollAnimation(playerRoll,playerStamina,playerSkill,monsterRoll,monsterStamina,monsterSkill,hitText,defeatedText)

def test():
    [print('') for _ in range(34)]
    printStep(
        playerRoll     = (1,2),
        playerStamina  = 13,
        playerSkill    = 9,
        monsterRoll    = (3,5),
        monsterStamina = 23,
        monsterSkill   = 12,
        hitText        = 'Player hit!',
        defeatedText   = 'MONSTER DEFEATED'
    )
    printBoard(
        playerRoll     = (3,3),
        playerStamina  = 13,
        playerSkill    = 9,
        monsterRoll    = (1,1),
        monsterStamina = 22,
        monsterSkill   = 12,
        hitText        = 'Player hit!',
        defeatedText   = 'MONSTER DEFEATED'
    )
    input('     Continue...')

def main():
    playerSkill    = int(input('Player skill:    '))
    playerStamina  = int(input('Player stamina:  '))
    monsterSkill   = int(input('Monster skill:   '))
    monsterStamina = int(input('Monster stamina: '))
    print('')
    [print('') for _ in range(34)]

    playerRoll   = roll(),roll()
    monsterRoll  = roll(),roll()

    printStep(
        playerRoll     = playerRoll,
        playerStamina  = playerStamina,
        playerSkill    = playerSkill,
        monsterRoll    = monsterRoll,
        monsterStamina = monsterStamina,
        monsterSkill   = monsterSkill,
        hitText        = '   READY    ',
        defeatedText   = ''
    )
    
    dead = False
    while not dead:
        hitText = ''
        defeatedText = ''

        playerRoll   = roll(),roll()
        monsterRoll  = roll(),roll()
        playerScore  = playerSkill  +  playerRoll[0] +  playerRoll[1]
        monsterScore = monsterSkill + monsterRoll[0] + monsterRoll[1]

        if playerScore == monsterScore:
            hitText = '   Miss!     '
        elif playerScore > monsterScore:
            hitText = 'Player hits! '
            monsterStamina -= 2
        elif playerScore < monsterScore:
            hitText = 'Monster hits!'
            playerStamina -= 2

        if playerStamina <= 0:
            defeatedText = 'PLAYER DEFEATED!'
            dead = True
        if monsterStamina <= 0:
            defeatedText = 'MONSTER DEFEATED'
            dead = True
            
        printStep(
            playerRoll     = playerRoll,
            playerStamina  = playerStamina,
            playerSkill    = playerSkill,
            monsterRoll    = monsterRoll,
            monsterStamina = monsterStamina,
            monsterSkill   = monsterSkill,
            hitText        = hitText,
            defeatedText   = defeatedText
        )
    
if __name__ == '__main__':
    main()
        

