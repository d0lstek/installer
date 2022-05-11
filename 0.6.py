#Англиская версия ..................................................................................................................................................
def change_language():                                              #Кнопка online (англисский)
    global self                                                     #Меин окно для self
    self = Toplevel(tk)                                             #Окно
    self.geometry("1290x900")                                       #Геометрия окна
    self.title("English version")                                   #Названия окна
    self.resizable(width=False, height=False)                       #Запрет на изменения окна
    self.image = PhotoImage(file="image/EnglishImage/ingl.png")                  #Экран англиский
    screen2 = Label(self, image=self.image)                         #Экран выбора режима и языка(англиский)
    screen2.grid(row=0, column=0)                                   #Экран выбора режима и языка(англиский)
    #bl = Button(self,image = online, command = onlin2)              #Кнопка онлаин (англиский)
    #bl.place(x=450,y=500, width=200, height=100)                    #Размеры кнопки
    bl = Button(self,image = ruEn, command = change_lang)           #Кнопка перевода на русский (англиский)
    bl.place(x=410,y=798, width=200, height=100)                    #Размеры кнопки
    bl = Button(self,image = exit1En, command = ext1)               #Кнопка выхода (англиский)
    bl.place(x=12,y=798, width=200, height=100)                     #Размеры кнопки
    bl = Button(self,image = sozdEn, command = creat)               #Кнопка о создателе En
    bl.place(x=210,y=848, width=200, height=50)                     #Размеры кнопки
    bl = Button(self,image = OPROGEn, command = oprogEn)            #Кнопка смены языка
    bl.place(x=210,y=798, width=200, height=50)                     #Размеры кнопки
    bl = Button(self,image = usb, command = ussbEn)                 #Кнопка смены языка
    bl.place(x=650,y=500, width=200, height=100)                    #Размеры кнопки
    bl = Button(self, image=git, command=lambda: webbrowser.open("https://github.com/d0lstek", new=2, autoraise="True")) #кнопка git
    bl.place(x=610,y=798, width=200, height=100)                    #Размеры кнопки
    tk.withdraw()                                                   #Закрытие русского окна


def change_lang():                                                  
    tk.deiconify()                                                  
    self.withdraw()                                                 

def ussbEn():
    ussbEn= Toplevel(tk)                                            
    ussbEn.geometry("1290x900")                                     
    ussbEn.title("USB INSTALLER")                                   
    ussbEn.resizable(width=False, height=False)                     
    ussbEn.image = PhotoImage(file="image/EnglishImage/ussbpinEn.png")           
    screen10 = Label(ussbEn, image=ussbEn.image)                    
    screen10.grid(row=0, column=0)                                  
    bl = Button(ussbEn,image = activEn)                            
    bl.place(x=100,y=400, width=300, height=100)                    
    self.withdraw()                                                

    


def oprogEn():
    OPROGEn= Toplevel(tk)                                           #Открытое англиского меню
    OPROGEn.geometry("800x400")                                     #Геометрия окна
    OPROGEn.title("About the program")                              #Названия окна
    OPROGEn.resizable(width=False, height=False)                    #Запрет на изменение окна (англ. версия)
    screen4 = Label(OPROGEn, image=oprog.image)                     #Экран выбора режима и языка(англиский)
    screen4.grid(row=0, column=0)
                                      
def creat():
    creator = Toplevel(tk)                                          #Окно
    creator.geometry("400x400")                                     #Геометрия окна
    creator.title("About the сreator")                              #Названия окна                              
    creator.resizable(width=False, height=False)                    #Запрет на изменения окна
    screen17 = Label(creator, image=cretEn1)                         #Экран выбора режима и языка(англиский)
    screen17.grid(row=0, column=0)

    
    
    


#Русская версия.....................................................................................................................................................    
def sozt():
    sozd = Toplevel(tk)                                            
    sozd.geometry("400x400")                                       
    sozd.title("О создателе")                                                                   
    sozd.resizable(width=False, height=False)                      
    sozd.image = PhotoImage(file="image/russianEmage/o_avtore.png")             
    screen5 = Label(sozd, image=sozd.image)                        
    screen5.grid(row=0, column=0)                                  
    bl = Button(sozd, image=vk, command=lambda: webbrowser.open("https://vk.com/d0lstek", new=2, autoraise="True"))
    bl.place(x=70,y=102, width=250, height=50)

def oprog():
    oprog = Toplevel(tk)                                           
    oprog.geometry("800x400")                                     
    oprog.title("О программе")                                                                
    oprog.resizable(width=False, height=False)                      
    oprog.image = PhotoImage(file="image/russianEmage/О_программе.png")          
    screen4 = Label(oprog, image=oprog.image)                      
    screen4.grid(row=0, column=0)                                   
                                                        
def ext1():
    tk.destroy()                                                   

def ussb5():                                                           
    global ussb
    ussb = Toplevel(tk)
    ussb.geometry("1280x900+320+60")                                        
    ussb.title("Меню")                                                                    
    ussb.resizable(width=False, height=False)                        
    ussb.image = PhotoImage(file="image/russianEmage/ussbpin.png")               
    screen8 = Label(ussb, image=ussb.image)                           
    screen8.grid(row=0, column=0)                                   
    bl = Button(ussb,image = winak, command = aktiv)                 
    bl.place(x=100,y=400, width=300, height=100)                   
    bl = Button(ussb,image = oboi, command = oboi1)                 
    bl.place(x=100,y=550, width=300, height=100)                   
    bl = Button(ussb,image = prog, command = installers5)                                  
    bl.place(x=450,y=400, width=300, height=100)                    
    bl = Button(ussb,image = razOC, command = razgentt)                                   
    bl.place(x=450,y=550, width=300, height=100)
    bl = Button(ussb, image = nazadd2, command = nazaddd)                                   
    bl.place(x=5,y=845, width=200, height=50)
    bl = Button(ussb, image = voskl, command = voskl2)                                   
    bl.place(x=210,y=845, width=50, height=50) 
    tk.withdraw()

def voskl2():
    voskl2 = Toplevel(tk)
    voskl2.geometry("500x500")                                     
    voskl2.title("Осторожно")
    voskl2.resizable(width=False, height=False)
    screen19 = Label(voskl2, image=voskl12)                           
    screen19.grid(row=0, column=0)
    bl = Button(voskl2, image = vk, command=lambda: webbrowser.open("https://vk.com/d0lstek", new=2, autoraise="True"))                                   
    bl.place(x=200,y=430, width=250, height=50) 
    
def razgentt():
    global razgen
    razgen = Toplevel(tk)
    razgen.geometry("500x400+720+340")                                     
    razgen.title("Выбор платформы")
    razgen.resizable(width=False, height=False)
    screen18 = Label(razgen, image=razgon)                           
    screen18.grid(row=0, column=0)
    bl = Button(razgen,image = razgIntel, command = lambda obj=razgIntel: razIntel(razgen))
    bl.place(x=40,y=120, width=200, height=100)
    bl = Button(razgen, image = razgAMD, command = razAMD)                                   
    bl.place(x=250,y=120, width=200, height=100)

def razIntel(obj):
    razIntel5 = Toplevel(tk)
    razIntel5.geometry("1280x720+320+180")                                     
    razIntel5.title("Intel core")                                    
    razIntel5.resizable(width=False, height=False)
    screen23 = Label(razIntel5, image=razIntelamg)                           
    screen23.grid(row=0, column=0)
    bl = Button(razIntel5,image = nazadd2blue, command = lambda obj=intelexit: intelexit(razIntel5))
    bl.place(x=5,y=670, width=200, height=50)
    bl = Button(razIntel5, image = kakblue, command = lambda: webbrowser.open("https://youtube.com/playlist?list=PLq1_Khrw-KtwxVZzf4EDi801XC0_NIOmr", new=2, autoraise="True"))                                 
    bl.place(x=230,y=670, width=300, height=50)
    bl = Button(razIntel5, image = fur, command = furmark)                                  
    bl.place(x=985,y=530, width=256, height=72)
    bl = Button(razIntel5, image = gpuz, command = gpu)                                  
    bl.place(x=985,y=603, width=256, height=72)
    bl = Button(razIntel5, image = msiavt, command = msi)                                  
    bl.place(x=690,y=530, width=256, height=144)
    bl = Button(razIntel5, image = aida, command = aida5)                                  
    bl.place(x=985,y=200, width=256, height=72)
    bl = Button(razIntel5, image = occt, command = OCCT1)                                  
    bl.place(x=985,y=273, width=256, height=72)
    bl = Button(razIntel5, image = intelmaster11, command = intelmasterst)                                  
    bl.place(x=700,y=200, width=256, height=144)
    razgen.withdraw()
    ussb.withdraw()

def intelmasterst():
    global intelwin
    intelwin = Toplevel(tk)
    intelwin.geometry("300x300+690+210")                                     
    intelwin.title("Intel core")                                    
    intelwin.resizable(width=False, height=False)
    screen25 = Label(intelwin, image=ystovkaintel)                           
    screen25.grid(row=0, column=0)
    bl = Button(intelwin, image = prodolintel, command = intelmasteru)                                  
    bl.place(x=50,y=230, width=200, height=50)
    
def intelmasteru():
    import os
    os.startfile("DLL_files\OC\INTEL\intl.exe")
    intelwin.withdraw()

def razAMD():
    razAMD = Toplevel(tk)
    razAMD.geometry("1280x720+320+180")                                     
    razAMD.title("AMD")
    screen22 = Label(razAMD, image=razAMDlabel)                           
    screen22.grid(row=0, column=0)
    razAMD.resizable(width=False, height=False)
    bl = Button(razAMD,image = nazadd2, command = lambda obj=amdexit: amdexit(razAMD))                                  
    bl.place(x=5,y=670, width=200, height=50)
    bl = Button(razAMD, image = ryzenmaster, command = ryzmaster)                                  
    bl.place(x=600,y=200, width=256, height=144)
    bl = Button(razAMD, image = aida, command = aida5)                                  
    bl.place(x=900,y=200, width=256, height=72)
    bl = Button(razAMD, image = occt, command = OCCT1)                                  
    bl.place(x=900,y=273, width=256, height=72)
    bl = Button(razAMD, image = fur, command = furmark)                                  
    bl.place(x=900,y=530, width=256, height=72)
    bl = Button(razAMD, image = gpuz, command = gpu)                                  
    bl.place(x=900,y=603, width=256, height=72)
    bl = Button(razAMD, image = msiavt, command = msi)                                  
    bl.place(x=600,y=530, width=256, height=144)
    bl = Button(razAMD, image = kak, command = lambda: webbrowser.open("https://youtube.com/playlist?list=PLq1_Khrw-KtwxVZzf4EDi801XC0_NIOmr", new=2, autoraise="True"))                                 
    bl.place(x=230,y=670, width=300, height=50)
    razgen.withdraw()
    ussb.withdraw()
def furmark():
    import os
    os.startfile("DLL_files\OC\TEST\ls1.lnk")

def gpu():
    import os
    os.startfile("DLL_files\OC\TEST\gpu-z\gpu.exe")

def msi():
    import os
    os.startfile("DLL_files\OC\TEST\ms.lnk")

def ryzmaster():
    import os
    os.startfile("DLL_files\OC\AMD\ms.lnk")

def aida5():
    import os
    os.startfile("DLL_files\OC\TEST\AIDA64Extreme\i64.lnk")

def OCCT1():
    import os
    os.startfile("DLL_files\OC\TEST\OCCT.exe")

def amdexit(obj):
    ussb.deiconify()
    obj.withdraw()

def intelexit(obj):
    ussb.deiconify()
    obj.withdraw()
    
def installers5():
    global installers3
    installers3 = Toplevel(tk)
    installers3.geometry("500x500+700+300")                                     
    installers3.title("Выбор версии")                                    
    installers3.resizable(width=False, height=False)
    screen29 = Label(installers3, image=viborInstaler)                           
    screen29.grid(row=0, column=0)
    bl = Button(installers3,image = onlininstaler, command = onlineinstalers)
    bl.place(x=40,y=400, width=200, height=50)
    bl = Button(installers3,image = instaler5, command = installers1)
    bl.place(x=260,y=400, width=200, height=50)

def onlineinstalers():
    global installers8
    installers8 = Toplevel(tk)
    installers8.geometry("1280x720")                                     
    installers8.title("online установщик")                                    
    installers8.resizable(width=False, height=False)
    tab_control = ttk.Notebook(installers8)
    tab4 = ttk.Frame(tab_control)
    tab5 = ttk.Frame(tab_control)
    tab6 = ttk.Frame(tab_control)
    tab_control.add(tab4,image=s1of3)
    tab_control.add(tab5,image=s2of3)
    tab_control.add(tab6,image=s3of3)
    tab_control.pack(expand=1, fill='both')   
    screen30 = Label(tab4, image=installerss)                           
    screen30.grid(row=0, column=0)
    screen31 = Label(tab5, image=installerss)                           
    screen31.grid(row=0, column=0)
    screen32 = Label(tab6, image=installerss)                           
    screen32.grid(row=0, column=0)
    ussb.withdraw()
    bl = Button(installers8,image = exit1, command = lambda obj=eeitttl5: eeitttl5(onlineinstalers))
    bl.place(x=5,y=660, width=200, height=50)
    installers3.withdraw()

def nws():
    installers81 = Toplevel(tk)
    installers81.geometry("1280x720")                                     
    installers81.title("online установщик")                                    
    installers81.resizable(width=False, height=False)

from tkinter import ttk
def installers1():
    global installers
    installers = Toplevel(tk)
    installers.geometry("1280x720+300+80")                                     
    installers.title("USB установщик")                                    
    installers.resizable(width=False, height=False)
    ussb.withdraw()
    tab_control = ttk.Notebook(installers)
    pro1 = ttk.Frame(tab_control)
    pro2 = ttk.Frame(tab_control)
    pro3 = ttk.Frame(tab_control)
    tab_control.add(pro1, image=s1of3)
    tab_control.add(pro2, image=s2of3)
    tab_control.add(pro3, image=s3of3)
    tab_control.pack(expand=1, fill='both')   
    screen33 = Label(pro1, image=installerss)                           
    screen33.grid(row=0, column=0)
    screen34 = Label(pro2, image=installerss)                           
    screen34.grid(row=0, column=0)
    screen35 = Label(pro3, image=installerss)                           
    screen35.grid(row=0, column=0)
    bl = Button(installers,image = exit1, command = lambda obj=eeitttl: eeitttl(installers))
    bl.place(x=5,y=665, width=200, height=50)
    bl = Button(pro1,image = chrome, command = chromeinstaler)
    bl.place(x=1,y=165, width=256, height=144)
    bl = Button(pro1,image = fairfox, command = fairfoxinstaler)
    bl.place(x=1,y=309, width=256, height=144)
    bl = Button(pro1,image = operaGX, command = operaGXinstaler)
    bl.place(x=1,y=453, width=256, height=144)
    o12 = Label(pro1,image = brauzers)
    o12.place(x=1,y=85, width=256, height=80)
    bl = Button(pro1,image = steam, command = steaminstaler)
    bl.place(x=257,y=165, width=256, height=144)
    bl = Button(pro1,image = origin, command = origininstaler)
    bl.place(x=257,y=309, width=256, height=144)
    bl = Button(pro1,image = epicgames , command = epicinstaler)
    bl.place(x=257,y=453, width=256, height=144)
    o13 = Label(pro1,image = gameprog)
    o13.place(x=257,y=85, width=256, height=80)
    bl = Button(pro1,image = cinema4d, command = cinema4dinstaler)
    bl.place(x=513,y=165, width=256, height=144)
    bl = Button(pro1,image = blender, command = blenderinstaler)
    bl.place(x=513,y=309, width=256, height=144)
    bl = Button(pro1,image = code3d, command = code3dinstaler)
    bl.place(x=513,y=453, width=256, height=144)
    o14 = Label(pro1,image = dredaktor)
    o14.place(x=513,y=85, width=256, height=80)
    bl = Button(pro1,image = OCCT2 , command = occtinstaler)
    bl.place(x=769,y=309, width=256, height=144)
    bl = Button(pro1,image = AIDA642, command = aidainstaler)
    bl.place(x=769,y=453, width=256, height=144)
    bl = Button(pro1,image = furmark2, command = furinstaler)
    bl.place(x=769,y=165, width=256, height=144)
    o14 = Label(pro1,image = pctests)
    o14.place(x=769,y=85, width=256, height=80)
    bl = Button(pro1,image = office2010 , command = office2010instaler)
    bl.place(x=1025,y=309, width=256, height=144)
    bl = Button(pro1,image = office2013, command = office2013instaler)
    bl.place(x=1025,y=453, width=256, height=144)
    bl = Button(pro1,image = office2019, command = office2019instaler)
    bl.place(x=1025,y=165, width=256, height=144)
    o15 = Label(pro1,image = office)
    o15.place(x=1025,y=85, width=256, height=80)
    installers3.withdraw()
    bl = Button(pro2,image = zip7, command = zip7s)
    bl.place(x=2,y=300, width=256, height=144)
    bl = Button(pro2,image = winrars, command = winrar)
    bl.place(x=2,y=165, width=256, height=144)
    o166 = Label(pro2,image = arhivators)
    o166.place(x=2,y=85, width=256, height=80)
    bl = Button(pro2,image = discord, command = discordinstaler)
    bl.place(x=257,y=165, width=256, height=144)
    bl = Button(pro2,image = teamsleak , command = x32or64speak)
    bl.place(x=257,y=300, width=256, height=144)
    o43 = Label(pro2,image = goloschat)
    o43.place(x=258,y=85, width=256, height=80)
    bl = Button(pro2,image = premerpro, command = instalerpremer)
    bl.place(x=513,y=165, width=256, height=144)
    bl = Button(pro2,image = vegas, command = vegasmenu)
    bl.place(x=513,y=300, width=256, height=144)
    o44 = Label(pro2,image = videoredactors )
    o44.place(x=513,y=85, width=256, height=80)
    bl = Button(pro2,image = photoshop1, command = photoinstaller1)
    bl.place(x=769,y=300, width=256, height=144)
    bl = Button(pro2,image = photoshop2, command =photoinstaller2)
    bl.place(x=769,y=165, width=256, height=144)
    o61 = Label(pro2,image = photoedits)
    o61.place(x=769,y=85, width=256, height=80)
    bl = Button(pro2,image = notepad, command = notepadinstaller)
    bl.place(x=1025,y=165, width=256, height=144)
    bl = Button(pro2,image = paychart, command = paychartinstaller)
    bl.place(x=1025,y=300, width=256, height=144)
    o15 = Label(pro2,image = textredacross)
    o15.place(x=1025,y=85, width=256, height=80)
    o15 = Label(pro3,image = raznastprogram)
    o15.place(x=1,y=85, width=1280, height=80)

def notepadinstaller():
    import os
    os.system("DLL_files\\usb\\textredaction\\not.exe")

def paychartinstaller():
    import os
    os.system("DLL_files\\usb\\textredaction\\pycharm.exe")

def photoinstaller1():
    import os
    os.system("DLL_files\\usb\\photoshops\\ph.exe")

def photoinstaller2():
    import os
    os.system("DLL_files\\usb\\photoshops\\ph2.exe")
    

def vegasmenu():
    global vegasmenu12
    vegasmenu12 = Toplevel(tk)
    vegasmenu12.geometry("500x200+710+340")                                     
    vegasmenu12.title("vegas")                                    
    vegasmenu12.resizable(width=False, height=False)
    screen37 = Label(vegasmenu12, image=vegasss)                           
    screen37.grid(row=0, column=0)
    bl = Button(vegasmenu12,image = vegas13, command = vegasinstaler13)
    bl.place(x=30,y=25, width=220, height=150)
    bl = Button(vegasmenu12,image = vegas15, command = vegasinstaler15)
    bl.place(x=260,y=25, width=220, height=150)

def discordinstaler():
    import os
    os.system("DLL_files\\usb\\chats\\discord")

def vegasinstaler13():
    import os
    os.system("DLL_files\\usb\\redacrorvideo\\13.exe")
    vegasmenu12.withdraw()

def vegasinstaler15():
    import os
    os.system("DLL_files\\usb\\redacrorvideo\\ex5.exe")
    vegasmenu12.withdraw()

def instalerpremer():
    import os
    os.system("DLL_files\\usb\\redacrorvideo\\premer.exe")

def x32or64speak():
    global speak32or64
    speak32or64 = Toplevel(tk)
    speak32or64.geometry("300x200")                                     
    speak32or64.title("x86orx64")                                    
    speak32or64.resizable(width=False, height=False)
    screen36 = Label(speak32or64, image=x86orx64)                           
    screen36.grid(row=0, column=0)
    bl = Button(speak32or64,image = x86, command = teamsleakinstaller86)
    bl.place(x=30,y=120, width=120, height=50)
    bl = Button(speak32or64,image = x64, command = teamsleakinstaller64)
    bl.place(x=165,y=120, width=120, height=50)
    bl = Button(speak32or64,image = sssvopros,command = osystem)
    bl.place(x=230,y=20, width=50, height=50)


def teamsleakinstaller86():
    import os
    os.system("DLL_files\\usb\\chats\\teamspeak32")
    speak32or64.withdraw()

def teamsleakinstaller64():
    import os
    os.system("DLL_files\\usb\\chats\\teamspeak64")
    speak32or64.withdraw()

def winrar():
    import os
    os.system("DLL_files\\usb\\arhivators\\win")

def zip7s():
    global zip32or64
    zip32or64 = Toplevel(tk)
    zip32or64.geometry("300x200")                                     
    zip32or64.title("x86orx64")                                    
    zip32or64.resizable(width=False, height=False)
    screen35 = Label(zip32or64, image=x86orx64)                           
    screen35.grid(row=0, column=0)
    bl = Button(zip32or64,image = x86, command = zip7x86)
    bl.place(x=30,y=120, width=120, height=50)
    bl = Button(zip32or64,image = x64, command = zip7x64)
    bl.place(x=165,y=120, width=120, height=50)
    bl = Button(zip32or64,image = sssvopros, command = osystem)
    bl.place(x=230,y=20, width=50, height=50)
    

def office2010instaler():
    global la64ox86
    la64ox86 = Toplevel(tk)
    la64ox86.geometry("300x200+750+360")                                     
    la64ox86.title("x86orx64")                                    
    la64ox86.resizable(width=False, height=False)
    screen30 = Label(la64ox86, image=x86orx64)                           
    screen30.grid(row=0, column=0)
    bl = Button(la64ox86,image = x86, command = x86installer)
    bl.place(x=30,y=120, width=120, height=50)
    bl = Button(la64ox86,image = x64, command = x64installer)
    bl.place(x=165,y=120, width=120, height=50)
    bl = Button(la64ox86,image = sssvopros, command = osystem)
    bl.place(x=230,y=20, width=50, height=50)

def zip7x86():
    import os
    os.startfile("DLL_files\\usb\\arhivators\\7zip\\32.exe")
    zip32or64.withdraw()

def zip7x64():
    import os
    os.startfile("DLL_files\\usb\\arhivators\\7zip\\64.exe")
    zip32or64.withdraw()
    

def osystem():
    import os
    os.system("explorer shell:::{BB06C0E4-D293-4F75-8A90-CB05B6477EEE}")

def x86installer():
    import os
    os.startfile("DLL_files\\usb\\OFFICE\\2010\\x86(32bit)\\x86.exe")
    la64ox86.withdraw()

def x64installer():
    import os
    os.startfile("DLL_files\\usb\\OFFICE\\2010\\x64(64bit)\\x64.exe")
    la64ox86.withdraw()
    

def office2013instaler():
    import os
    os.startfile("DLL_files\\usb\\OFFICE\\2013\\x64_and_x86\\ofis")
    
def office2019instaler():
    import os
    #os.startfile("C:\\Users\\Dmitriy\\Desktop\\Программа\\DLL_files\\usb\\OFFICE\\2019\\Setup.exe")

def furinstaler():
    import os
    os.startfile("DLL_files\\usb\\PCTEST\\FurMark.exe")

def occtinstaler():
    import os
    os.startfile("DLL_files\\usb\\PCTEST\\OCCT.exe")
    
def aidainstaler():
    import os
    os.startfile("DLL_files\\usb\\PCTEST\\aida64.exe")

def cinema4dinstaler():
    global cinema4dinstaler55
    cinema4dinstaler55 = Toplevel(tk)
    cinema4dinstaler55.geometry("600x200+660+240")                                     
    cinema4dinstaler55.title("Ключ активации")                                    
    cinema4dinstaler55.resizable(width=False, height=False)
    screen30 = Label(cinema4dinstaler55, image=keyslagCinema)                           
    screen30.grid(row=0, column=0)
    bl = Button(cinema4dinstaler55,image = scopiravat, command = cinema4dinstaler2)
    bl.place(x=530,y=20, width=50, height=50)
    bl = Button(cinema4dinstaler55,image = ystanovka, command = cinema4dinstaler22)
    bl.place(x=175,y=130, width=250, height=50)

def cinema4dinstaler2():
    tk.clipboard_clear()
    tk.clipboard_append('14904057274-SHJL-WDFT-JZTM-RTKX-ZSXV-PXBZ')

def cinema4dinstaler22():
    import os
    os.startfile("DLL_files\\usb\\3dredaktors\\CINEMA\\R19_Install_Web_Win\\MAXON-Start.exe")
    cinema4dinstaler55.withdraw()
    
def blenderinstaler():
    import os
    os.startfile("DLL_files\\usb\\3dredaktors\\Blender\\Blender\\blender.msi")

def code3dinstaler():
    import os
    os.startfile("DLL_files\\usb\\3dredaktors\\3dCODE\\3d\\3DCoat.exe")


def steaminstaler():
    import os
    os.startfile("DLL_files\\usb\\gamelauncher\\steam\\SteamSetup.exe")

def epicinstaler():
    import os
    os.startfile("DLL_files\\usb\\gamelauncher\\epic\\epic.msi")

def origininstaler():
    import os
    os.startfile("DLL_files\\usb\\gamelauncher\\origin\\OriginThinSetup.exe")

def operaGXinstaler():
    import os
    os.startfile("DLL_files\\usb\\brauzers\\opersGX\\OperaGXSetup")

def fairfoxinstaler():
    import os
    os.startfile("DLL_files\\usb\\brauzers\\firefox\\FirefoxSetup")

def chromeinstaler():
    import os
    os.startfile("DLL_files\\usb\\brauzers\\chrome\\google")
    
def eeitttl(obj):
    ussb.deiconify()
    obj.destroy()

def eeitttl5(obj):
    ussb.deiconify()
    installers8.withdraw()

def nazaddd():
    ussb.withdraw()
    tk.deiconify()

def oboi1():
    global oboi1
    oboi = Toplevel(tk)
    oboi.geometry("500x200+710+440")                                     
    oboi.title("Обои")                                    
    oboi.resizable(width=False, height=False)                    
    screen12 = Label(oboi, image=sprosobi)                           
    screen12.grid(row=0, column=0)                                   
    bl = Button(oboi,image = animoct, command = lambda obj=oboi: animeoct(oboi))                                  
    bl.place(x=255,y=100, width=150, height=75)                    
    bl = Button(oboi, image = animoobrat, command = lambda obj=oboi: nanimenol(oboi))                                  
    bl.place(x=70,y=100, width=150, height=75)

def nanimenol(obj):
    global nanimeno
    nanimeno = Toplevel(tk)
    nanimeno.geometry("1280x600+320+240")                                    
    nanimeno.title("Обои 1из2")                                    
    nanimeno.resizable(width=False, height=False)
    screen20 = Label(nanimeno, image=viberit)                           
    screen20.grid(row=0, column=0)
    bl = Button(nanimeno, image = dalee, command = lambda obj=nanimeno: dale15(nanimeno))
    bl.place(x=700,y=530, width=150, height=75)  
    bl = Button(nanimeno, image = vahod, command = lambda obj=nanimeno: exitt3(nanimeno))
    bl.place(x=550,y=530, width=150, height=75)
    bl = Button(nanimeno, image = liza, command = lizaa)                                  
    bl.place(x=257,y=150, width=256, height=144)
    bl = Button(nanimeno, image = anime10, command = anim10)                                  
    bl.place(x=513,y=150, width=256, height=144)
    bl = Button(nanimeno, image = anime11, command = anim11)                                  
    bl.place(x=769,y=150, width=256, height=144)
    bl = Button(nanimeno, image = anime12, command = anim12)                                  
    bl.place(x=1,y=150, width=256, height=144)
    bl = Button(nanimeno, image = anime13, command = anim13)                                  
    bl.place(x=1025,y=150, width=256, height=144)
    bl = Button(nanimeno, image = anime14, command = anim14)                                  
    bl.place(x=257,y=296, width=256, height=144)
    bl = Button(nanimeno, image = anime15, command = anim15)                                  
    bl.place(x=513,y=296, width=256, height=144)
    bl = Button(nanimeno, image = anime16, command = anim16)                                  
    bl.place(x=769,y=296, width=256, height=144)
    bl = Button(nanimeno, image = anime17, command = anim17)                                  
    bl.place(x=1,y=296, width=256, height=144)
    bl = Button(nanimeno, image = anime18, command = anim18)                                  
    bl.place(x=1025,y=296, width=256, height=144)
    ussb.withdraw()
    obj.withdraw()

def dale15(obj):
    dale15 = Toplevel(tk)
    dale15.geometry("1280x600+320+240")                                    
    dale15.title("Обои 2из2")                                    
    dale15.resizable(width=False, height=False)
    screen15 = Label(dale15, image=viberit)                           
    screen15.grid(row=0, column=0)
    bl = Button(dale15, image = nazad, command = lambda obj=dale15: exitt333(dale15))
    bl.place(x=550,y=530, width=150, height=75)
    bl = Button(dale15, image = vahod, command = lambda obj=dale15: exitt111(dale15))
    bl.place(x=700,y=530, width=150, height=75)
    bl = Button(dale15, image = anime24, command = anim24)                                  
    bl.place(x=257,y=150, width=256, height=144)
    bl = Button(dale15, image = anime25, command = anim25)                                  
    bl.place(x=0,y=150, width=256, height=144)
    bl = Button(dale15, image = anime26, command = anim26)                                  
    bl.place(x=513,y=150, width=256, height=144)
    bl = Button(dale15, image = anime27, command = anim27)
    bl.place(x=769,y=150, width=256, height=144)
    bl = Button(dale15, image = anime28, command = anim28)                                  
    bl.place(x=1025,y=150, width=256, height=144)
    bl = Button(dale15, image = anime29, command = anim29)                                  
    bl.place(x=1,y=296, width=256, height=144)
    bl = Button(dale15, image = intell, command = intel)                                  
    bl.place(x=257,y=296, width=256, height=144)
    bl = Button(dale15, image = huangg, command = huang)                                  
    bl.place(x=513,y=296, width=256, height=144)
    bl = Button(dale15, image = winpirat, command = winrt)                                  
    bl.place(x=769,y=296, width=256, height=144)
    bl = Button(dale15, image = anime19, command = anim19)                                  
    bl.place(x=1025,y=296, width=256, height=144)
    obj.withdraw()

def exitt111(obj):
    obj.withdraw()
    ussb.deiconify()

def exitt333(obj):
    obj.withdraw()
    nanimeno.deiconify()

def exitt3(obj):
    ussb.deiconify()
    obj.withdraw()
    
def animeoct(obj):
    global oboiaime
    oboiaime = Toplevel(tk)
    oboiaime.geometry("1280x600+320+240")                                    
    oboiaime.title("Обои(1из3)")                                    
    oboiaime.resizable(width=False, height=False)
    screen13 = Label(oboiaime, image=viberit)                           
    screen13.grid(row=0, column=0)
    bl = Button(oboiaime, image = dalee, command = lambda obj=oboiaime: daluu(oboiaime))
    bl.place(x=700,y=530, width=150, height=75)  
    bl = Button(oboiaime, image = vahod, command = exitt)                                  
    bl.place(x=550,y=530, width=150, height=75)            
    bl = Button(oboiaime, image = liza, command = lizaa)                                  
    bl.place(x=257,y=150, width=256, height=144)
    bl = Button(oboiaime, image = anime2, command = anim2)                                  
    bl.place(x=513,y=150, width=256, height=144)
    bl = Button(oboiaime, image = anime3, command = anim3)                                  
    bl.place(x=769,y=150, width=256, height=144)
    bl = Button(oboiaime, image = anime4, command = anim4)                                  
    bl.place(x=1,y=150, width=256, height=144)
    bl = Button(oboiaime, image = winpirat, command = winrt)                                  
    bl.place(x=1025,y=150, width=256, height=144)
    bl = Button(oboiaime, image = anime5, command = anime55)                                  
    bl.place(x=257,y=296, width=256, height=144)
    bl = Button(oboiaime, image = intell, command = intel)                                  
    bl.place(x=513,y=296, width=256, height=144)
    bl = Button(oboiaime, image = anime6, command = anim6)                                  
    bl.place(x=769,y=296, width=256, height=144)
    bl = Button(oboiaime, image = anime7, command = anim7)                                  
    bl.place(x=1,y=296, width=256, height=144)
    bl = Button(oboiaime, image = huangg, command = huang)                                  
    bl.place(x=1025,y=296, width=256, height=144)
    obj.withdraw()
    ussb.withdraw()

def exitt():
    ussb.deiconify()
    oboiaime.withdraw()
    
def daluu(obj):
    global dal
    dal = Toplevel(tk)
    dal.geometry("1280x600+320+240")                                     
    dal.title("Выбор обоев(2из3)")                                    
    dal.resizable(width=False, height=False)
    screen13 = Label(dal, image = vibordal)              
    screen13.grid(row=0, column=0)
    bl = Button(dal, image = nazad, command = lambda obj=dal: backk2(dal))
    bl.place(x=400,y=530, width=150, height=75)
    bl = Button(dal, image = vahod, command = lambda obj=dal: exitt2(dal))
    bl.place(x=550,y=530, width=150, height=75)
    bl = Button(dal, image = dalee, command = lambda obj=dal: epoct1(dal))
    bl.place(x=700,y=530, width=150, height=75)
    bl = Button(dal, image = anime10, command = anim10)                                  
    bl.place(x=257,y=150, width=256, height=144)
    bl = Button(dal, image = anime11, command = anim11)                                  
    bl.place(x=0,y=150, width=256, height=144)
    bl = Button(dal, image = anime12, command = anim12)                                  
    bl.place(x=513,y=150, width=256, height=144)
    bl = Button(dal, image = anime13, command = anim13)
    bl.place(x=769,y=150, width=256, height=144)
    bl = Button(dal, image = anime14, command = anim14)                                  
    bl.place(x=1025,y=150, width=256, height=144)
    bl = Button(dal, image = anime15, command = anim15)                                  
    bl.place(x=1,y=296, width=256, height=144)
    bl = Button(dal, image = anime16, command = anim16)                                  
    bl.place(x=257,y=296, width=256, height=144)
    bl = Button(dal, image = anime17, command = anim17)                                  
    bl.place(x=513,y=296, width=256, height=144)
    bl = Button(dal, image = anime18, command = anim18)                                  
    bl.place(x=769,y=296, width=256, height=144)
    bl = Button(dal, image = anime19, command = anim19)                                  
    bl.place(x=1025,y=296, width=256, height=144)
    oboiaime.withdraw()

def exitt2(obj):
    ussb.deiconify()
    obj.withdraw()

def backk2(obj):
    obj.withdraw()
    oboiaime.deiconify()
    
def epoct1(obj):
    global epoct
    epoct = Toplevel(tk)
    epoct.geometry("1280x600+320+240")                                     
    epoct.title("Обои 3из3")                                    
    epoct.resizable(width=False, height=False)
    screen14 = Label(epoct, image = vibordal)              
    screen14.grid(row=0, column=0)
    bl = Button(epoct, image = vahod, command = lambda obj=epoct: exxxxxit(epoct))
    bl.place(x=550,y=530, width=150, height=75)
    bl = Button(epoct, image = nazad, command = lambda obj=epoct: backk3(epoct))
    bl.place(x=400,y=530, width=150, height=75)
    bl = Button(epoct, image = anime20, command = anim20)                                  
    bl.place(x=1,y=150, width=256, height=144)
    bl = Button(epoct, image = anime21, command = anim21)                                  
    bl.place(x=257,y=150, width=256, height=144)
    bl = Button(epoct, image = anime22, command = anim22)                                  
    bl.place(x=513,y=150, width=256, height=144)
    bl = Button(epoct, image = anime23, command = anim23)                                  
    bl.place(x=769,y=150, width=256, height=144)
    bl = Button(epoct, image = anime24, command = anim24)                                  
    bl.place(x=1025,y=150, width=256, height=144)
    bl = Button(epoct, image = anime25, command = anim25)                                  
    bl.place(x=1,y=296, width=256, height=144)
    bl = Button(epoct, image = anime26, command = anim26)                                  
    bl.place(x=257,y=296, width=256, height=144)
    bl = Button(epoct, image = anime27, command = anim27)                                  
    bl.place(x=513,y=296, width=256, height=144)
    bl = Button(epoct, image = anime28, command = anim28)                                  
    bl.place(x=769,y=296, width=256, height=144)
    bl = Button(epoct, image = anime29, command = anim29)                                  
    bl.place(x=1025,y=296, width=256, height=144)
    obj.withdraw()

def exxxxxit(obj):
    ussb.deiconify()
    obj.withdraw()

def backk3(obj):
    obj.withdraw()
    dal.deiconify()

import ctypes
from pathlib import Path

def anim29():
    img_dir = Path(__file__).parent
    ctypes.windll.user32.SystemParametersInfoW(20, 0, img_dir.joinpath('font/anime29.jpg').as_posix(), 0)

def anim28():
    img_dir = Path(__file__).parent
    ctypes.windll.user32.SystemParametersInfoW(20, 0, img_dir.joinpath('font/anime28.jpg').as_posix(), 0)

def anim27():
    img_dir = Path(__file__).parent
    ctypes.windll.user32.SystemParametersInfoW(20, 0, img_dir.joinpath('font/anime27.jpg').as_posix(), 0)

def anim26():
    img_dir = Path(__file__).parent
    ctypes.windll.user32.SystemParametersInfoW(20, 0, img_dir.joinpath('font/anime26.jpg').as_posix(), 0)

def anim25():
    img_dir = Path(__file__).parent
    ctypes.windll.user32.SystemParametersInfoW(20, 0, img_dir.joinpath('font/anime25.jpg').as_posix(), 0)

def anim24():
    img_dir = Path(__file__).parent
    ctypes.windll.user32.SystemParametersInfoW(20, 0, img_dir.joinpath('font/anime24.jpg').as_posix(), 0)

def anim23():
    img_dir = Path(__file__).parent
    ctypes.windll.user32.SystemParametersInfoW(20, 0, img_dir.joinpath('font/anime23.jpg').as_posix(), 0)

def anim22():
    img_dir = Path(__file__).parent
    ctypes.windll.user32.SystemParametersInfoW(20, 0, img_dir.joinpath('font/anime22.jpg').as_posix(), 0)

def anim21():
    img_dir = Path(__file__).parent
    ctypes.windll.user32.SystemParametersInfoW(20, 0, img_dir.joinpath('font/anime21.jpg').as_posix(), 0)

def anim20():
    img_dir = Path(__file__).parent
    ctypes.windll.user32.SystemParametersInfoW(20, 0, img_dir.joinpath('font/anime20.jpg').as_posix(), 0)

def anim19():
    img_dir = Path(__file__).parent
    ctypes.windll.user32.SystemParametersInfoW(20, 0, img_dir.joinpath('font/anime19.jpg').as_posix(), 0)

def anim18():
    img_dir = Path(__file__).parent
    ctypes.windll.user32.SystemParametersInfoW(20, 0, img_dir.joinpath('font/anime18.jpg').as_posix(), 0)

def anim17():
    img_dir = Path(__file__).parent
    ctypes.windll.user32.SystemParametersInfoW(20, 0, img_dir.joinpath('font/anime17.jpg').as_posix(), 0)

def anim16():
    img_dir = Path(__file__).parent
    ctypes.windll.user32.SystemParametersInfoW(20, 0, img_dir.joinpath('font/anime16.jpg').as_posix(), 0)

def anim15():
    img_dir = Path(__file__).parent
    ctypes.windll.user32.SystemParametersInfoW(20, 0, img_dir.joinpath('font/anime15.jpg').as_posix(), 0)

def anim14():
    img_dir = Path(__file__).parent
    ctypes.windll.user32.SystemParametersInfoW(20, 0, img_dir.joinpath('font/anime14.jpg').as_posix(), 0)

def anim13():
    img_dir = Path(__file__).parent
    ctypes.windll.user32.SystemParametersInfoW(20, 0, img_dir.joinpath('font/anime13.jpg').as_posix(), 0)

def anim12():
    img_dir = Path(__file__).parent
    ctypes.windll.user32.SystemParametersInfoW(20, 0, img_dir.joinpath('font/anime12.jpg').as_posix(), 0)

def anim11():
    img_dir = Path(__file__).parent
    ctypes.windll.user32.SystemParametersInfoW(20, 0, img_dir.joinpath('font/anime11.jpg').as_posix(), 0)

def anim10():
    img_dir = Path(__file__).parent
    ctypes.windll.user32.SystemParametersInfoW(20, 0, img_dir.joinpath('font/anime10.jpg').as_posix(), 0)

def lizaa():
    img_dir = Path(__file__).parent
    ctypes.windll.user32.SystemParametersInfoW(20, 0, img_dir.joinpath('font/amd.jpg').as_posix(), 0)
    
def winrt():
    img_dir = Path(__file__).parent
    ctypes.windll.user32.SystemParametersInfoW(20, 0, img_dir.joinpath('font/win.jpg').as_posix(), 0)

def anim2():
    img_dir = Path(__file__).parent
    ctypes.windll.user32.SystemParametersInfoW(20, 0, img_dir.joinpath('font/anime2.jpg').as_posix(), 0)

def anim3():
    img_dir = Path(__file__).parent
    ctypes.windll.user32.SystemParametersInfoW(20, 0, img_dir.joinpath('font/anime3.jpg').as_posix(), 0)

def anim4():
    img_dir = Path(__file__).parent
    ctypes.windll.user32.SystemParametersInfoW(20, 0, img_dir.joinpath('font/anime4.png').as_posix(), 0)

def anime55():
    img_dir = Path(__file__).parent
    ctypes.windll.user32.SystemParametersInfoW(20, 0, img_dir.joinpath('font/anime5.jpg').as_posix(), 0)

def intel():
    img_dir = Path(__file__).parent
    ctypes.windll.user32.SystemParametersInfoW(20, 0, img_dir.joinpath('font/intel.png').as_posix(), 0)

def anim6():
    img_dir = Path(__file__).parent
    ctypes.windll.user32.SystemParametersInfoW(20, 0, img_dir.joinpath('font/anime6.jpg').as_posix(), 0)

def anim7():
    img_dir = Path(__file__).parent
    ctypes.windll.user32.SystemParametersInfoW(20, 0, img_dir.joinpath('font/anime7.png').as_posix(), 0)

def huang():
    img_dir = Path(__file__).parent
    ctypes.windll.user32.SystemParametersInfoW(20, 0, img_dir.joinpath('font/huang.png').as_posix(), 0)
    
def aktiv():
    global aktivwin
    aktivwin = Toplevel(tk)                                         
    aktivwin.geometry("400x200+760+435")
    aktivwin.title("активация windows")                              
    aktivwin.resizable(width=False, height=False)
    aktivwin.image = PhotoImage(file="image/russianEmage/otklanivirus.png")       
    screen11 = Label(aktivwin, image=aktivwin.image)                 
    screen11.grid(row=0, column=0)                                   
    bl = Button(aktivwin,image = aktivwinbut, command = aktivbut)    
    bl.place(x=75,y=120, width=250, height=60)                       
def aktivbut():
    import os
    os.startfile("DLL_files\\usb\\kms\\kms.exe")
    aktivwin.withdraw()

from tkinter import *                                                            
import webbrowser                                                               
import ctypes
tk = Tk()                                                                       
tk.title("D0LSTEK INSTALLER HELPER")                                            
tk.geometry("1280x900+320+60")                                                          
tk.image = PhotoImage(file="image/russianEmage/режим _установки1.png")           
screen1 = Label(tk, image=tk.image)                                             
screen1.grid(row=0, column=0)                                                   
tk.resizable(width=False, height=False)                                         
sozd = PhotoImage(file="image/russianEmage/sozd.png")                             
bl = Button(tk,image = sozd, command = sozt)                                     
bl.place(x=200,y=848, width=200, height=50)                                      
OPROG = PhotoImage(file="image/russianEmage/o_programe.png")                    
bl = Button(tk,image = OPROG, command = oprog)                                   
bl.place(x=200,y=798, width=200, height=50)                                      
svapLANG = PhotoImage(file="image/russianEmage/key_english.png")                
bl = Button(tk,image = svapLANG)                      
bl.place(x=400,y=798, width=200, height=100)                                                                        
usb = PhotoImage(file="image/russianEmage/ustanovki.png")                                             
bl = Button(tk,image = usb, command = ussb5)                                      
bl.place(x=600,y=500, width=200, height=100)                                    
exit1 = PhotoImage(file="image/russianEmage/exit.png")                           
bl = Button(tk,image = exit1, command = ext1)                                    
bl.place(x=2,y=798, width=200, height=100)                                      
git = PhotoImage(file="image/russianEmage/git.png")                              
bl = Button(tk, image=git, command=lambda: webbrowser.open("https://github.com/d0lstek", new=2, autoraise="True")) 
bl.place(x=600,y=798, width=200, height=100)                                   
Button.pack                                                                     
ruEn = PhotoImage(file="image/EnglishImage/RUEn.png")                                        
exit1En = PhotoImage(file="image/EnglishImage/exitEn.png")                                  
sozdEn = PhotoImage(file="image/EnglishImage/sozdEn.png")                                     
OPROGEn = PhotoImage(file="image/EnglishImage/o_programeEm.png")                              
git1 = PhotoImage(file="image/russianEmage/git.png")                                         
oprog.image = PhotoImage(file="image/EnglishImage/О_программеEn.png")                        
winak = PhotoImage(file="image/russianEmage/aktivwin.png")
cretEn1 = PhotoImage(file="image/russianEmage/avtoreEn.png")
aktivwinbut = PhotoImage(file="image/russianEmage/aktivbutton.png")
activEn = PhotoImage(file="image/EnglishImage/aktbut.png")
oboi = PhotoImage(file="image/russianEmage/oboi.png")
prog = PhotoImage(file="image/russianEmage/prog.png")
razOC = PhotoImage(file="image/russianEmage/razOC.png")
sprosobi = PhotoImage(file="image/russianEmage/oboivibor.png")
animoct = PhotoImage(file="image/russianEmage/animoct.png")
animoobrat = PhotoImage(file="image/russianEmage/ubrataime.png")
liza = PhotoImage(file="image/russianEmage/liza.png")
dalee = PhotoImage(file="image/russianEmage/dalee.png")
winpirat = PhotoImage(file="image/russianEmage/winpirat.png")
vahod = PhotoImage(file="image/russianEmage/vahod.png")
viberit = PhotoImage(file="image/russianEmage/vivirite.png")
anime2 = PhotoImage(file="image/russianEmage/anime2.png") 
anime3 = PhotoImage(file="image/russianEmage/anime3.png")
anime4 = PhotoImage(file="image/russianEmage/anime4.png")
anime5 = PhotoImage(file="image/russianEmage/anime5.png") 
anime6 = PhotoImage(file="image/russianEmage/anime6.png")
anime7 = PhotoImage(file="image/russianEmage/anime7.png")
intell = PhotoImage(file="image/russianEmage/intel.png")
huangg = PhotoImage(file="image/russianEmage/huang.png")
vibordal = PhotoImage(file="image/russianEmage/vivirite.png")
nazad = PhotoImage(file="image/russianEmage/nazad.png")
nazadd2 = PhotoImage(file="image/russianEmage/nazad2.png")
vk = PhotoImage(file="image/russianEmage/vk.png")
razgon = PhotoImage(file="image/russianEmage/razgon.png")
razgIntel =  PhotoImage(file="image/russianEmage/razgIntel.png")
razgAMD =  PhotoImage(file="image/russianEmage/razgAMD.png")
installerss = PhotoImage(file="image/russianEmage/installers.png")
voskl = PhotoImage(file="image/russianEmage/voskl.png")
voskl12 = PhotoImage(file="image/russianEmage/voskl12.png")
anime10 = PhotoImage(file="image/russianEmage/anime10.png")
anime11 = PhotoImage(file="image/russianEmage/anime11.png")
anime12 = PhotoImage(file="image/russianEmage/anime12.png")
anime13 = PhotoImage(file="image/russianEmage/anime13.png")
anime14 = PhotoImage(file="image/russianEmage/anime14.png")
anime15 = PhotoImage(file="image/russianEmage/anime15.png")
anime16 = PhotoImage(file="image/russianEmage/anime16.png")
anime17 = PhotoImage(file="image/russianEmage/anime17.png")
anime18 = PhotoImage(file="image/russianEmage/anime18.png")
anime19 = PhotoImage(file="image/russianEmage/anime19.png")
anime20 =  PhotoImage(file="image/russianEmage/anime20.png")
anime21 =  PhotoImage(file="image/russianEmage/anime21.png")
anime22 =  PhotoImage(file="image/russianEmage/anime22.png")
anime23 =  PhotoImage(file="image/russianEmage/anime23.png")
anime24 =  PhotoImage(file="image/russianEmage/anime24.png")
anime25 =  PhotoImage(file="image/russianEmage/anime25.png")
anime26 =  PhotoImage(file="image/russianEmage/anime26.png")
anime27 =  PhotoImage(file="image/russianEmage/anime27.png")
anime28 =  PhotoImage(file="image/russianEmage/anime28.png")
anime29 =  PhotoImage(file="image/russianEmage/anime29.png")
razAMDlabel =  PhotoImage(file="image/russianEmage/razAMDlabel.png")
ryzenmaster = PhotoImage(file="image/russianEmage/ryzenmaster.png")
aida =  PhotoImage(file="image/russianEmage/aida.png")
occt = PhotoImage(file="image/russianEmage/occt.png")
msiavt  = PhotoImage(file="image/russianEmage/msiavt.png")
gpuz = PhotoImage(file="image/russianEmage/gpuz.png")
fur = PhotoImage(file="image/russianEmage/fur.png")
kak = PhotoImage(file="image/russianEmage/kak.png")
razIntelamg = PhotoImage(file="image/russianEmage/razintel.png")
nazadd2blue = PhotoImage(file="image/russianEmage/nazadd2blue.png")
kakblue = PhotoImage(file="image/russianEmage/kakblue.png")
prodolintel = PhotoImage(file="image/russianEmage/prodolintel.png")
ystovkaintel = PhotoImage(file="image/russianEmage/ystovkaintel.png")
intelmaster11 = PhotoImage(file="image/russianEmage/intelmaster11.png")
onlininstaler = PhotoImage(file="image/russianEmage/onlininstaler.png")
instaler5 = PhotoImage(file="image/russianEmage/instaler5.png")
viborInstaler = PhotoImage(file="image/russianEmage/viborInstaler.png")
chrome = PhotoImage(file="image/russianEmage/chrome.png")
fairfox = PhotoImage(file="image/russianEmage/fairfox.png")
operaGX = PhotoImage(file="image/russianEmage/operaGX.png")
brauzers = PhotoImage(file="image/russianEmage/brauzers.png")
steam = PhotoImage(file="image/russianEmage/steam.png")
epicgames = PhotoImage(file="image/russianEmage/epicgames.png")
origin = PhotoImage(file="image/russianEmage/origin.png")
gameprog = PhotoImage(file="image/russianEmage/game.png")
dredaktor = PhotoImage(file="image/russianEmage/dredaktor.png")
cinema4d = PhotoImage(file="image/russianEmage/cinema4d.png")
blender = PhotoImage(file="image/russianEmage/blender.png")
code3d = PhotoImage(file="image/russianEmage/code3d.png")
pctests = PhotoImage(file="image/russianEmage/pctests.png")
OCCT2 = PhotoImage(file="image/russianEmage/OCCT2.png")
AIDA642 = PhotoImage(file="image/russianEmage/AIDA642.png")
furmark2 = PhotoImage(file="image/russianEmage/furmark2.png")
office = PhotoImage(file="image/russianEmage/office.png")
office2010 = PhotoImage(file="image/russianEmage/office2010.png")
office2013 = PhotoImage(file="image/russianEmage/office2013.png")
office2019 = PhotoImage(file="image/russianEmage/office2019.png")
x86orx64 = PhotoImage(file="image/russianEmage/x86orx64.png")
x86 = PhotoImage(file="image/russianEmage/x86.png")
x64 = PhotoImage(file="image/russianEmage/x64.png")
sssvopros = PhotoImage(file="image/russianEmage/sssvopros.png")
arhivators = PhotoImage(file="image/russianEmage/arhivators.png")
winrars = PhotoImage(file="image/russianEmage/winrars.png")
zip7 = PhotoImage(file="image/russianEmage/zip7.png")
goloschat = PhotoImage(file="image/russianEmage/goloschat.png")
discord = PhotoImage(file="image/russianEmage/discord.png")
teamsleak = PhotoImage(file="image/russianEmage/teamsleak.png")
videoredactors = PhotoImage(file="image/russianEmage/videoredactors.png")
vegas = PhotoImage(file="image/russianEmage/vegas.png")
premerpro = PhotoImage(file="image/russianEmage/premerpro.png")
vegasss = PhotoImage(file="image/russianEmage/vegasss.png")
vegas13 = PhotoImage(file="image/russianEmage/vegas13.png")
vegas15 = PhotoImage(file="image/russianEmage/vegas15.png")
scopiravat = PhotoImage(file="image/russianEmage/scopiravat.png")
ystanovka = PhotoImage(file="image/russianEmage/ystanovka.png")
photoedits = PhotoImage(file="image/russianEmage/photoedits.png")
photoshop1 = PhotoImage(file="image/russianEmage/photoshop1.png")
photoshop2 = PhotoImage(file="image/russianEmage/photoshop2.png")
ustanovki = PhotoImage(file="image/russianEmage/ustanovki.png")
textredacross = PhotoImage(file="image/russianEmage/textredacross.png")
keyslagCinema = PhotoImage(file="image/russianEmage/keyslagCinema.png")
notepad = PhotoImage(file="image/russianEmage/notepad+.png")
paychart = PhotoImage(file="image/russianEmage/paychart.png")
s1of3 = PhotoImage(file="image/russianEmage/s1of3.png")
s2of3 = PhotoImage(file="image/russianEmage/s2of3.png")
s3of3 = PhotoImage(file="image/russianEmage/s3of3.png")
raznastprogram = PhotoImage(file="image/russianEmage/raznastprogram.png")
tk.mainloop()                                                                   





