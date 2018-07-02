import datetime
import pygame,sys
from pygame.locals import*
from pygame import mixer
import time
import os
import subprocess
import webbrowser

mixer.init()
mixer.music.load("click.wav")

running = True
now = datetime.datetime.now()

#ICONS
allapps= pygame.image.load('AllApps.png')
bankicon= pygame.image.load('bank.png')
calcuicon= pygame.image.load('calcu.png')
calendicon= pygame.image.load('calender.png')
carrenticon= pygame.image.load('carrent.png')
chromeicon= pygame.image.load('chrome.png')
expediaicon= pygame.image.load('expedia.png')
hotelicon= pygame.image.load('hotel.png')
mailicon= pygame.image.load('mail.png')
musicicon= pygame.image.load('music.png')
resticon= pygame.image.load('restaurant.png')
gamesicon=pygame.image.load('games.png')
booksicon=pygame.image.load('books.png')
youticon=pygame.image.load('youtube.png')
ticicon=pygame.image.load('tic.png')
guessicon=pygame.image.load('guess.png')
homebttn=pygame.image.load('AHome.png')
quizicon=pygame.image.load('quiz.png')

#SCREENS
Homescrn = pygame.image.load('AHomescrn.png')
Homescrn2 = pygame.image.load('AHomescrn2.png')
Gamescrn = pygame.image.load('AGamescrn.png')
calcload=pygame.image.load('ACalcLoad.png')
booksload=pygame.image.load('ABooksLoad.png')
bankload=pygame.image.load('ABankLoad.png')
calenload=pygame.image.load('ACalendarLoad.png')
musicload=pygame.image.load('AMusicLoad.png')
carload=pygame.image.load('ACarLoad.png')
hotelload=pygame.image.load('AHotelLoad.png')
restload=pygame.image.load('ARestLoad.png')
chromeload=pygame.image.load('AChromeLoad.png')
youtload=pygame.image.load('AYoutLoad.png')
expedload=pygame.image.load('AExpedLoad.png')
mailload=pygame.image.load('AMailLoad.png')
guessload=pygame.image.load('AGuessLoad.png')
quizload=pygame.image.load('AQuizLoad.png')
ticload=pygame.image.load('ATicLoad.png')
Mailscrn=pygame.image.load('AMailscrn.png')


#MailStuff
yahoo=pygame.image.load('yahoo.png')
aol=pygame.image.load('aol.png')
outlook=pygame.image.load('outlook.png')
rediff=pygame.image.load('rediff.png')
gmail=pygame.image.load('gmail.png')

#Random
cir1=pygame.image.load('cir1.png')
cir2=pygame.image.load('cir2.png')
cir3=pygame.image.load('cir3.png')
cir4=pygame.image.load('cir4.png')
Next=pygame.image.load('Arrow.png')
Previous=pygame.image.load("Arrow(1).png")

x=778
y=157
os.environ['SDL_VIDEO_WINDOW_POS']='%d,%d' %(x,y)
w = 365
h = 767
screen = pygame.display.set_mode([w, h])



location="home"    
    

   
x = y = 0


pygame.init()


black = (0,0,0)
WHITE=(255,255,255)
blue=(0,0,255)

pygame.init()
font = pygame.font.SysFont("Monospace", 70)
font2 = pygame.font.SysFont(None, 20)

def home(location):
    running = True
    pygame.draw.rect(screen,blue,(48,164,58,58))
    while running and location=='home':
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

        dt=str(datetime.datetime.today())
        time = dt[11:19]
        hr = dt[11:13]
        min = dt[14:16]
        fontimg = font.render(hr,3,WHITE)
        fontimg1 = font.render(min,3,WHITE)
        fontimg2 = font.render(":",3,WHITE)
        screen.blit(fontimg, (100,192))
        screen.blit(fontimg1, (195,192))
        screen.blit(fontimg2, (165,188))
        pygame.time.delay(0)
        pygame.display.update() 
        
        
        Homescrn2 = pygame.image.load('AHomescrn2.png')
        screen.blit(Homescrn2,(0,0))
        allapps= pygame.image.load('allapps.png')
        Homebttn=screen.blit(homebttn,(154,710))
        allapps=screen.blit(allapps,(164,600))
        pygame.display.flip()
        #pygame.time.delay(500)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
                pygame.quit()
                quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click
                #mixer.music.play(0)
                X= pygame.mouse.get_pos()
                print ("Click: "),X
                print (X[0],X[1])
                
                if allapps.collidepoint(X[0],X[1]):
                    
                   
                    location = 'home1'
                    home1(location)

def home1(location):
    running = True
    pygame.draw.rect(screen,blue,(48,164,58,58))
    while running and location=='home1':
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        screen.blit(Homescrn,(0,0))
        #Column 1
        Calendar=screen.blit(calendicon,(48,163))
        screen.blit(font2.render("Calendar",1,WHITE), (50,225))
        Restaurant=screen.blit(resticon,(45,254))
        screen.blit(font2.render("Oriental",1,WHITE), (45,310))
        Bank=screen.blit(bankicon,(45,343))
        screen.blit(font2.render("Ex.Banks",1,WHITE), (47,400))
        Youtube=screen.blit(youticon,(45,423))
        screen.blit(font2.render("Youtube",1,WHITE), (46,478))
        Calculator=screen.blit(calcuicon,(44,580))
        screen.blit(font2.render("Calculator",1,WHITE), (43,640))
        #Column 2
        Mail=screen.blit(mailicon,(157,163))
        screen.blit(font2.render("Mail",1,WHITE), (167,218))
        Hotel=screen.blit(hotelicon,(157,253))
        screen.blit(font2.render("Hotel",1,WHITE), (166,310))
        Books=screen.blit(booksicon,(157,343))
        screen.blit(font2.render("Books",1,WHITE), (165,400))
        Chrome=screen.blit(chromeicon,(156,580))
        screen.blit(font2.render("Chrome",1,WHITE), (160,640))
        #Column 3
        Expedia=screen.blit(expediaicon,(266,167))
        screen.blit(font2.render("Expedia",1,WHITE), (269,221))
        CarRent=screen.blit(carrenticon,(265,254))
        screen.blit(font2.render("CRS",1,WHITE), (279,313))
        Games=screen.blit(gamesicon,(265,343))
        screen.blit(font2.render("Games",1,WHITE), (270,400))
        Music=screen.blit(musicicon,(265,583))
        screen.blit(font2.render("Music",1,WHITE), (271,640))
        #------------------------------------------#
        Homebttn=screen.blit(homebttn,(154,710))
        pygame.display.flip()
        #event = pygame.event.poll()
        

               

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
                pygame.quit()
                quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click
                #mixer.music.play(0)
                X= pygame.mouse.get_pos()
                print ("Click: "),X
                print (X[0],X[1])
                
                if Bank.collidepoint(X[0],X[1]):
                    
                   
                    location = 'bank'
                    bank(location)
                    
                elif Calculator.collidepoint(X[0],X[1]):
                    
                    
                    location = 'calculator'
                    calculator(location)
                    
                elif Calendar.collidepoint(X[0],X[1]):
                    
                    
                    location = 'calendar'
                    calendar(location)
                    
                elif CarRent.collidepoint(X[0],X[1]):
                    
                    
                    location = 'carrent'
                    carrent(location)
                    
                elif Chrome.collidepoint(X[0],X[1]):
                    
                    
                    location = 'chrome'
                    chrome(location)
                    
                elif Expedia.collidepoint(X[0],X[1]):
                    
                    
                    location = 'expedia'
                    expedia(location)
                    
                elif Hotel.collidepoint(X[0],X[1]):
                    
                    
                    location = 'hotel'
                    hotel(location)
                    
                elif Mail.collidepoint(X[0],X[1]):
                    
                   
                    location = 'mail'
                    mail(location)
                    
                elif Music.collidepoint(X[0],X[1]):
                    
                    
                    location = 'music'
                    music(location)
                    
                elif Restaurant.collidepoint(X[0],X[1]):
                    
                    
                    location = 'restaurant'
                    restaurant(location)
                    
                elif Books.collidepoint(X[0],X[1]):
                    
                    location = 'books'
                    books(location)
                    
                elif Games.collidepoint(X[0],X[1]):
                    
                    
                    location = 'games'
                    games(location)
                    
                elif Youtube.collidepoint(X[0],X[1]):
                    
                    
                    location = 'youtube'
                    youtube(location)
                elif Homebttn.collidepoint(X[0],X[1]):
                    location='home'
                    home(location)


def bank(location):
    running = True
    pygame.draw.rect(screen,blue,(48,164,58,58))
    Loadscr=screen.blit(bankload,(0,0))
    Homebttn=screen.blit(homebttn,(154,710))
    pygame.display.flip()

    
    cir1=pygame.image.load('cir1.png')
    cir2=pygame.image.load('cir2.png')
    cir3=pygame.image.load('cir3.png')
    cir4=pygame.image.load('cir4.png')
    
    
    time.sleep(0.5)
    cir1=screen.blit(cir1,(102,600))
    pygame.display.flip()
    time.sleep(0.5)
    cir2=screen.blit(cir2,(146,600))
    pygame.display.flip()
    time.sleep(0.5)
    cir3=screen.blit(cir3,(190,600))
    pygame.display.flip()
    time.sleep(0.5)
    cir4=screen.blit(cir4,(234,600))
    pygame.display.flip()
    time.sleep(0.5)
    subprocess.call("Bank.py",shell=True)
    while running and location=='bank':
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        Loadscr=screen.blit(bankload,(0,0))
        Homebttn=screen.blit(homebttn,(154,710))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
                pygame.quit()
                quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click
                #mixer.music.play(0)
                X= pygame.mouse.get_pos()
                print ("Click: "),X
                print (X[0],X[1])
                
                if Homebttn.collidepoint(X[0],X[1]):
                    location='home'
                    home(location)

def calculator(location):
    
    running = True
    pygame.draw.rect(screen,blue,(48,164,58,58))
    Loadscr=screen.blit(calcload,(0,0))
    Homebttn=screen.blit(homebttn,(154,710))
    pygame.display.flip()

    cir1=pygame.image.load('cir1.png')
    cir2=pygame.image.load('cir2.png')
    cir3=pygame.image.load('cir3.png')
    cir4=pygame.image.load('cir4.png')
    
    
    time.sleep(0.5)
    cir1=screen.blit(cir1,(102,600))
    pygame.display.flip()
    time.sleep(0.5)
    cir2=screen.blit(cir2,(146,600))
    pygame.display.flip()
    time.sleep(0.5)
    cir3=screen.blit(cir3,(190,600))
    pygame.display.flip()
    time.sleep(0.5)
    cir4=screen.blit(cir4,(234,600))
    pygame.display.flip()
    time.sleep(0.5)
    subprocess.call("Calculator.py",shell=True)
    while running and location=='calculator':
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        Loadscr=screen.blit(calcload,(0,0))
        Homebttn=screen.blit(homebttn,(154,710))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
                pygame.quit()
                quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click
                #mixer.music.play(0)
                X= pygame.mouse.get_pos()
                print ("Click: "),X
                print (X[0],X[1])
                
                if Homebttn.collidepoint(X[0],X[1]):
                    location='home'
                    home(location)

def calendar(location):
    cir1=pygame.image.load('cir1.png')
    cir2=pygame.image.load('cir2.png')
    cir3=pygame.image.load('cir3.png')
    cir4=pygame.image.load('cir4.png')
    
    
    running = True
    pygame.draw.rect(screen,blue,(48,164,58,58))
    Loadscr=screen.blit(calenload,(0,0))
    Homebttn=screen.blit(homebttn,(154,710))
    pygame.display.flip()
    time.sleep(0.5)
    cir1=screen.blit(cir1,(102,600))
    pygame.display.flip()
    time.sleep(0.5)
    cir2=screen.blit(cir2,(146,600))
    pygame.display.flip()
    time.sleep(0.5)
    cir3=screen.blit(cir3,(190,600))
    pygame.display.flip()
    time.sleep(0.5)
    cir4=screen.blit(cir4,(234,600))
    pygame.display.flip()
    time.sleep(0.5)
    subprocess.call('Calendar (2).py',shell=True)
    while running and location=='calendar':
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        Loadscr=screen.blit(calenload,(0,0))
        Homebttn=screen.blit(homebttn,(154,710))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
                pygame.quit()
                quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click
                #mixer.music.play(0)
                X= pygame.mouse.get_pos()
                print ("Click: "),X
                print (X[0],X[1])
                
                if Homebttn.collidepoint(X[0],X[1]):
                    location='home'
                    home(location)
                

def carrent(location):
    running = True
    pygame.draw.rect(screen,blue,(48,164,58,58))
    Loadscr=screen.blit(carload,(0,0))
    Homebttn=screen.blit(homebttn,(154,710))
    pygame.display.flip()
    cir1=pygame.image.load('cir1.png')
    cir2=pygame.image.load('cir2.png')
    cir3=pygame.image.load('cir3.png')
    cir4=pygame.image.load('cir4.png')
    
    
    time.sleep(0.5)
    cir1=screen.blit(cir1,(102,600))
    pygame.display.flip()
    time.sleep(0.5)
    cir2=screen.blit(cir2,(146,600))
    pygame.display.flip()
    time.sleep(0.5)
    cir3=screen.blit(cir3,(190,600))
    pygame.display.flip()
    time.sleep(0.5)
    cir4=screen.blit(cir4,(234,600))
    pygame.display.flip()
    time.sleep(0.5)
    while running and location=='carrent':
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        screen.blit(Homescrn,(0,0))
        Loadscr=screen.blit(carload,(0,0))
        Homebttn=screen.blit(homebttn,(154,710))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
                pygame.quit()
                quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click
                #mixer.music.play(0)
                X= pygame.mouse.get_pos()
                print ("Click: "),X
                print (X[0],X[1])
                
                if Homebttn.collidepoint(X[0],X[1]):
                    location='home'
                    home(location)

def chrome(location):
    running = True
    pygame.draw.rect(screen,blue,(48,164,58,58))
    Loadscr=screen.blit(chromeload,(0,0))
    Homebttn=screen.blit(homebttn,(154,710))
    pygame.display.flip()
    
    cir1=pygame.image.load('cir1.png')
    cir2=pygame.image.load('cir2.png')
    cir3=pygame.image.load('cir3.png')
    cir4=pygame.image.load('cir4.png')
    
    
    time.sleep(0.5)
    cir1=screen.blit(cir1,(102,600))
    pygame.display.flip()
    time.sleep(0.5)
    cir2=screen.blit(cir2,(146,600))
    pygame.display.flip()
    time.sleep(0.5)
    cir3=screen.blit(cir3,(190,600))
    pygame.display.flip()
    time.sleep(0.5)
    cir4=screen.blit(cir4,(234,600))
    pygame.display.flip()
    time.sleep(0.5)
    subprocess.call("Google.py",shell=True)
    while running and location=='chrome':
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        screen.blit(Homescrn,(0,0))
        Loadscr=screen.blit(chromeload,(0,0))
        Homebttn=screen.blit(homebttn,(154,710))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
                pygame.quit()
                quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click
                #mixer.music.play(0)
                X= pygame.mouse.get_pos()
                print ("Click: "),X
                print (X[0],X[1])
                
                if Homebttn.collidepoint(X[0],X[1]):
                    location='home'
                    home(location)

def expedia(location):
    running = True
    pygame.draw.rect(screen,blue,(48,164,58,58))
    Loadscr=screen.blit(expedload,(0,0))
    Homebttn=screen.blit(homebttn,(154,710))
    pygame.display.flip()

    cir1=pygame.image.load('cir1.png')
    cir2=pygame.image.load('cir2.png')
    cir3=pygame.image.load('cir3.png')
    cir4=pygame.image.load('cir4.png')
    
    
    time.sleep(0.5)
    cir1=screen.blit(cir1,(102,600))
    pygame.display.flip()
    time.sleep(0.5)
    cir2=screen.blit(cir2,(146,600))
    pygame.display.flip()
    time.sleep(0.5)
    cir3=screen.blit(cir3,(190,600))
    pygame.display.flip()
    time.sleep(0.5)
    cir4=screen.blit(cir4,(234,600))
    pygame.display.flip()
    time.sleep(0.5)
    while running and location=='expedia':
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        screen.blit(Homescrn,(0,0))
        Loadscr=screen.blit(expedload,(0,0))
        Homebttn=screen.blit(homebttn,(154,710))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
                pygame.quit()
                quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click
                #mixer.music.play(0)
                X= pygame.mouse.get_pos()
                print ("Click: "),X
                print (X[0],X[1])
                
                if Homebttn.collidepoint(X[0],X[1]):
                    location='home'
                    home(location)

def hotel(location):
    running = True
    pygame.draw.rect(screen,blue,(48,164,58,58))
    Loadscr=screen.blit(hotelload,(0,0))
    Homebttn=screen.blit(homebttn,(154,710))
    pygame.display.flip()

    cir1=pygame.image.load('cir1.png')
    cir2=pygame.image.load('cir2.png')
    cir3=pygame.image.load('cir3.png')
    cir4=pygame.image.load('cir4.png')
    
    
    time.sleep(0.5)
    cir1=screen.blit(cir1,(102,600))
    pygame.display.flip()
    time.sleep(0.5)
    cir2=screen.blit(cir2,(146,600))
    pygame.display.flip()
    time.sleep(0.5)
    cir3=screen.blit(cir3,(190,600))
    pygame.display.flip()
    time.sleep(0.5)
    cir4=screen.blit(cir4,(234,600))
    pygame.display.flip()
    time.sleep(0.5)
    while running and location=='hotel':
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        screen.blit(Homescrn,(0,0))
        Loadscr=screen.blit(hotelload,(0,0))
        Homebttn=screen.blit(homebttn,(154,710))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
                pygame.quit()
                quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click
                #mixer.music.play(0)
                X= pygame.mouse.get_pos()
                print ("Click: "),X
                print (X[0],X[1])
                
                if Homebttn.collidepoint(X[0],X[1]):
                    location='home'
                    home(location)
                    
def mail(location):
    Mailscrn=pygame.image.load('AMailscrn.png')
    yahoo=pygame.image.load('yahoo.png')
    aol=pygame.image.load('aol.png')
    outlook=pygame.image.load('outlook.png')
    rediff=pygame.image.load('rediff.png')
    gmail=pygame.image.load('gmail.png')
    running = True
    pygame.draw.rect(screen,blue,(48,164,58,58))
    Loadscr=screen.blit(mailload,(0,0))
    Homebttn=screen.blit(homebttn,(166,686))
    pygame.display.flip()
    
    running = True
    pygame.draw.rect(screen,blue,(48,164,58,58))
    Loadscr=screen.blit(mailload,(0,0))
    Homebttn=screen.blit(homebttn,(154,710))
    pygame.display.flip()

    cir1=pygame.image.load('cir1.png')
    cir2=pygame.image.load('cir2.png')
    cir3=pygame.image.load('cir3.png')
    cir4=pygame.image.load('cir4.png')
    
    
    time.sleep(0.5)
    cir1=screen.blit(cir1,(102,600))
    pygame.display.flip()
    time.sleep(0.5)
    cir2=screen.blit(cir2,(146,600))
    pygame.display.flip()
    time.sleep(0.5)
    cir3=screen.blit(cir3,(190,600))
    pygame.display.flip()
    time.sleep(0.5)
    cir4=screen.blit(cir4,(234,600))
    pygame.display.flip()
    time.sleep(0.5)
    Mailscrn=screen.blit(Mailscrn,(0,0))
    screen.blit(font.render("Mail",1,WHITE), (50,190))
    Yahoo=screen.blit(yahoo,(40,160))
    Outlook=screen.blit(outlook,(40,160+99))
    Gmail=screen.blit(gmail,(40,99+99+160))
    AOL=screen.blit(aol,(40,99+99+99+160))
    Rediff=screen.blit(rediff,(40,99+99+99+99+160))
    Homebttn=screen.blit(homebttn,(154,710))
    pygame.display.flip()
    while running and location=='mail':
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
                pygame.quit()
                quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click
                #mixer.music.play(0)
                X= pygame.mouse.get_pos()
                print ("Click: "),X
                print (X[0],X[1])
                
                if Homebttn.collidepoint(X[0],X[1]):
                    location='home'
                    home(location)

                elif Yahoo.collidepoint(X[0],X[1]):
                    url="https://mail.yahoo.com/";
                    webbrowser.open(url,new=2);

                elif Outlook.collidepoint(X[0],X[1]):
                    url="https://www.outlook.com/";
                    webbrowser.open(url,new=2);

                elif Gmail.collidepoint(X[0],X[1]):
                    url="https://www.google.com/gmail/";
                    webbrowser.open(url,new=2);

                elif AOL.collidepoint(X[0],X[1]):
                    url="https://mail.aol.com/";
                    webbrowser.open(url,new=2);

                elif Rediff.collidepoint(X[0],X[1]):
                    url="www.rediffmail.com/cgi-bin/login.cgi";
                    webbrowser.open(url,new=2);
                    
def music(location):
    running = True
    pygame.draw.rect(screen,blue,(48,164,58,58))
    Loadscr=screen.blit(musicload,(0,0))
    Homebttn=screen.blit(homebttn,(154,710))
    pygame.display.flip()

    cir1=pygame.image.load('cir1.png')
    cir2=pygame.image.load('cir2.png')
    cir3=pygame.image.load('cir3.png')
    cir4=pygame.image.load('cir4.png')
    
    
    time.sleep(0.5)
    cir1=screen.blit(cir1,(102,600))
    pygame.display.flip()
    time.sleep(0.5)
    cir2=screen.blit(cir2,(146,600))
    pygame.display.flip()
    time.sleep(0.5)
    cir3=screen.blit(cir3,(190,600))
    pygame.display.flip()
    time.sleep(0.5)
    cir4=screen.blit(cir4,(234,600))
    pygame.display.flip()
    time.sleep(0.5)
    subprocess.call("music_1.py",shell=True)
    
    while running and location=='music':
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        screen.blit(Homescrn,(0,0))
        Loadscr=screen.blit(musicload,(0,0))
        Homebttn=screen.blit(homebttn,(154,710))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
                pygame.quit()
                quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click
                #mixer.music.play(0)
                X= pygame.mouse.get_pos()
                print ("Click: "),X
                print (X[0],X[1])
                
                if Homebttn.collidepoint(X[0],X[1]):
                    location='home'
                    home(location)
                    
def restaurant(location):
    running = True
    pygame.draw.rect(screen,blue,(48,164,58,58))
    Loadscr=screen.blit(restload,(0,0))
    Homebttn=screen.blit(homebttn,(154,710))
    pygame.display.flip()

    cir1=pygame.image.load('cir1.png')
    cir2=pygame.image.load('cir2.png')
    cir3=pygame.image.load('cir3.png')
    cir4=pygame.image.load('cir4.png')
    
    
    time.sleep(0.5)
    cir1=screen.blit(cir1,(102,600))
    pygame.display.flip()
    time.sleep(0.5)
    cir2=screen.blit(cir2,(146,600))
    pygame.display.flip()
    time.sleep(0.5)
    cir3=screen.blit(cir3,(190,600))
    pygame.display.flip()
    time.sleep(0.5)
    cir4=screen.blit(cir4,(234,600))
    pygame.display.flip()
    time.sleep(0.5)
    subprocess.call('Main.py',shell=True)
    while running and location=='restaurant':
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        screen.blit(Homescrn,(0,0))
        Loadscr=screen.blit(restload,(0,0))
        Homebttn=screen.blit(homebttn,(154,710))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
                pygame.quit()
                quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click
                #mixer.music.play(0)
                X= pygame.mouse.get_pos()
                print ("Click: "),X
                print (X[0],X[1])
                
                if Homebttn.collidepoint(X[0],X[1]):
                    location='home'
                    home(location)
                    
def books(location):
    running = True
    pygame.draw.rect(screen,blue,(48,164,58,58))
    Loadscr=screen.blit(booksload,(0,0))
    Homebttn=screen.blit(homebttn,(154,710))
    pygame.display.flip()

    cir1=pygame.image.load('cir1.png')
    cir2=pygame.image.load('cir2.png')
    cir3=pygame.image.load('cir3.png')
    cir4=pygame.image.load('cir4.png')
    
    
    time.sleep(0.5)
    cir1=screen.blit(cir1,(102,600))
    pygame.display.flip()
    time.sleep(0.5)
    cir2=screen.blit(cir2,(146,600))
    pygame.display.flip()
    time.sleep(0.5)
    cir3=screen.blit(cir3,(190,600))
    pygame.display.flip()
    time.sleep(0.5)
    cir4=screen.blit(cir4,(234,600))
    pygame.display.flip()
    time.sleep(0.5)
    subprocess.call('storymain.py',shell=True)
    while running and location=='books':
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        screen.blit(Homescrn,(0,0))
        Loadscr=screen.blit(booksload,(0,0))
        Homebttn=screen.blit(homebttn,(154,710))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
                pygame.quit()
                quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click
                #mixer.music.play(0)
                X= pygame.mouse.get_pos()
                print ("Click: "),X
                print (X[0],X[1])
                
                if Homebttn.collidepoint(X[0],X[1]):
                    location='home'
                    home(location)
                    
def games(location):
    running = True
    pygame.draw.rect(screen,blue,(48,164,58,58))
    while running and location=='games':
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        screen.blit(Homescrn,(0,0))
        Loadscr=screen.blit(Gamescrn,(0,0))
        Homebttn=screen.blit(homebttn,(154,710))
        Guess=screen.blit(guessicon,(45,336))
        screen.blit(font2.render("Guess Game",1,WHITE), (46,406))

        Tic=screen.blit(ticicon,(160,343))
        screen.blit(font2.render("TicTacToe",1,WHITE), (157,406))


        Quiz=screen.blit(quizicon,(265,343))
        screen.blit(font2.render("Quiz App",1,WHITE), (262,406))

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
                pygame.quit()
                quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click
                #mixer.music.play(0)
                X= pygame.mouse.get_pos()
                print ("Click: "),X
                print (X[0],X[1])
                
                if Homebttn.collidepoint(X[0],X[1]):
                    location='home'
                    home(location)

                elif Guess.collidepoint(X[0],X[1]):
                    location='guess'
                    guess(location)

                elif Tic.collidepoint(X[0],X[1]):
                    location='tic'
                    tic(location)

                elif Quiz.collidepoint(X[0],X[1]):
                    location='quiz'
                    quiz(location)
                    
def youtube(location):
    running = True
    pygame.draw.rect(screen,blue,(48,164,58,58))
    Loadscr=screen.blit(youtload,(0,0))
    Homebttn=screen.blit(homebttn,(154,710))
    pygame.display.flip()

    cir1=pygame.image.load('cir1.png')
    cir2=pygame.image.load('cir2.png')
    cir3=pygame.image.load('cir3.png')
    cir4=pygame.image.load('cir4.png')
    
    
    time.sleep(0.5)
    cir1=screen.blit(cir1,(102,600))
    pygame.display.flip()
    time.sleep(0.5)
    cir2=screen.blit(cir2,(146,600))
    pygame.display.flip()
    time.sleep(0.5)
    cir3=screen.blit(cir3,(190,600))
    pygame.display.flip()
    time.sleep(0.5)
    cir4=screen.blit(cir4,(234,600))
    pygame.display.flip()
    time.sleep(0.5)
    subprocess.call("youtube.py",shell=True)
    while running and location=='youtube':
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        screen.blit(Homescrn,(0,0))
        Loadscr=screen.blit(youtload,(0,0))
        Homebttn=screen.blit(homebttn,(154,710))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
                pygame.quit()
                quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click
                #mixer.music.play(0)
                X= pygame.mouse.get_pos()
                print ("Click: "),X
                print (X[0],X[1])
                
                if Homebttn.collidepoint(X[0],X[1]):
                    location='home'
                    home(location)
                    
def guess(location):
    running = True
    pygame.draw.rect(screen,blue,(48,164,58,58))
    Loadscr=screen.blit(guessload,(0,0))
    Homebttn=screen.blit(homebttn,(154,710))
    pygame.display.flip()

    cir1=pygame.image.load('cir1.png')
    cir2=pygame.image.load('cir2.png')
    cir3=pygame.image.load('cir3.png')
    cir4=pygame.image.load('cir4.png')
    
    
    time.sleep(0.5)
    cir1=screen.blit(cir1,(102,600))
    pygame.display.flip()
    time.sleep(0.5)
    cir2=screen.blit(cir2,(146,600))
    pygame.display.flip()
    time.sleep(0.5)
    cir3=screen.blit(cir3,(190,600))
    pygame.display.flip()
    time.sleep(0.5)
    cir4=screen.blit(cir4,(234,600))
    pygame.display.flip()
    time.sleep(0.5)
    subprocess.call("GG.py",shell=True)
    while running and location=='guess':
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        screen.blit(Homescrn,(0,0))
        Loadscr=screen.blit(guessload,(0,0))
        Homebttn=screen.blit(homebttn,(154,710))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
                pygame.quit()
                quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click
                #mixer.music.play(0)
                X= pygame.mouse.get_pos()
                print ("Click: "),X
                print (X[0],X[1])
                
                if Homebttn.collidepoint(X[0],X[1]):
                    location='home'
                    home(location)
                    
def tic(location):
    running = True
    pygame.draw.rect(screen,blue,(48,164,58,58))
    Loadscr=screen.blit(ticload,(0,0))
    Homebttn=screen.blit(homebttn,(154,710))
    pygame.display.flip()

    cir1=pygame.image.load('cir1.png')
    cir2=pygame.image.load('cir2.png')
    cir3=pygame.image.load('cir3.png')
    cir4=pygame.image.load('cir4.png')
    
    
    time.sleep(0.5)
    cir1=screen.blit(cir1,(102,600))
    pygame.display.flip()
    time.sleep(0.5)
    cir2=screen.blit(cir2,(146,600))
    pygame.display.flip()
    time.sleep(0.5)
    cir3=screen.blit(cir3,(190,600))
    pygame.display.flip()
    time.sleep(0.5)
    cir4=screen.blit(cir4,(234,600))
    pygame.display.flip()
    time.sleep(0.5)
    subprocess.call("TTT.py",shell=True)
    while running and location=='tic':
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        Loadscr=screen.blit(ticload,(0,0))
        Homebttn=screen.blit(homebttn,(154,710))
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
                pygame.quit()
                quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click
                #mixer.music.play(0)
                X= pygame.mouse.get_pos()
                print ("Click: "),X
                print (X[0],X[1])
                
                if Homebttn.collidepoint(X[0],X[1]):
                    location='home'
                    home(location)
                    
def quiz(location):
    running = True
    pygame.draw.rect(screen,blue,(48,164,58,58))
    Loadscr=screen.blit(quizload,(0,0))
    Homebttn=screen.blit(homebttn,(154,710))
    pygame.display.flip()

    cir1=pygame.image.load('cir1.png')
    cir2=pygame.image.load('cir2.png')
    cir3=pygame.image.load('cir3.png')
    cir4=pygame.image.load('cir4.png')
    
    
    time.sleep(0.5)
    cir1=screen.blit(cir1,(102,600))
    pygame.display.flip()
    time.sleep(0.5)
    cir2=screen.blit(cir2,(146,600))
    pygame.display.flip()
    time.sleep(0.5)
    cir3=screen.blit(cir3,(190,600))
    pygame.display.flip()
    time.sleep(0.5)
    cir4=screen.blit(cir4,(234,600))
    pygame.display.flip()
    time.sleep(0.5)
    subprocess.call('Quiz.py',shell=True)
    while running and location=='quiz':
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        screen.blit(Homescrn,(0,0))
        Loadscr=screen.blit(quizload,(0,0))
        Homebttn=screen.blit(homebttn,(154,710))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
                pygame.quit()
                quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click
                #mixer.music.play(0)
                X= pygame.mouse.get_pos()
                print ("Click: "),X
                print (X[0],X[1])
                
                if Homebttn.collidepoint(X[0],X[1]):
                    location='home'
                    home(location)

home(location)

