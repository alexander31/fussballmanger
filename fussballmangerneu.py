#-*- coding:utf-8 -*-
#from __future__ import print

import random


mannschaft=[] 
geld=1200
spieler=0
nummer_strafen=0


class Fussballer():
    nummer=0
    def __init__ (self,name):
        self.name=name
        self.nummer=Fussballer.nummer
        Fussballer.nummer+=1
        self.passgenauigkeit=random.random()
        self.elfmeter=random.random()
        self.kontrolle=random.random()
        self.laufgeschwindichkeit=random.random()
        self.gabberln=random.random()
        self.sprung=random.random()
        
    def hallo(self):
        print ('___________________________________________')
        print ('Name:                {}'.format(self.name))
        print ('Spielernummer:       {}'.format(self.nummer))
        print ('Passgenauigkeit:     {}'.format(beschreibung(self.passgenauigkeit)))
        print ('Elfmeterschuetze:    {}'.format(beschreibung(self.elfmeter)))
        print ('Ballkontrolle:       {}'.format(beschreibung(self.kontrolle)))
        print ('Laufgeschwindichkeit:{}'.format(beschreibung(self.laufgeschwindichkeit)))
        print ('Gabberln:            {}'.format(beschreibung(self.gabberln)))
        print ('Sprungkraft:         {}'.format(beschreibung(self.sprung)))
        
    def tabelle(self):
        return '| {} | {} | {} | {} | {} | {} | {} | {} |'.format(
                self.name +(15-len(self.name))*' ',
                ' '+str(self.nummer) if self.nummer<10 else self.nummer,
                beschreibung(self.passgenauigkeit),
                beschreibung(self.elfmeter),
                beschreibung(self.kontrolle),
                beschreibung(self.laufgeschwindichkeit),
                beschreibung(self.gabberln),
                beschreibung(self.sprung))
            
                
    def kopfzeile(self):
        return '+-----------------+----+-----+-----+-----+-----+-----+-----+\n| {} | {} | {} | {} | {} | {} | {} | {} |\n+-----------------+----+-----+-----+-----+-----+-----+-----+'.format(
                "name           ",
                "nr",
                "ps ",
                "11 ",
                "ko ",
                "lf ",
                "gb ",
                "sg ")
        
    def schlusszeile(self):
        return '+-----------------+----+-----+-----+-----+-----+-----+-----+'
        
    def legende(self):
        text="""
LEGENDE:
                                     +++...Sehr gut
        11...elfmeter                 ++...Gut
                                       +...Passt
                                      +~...Geht so
        ps...passgenauigkeit          ~-...Nicht so gut  
                                      ~~...Eine Schande !
        ko...kontrolle                -~...Naja
        lf...laufgeschwindichkeit      -...Schlecht
        gb...gabberln                 --...Sehr schlecht
        sg...sprungkraft'            ---...Super schlecht
            
        
"""
        #print 'LEGENDE:'
        #print ' '
        #return 'ps...passgenauigkeit\n11...elfmeter\nko...kontrolle\nlf...laufgeschwindichkeit\ngb...gabberln\nsg...sprungkraft\n'
        return text
    
           
    def veraendern(self, faktor=1.0):
        self.passgenauigkeit*=faktor
        self.elfmeter*=faktor
        self.kontrolle*=faktor
        self.laufgeschwindichkeit*=faktor
        self.gabberln*=faktor
        self.sprung*=faktor
        
        
        
        
def beschreibung(p):
    if p < 0.1:
        return '---'
    if p < 0.2:
        return '-- '
    if p < 0.3: 
        return '-  '
    if p < 0.4:
        return '-~ '
    if p < 0.5:
        return '~- '
    if p < 0.6:
        return '~~ '
    if p < 0.7:
        return '+~ '
    if p < 0.8:
        return '+  '
    if p < 0.9:
        return '++ '
    else:
        return '+++'

        
        
 
    
            
            

              
    
               
def spielerkauf(spieler,geld,mannschaft,level):
    if level == 1:
        if geld>=300:
            geld=geld-300
            spieler=spieler+1
                
            print ('')
            print ('------------------------')
            print ('du kaufst einen teuren Spieler')
            print ('------------------------')
            name=raw_input('Wie soll der neue Spieler heissen ?')
            mannschaft.append(Fussballer(name))
    
                
        else: 
            print('------------------------------')
            print('Du hast nicht genuegend Geld !')
            print('------------------------------')
            
    if level == 2:
        if geld>=200:
            geld=geld-200
            spieler=spieler+1
                
            print ('')
            print ('------------------------')
            print ('du kaufst einen mittelmaessigen Spieler')
            print ('------------------------')
            name=raw_input('Wie soll der neue Spieler heissen ?')
            f = Fussballer(name)
            f.veraendern(0.8)
            mannschaft.append(f)
 
        else: 
            print('------------------------------')
            print('Du hast nicht genuegend Geld !')
            print('------------------------------')
    
 
            
    if level == 3:
        if geld>=100:
            geld=geld-100
            spieler=spieler+1
                
            print ('')
            print ('------------------------')
            print ('du kaufst einen billigen Spieler')
            print ('------------------------')
            name=raw_input('Wie soll der neue Spieler heissen ?')
            f = Fussballer(name)
            f.veraendern(0.5)
            mannschaft.append(f)
    
                
        else: 
            print('------------------------------')
            print('Du hast nicht genuegend Geld !')
            print('------------------------------')
    
                
        
    
        
    return spieler,geld,mannschaft
    

def spielen(spielen1):
    w= random.randint(1,2)
    if w==1:
        print 'Gegner hat gewonnen,Deine Mannschaft hat gewonnen'
    else:
        print 'Der Gegener hat verloren,Deine Mannschaft hat verloren'
    



def strafe1(strafe):
    if geld>=100:
        geld=geld-100
        strafe=strafe+1
        print ('')
        print ('----------------------------------------------------------------------------')
        print ('Du musst jetzt Strafe zahlen  !')
        print ('----------------------------------------------------------------------------')
        
    else:
        print ('')
        print ('-----------------------------------------------')
        print ('Du hast Glueck ! Du musst keine Strafe zahlen !')
        print ('------------------------------------------------')
            
    return strafe,geld
    
    
    
def mannschaft_anschauen(mannschaft,geld):
    print ('')
    print ('-----------------------------')
    print ('Du schaust die Mannschaft an')
    print ('-----------------------------')
    
    
def spielerverkauf(spieler,geld):
    if spieler>0:
        print ('')
        print ('---------------------------')
        print ('du verkaufst einen Spieler')
        print ('---------------------------')
        geld=geld+150
        spieler=spieler-1
    else: 
        print('--------------------------------------------------------')
        print('Du kannst keine Spieler verkaufen , da du keine besitzt.')
        print('--------------------------------------------------------')
    return spieler,geld

def beobachten():
    print ('')
    print ('------------------------')
    print ('du beobachtest ein Spiel')
    print ('------------------------')
    return

def besuchen():
    print ('')
    print ('-------------------------------')
    print ('du besuchst jetzt das Stadion !')
    print ('-------------------------------')
    rapidfanprogramm.main()
    return
    
def gegner_anschauen(mannschaft):
    gegnermannschaften=['Salzburg','Austria','Sturm','Grödig']
    gegnerische_spieler={"Salzburg":
                      ["Kevin Kampl","Martin Hinteregger","Jonatan Soriano","Isaac Vorsah","Christoph Leitgeb",
                       "Stefan Hierländer","Dusan Svento","Andreas Ulmer","Franz Schiemer","Valon Berisha","Florian Klein"],
                       
                    "Austria":
                        ["Markus Suttner","Rubin Okotie","Lukas Rotpuller","Roman Kienast","Philipp Hosiner","Daniel Royer","Fabian Koch"
                        "Christian Ramsebner","Alexander Grünwald","Manuel Ortlechner","Florian Mader"],
                        
                    "Groedig":
                        ["Robert Strobl"," Stefan Nutz", "Marvin Potzmann", "Adnan Adilovic", "Kevin Fend", "Cican Stankovic",
                         "Simon Handle", "Philipp Huspek", "Thomas Salamon ","Mario Leitgeb", "Tadej Trdina"   ],  
                    
                    "Sturm":
                        ["Christian Gratzei","Milan Dudic","Andreas Hölzl","Robert Beric","Pascal Legat",
                         "Daniel Beicher","Marco Djuricin","Anel Hadzic","Nikola Vujadinovic","Benedikt Pliquett","Michael Madel"]}
    print'du siehst die Spieler der Mannschaft:',mannschaft
    for mann in gegnerische_spieler[mannschaft]:
        print (mann)

def verlassen():
   print ('')
   print ('---------------------')
   print ('du verlaesst das Spiel')
   print ('---------------------')
   return
   


def trainingslager():
    while True:
        
        print ('0...Trainingsmenue verlassen')
        print ('1...Elfmeter trainieren')
        print ('2...Ballkontrolle trainieren')
        print ('3...Passgenauigkeit verbessern')
        print ('4...Laufgeschwindichkeit verbessern')
        print ('5...Ausdauer trainieren')
        print ('6...Kondition verbessern')
        print ('7...Gabberln ueben')
        print ('8...Sprung erhoehen')
        print ('9...Spielen')
        print ('geld:{}'.format(geld))
        print ('spieler:{}'.format(spieler))
        print ('strafe:{}'.format(nummer_strafen))
        antwort=raw_input ('Deine Wahl ?')
        if antwort =='0':
            return
        elif antwort=='1':
            
            #elfmeter trainieren
            hofmann=0.9
            print ('')
            print ('------------------------------')
            print ('Du uebst Elfmeterschießen....')
            print ('------------------------------')
            for versuch in range(10):
                
                schuss=random.random()
                if schuss <=hofmann:
                    print ('')
                    print ('-----------')
                    print ('Getroffen !',schuss)
                    print ('-----------')
                else:
                    print ('')
                    print ('-------------------')
                    print ('Leider daneben...!',schuss)
                    print ('-------------------')
        elif antwort=='2':
            #ballkontrolle
            hofmann=0.5
            print ('')
            print ('-----------------------------')
            print ('Du kontrollierst den Ball....')
            print ('-----------------------------')
            for versuch in range (10):
                
                kontrolle=random.random()
                if kontrolle <=hofmann:
                    print ('')
                    print ('------------------------------------')
                    print ('Du kontrollierst sehr gut den Ball !',kontrolle)
                    print ('------------------------------------')
                else:
                    print ('------------------------------------')
                    print ('Das musst du noch ein bisschen ueben',kontrolle)
                    print ('------------------------------------')
                    
        elif antwort=='3':
            #passgenauigkeit
            hofmann =0.8
            print ('Du passt den Ball....')
            for versuch in range (10):
                
                passgenauigkeit=random.random()
                if passgenauigkeit<=hofmann:
                    print ('------------------------------')
                    print ('Du passt den Ball sehr genau !',passgenauigkeit)
                    print ('------------------------------')
                else:
                    print ('--------------------------------------')
                    print ('Das musst du noch ein bisschen ueben !',passgenauigkeit)
                    print ('--------------------------------------')
                    
        elif antwort=='4':
            #laufgeschwindichkeit
            hofmann =0.92
            print ('-------------')
            print ('Du laeufst...')
            print ('-------------')
            for versuch in range (10):
                
                laufgeschwindichkeit=random.random()
                if laufgeschwindichkeit<=hofmann:
                    print ('------------------------')
                    print ('Du laufst sehr schnell !',laufgeschwindichkeit)
                    print ('------------------------')
                else:
                    print ('--------------------------------------')
                    print ('Etwas schneller musst du noch werden !')
                    print ('--------------------------------------')
                    
        elif antwort=='7':
            #Gabberln
            hofmann =0.99
            print ('---------------')
            print ('Du gabberlst...')
            print ('---------------')
            for versuch in range (10):
                
                gabberln=random.random()
                if gabberln<=hofmann:
                    print ('----------------------------------')
                    print ('Du kannst schon sehr oft gaberln !',gabberln)
                    print ('----------------------------------')
                else:
                    print ('-----------------------------------')
                    print ('Etwas oefter könnte es noch gehen !')
                    print ('-----------------------------------')
                    
        elif antwort=='8':
            #sprung
            hofmann =0.75
            print ('--------------')
            print ('Du springst...')
            print ('--------------')
            for versuch in range (10):
                
                sprung=random.random()
                if sprung<=hofmann:
                    print ('-----------------------------')
                    print ('Du springst schon sehr hoch !',sprung)
                    print ('-----------------------------')
                else:
                    print ('------------------------------------------')
                    print ('Ich glaube das geht noch bisschen hoeher !')
                    print ('------------------------------------------')
                    
        elif antwort=='9':
            #spielen
            rapid=0.5
            print ('-----------------------------------------')
            print (' Deine Mannschaft hat begonnen zu spielen')
            print ('-----------------------------------------')
            for versuch in range (1):
                
                spielen=random.random()
                if spielen<=rapid:
                    print ('-------------------------------')
                    print ('Deine Mannschaft hat gewonnen !')
                    print ('-------------------------------')
                    
                else:
                    print ('-------------------------------')
                    print ('Deine Mannschaft hat verloren !')
                    print ('-------------------------------')
                
                
                
def erwischt(chance=0.1):
    if random.random()<chance:
        print ('------------------------------------------------')
        print ('Du wurdest erwischt ! Nun musst du Strafe zahlen')
        print ('------------------------------------------------')
        return True
    else:
        return False
        
def besterspieler(mannschaft):
    if len(mannschaft)>0:
        print 'Der beste Spieler ist :'+random.choice(mannschaft).name
    else:
        print 'Du musst erst einen Spieler kaufen um den besten Spieler sehen zu können !'    
    
        
    
        
            
        
            
    
        
       
    

def illegal(geld,nummer_strafen):
    while True:
        print ('                                                           RISIKO:')
        print ('0...Illegales Menue verlassen')
        print ('1...Schiri bestechen   (kann 100EURO kosten)...............SELTEN')
        print ('2...Pyrotechnik zuenden (kann 150EURO kosten)..............MANCHMAL')
        print ('3...Dose auf das Spielfeld werfen (kann 50EURO kosten).....NICHT OFT')
        print ('4...Hooligans informieren')
        print ('5...Gegnerischen Spieler verletzen (kann 200EURO kosten)...OFT')
        print ('6...Eigene Spieler dopen')
        print ('7...Generische Fans verletzen (kann 120EURO kosten)........OFT')
        print ('8...Platzsturm (kann 300EURO kosten).......................FAST IMMER')
        print ('geld:{}'.format(geld))
        print ('spieler: {}'.format(spieler))
        print ('strafen: {}'.format(nummer_strafen))
        
        antwort=raw_input ('Deine Wahl ? :  ')
        
        if antwort=='0':
           verlassen()
           return geld,nummer_strafen
           
        if antwort=='1':
            print (' ')
            print ('------------------------')
            print ('du bestichst den Schiri')
            print ('------------------------')
            print ('')
            if erwischt(0.2):
                nummer_strafen+=1
                geld-=100   
            else:
                print ('---------------------------')
                print ('Du wurdest nicht erwischt !')
                print ('---------------------------')
                
        if antwort=='2':
            print ('')
            print ('------------------------')
            print ('du zuendest Pyrotechnik')
            print ('------------------------')
            print ('')
            if erwischt(0.5):
                nummer_strafen+=1
                geld-=130
            else:
                print ('-------------------------')
                print ('Du wurdest nicht erwischt')
                print ('-------------------------')
            
        if antwort=='3':
            print ('')
            print ('----------------------------------------')
            print ('Du wirfst eine Dose auf das Spielfeld')
            print ('----------------------------------------')
            print ('')
            if erwischt(0.4):
                nummer_strafen+=1
                geld-=50
            else:
                print ('---------------------------')
                print ('Du wurdest nicht erwischt !')
                print ('---------------------------')
            
        if antwort=='4':
            print ('')
            print ('------------------------')
            print ('Du informierst Hooligans')
            print ('------------------------')
            print ('')
            
        if antwort== '5':
            print ('')
            print ('---------------------------------------')
            print ('Du verletzt einen generischen Spieler !')
            print ('---------------------------------------')
            print ('')
            if erwischt(0.7):
                nummer_strafen+=1
                geld-=250 
            else:
                print ('---------------------------')
                print ('Du wurdest nicht erwischt !')
                print ('---------------------------')
        
            
        if antwort== '6':
           print ('')
           print ('------------------------------------')
           print ('Du dopst jetzt einen eigenen Spieler')
           print ('------------------------------------')
           print ('')
           
        if antwort== '7':
           print ('')
           print ('----------------------------')
           print ('Du verletzt gegnerische Fans')
           print ('----------------------------')
           print ('')
           if erwischt(0.7):
                nummer_strafen+=1
                geld-=100 
           else:
                print ('---------------------------')
                print ('Du wurdest nicht erwischt !')
                print ('---------------------------')
           
        
        if antwort== '8':
            print ('')
            print ('-----------------------------------------------------------------')
            print ('Du veranstaltest einen Platzsturm fuer den du Strafe zahlen musst')
            print ('-----------------------------------------------------------------')
            print ('')
            if erwischt(0.9):
                nummer_strafen+=1
                geld-=265
            
            
            
            

            
#gegner
gegnermannschaften=['Salzburg','Austria','Sturm','Grödig']
generische_spieler={"Salzburg":
                      ["Kevin Kampl","Martin Hinteregger","Jonatan Soriano","Isaac Vorsah","Christoph Leitgeb",
                       "Stefan Hierländer","Dusan Svento","Andreas Ulmer","Franz Schiemer","Valon Berisha","Florian Klein"],
                       
                    "Austria":
                        ["Markus Suttner","Rubin Okotie","Lukas Rotpuller","Roman Kienast","Philipp Hosiner","Daniel Royer","Fabian Koch"
                        "Christian Ramsebner","Alexander Grünwald","Manuel Ortlechner","Florian Mader"],
                        
                    "Groedig":
                        ["Robert Strobl"," Stefan Nutz", "Marvin Potzmann", "Adnan Adilovic", "Kevin Fend", "Cican Stankovic",
                         "Simon Handle", "Philipp Huspek", "Thomas Salamon ","Mario Leitgeb", "Tadej Trdina"   ],  
                    
                    "Sturm":
                        ["Christian Gratzei","Milan Dudic","Andreas Hölzl","Robert Beric","Pascal Legat",
                         "Daniel Beicher","Marco Djuricin","Anel Hadzic","Nikola Vujadinovic","Benedikt Pliquett","Michael Madel"]}
while True:
    print('')
    print('Willkommen , wollen Sie einen Spieler kaufen oder verkaufen oder bei Matches zuschauen , waehlen sie aus')
    print('0... Spiel verlassen')
    print('1a...Teuren Spieler kaufen (300)')
    print('1b...Mittelmaessigen Spieler kaufen (200)')
    print('1c...Schlechten Spieler kaufen (100)')
    print('2... Spieler verkaufen')
    print('3... Bei einem Match zuschauen')
    print('4... Spieler ins Trainingslager schicken')
    print('5... Stadion besuchen')
    print('6... Traininglager besuchen')
    print('7... Illegale Handlungen')
    print('8... Eigene Mannschaft anschauen')
    print('9a.. Salzburg anschauen')
    print('9b.. Austria anschauen')
    print('9c.. Groedig anschauen')
    print('9d.. Sturm anschauen')
    print('10.. Besten Spieler wählen')
    print('geld: {}'.format(geld))
    print('spieler: {}'.format(spieler))
    print('strafen: {}'.format(nummer_strafen))
    z = 0
    for mann in mannschaft:
        if z== 0:
            print mann.kopfzeile()
        z+=1
        #print (mann.name)
        #mann.hallo()
        print mann.tabelle()
        if z== len(mannschaft):
            print mann.schlusszeile()
            print mann.legende()
    
    
    antwort=raw_input ('Deine Wahl ? :  ')
    
    if antwort=='0':
       verlassen()
       break
    
    if antwort=='1a':
        spieler,geld,mannschaft=spielerkauf(spieler,geld,mannschaft,1)
        
    if antwort=='1b':
        spieler,geld,mannschaft=spielerkauf(spieler,geld,mannschaft,2)
        
    if antwort=='1c':
        spieler,geld,mannschaft=spielerkauf(spieler,geld,mannschaft,3)
        
            
    if antwort=='2':
       spieler,geld=spielerverkauf(spieler,geld)
       

    if antwort=='3':
       beobachten()
       geld=geld-15
    
    
    if antwort=='4':
        print ('')
        print ('----------------------------------------------------')
        print ('Du schickst deine Spieler jetzt ins Trainingslager !')
        print ('----------------------------------------------------')
        
   

    if antwort=='5':
        besuchen()
        break
        
    if antwort=='6':
        trainingslager()
        
    if antwort=='7':
        geld,nummer_strafen=illegal(geld,nummer_strafen)
        
        
    if antwort=='9a':
        gegner_anschauen('Salzburg')
        
    if antwort=='9b':
        gegner_anschauen('Austria')
    
    if antwort=='9c':
        gegner_anschauen('Groedig')
        
    if antwort=='9d':
        gegner_anschauen('Sturm')
        
    if antwort=='10':
        besterspieler(mannschaft)
        
   
        
        
        
        
        
    
        




    
    
    
print ('---------')
print ('---------')
print ('Game Over')
print ('---------')
print ('---------')
