i=2
import random
money=100000
army= 10000
conqpro = 0
amr = 100
mcr = 15000
drf = 1
acr = 10576

print("Countries War")
start_country = raw_input("Select your country: ")
print"Country selected:",start_country
while i<3:
    if army < 0:
        army = 0
        money -= 100000
    print money, "$"
    print"Troops:",army
    print"Conquered provinces:",conqpro
    money += amr
    turnskip = raw_input("(Enter: skip turn, addarmy: Add army menu, Research: research, Start War: war) :")
    if turnskip == "addarmy":
        addarmy1 = input("Select how many troops you want to recruit: ")
        if addarmy1 >= 10000:
            print("Max army size 9999")
        if addarmy1 <= 0:
            print"Min army size 1"
        else:
            if money - addarmy1 * drf <= 0:
                print("no")
            else:
                army+= addarmy1
                
                print"Remaining money:", money - addarmy1 * drf
                print"Proof:", money,"-",addarmy1 * drf
                money -= addarmy1 * drf
    elif turnskip == "war":
        war1 = raw_input("Select country to start a war with: ")
        enemyarmy = random.randint(1, 9999)
        print "Enemy army:",enemyarmy
        print "Your army:", army
        if army < enemyarmy:
            print"You lost"
            print "Enemy army:",enemyarmy
            print "Your army:", army
            army = army - enemyarmy
            enemy = enemyarmy - army
        elif army == enemyarmy:
            print"Nobody won"
            
            print "Enemy army:",enemyarmy
            print "Your army:", army
            army = army - enemyarmy
            enemy = enemyarmy - army

        elif army >= enemyarmy:
            print"You won!"
            conqpro += 1
            print "Enemy army:",enemyarmy
            print "Your army:", army
            army = army - enemyarmy
            enemy = enemyarmy - army

            
    elif turnskip == "research":
        rs = raw_input("Research subject(Add money rate= amr, Decrease Recruit Fee = drf: ")
        if rs == "amr":
            print"This will cost",mcr
            askq = raw_input("Continue? (y or n): ")
            if askq == "y" or askq == "Y":
                if money - mcr <= 0:
                    print"Can't afford, noob"
                else:
                    money -= mcr
                    amr += 100
                    mcr += 10000
        if rs == "drf":
            print"This will cost",acr
            askq = raw_input("Continue? (y or n): ")
            if askq == "y" or askq == "Y":
                if money - acr <= 0:
                    print"You can't afford this upgrade, what a noob"
                else:
                    if drf == 0:
                        print"Recruit Fee is already 0, what you tryning to do bro"
                    else:
                        money -= acr
                        drf -= 1
                        acr += 5678
                
                
