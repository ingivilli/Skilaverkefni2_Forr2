#Ingimundur Vilberg Ingason
#9. nov 2021
#Skilaverkefni 2
import csv
import random

def lesaSkra(nafntxt):
    with open(nafntxt,"r") as f:
        
        texti = csv.reader(f,delimiter=";")
        listi = []
        for i in texti:
            listi=listi+[i]

    f.close()
    return listi

def spurning(spurningsvar):
    
    svar=input(spurningsvar[0])
    
    if svar == spurningsvar[1]:
        return True
    else:
        return False

def skrifaiskra(listi,nafntxt):
    with open(nafntxt,"a") as f:
        
        writer=csv.writer(f)

        writer.writerow(listi)
    
    f.close

def breytauppl(simaskra,nafn,nyttGSM):
    listi=[]
    with open(simaskra,"r+") as f:
        
        texti = csv.reader(f)

        for i in texti:
            
            if i[0] != nafn:
                
                listi.append(i)

            if i[0] == nafn:

                i[1] == nyttGSM
                listi.append(i)

        csv.writer(f).writerows(listi)
        
    f.close
def eyda(simaskra,nafn):
    listi=[]
    with open(simaskra,"r+") as f:
        
        texti = csv.reader(f)

        for i in texti:
            if i[0] != nafn:
                listi.append(i)
        csv.writer(f).writerows(listi)
    
    f.close

def prenta(simaskra):
    with open(simaskra,"r") as listi:
        
        texti = csv.reader(listi)

        for i in texti:
            print(i)
    
    f.close
valmynd = True

while valmynd:
    val=int(input("Hvað viltu gera?\n1. Spurningaleikur\n2. Símaskrá \n3. Hætta\n$ "))
    
    if val == 1:
        
        texti = lesaSkra("Spurningar.csv")
        stig = 0
        random.shuffle(texti)   
        print(texti)
        
        for i in texti:
            
            tilraun1=False
            tilraun2=True

            while tilraun2:
                hi = spurning(i)
                
                if hi:
                    print("rétt! næsta spurning!")
                    stig=stig+1
                    tilraun2=False
                
                if tilraun1:
                    print("rangt! svarið var:",i[1])
                    tilraun2=False
                
                if not hi and not tilraun1:
                    print("rangt! þú færð einn annan séns!")
                    tilraun1=True
        
        print("þú hefur fengið",stig,"stig!")
    
    if val == 2: 

        valmynd2 = True
        
        while valmynd2:
            val2=int(input("Hvað viltu gera?\n1. bæta við simaskra\n2. breyta i simaskra\n3. eyða ur simaskra\n4. prenta úr símaskrá\n5. hætta\n$ "))
        
            if val2==1:
                nafn=input("hverjum viltu bæta við?: ")
                numer=input("hvað er numerið þeirra?: ")
                skrifaiskra([nafn,numer],"Simaskra.csv")
            
            if val2==2:

                nafn=input("hvað er nafnið sem þu vilt breyta nr?: ")
                nr=input("hvað er nya numerið?: ")
                breytauppl("Simaskra.csv",nafn,nr)
            
            if val2==3:

                nafn=input("Hverjum viltu eyða?: ")
                eyda("Simaskra.csv",nafn)

            if val==4:
                
                prenta("Simaskra.csv")

            if val==5:
                valmynd2 = False
                break
    if val == 3:
        break
