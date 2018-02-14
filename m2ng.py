# töötab
# project

import tkinter
from tkinter import messagebox
import random
import sys
print("!!!! EESTIKEELSED SÕNAD !!!!")
#Küsib nime
nimi=input("Mis on sinu nimi?:")
print("Tere tulemast",nimi,"aeg mängida poomist!")

#Genereerib sõna
def genereeri_sõna(infile):
    random_sõna= random.choice(open(infile).read().split("\n"))
    return random_sõna
#Poomise mäng
def poomine():
    teema=input("Mis teema sa valid? (loodus, sport, ajalugu):")
    print("Sa valisid teema:",teema)
    if teema=="loodus":
        infile="loodus.txt"
    elif teema=="sport":
        infile="sport.txt"
    elif teema=="ajalugu":
        infile="ajalugu.txt"
    else:
        print("Olen segaduses")
    sõna=genereeri_sõna(infile)
    print(sõna)
    print("Sõnas on",len(sõna),"sõna")
    käike=10
    vastuseid=""


    while käike>0:
    
        valesti=0
    

        for char in sõna:
            if char in vastuseid:
                    print(char)
            
            else:
                print("_")
                valesti += 1
            
        if valesti==0:
            print("Sa võitsid!")
            break
        
        täht=input("Sisestage täht:")
        vastuseid += täht
        if täht not in sõna:
            käike -= 1
            print("Vale")
        if käike==0:
            print("Sa kaotasid")
poomine()


kasutaja_skoor=0
arvuti_skoor=0
def kpk():
    
    päis=tkinter.Tk()
    päis.title("Kivi|Paber|Käärid")

    
    def Kivi():

        global kasutaja_skoor, arvuti_skoor
        arvuti= random.randint(1,3)
        if arvuti==3:
            arvuti="Käärid"
            kasutaja_skoor+=1
            messagebox.showinfo("PALJU ÕNNE!","SA VÕITSID!\n"+"Sinu valik:Kivi"+"\nArvuti Valik: "+arvuti+"\nSinu skoor: " +str(kasutaja_skoor)+"\nArvuti skoor:"+str(arvuti_skoor))
        elif arvuti==1:
            arvuti = "Kivi"
            messagebox.showinfo("Sama mis arvutil!", "VIIK\n"+"Sinu valik:Kivi"+"\nArvuti valik: "+arvuti+"\nSinu skoor: "+str(kasutaja_skoor)+"\nArvuti skoor: "+str(arvuti_skoor))
        else:
            arvuti="Paber"
            arvuti_skoor+=1
            messagebox.showinfo("Ossa pagan!", "SA KAOTASID\n"+"Sinu valik:Kivi"+"\nArvuti valik: "+arvuti+"\nSinu skoor: "+str(kasutaja_skoor)+"\nArvuti skoor: "+str(arvuti_skoor))
    def Paber():
        
        arvuti=random.randint(1,3)
        global kasutaja_skoor, arvuti_skoor
        if arvuti==1:
            arvuti="Kivi"
            kasutaja_skoor+=1
            messagebox.showinfo("PALJU ÕNNE!","SA VÕITSID!\n"+"Sinu valik:Paber"+"\nArvuti Valik: "+arvuti+"\nSinu skoor: " +str(kasutaja_skoor)+"\nArvuti skoor:"+str(arvuti_skoor))
        elif arvuti==2:
            arvuti="Paber"
            messagebox.showinfo("Sama mis arvutil!","VIIK!\n"+"Sinu valik:Paber"+"\nArvuti Valik: "+arvuti+"\nSinu skoor: " +str(kasutaja_skoor)+"\nArvuti skoor:"+str(arvuti_skoor))
        else:
            arvuti="Käärid"
            arvuti_skoor+=1
            messagebox.showinfo("Ossa pagan!","SA KAOTASID!\n"+"Sinu valik:Paber"+"\nArvuti Valik: "+arvuti+"\nSinu skoor: " +str(kasutaja_skoor)+"\nArvuti skoor:"+str(arvuti_skoor))
    def Käärid():
        
        arvuti=random.randint(1,3)
        global kasutaja_skoor, arvuti_skoor
        if arvuti == 2:
            arvuti="Paber"
            kasutaja_skoor+=1
            messagebox.showinfo("PALJU ÕNNE!","SA VÕITSID!\n"+"Sinu valik:Käärid"+"\nArvuti Valik: "+arvuti+"\nSinu skoor: " +str(kasutaja_skoor)+"\nArvuti skoor:"+str(arvuti_skoor))
        elif arvuti==3:
            arvuti="Käärid"
            messagebox.showinfo("Sama mis arvutil!","VIIK!\n"+"Sinu valik:Käärid"+"\nArvuti Valik: "+arvuti+"\nSinu skoor: " +str(kasutaja_skoor)+"\nArvuti skoor:"+str(arvuti_skoor))
        else:
            arvuti="Kivi"
            arvuti_skoor+=1
            messagebox.showinfo("Ossa pagan!","SA KAOTASID!\n"+"Sinu valik:Käärid"+"\nArvuti Valik: "+arvuti+"\nSinu skoor: " +str(kasutaja_skoor)+"\nArvuti skoor:"+str(arvuti_skoor))
    B1=tkinter.Button(päis, text = "Kivi",bg='red',height="10",width="20", command = Kivi)
    B2=tkinter.Button(päis, text = "Paber",bg='green',height="10",width="20", command = Paber)
    B3=tkinter.Button(päis, text = "Käärid",bg='blue',height="10",width="20", command = Käärid)
    B1.pack(side='left')
    B2.pack(side='left')
    B3.pack(side='left')

    päis.mainloop()

#Uuesti mängimine
while True:
    vastus=input("Tahad sa uuesti mängida? (jah/ei) ")
    if vastus=="jah":
        poomine()
    elif vastus=="ei":
        vastus2=input("Soovid sa mängida kivi-paber-käärid mängu? (jah/ei) ")
        if vastus2=="jah":
            kpk()
        elif vastus=="ei":
            print("Nägemiseni!")
    else:
        print("Ei mõista sinu vastust")