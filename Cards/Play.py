'''
Created on Jan 28, 2014

@author: t-darren.kiely
'''
import deck
from random import randint
import sys
import time
import shelve
import msgpack 

if __name__ == '__main__':
    pass
top = 21
db=shelve.open("Jack.txt")

playerm=db ['money']
count=0
bet=int(raw_input("Place your bet: "))
playerm=playerm-bet
game = deck.deck()
one = game.SelectCard(randint(0, 51))
two = game.SelectCard(randint(0, 51))
play=one
dealer=two
resd = "h"
res = "h"
p=game.SelectCard(randint(0, 51))
q=game.SelectCard(randint(0, 51))
if play==11 and p==11:
    play+=1
else:
    play+=p
    
if dealer==11 and q==11:
    dealer+=1
else:
    dealer+=q
    
if one==p:
    print "%d  %d"%(one,p)
    split=raw_input("Would you like to split? y/n")
    if split=='y':
        play1=p
        ress='h'
        while ress=='h':
            next_card=game.SelectCard(randint(0,51))
            print play1
            
            if play1 > 21:
                print"You are bust"
                ress="s"
            
            
            elif play1 < 21:
            
                ress = str(raw_input("Hit or stand?<h/s>"))
                if ress == "h":
                    play1 += next_card
                    ress = "h"
                else:
                    ress = "s"
            
            else:
                print"You are on 21"
                ress="s"
            if ress == "s":
                if play<=21:
                    print"you stood at %d" % play
                else:
                    print"Bust"    
    else:
        pass
        
            
  '''wish'''  
    
if play == 21:
    playerm+=bet*3
    db['money']=playerm
    print "Player 1 BLACKJACK"
    sys.exit("Game Over")
    playerm+=bet*3
    db['money']=playerm
    print playerm
elif dealer == 21:
    print "Dealer BLACKJACK"
    sys.exit("Game Over")

while res == "h":
    count+=1
    
    next_card=game.SelectCard(randint(0, 51))
    if count ==1 and next_card==11:
        print play
        
        
   
    
    
        
    
 
        
    print play

    if play > 21:
            print"You are bust"
            res="s"
            
            
    elif play < 21:
            
            
            res = str(raw_input("Hit or stand?<h/s>"))
            if next_card==11 and play<=10:
                choice=int(raw_input("Drew an ace do you want 1 or 11?"))
                if choice==1:
                    play+=1
                elif choice==11:
                    play+=11
                else:
                    print "idiot"
            elif next_card==11 and play>10:
                play+=1       
            elif res == "h":
                play += next_card
                res = "h"
            else:
                res = "s"
            
    else:
        print"You are on 21"
        res="s"
    
if res == "s":
    if play<=21:
        print"you stood at %d" % play
    while resd == "h":
        next_card = game.SelectCard(randint(0, 51))
        
        print "Dealer is on %d" % dealer
        if dealer>=11 and next_card==11 and dealer<=play:
            dealer+=1
            print "Dealer hits"
        elif dealer > 21 and play <= 21:
            print "Dealer busts. YOU WIN!!"
            resd = "s"
        elif dealer<21 and play>21:
            print "Dealer stands. Dealer wins"
            resd="s"
        elif dealer > 21 and play > 21:
            print "PUSH"
            resd="s"
        elif dealer < 16:
            resd = "h"
            dealer += next_card
            print "Dealer hits"
        elif dealer <= play and dealer<19:
            resd = "h"
            dealer += next_card
            print"Dealer hits"
        elif dealer <=play and dealer>=19:
            resd="s"
            print "Dealer stands"
        elif dealer > play:
            resd = "s"
            print"Dealer stands"
    time.sleep(1)
            
if resd == "s" and res == "s":
    if play > dealer and play <= 21 and dealer <= 21:
        playerm+=bet*2
        db['money']=playerm
        print 'You now have this much money %d'%playerm
        sys.exit("Player 1 wins")
    elif play < dealer and play <= 21 and dealer <= 21:
        db['money']=playerm
        print 'You now have this much money %d'%playerm
        sys.exit("Dealer Wins!")
         
    elif play>21 and dealer<21:
        print "You now have this much money %d"% playerm
        db['money']=playerm
        sys.exit("Dealer wins")
     
    elif dealer>21 and play<21:
        playerm+=bet*2
        db['money']=playerm
        print "You now have this much money %d" %playerm
        sys.exit("Dealer bust you win")
    elif dealer==play:
        playerm+=bet
        print 'PUSH You now have this much money %d'%playerm
        sys.exit("PUSH")
        
        

