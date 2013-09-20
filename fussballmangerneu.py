# -*- coding: utf-8 -*-
import rapidfanprogramm


geld=500
spieler=0

def spielerkauf(spieler,geld):
    if geld>=100:
            geld=geld-100
            spieler=spieler+1
            print ('du kaufst einen Spieler')
    else:
            print('Du hast nicht genügend Geld !')
    
    return spieler,geld
    
def spielerverkauf(spieler,geld):
    if spieler>0:
        print ('du verkaufst einen Spieler')
        geld=geld+150
        spieler=spieler-1
    else:
        print 'Du kannst keine Spieler verkaufen , da du keine besitzt.'
    return spieler,geld

def beobachten():
    print ('du beobachtest ein Spiel')
    return

def besuchen():
    print ('du besuchst jetzt das Stadion !')
    rapidfanprogramm.main()
    return

def verlassen():
   print ('du verlässt das Spiel')
   return







while True:
    print('')
    print('Willkommen , wollen Sie einen Spieler kaufen oder verkaufen oder bei Matches zuschauen , waehlen sie aus')
    print('0... Spiel verlassen')
    print('1... Spieler kaufen')
    print('2... Spieler verkaufen')
    print('3... Bei einem Match zuschauen')
    print('4... Spieler ins Trainingslager schicken')
    print('5... Stadion besuchen')
    print ('geld:',geld)
    print ('spieler:',spieler)
    
    antwort=raw_input('Deine Wahl ?')
    
    if antwort=='0':
       verlassen()
       break
    
    if antwort=='1':
        spieler,geld=spielerkauf(spieler,geld)
        
            
    if antwort=='2':
       spieler,geld=spielerverkauf(spieler,geld)
       

    if antwort=='3':
       beobachten()
       geld=geld-15
    
    
       
    
       
    if antwort=='4':
        print 'Du schickst deine Spieler jetzt ins Trainingslager !'
        
   

    if antwort=='5':
        besuchen()
        break
        
    
        




    
    
    
    
    
print ('Game Over')
