import PySimpleGUI as sg
from pygame import mixer
import pandas as pd
import datetime
import random as rd

from datetime import datetime
import datetime as dt
import numpy as np
from os import startfile

#background music

mixer.init() #background music
mixer.music.load("final.mp3") 
mixer.music.set_volume(0.9) 
mixer.music.play(-1)


#to create a unique value of dataframe's column which is stored in a list
def unique_value(dataframe,column):
    lt=[]
    for var in dataframe[column]:
        if var not in lt:
            lt=lt+[var]
        elif var in lt:
            lt=lt
    return(lt)

#to create a unique value of list which is stored in a list
def uniquelist(lisa):
    lt=[]
    for var in lisa:
        if var not in lt:
            lt=lt+[var]
        elif var in lt:
            lt=lt
    return(lt)

#csv file of customer details           
customer=pd.read_csv("customer.csv")
customer=customer.set_index("_")

#csv file of ordered snacks details of customer
customersnacks=pd.read_csv("customer snacks.csv")
customersnacks=customersnacks.set_index("_")

vari=0
while vari<1:
  layout0=[[sg.T("SOAPANASUNDARI 2.O CINEMAS",size=(27,1),justification='c',font=("gothic",40))],
           [sg.Image('opening.png')],
           [sg.Button('BOOK TICKETS',size=(28,1)),sg.Button('MY DETAILS',size=(28,1)),
            sg.Button('CANCEL TICKETS',size=(29,1))],
           [sg.B("THEATRE REVIEWS",size=(90,1))],
           [sg.Button('EXIT',size=(90,1))]]
                
  window0=sg.Window('SOAPANASUNDARI CINEMAS',layout0,finalize=True)
  eventing,values=window0.read()
  window0.close()
  onetimeselect=0
  multitime=0
  variable0=0

  if eventing=="THEATRE REVIEWS":             
         vari=vari-1
         mixer.music.set_volume(0.0) 
         startfile("moviereview.mp4")
  elif eventing=='BOOK TICKETS':
     while variable0<1:                                                                                             
        now=dt.datetime.now()                                                                                      
        nowstr=now.strftime("%d-%m-%Y %HH:%MM:%SS")                                                               
        today,time=nowstr.split(' ')                                                                            
        todayday,todaymonth,todayyear=today.split('-')                                                          
        tomorrow=dt.datetime.now()+dt.timedelta(1)                                                               
        dayaftertomorrow=dt.datetime.now()+dt.timedelta(2)                                                      
        tomorrow=tomorrow.strftime("%d-%m-%y")                                                                
        tomorrowday,tomorrowmonth,tomorrowyear=tomorrow.split('-')                                             
        dayaftertomorrow=dayaftertomorrow.strftime("%d-%m-%y")                                                 
        dayaftertomorrowday,dayaftertomorrowmonth,dayaftertomorrowyear=dayaftertomorrow.split('-')            
        tomorrow=tomorrowday+'/'+tomorrowmonth+'/'+todayyear[:2]+tomorrowyear                                 
        dayaftertomorrow=dayaftertomorrowday+'/'+dayaftertomorrowmonth+'/'+todayyear[:2]+dayaftertomorrowyear

        df=pd.read_csv('movie timing pro.csv')
        df=df.set_index('_')
   
        for ggwp in df.index:                                                  
                timeobj=df.loc[ggwp]['date']+(" ")+df.loc[ggwp]['programtime']
                timeformat=datetime.strptime(timeobj,"%d-%m-%Y %H:%M")
                timeformatstr=timeformat.strftime("%d-%m-%Y %H:%M")
                timeformatday,timeformattime=timeformatstr.split(' ')
                         
                if timeformat<now  :      
                    df=df.drop([ggwp])
                elif timeformat > dt.datetime.now()+dt.timedelta(2):
                    df=df.drop([ggwp])
                             
        uniquedate=unique_value(df,'date')
        uniquemoviename=unique_value(df,'movie')
        uniquemovieimage=unique_value(df,'image file 1')
        uniquemovieimage2=unique_value(df,'image file 2')
        lst=[]
        onetimeselect=1+onetimeselect
        if len(uniquedate)==0:
                    sg.popup("sorry booking is not available")
                    vari=vari-1
                    break
        elif onetimeselect==1:                                                       #to set default date as today in the layout
            lst.append(sg.T(uniquedate[0],size=(40,1),justification='center'))
            showdate=uniquedate[0]
            showdatemovies=[]
            uniqueshowdatemovies=[]
            uniqueimages=[]
            showdatetime=[]
            for kg in (df[df.date==uniquedate[0]]).values:
                    showdatemovies.append(kg[2])
                    showdatetime.append(kg[4])
            uniqueshowdatemovies=unique_value(df[df.date==uniquedate[0]],'movie')
            
            uniqueimages=unique_value(df[df.date==uniquedate[0]],'image file 1')
            uniqueimages2=unique_value(df[df.date==uniquedate[0]],'image file 2')
                              
            uniquedate.remove(uniquedate[0])
            for wwe in uniquedate:
                                     lst.append(sg.B(wwe,size=(40,1)))
        else:                                                                        #to set user selected date  in the layout
             for wwe in uniquedate:
                 if event!=wwe :
                        lst.append(sg.B(wwe,size=(40,1)))
                 elif event==wwe or showdate==wwe:
                        lst.insert(uniquedate.index(wwe),sg.T(wwe,size=(40,1),justification='center'))
                        showdate=wwe
                        showdatemovies=[]
                        uniqueshowdatemovies=[]
                        uniqueimages=[]
                        showdatetime=[]
                        for kg in (df[df.date==wwe]).index:
                             showdatemovies.append(df[df.date==wwe].loc[kg]["movie"])
                             showdatetime.append(df[df.date==wwe].loc[kg]["showtime"])
                        uniqueshowdatemovies=unique_value(df[df.date==wwe],'movie')
                        uniqueimages=unique_value(df[df.date==wwe],'image file 1')
        bookingimage=[]
        bookingbutton=[]
        bookingtext=[]
        for dj in range(len(uniqueimages)):
                bookingimage.append(sg.Image(filename=uniqueimages[dj]) )
                bookingbutton.append(sg.B("BOOK NOW",key=uniqueshowdatemovies[dj],size=(29,1)))
                bookingtext.append(sg.T(uniqueshowdatemovies[dj].upper(),size=(22,1),font=('Times',15),justification='c'))
            
                
        layout1=[
                [sg.T("SOAPANASUNDARI 2.O CINEMAS",size=(32,1),justification='c',font=("arial",40))],
                 lst,
                [sg.T("                                                                                                                                                                                       ")],           
                [sg.T('---------------------------------------------------------------------------Showing On '+showdate+'------------------------------------------------------------------------------------',justification='center',size=(124,1))],
                [sg.T(' ')],
                bookingtext,
                bookingimage,
                bookingbutton,              
                [sg.Button('BACK',size=(124,1))],
                [sg.T(' ')]]
                                              
        window1=sg.Window('Showing on '+showdate,layout1)
        event,values=window1.read()
        window1.close()
        jaks=3
        if event=='BACK' or event==sg.WIN_CLOSED:

            jaks=0
            vari=vari-1
            event=showdate
                           
        for horn in uniquedate:
            if event==horn and jaks!=0:
                jaks=1
                variable0=variable0-1
                event=horn
        for horn in uniqueshowdatemovies:
            if event==horn and jaks!=0:
                jaks=2
        if jaks==2:
            sandy=0
            while sandy<1:
                timebutton=[]
                imagebutton=[]
                directedby=[sg.T('Directed by:')]
                cast=[sg.T('Cast:')]
                genre=[sg.T('Genre:')]
                    
                for buti in uniqueshowdatemovies:
                    if event==buti:
                        imagebutton.append(sg.Image(df.loc[(df.loc[(df[df.movie==buti]).index]['image file 2']).index[0]]['image file 2']))
                            
                for kuti in range(len(showdatemovies)):
                    if showdatemovies[kuti]==event:
                        timebutton.append(sg.B(showdatetime[kuti],size=(7,1)))
                toein=0
                for bravo in df.index:
                                          
                    if df.loc[bravo]['movie']==event and toein==0:
                        toein=1
                        certification=df.loc[bravo]['certification']
                        language=df.loc[bravo]['language']
                        formt=df.loc[bravo]['format']
                        directedby.append(sg.T(df.loc[bravo]['directed by']))
                        cast.append(sg.T(df.loc[bravo]['cast']))
                        genre.append(sg.T(df.loc[bravo]['genre']))
                        trailer=df.loc[bravo]['trailer']
  
                layout1=[[sg.T('-----------------------------On '+showdate+'--------------------',justification='center')],
                        imagebutton,
                        [sg.B("WATCH TRAILER")],
                        [sg.T(event.upper(),size=(17,1),font=("arial",15)),sg.T('-'+certification+ ' - '+language+formt)],
                        genre,
                        cast,
                        directedby,
                                    
                        timebutton,
                        [sg.B('BACK',size=(35,1))]]
                windo1=sg.Window(event,layout1)
                even,values=windo1.read()
                windo1.close()
                
                if even=='BACK' or even==sg.WIN_CLOSED:
                        event=showdate
                        variable0=variable0-1
                        mixer.music.set_volume(0.9) 
                                              
                elif even=="WATCH TRAILER":
                     sandy=sandy-1
                     mixer.music.set_volume(0.0) 
                     startfile(trailer)
                                               
                else:
                     mixer.music.set_volume(0.9) 
                     for loki in df.index:
                                          
                        if df.loc[loki]['movie']==event and df.loc[loki]['date']==showdate and df.loc[loki]['showtime']==even :
                            strfttime=df.loc[loki]['programtime']            
                                              

                            if certification=="(A)":
                                    sg.popup(" ADULT(18+) movie")                  
                            u=0
                            while u<1:                                                                
                                                             
                                a=pd.read_csv(df.loc[loki]['bookingscreen'])
                                a=a.set_index("_")
                                seatsfilled=0
                                seatsavailable=0
                                for mrf in a.index:
                                                                                           
                                    for kcg in range(1,11):
                                        if a.loc[mrf][str(kcg)]=="BKED":
                                            seatsfilled=seatsfilled+1
                                        else:
                                            seatsavailable=seatsavailable+1             
                                noseatslist=[]
                                                    
                                if seatsavailable==0:
                                    sg.popup("House Full")
                                    sandy=sandy-1
                                else:
                                    for pen in range(1,11):
                                        if seatsavailable >= pen:
                                            noseatslist.append(sg.B(str(pen)))
                                        else:
                                            noseatslist.append(sg.T(str(pen),size=(3,1),justification='c'))
                                                       
                                    layout=[[sg.T("Number of Seats to Book",size=(30,1),font=("gothic",14))],
                                            noseatslist,
                                            [sg.B('back')]]
                                    window=sg.Window("Number of Seats",layout,default_button_element_size=(3,1), auto_size_buttons=False)
                                    gym,vals = window.read()
                                    window.close()
                                    i=0 
                                    if gym==sg.WIN_CLOSED or gym=='back' :                                                            
                                        sandy=sandy-1

                                    else:
                                        for ps in range(1,11):
                                            if gym==str(ps):
                                                noseats=ps
                                                                                                                               
                                        p=0

                                        seatrow=[]
                                        seatno=[]
                                        index=[]
                                        silverseats=[]
                                        premiereseats=[]
                                                                             
                                        while i<=noseats:           #for booking the seats in a particular csv file of booking seats
                                            
                                            a=pd.read_csv(df.loc[loki]['bookingscreen'])
                                            a=a.set_index("_")
                                                                                     
                                            kkk=[]
                                            jjj=[]
                                            iii=[]
                                            hhh=[]
                                            ggg=[]
                                            fff=[]
                                            eee=[]
                                            ddd=[]
                                            ccc=[]
                                            bbb=[]
                                            aaa=[]
                                            rows=[kkk,jjj,iii,hhh,ggg,fff,eee,ddd,ccc,bbb,aaa]
                                                                                     
                                            for var in a.index:
                                                for dor in range(1,11):
                                                    if a.loc[var][str(dor)]=="BKED":
                                                        rows[var].append(sg.T("BKED"))
                                                    elif a.loc[var][str(dor)]==" THIS ":
                                                        rows[var].append(sg.T(" THIS "))    
                                                    else:
                                                        rows[int(var)].append(sg.B(a.loc[int(var)][str(dor)]))                                                  
 
                                            for sumo in rows: 
                                                    sumo.insert(-2,sg.T("|   |"))
                                                    sumo.insert(2,sg.T("|   |"))
                                                                                                
                                                    sumo.insert(0,sg.T("|   |"))
                                                    sumo.append(sg.T("|   |"))  
                                            alphabets=["K","J","I","H","G","F","E","D","C","B","A"]     
                                            if i==noseats and i==len(seatno) :
                                                 butt=sg.B("BOOK")
                                                                                            
                                            else:
                                                 butt=sg.T("")
                                            back=sg.B("back")
                                                                                    
                                            if i<=noseats:
                                                    lay=[[sg.T("SOAPANASUNDARI CINEMAS",size=(55,1),justification='c',font=("arial",15))],
                                                        [sg.T("ShowDate:"+showdate,size=(25,1)),sg.T("Movie:"+event,size=(25,1)),sg.T("ShowTime:"+even,size=(25,1))],                                      
                                                        [sg.T("EXT"),sg.T("                                                                                                                                      "),sg.T("EXT")],
                                                         kkk,
                                                         jjj,
                                                        [sg.T("|   |     ___  ___  ___ _ |   |___  ___  ___  __  __  __   ___  ____  ___  __    ___  |   |___   ___   ___ __   |   |")],
                                                        iii,hhh,ggg,fff,eee,ddd,ccc,bbb,aaa,
                                                        [sg.T("|   ___  ___  ___  ___  |   |___  ___  ___  __  __  __   ___   ___   ___  ___   ___  |   |   ___  ___  ___  ___ __|")],                                 
                                                        [sg.T("____________________________________________________________________________________")],
                                                        [sg.T("                     A  L  L         E  Y  E  S        T  H  I  S        W  A  Y         P  L  E  A  S  E               ")],
                                                        [sg.T("____________________________________________________________________________________") ],
                                                        [butt,back,sg.T("BKED  - already booked"),sg.T("               THIS   -  seat selected by you")],
                                                        [sg.T("                           "),sg.T("SILVER(A-I): Rs 150",font=("arial",10)),sg.T("    "),sg.T("PREMIERE(J,K): Rs 170",font=("arial",10)),sg.T("   seats left for selection :"+str(noseats-i)+" ")]]
                                                    window=sg.Window("bookingscreen",lay,default_button_element_size=(4,1), auto_size_buttons=False)
                                                    bucket,vals = window.read()
                                                    window.close()
                                                                                                
                                            if  i<noseats :
                                                    for dum in a.index:
                                                        for col in range(1,11):
                                                            if bucket== a.loc[dum][str(col)]:
                                                                    for gg in range(len(a.loc[dum][str(col)])):                                                                                  
                                                                      
                                                                        if gg==0:
                                                                            seatrow.append((a.loc[dum][str(col)])[0])
                                                                                                                                                                                      
                                                                                                                                              
                                                                    seatno.append(str(col))
                                                                                                                      
                              
                                                                    a.loc[dum][str(col)]=" THIS "
                                                                    index.append(dum)
                                                                    a.to_csv(df.loc[loki]['bookingscreen'])                                                                     
                                                                    i=i+1
                                            if bucket=="back" and len(seatno)!=0:
                                                i=i-1
                                                a.loc[index[-1]][seatno[-1]]=seatrow[-1]+seatno[-1]
                                                                                             
                                                del(seatrow[-1])
                                                del(seatno[-1])
                                                del(index[-1])
                                                                         
                                                a.to_csv(df.loc[loki]['bookingscreen'])
                                            elif bucket==sg.WIN_CLOSED :

                                                if len(seatno)!=0:
                                                    i=0
                                                    for k in range(len(seatno)):
                                                                                                 
                                                                                                     
                                                        a.loc[index[-1]][seatno[-1]]=seatrow[-1]+seatno[-1]
                                                                                                        
                                                        del(seatrow[-1])
                                                        del(seatno[-1])
                                                        del(index[-1])
                                                else:
                                                        i=1+noseats
                                                        u=u-1
                                                                        
                                                                                             
                                                a.to_csv(df.loc[loki]['bookingscreen'])
                                                silverseats=[]
                                                premiereseats=[]
                                                                                             
                                            elif bucket=="back" and len(seatno)==0:
                                                                                              
                                                u=u-1
                                                i=noseats+1         
                                                                                     
                                            if bucket=="BOOK":
                                                now1=dt.datetime.now()
                                                now2=now1+dt.timedelta(minutes=4)
                                            
                                                i=noseats+1 
                                                for hi in range(len(seatrow)):
                                                    if seatrow[hi]=="J" or seatrow[hi]=="K":
                                                        premiereseats.append((seatrow[hi],seatno[hi]))                                                                                
                                                    else:
                                                        silverseats.append((seatrow[hi],seatno[hi]))
                                                         
                                                orderedsnacksname=[]
                                                orderedsnacksprice=[]                                                                                          
                                                                                                      
                                                sunny=0
                                                bill=0
                                                while sunny<1:                # refreshments                                                                                                                                                                    
                                                    refreshments=pd.read_csv("movie refreshments.csv")                                                                                
                                                    refreshments=refreshments.set_index("id")
                                                                                                                                          
                                                    uniquesnackstype=unique_value(refreshments,"type")                                               
                                                    uniquesnacksimage=unique_value(refreshments,"image")                                 
                                                                                                                                          
                                                    textsnackstype=[]                                                                          
                                                    imagesnacksimage=[]
                                                    snacksbutton=[]                                                                          
                                                    for tip in range(len(uniquesnackstype)):
                                                        textsnackstype.append(sg.T(uniquesnackstype[tip].upper(),size=(27,1),font=("arial",13),justification="c"))
                                                        imagesnacksimage.append(sg.Image(uniquesnacksimage[tip]))
                                                        snacksbutton.append(sg.B("ORDER NOW",key=uniquesnackstype[tip]))
                                                                                                                                                                                                                                                                                                                                          
                                                    snackswindow=[[sg.T("R E F R E S H M E N T S",size=(31,1),font=("Times",40),justification='c')],
                                                                    textsnackstype,                                                                       
                                                                    imagesnacksimage,
                                                                    snacksbutton,
                                                                 [sg.B("PREVIOUS",size=(60,1)),sg.B("NEXT",size=(60,1))] ]                   
                                                    dora=sg.Window(" ",snackswindow,default_button_element_size=(29,1), auto_size_buttons=False)                                          
                                                    item,vals=dora.read()                                                                                          
                                                    dora.close()
                                                    blesso=0
                                                    while blesso<1:

                                                        snacksname=[]
                                                                                                                                                  
                                                        snacksprice=[]                                                                               
                                                        chatbutton=[]
                                                        refreshmentsname=[]
                                                        refreshmentsprice=[]
                                                        refreshmentlisting=[]                                                                 
                                                        for yoyo in uniquesnackstype:                                          
                                                            if item==yoyo:
                                                                                                                                                        
                                                                refreshments=refreshments[refreshments.type==item]                                                                  
                                                                refreshmentlisting.append([sg.T(yoyo.upper(),size=(30,1),font=("arial",20),justification='c')])
                                                                refreshmentlisting.append([sg.T("Item Name",size=(8,1),font=("Times",17)),sg.T("cost",size=(8,1),font=("Times",17),justification='c'),sg.T("          click to add",size=(15,1),font=("Times",17),justification='c')])
                                                                for jog in refreshments.index:                                                                               
                                                                    snacksname.append(sg.T(refreshments.loc[jog]["item"],size=(15,1)))
                                                                    snacksprice.append(sg.T("Rs:"+str(refreshments.loc[jog]["cost"]),size=(15,1)))           
                                                                    chatbutton.append(sg.B(refreshments.loc[jog]["item"]))
                                                                    refreshmentsname.append(refreshments.loc[jog]["item"])
                                                                    refreshmentsprice.append(refreshments.loc[jog]["cost"])
                                                                                                                                                                          
                                                                    refreshmentlisting.append([sg.T(refreshments.loc[jog]["item"],size=(20,1)),sg.T("Rs:"+str(refreshments.loc[jog]["cost"]),size=(20,1)),sg.B("ADD",key=refreshments.loc[jog]["item"])])
                                                                refreshmentlisting.append([sg.B("BACK")])                                                                                            

                                                                typ=refreshmentlisting
                                                                                                                                                                            
                                                                typewind=sg.Window(" ",typ,default_button_element_size=(14,1), auto_size_buttons=False)
                                                                mad,vals=typewind.read()

                                                                                                                                                  
                                                                typewind.close()                                                                  
                                                                                        
                                                                if mad=="BACK" or mad==sg.WIN_CLOSED:
                                                                        sunny=sunny-1
                                                                                                                                                                        
                                                                for thor in range(len(refreshmentsname)):
                                                                    if mad==refreshmentsname[thor]:
                                                                        sg.popup(mad,"+1 Item Added")                                                                                                                                                                                                        
                                                                        orderedsnacksname.append(mad)
                                                                        orderedsnacksprice.append(int(refreshmentsprice[thor]))
                                                                        blesso=blesso-1                                                                                                                         
                                                                                                                                                                                                                                                                                                                                
                                                        blesso=blesso+1                                
                                                                                                                                                                                  
                                                                                                                                                        
                                                    if item=="NEXT":                                                                                                                   
                                                            rice=0
                                                            bill=0
                                                            while rice<1:                                                                                                                      
                                                                orderedsnacksquantity=[]
                                                                uniqueorderedsnacksname=uniquelist(orderedsnacksname)
                                                                uniqueorderedsnacksprice=uniquelist(orderedsnacksprice)
                                         
                                                                for wiz in uniqueorderedsnacksname:
                                                                    quan=0
                                                                    for electro in orderedsnacksname:
                                                                        if wiz==electro:
                                                                             quan=quan+1
                                                                    orderedsnacksquantity.append(quan)
                                                                  
                                                                                                                                                                              
                                                                finalrefreshmentlisting=[]

                                                                if len(orderedsnacksname)!=0:
                                                                    finalrefreshmentlisting.append([sg.T("---------------------------------------------------------------------------------------------------------------------")])
                                                                    finalrefreshmentlisting.append([sg.T("SNACKS BILL",size=(30,1),font=("times",20),justification='c')])
                                                                    finalrefreshmentlisting.append([sg.T("---------------------------------------------------------------------------------------------------------------------")])
                                                                    finalrefreshmentlisting.append([sg.T("Items     cost       quantity     click to delete(-1)",size=(45,1),font=("arial",15),justification='c')])
                                                                                                                                                                     
                                                                    for kar in range(len(uniqueorderedsnacksname)):
                                                                            finalrefreshmentlisting.append(([sg.T(uniqueorderedsnacksname[kar],size=(15,1)),sg.T(orderedsnacksprice[kar],size=(15,1)),sg.T(orderedsnacksquantity[kar],size=(5,1)),sg.B("REMOVE",key=uniqueorderedsnacksname[kar])]))

                                                                                                                                                                                        
                                                                    finalrefreshmentlisting.append([sg.T("---------------------------------------------------------------------------------------------------------------------")])                                              

                                                                    finalrefreshmentlisting.append([sg.T("Total cost",size=(15,1)),sg.T("Rs:"+str(sum(orderedsnacksprice)),size=(15,1)),sg.T("Total quantity = "+str(len(orderedsnacksprice)),size=(15,1),justification='l')])
                                                                                                                                                                                     
                                                                    finalrefreshmentlisting.append([sg.B("Back"),sg.B("Proceed"),sg.B("Delete All")])
                                                                else:
                                                                    finalrefreshmentlisting.append([sg.B("Proceed",size=(20,1)),sg.B("Back",size=(20,1))])
                                                                                                                                                                                             

                                                                lake=finalrefreshmentlisting                                    
                                                                corn=sg.Window("Refreshment Bill",lake,default_button_element_size=(14,1), auto_size_buttons=False)
                                                                bad,vals=corn.read()                                                       
                                                                corn.close()
                                                                if (bad=="Back" or bad==sg.WIN_CLOSED)  :                                              
                                                                                                                                                                  
                                                                        rice=rice
                                                                        sunny=sunny-1                                                                           
                                                                elif bad!="Proceed" and bad!="Delete All":
                                                                                                                                                                           
                                                                        bat=0
                                                                        iq=-1
                                                                     
                                                                        for god in range(len(orderedsnacksname)):
                                                                                                                                                                                
                                                                                if orderedsnacksname[god]==bad :

                                                                                    bat=bat+1
                                                                                                                                                                                    
                                                                                    for monk in range(len(uniqueorderedsnacksname)):
                                                                                        if bad==uniqueorderedsnacksname[monk]:
                                                                                            iq=orderedsnacksquantity[monk]
                                                                                    
                                                                                            ram=monk
                                                                                    if bat==iq:                                                                     
                                                                                                                                                                                         
                                                                                        sai=god
                                                                                        finish=1
                                                                                      
                                                                                                                                                                                         
                                                                        if finish==1:
                                                                                                                                                                                

                                                                                del(orderedsnacksprice[sai])
                                                                                                                                                                                
                                                                                del(orderedsnacksname[sai])
                                                                                del(orderedsnacksquantity[ram])
                                                                                                                                                                                    
                                                                                                                                                                  
                                                                        rice=rice-1
                                                                if bad=="Proceed":                                                                                                                                
                                                                        print("")
                                                                                                                                                                             
                                                                                                                                                                             
                                                                elif bad=="Delete All":
                                                                        orderedsnacksname=[]
                                                                        orderedsnacksprice=[]
                                                                        orderedsnacksquantity=[]
                                                                        sunny=sunny-1
                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                   
                                                                rice=rice+1                    
                                                    if item=="PREVIOUS" or item==sg.WIN_CLOSED:
                                                            now3=dt.datetime.now()
                                                                                                                                                 
                                                            bill=1
                                                            if now3>now2:
                                                                                                                                                                                                                                       
                                                                orderedsnacksname=[]                              
                                                                orderedsnacksprice=[]
                                                                orderedsnacksquantity=[]
                                                                sandy=sandy-1                                                          
                                                                                                                                                    
                                                                i=noseats+1
                                                                zing=index
                                                                for gaythe in range(len(zing)):
                                                                    a.loc[zing[gaythe]][seatno[gaythe]]=seatrow[gaythe]+seatno[gaythe]
                                                                    a.to_csv(df.loc[loki]['bookingscreen'])
                                                            else:
                                                                                                                                                     
                                                                print(now3,now2,now1)                                                          
                                                                i=noseats
                                                                silverseats=[]
                                                                premiereseats=[]
                                                    sunny=sunny+1
                                                                                                                                                                                                                                                                                                          
                                                #total bill                                                                  
                                                if bill==0 :                                                                       
                                                                                                               
                                                        ticketcost=len(silverseats)*150 + len(premiereseats)*170
                                                        onlinecharges=(len(silverseats) + len(premiereseats))*40
                                                        totalcost=ticketcost+onlinecharges
                                                        snackscost=sum(orderedsnacksprice)
                                                        finalcost=snackscost+totalcost
                                                        bookingconfirm=[[sg.T("_____________________________________")],
                                                                        [sg.T("BILL",size=(15,1),font=("Times",20),justification='c')],
                                                                        [sg.T("_____________________________________")],
                                                                        [sg.T("Would you like to proceed further ?            ")],
                                                                        [sg.T("Ticketcost                     Rs:"+str(ticketcost))],
                                                                        [sg.T("Onlinecharges               Rs:"+str(onlinecharges))],
                                                                        [sg.T("Totalcost                      Rs:"+str(totalcost))],
                                                                        [sg.T("Snackscost                  Rs:"+str(snackscost))],
                                                                        [sg.T("_____________________________________")],
                                                                        [sg.T("Finalcost                      Rs:"+str(finalcost))],                                      
                                                                        [sg.T("______________________________________")],
                                                                                                                         
                                                                                                                  
                                                                        [sg.B("No"),sg.T("       "),sg.B("Yes")]]
                                                        work=sg.Window("Confirmation",bookingconfirm,default_button_element_size=(3,1), auto_size_buttons=False)

                                                        confirm,values=work.read()
                                                        work.close()
                                                        if confirm=="Yes":
                                                            for gaythe in a.index:
                                                                for jaga in range(1,11):
                                                                    if a.loc[gaythe][str(jaga)]==" THIS ":
                                                                        a.loc[gaythe][str(jaga)]="BKED"
                                                            sg.popup("Payment Successful")
                                                                                                                     

                                                            g=0
                                                            
                                                            #for creating a 5 digit unique code number for the user
                                                            while g<1:                   
                                                                codeno=rd.randint(10000,99999)
                                                                for xx in customer['codenos']:
                                                                    if xx==codeno:
                                                                         g=-1
                                                                g=g+1
                                                            codeno=str(codeno)
                                                            ww=0
                                                            while ww<1:
                                                                num=[[sg.Text("Enter your Name")],[sg.Input()],
                                                                    [sg.T("Enter your Phone Number")],[sg.Input()],                                                                        

                                                                    [sg.Button("Ok")]]

                                                                tata=sg.Window("Enter Details",num)
                                                                ting,vals=tata.read()
                                                                tata.close()
                                                                number=(vals[1])
                                                                customername=vals[0]

                                                                number=str(number)
                                                                if len(number)!=10 or ting==sg.WIN_CLOSED :
                                                                    sg.popup("Enter Valid Number")
                                                                    ww=ww-1
                                                                ww=ww+1
                                                                                                                            

                                                            for you in range(len(silverseats)):
                                                                if len(customer)!=0:
                                                                    customer.loc[max(customer.index)+1]=customername,number,codeno,showdate,event,even,silverseats[you][0],silverseats[you][1],"silver",str(150),strfttime,df.loc[loki]['bookingscreen']
                                                                else:
                                                                    customer.loc[1]=customername,number,codeno,showdate,event,even,silverseats[you][0],silverseats[you][1],"silver",str(150),strfttime,df.loc[loki]['bookingscreen']
                                                                
                                                            for you in range(len(premiereseats)):
                                                                if len(customer)!=0:
                                                                    customer.loc[max(customer.index)+1]=customername,number,codeno,showdate,event,even,premiereseats[you][0],premiereseats[you][1],"premre",str(170),strfttime,df.loc[loki]['bookingscreen']
                                                                else:
                                                                    customer.loc[1]=customername,number,codeno,showdate,event,even,premiereseats[you][0],premiereseats[you][1],"premre",str(170),strfttime,df.loc[loki]['bookingscreen']
                                                            
                                                                    
                                                            for you in range(len(orderedsnacksname)):
                                                                    kasx=refreshments[refreshments.item== orderedsnacksname[you]]
                                                                    if len(customersnacks)!=0:  
                                                                             customersnacks.loc[max(customersnacks.index)+1]=customername,number,codeno,showdate,even,seatrow[0],seatno[0],orderedsnacksname[you],kasx.loc[max(kasx.index)]["type"],str(1),orderedsnacksprice[you]
                                                                    else:
                                                                        customersnacks.loc[1]=customername,number,codeno,showdate,even,seatrow[0],seatno[0],orderedsnacksname[you],kasx.loc[max(kasx.index)]["type"],str(1),orderedsnacksprice[you]
                                                                
                                                                        
                                                            df=pd.read_csv("movie timing pro.csv")
                                                            df=df.set_index("_")
                                                            df.loc[loki,"seatsfilled"]=seatsfilled+len(seatrow)
                                                            df.loc[loki,"silver"]=df.loc[loki,"silver"]+len(silverseats)
                                                            df.loc[loki,"premiere"]=df.loc[loki,"premiere"]+len(premiereseats)
                                                            df.to_csv("movie timing pro.csv")

                                                            customersnacks.to_csv("customer snacks.csv")
                                                            customer.to_csv("customer.csv")
                                                            a.to_csv(df.loc[loki]['bookingscreen'])
                                                            sg.popup("your code number is:",codeno)

                                                            sg.popup("Thank you for booking.",
                                                                            "view your details in MY Details")
                                                            vari=vari-1
                                                                                                         
                                                        else:
                                                                                                                     
                                                            sandy=sandy-1
                    
                                                            zing=index
                                                            for gaythe in range(len(zing)):
                                                                a.loc[zing[gaythe]][seatno[gaythe]]=seatrow[gaythe]+seatno[gaythe]
                                                                a.to_csv(df.loc[loki]['bookingscreen'])                                                                                  
                                                                                         
                                u=u+1       

                sandy=sandy+1                   
        variable0=variable0+1 
  elif eventing=='EXIT' or eventing==sg.WIN_CLOSED:
      sg.popup("Thank you for visiting","Have a Good Day!")

  else:
      ww=0
      while ww<1:
            num=[[sg.Text("enter your name")],[sg.Input()],
                 [sg.T("enter your phone number")],[sg.Input()],
                 [sg.T("enter your codeno")],[sg.Input()],
                 [sg.B("submit"),sg.B("back")]]

            tata=sg.Window("number",num)
            ting,vals=tata.read()
            tata.close()
            
            looty=0
            if ting=="submit":
                  number=(vals[1])
                  customername=vals[0]
                  codeno=vals[2]
                  codeno=str(codeno)
                  number=str(number)
                  if len(number)!=10  :
                         sg.popup("enter valid number")
                         ww=ww-1
                  else:
                       pain=0
                       messi=0
                       while pain<1:
                            ktm=0
                            for guc in customer.index:
                                if messi==0:
                                   if customer.loc[guc]["name"]==customername and  str(customer.loc[guc]["phnno"])==str(number) and  str(customer.loc[guc]["codenos"])==str(codeno) and ktm==0:
                                      looty=1
                                      ktm=1
                                     
                                      customerdetails=customer[customer.codenos==str(codeno)]
                                      if len(customerdetails)==0:
                                          customerdetails=customer[customer.codenos==int(codeno)]
                                      bookingscreenloc=unique_value(customerdetails,"bookingscreen")
                                      customerdetails=customerdetails.drop(["name","phnno","codenos","programtime","bookingscreen"],axis=1)
                                      customersnacksdetails=customersnacks[customersnacks.codenos==str(codeno)]
                                      if len(customersnacksdetails)==0:
                                          customersnacksdetails=customersnacks[customersnacks.codenos==int(codeno)]
                                      customersnacksdetails=customersnacksdetails.drop(["name","phnno","codenos","seat","no","date","showtime"],axis=1)
                                      b=pd.read_csv(bookingscreenloc[0])
                                                    
                                      b=b.set_index("alphabets")
                                      totaltickets=len(customerdetails)
                                      if len(customersnacksdetails)==0:
                                                    sg.popup("name:"+customername+"   "+"phnno:"+number+"   "+"codenos:"+str(codeno),customerdetails,"totaltickets:"+str(totaltickets),title="details")
                                            
                                      else:
                                                    sg.popup("name:"+customername+"   "+"phnno:"+number+"   "+"codenos:"+str(codeno),customerdetails,"totaltickets:"+str(totaltickets),"SNACKS DETAILS  ",customersnacksdetails,"quantity:"+str(len(customersnacksdetails)),title="details")
                                 
                                      if eventing!='MY DETAILS':
                                            customerdetails=customer[customer.codenos==str(codeno)]
                                            if len(customerdetails)==0:
                                                    customerdetails=customer[customer.codenos==int(codeno)]
                                            customerdetails=customerdetails.drop(["name","phnno","codenos","bookingscreen"],axis=1)


                                          
                                            now=dt.datetime.now()
                                            for t in customerdetails.index:
                                                print("")
                                            timeobj=customerdetails.loc[t]['date']+(" ")+customerdetails.loc[t]['programtime']
                                            timeformat=datetime.strptime(timeobj,"%d-%m-%Y %H:%M")-dt.timedelta(minutes=30)
                                            if timeformat<now:
                                                sg.popup("you cant cancel since time is up")
                                            else:
                                                customerdetailslist=[[sg.T("tick to cancel")],[sg.T(" ",size=(10,1)),sg.T("seat alp",size=(10,1)),sg.T("seat no",size=(10,1))]]
                                                cusindex=list(customerdetails.index)
                                                cusseatalp=list(customerdetails.seat)
                                                cusseatno=list(customerdetails.no)
                                                cusseatalpno=[]
                                                indexdel=[]
                                                for pro in range(len(cusindex)):
                                                    customerdetailslist.append([sg.T(str((pro+1)),size=(10,1)),sg.T(cusseatalp[pro],size=(10,1)),sg.T(str(cusseatno[pro]),size=(10,1)),sg.Checkbox("remove",key=cusseatalp[pro]+str(cusseatno[pro]),size=(10,1))])
                                                    
                                                    cusseatalpno.append(cusseatalp[pro]+str(cusseatno[pro]))
                                                customerdetailslist.append([sg.B("OK"),sg.B("Back")])    
                                                icewiz=customerdetailslist
                                                punk=sg.Window("cancellation",icewiz)
                                                dumal,vals=punk.read()
                                                punk.close()
                                                if dumal==sg.WIN_CLOSED or dumal=="Back":
                                              
                                                    ww=ww-1
                                                    
                                                elif dumal=="OK":
                                                    cashreturn=0
                                                    df=pd.read_csv('movie timing pro.csv')
                                                    df=df.set_index('_')
                                                 
                                                
                                                    for maxi in range(len(cusseatalpno)):
                                                         if vals[cusseatalpno[maxi]]==True:
                                                              
                                                              for kgd in df.index:
                                                                     if df.loc[kgd]["movie"]==customerdetails.loc[max(customerdetails.index)]["movie"] and df.loc[kgd]["showtime"]==customerdetails.loc[max(customerdetails.index)]["showtime"] and df.loc[kgd]["date"]==customerdetails.loc[max(customerdetails.index)]["date"] :
                                                                           df.loc[kgd,"seatsfilled"]=df.loc[kgd,"seatsfilled"] - 1
                                                                           if cusseatalpno[maxi][0] in ("K","J"):
                                                                               df.loc[kgd,"premiere"]=df.loc[kgd,"premiere"] - 1
                                                                           else:
                                                                               df.loc[kgd,"silver"]=df.loc[kgd,"silver"] - 1
                                                              df.to_csv('movie timing pro.csv')
                                                           
                                                              cashreturn=cashreturn+int(customerdetails.loc[cusindex[maxi]]["cost"])
                                                              customerdetails=customerdetails.drop(cusindex[maxi])
                                                              customer=customer.drop(cusindex[maxi])
                                                             
                                                              
                                                              b.loc[cusseatalp[maxi],str(cusseatno[maxi])]=cusseatalpno[maxi]
                                                             
                                                              b.to_csv(bookingscreenloc[0])
                                                    customer.to_csv("customer.csv")
                                                    customerdetails=customer[customer.codenos==int(codeno)]
                                                    if len(customerdetails)==0:
                                                         customerdetails=customer[customer.codenos==str(codeno)]
                                                
                                                    sg.popup("scucessfully cancelled and cash Rs:"+str(cashreturn)+"retured")
                                                    messi=1
                                                    vari=vari-1
    
                                      else:
                                          vari=vari-1
                            pain=pain+1          
    
                       if looty==0:
                              sg.popup("your mobileno or codeno or name is invalid") 
                              ww=ww-1
            elif ting!="submit" :
                vari=vari-1                    
            ww=ww+1       
  vari=vari+1
  #customer=customer[customer.index==0]
  #customer.to_csv("customer.csv")
  #customersnacks=customersnacks[customersnacks.index==0]
  #customersnacks.to_csv("customer snacks.csv")
                                
            
            
                  
