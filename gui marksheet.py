from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageFont
import math
import tkinter as tk
import tkinter.messagebox


master = tk.Tk() 

master.title("MARKSHEET") 

master.geometry("700x400")


e1 = tk.Entry(master) 
e2 = tk.Entry(master) 
e3 = tk.Entry(master) 
e4 = tk.Entry(master) 
e5 = tk.Entry(master) 
e6 = tk.Entry(master) 
e7 = tk.Entry(master)
e8 = tk.Entry(master)
e9 = tk.Entry(master)
e10 = tk.Entry(master) 
e11 = tk.Entry(master) 
e12 = tk.Entry(master) 
e13 = tk.Entry(master)


def display(self,root): 
	

	tot=0
	
	if e4.get() == "O": 
		
		# grid method is used for placing 
		# the widgets at respective positions 
		# in table like structure . 
		tk.Label(master, text ="50").grid(row=4, column=4) 
		tot += 50
		

	if e4.get() == "A": 
		tk.Label(master, text ="45").grid(row=4, column=4) 
		tot += 45
		

	if e4.get() == "B": 
		tk.Label(master, text ="40").grid(row=4, column=4) 
		tot += 40
		
	 
	if e4.get() == "C": 
		tk.Label(master, text ="35").grid(row=4, column=4) 
		tot += 35
		
	 
	if e4.get() == "D": 
		tk.Label(master, text ="30").grid(row=4, column=4) 
		tot += 30
		
	 
	if e4.get() == "E": 
		tk.Label(master, text ="25").grid(row=4, column=4) 
		tot += 25

	 
	if e4.get() == "P": 
		tk.Label(master, text ="20").grid(row=4, column=4) 
		tot += 20

	 
	if e4.get() == "F": 
		tk.Label(master, text ="0").grid(row=4, column=4) 
		tot += 0



	if e5.get() == "O": 
		
		# grid method is used for placing 
		# the widgets at respective positions 
		# in table like structure . 
		tk.Label(master, text ="40").grid(row=5, column=4) 
		tot += 40
		
 
	if e5.get() == "A": 
		tk.Label(master, text ="36").grid(row=5, column=4) 
		tot += 36
		
 
	if e5.get() == "B": 
		tk.Label(master, text ="32").grid(row=5, column=4) 
		tot += 32
		
	 
	if e5.get() == "C": 
		tk.Label(master, text ="28").grid(row=5, column=4) 
		tot += 28
		
	 
	if e5.get() == "D": 
		tk.Label(master, text ="24").grid(row=5, column=4) 
		tot += 24
		
	 
	if e5.get() == "E": 
		tk.Label(master, text ="20").grid(row=5, column=4) 
		tot += 20
	 
	if e5.get() == "P": 
		tk.Label(master, text ="16").grid(row=5, column=4) 
		tot += 16

	# 0*number of subject credits give 
	# total credits for grade F	 
	if e5.get() == "F": 
		tk.Label(master, text ="0").grid(row=5, column=4) 
		tot += 0

 
	if e6.get() == "O": 
		
		# grid method is used for placing 
		# the widgets at respective positions 
		# in table like structure . 
		tk.Label(master, text ="40").grid(row=6, column=4) 
		tot += 40
		
 
	if e6.get() == "A": 
		tk.Label(master, text ="36").grid(row=6, column=4) 
		tot += 36
		
 
	if e6.get() == "B": 
		tk.Label(master, text ="32").grid(row=6, column=4) 
		tot += 32
		
	 
	if e6.get() == "C": 
		tk.Label(master, text ="28").grid(row=6, column=4) 
		tot += 28
		
	 
	if e6.get() == "D": 
		tk.Label(master, text ="24").grid(row=6, column=4) 
		tot += 24
		
	 
	if e6.get() == "E": 
		tk.Label(master, text ="20").grid(row=6, column=4) 
		tot += 20

	 
	if e6.get() == "P": 
		tk.Label(master, text ="16").grid(row=6, column=4) 
		tot += 16

	 
	if e6.get() == "F": 
		tk.Label(master, text ="0").grid(row=6, column=4) 
		tot += 0


	if e7.get() == "O": 
		
		# grid method is used for placing 
		# the widgets at respective positions 
		# in table like structure . 
		tk.Label(master, text ="40").grid(row=7, column=4) 
		tot += 40
		
 
	if e7.get() == "A": 
		tk.Label(master, text ="36").grid(row=7, column=4) 
		tot += 36
		
 
	if e7.get() == "B": 
		tk.Label(master, text ="32").grid(row=7, column=4) 
		tot += 32
		
	 
	if e7.get() == "C": 
		tk.Label(master, text ="28").grid(row=7, column=4) 
		tot += 28
		
	 
	if e7.get() == "D": 
		tk.Label(master, text ="24").grid(row=7, column=4) 
		tot += 24
		
	 
	if e7.get() == "E": 
		tk.Label(master, text ="20").grid(row=7, column=4) 
		tot += 20

	 
	if e7.get() == "P": 
		tk.Label(master, text ="16").grid(row=7, column=4) 
		tot += 16

	 
	if e7.get() == "F": 
		tk.Label(master, text ="0").grid(row=7, column=4) 
		tot += 0

 
	if e8.get() == "O": 
		
		# grid method is used for placing 
		# the widgets at respective positions 
		# in table like structure . 
		tk.Label(master, text ="40").grid(row=8, column=4) 
		tot += 40
		
 
	if e8.get() == "A": 
		tk.Label(master, text ="36").grid(row=8, column=4) 
		tot += 36
		
 
	if e8.get() == "B": 
		tk.Label(master, text ="32").grid(row=8, column=4) 
		tot += 32
		
	 
	if e8.get() == "C": 
		tk.Label(master, text ="28").grid(row=8, column=4) 
		tot += 28
		
	 
	if e8.get() == "D": 
		tk.Label(master, text ="24").grid(row=8, column=4) 
		tot += 24
		
	 
	if e8.get() == "E": 
		tk.Label(master, text ="20").grid(row=8, column=4) 
		tot += 20

	 
	if e8.get() == "P": 
		tk.Label(master, text ="16").grid(row=8, column=4) 
		tot += 16
	 
	if e8.get() == "F": 
		tk.Label(master, text ="0").grid(row=8, column=4) 
		tot += 0


 
	if e9.get() == "O": 
		
		# grid method is used for placing 
		# the widgets at respective positions 
		# in table like structure . 
		tk.Label(master, text ="10").grid(row=9, column=4) 
		tot += 10
		

	if e9.get() == "A": 
		tk.Label(master, text ="9").grid(row=9, column=4) 
		tot += 9
		
 
	if e9.get() == "B": 
		tk.Label(master, text ="8").grid(row=9, column=4) 
		tot += 8
		
	 
	if e9.get() == "C": 
		tk.Label(master, text ="7").grid(row=9, column=4) 
		tot += 7
		
	 
	if e9.get() == "D": 
		tk.Label(master, text ="6").grid(row=9, column=4) 
		tot += 6
		
	 
	if e9.get() == "E": 
		tk.Label(master, text ="5").grid(row=9, column=4) 
		tot += 5
	 
	if e9.get() == "P": 
		tk.Label(master, text ="4").grid(row=9, column=4) 
		tot += 4
	 
	if e9.get() == "F": 
		tk.Label(master, text ="0").grid(row=9, column=4) 
		tot += 0



	if e10.get() == "O": 
		
		# grid method is used for placing 
		# the widgets at respective positions 
		# in table like structure . 
		tk.Label(master, text ="10").grid(row=10, column=4) 
		tot += 10
		
 
	if e10.get() == "A": 
		tk.Label(master, text ="9").grid(row=10, column=4) 
		tot += 9
		
 
	if e10.get() == "B": 
		tk.Label(master, text ="8").grid(row=10, column=4) 
		tot += 8
		
	 
	if e10.get() == "C": 
		tk.Label(master, text ="7").grid(row=10, column=4) 
		tot += 7
		
	 
	if e10.get() == "D": 
		tk.Label(master, text ="6").grid(row=10, column=4) 
		tot += 6
		
	 
	if e10.get() == "E": 
		tk.Label(master, text ="5").grid(row=10, column=4) 
		tot += 5

	 
	if e10.get() == "P": 
		tk.Label(master, text ="4").grid(row=10, column=4) 
		tot += 4

	 
	if e10.get() == "F": 
		tk.Label(master, text ="0").grid(row=10, column=4) 
		tot += 0



	if e11.get() == "O": 
		
		# grid method is used for placing 
		# the widgets at respective positions 
		# in table like structure . 
		tk.Label(master, text ="10").grid(row=11, column=4) 
		tot += 10
		

	if e11.get() == "A": 
		tk.Label(master, text ="9").grid(row=11, column=4) 
		tot += 9
		
 
	if e11.get() == "B": 
		tk.Label(master, text ="8").grid(row=11, column=4) 
		tot += 8
		
	 
	if e11.get() == "C": 
		tk.Label(master, text ="7").grid(row=11, column=4) 
		tot += 7
		
	 
	if e11.get() == "D": 
		tk.Label(master, text ="6").grid(row=11, column=4) 
		tot += 6
		
	 
	if e11.get() == "E": 
		tk.Label(master, text ="5").grid(row=11, column=4) 
		tot += 5

	 
	if e11.get() == "P": 
		tk.Label(master, text ="4").grid(row=11, column=4) 
		tot += 4
	 
	if e11.get() == "F": 
		tk.Label(master, text ="0").grid(row=11, column=4) 
		tot += 0

 
	if e12.get() == "O": 
		
		# grid method is used for placing 
		# the widgets at respective positions 
		# in table like structure . 
		tk.Label(master, text ="10").grid(row=12, column=4) 
		tot += 10
		
 
	if e12.get() == "A": 
		tk.Label(master, text ="9").grid(row=12, column=4) 
		tot += 9
		
 
	if e12.get() == "B": 
		tk.Label(master, text ="8").grid(row=12, column=4) 
		tot += 8
		
	 
	if e12.get() == "C": 
		tk.Label(master, text ="7").grid(row=12, column=4) 
		tot += 7
		
	 
	if e12.get() == "D": 
		tk.Label(master, text ="6").grid(row=12, column=4) 
		tot += 6
		
	 
	if e12.get() == "E": 
		tk.Label(master, text ="5").grid(row=12, column=4) 
		tot += 5

	 
	if e12.get() == "P": 
		tk.Label(master, text ="4").grid(row=12, column=4) 
		tot += 4

	 
	if e12.get() == "F": 
		tk.Label(master, text ="0").grid(row=12, column=4) 
		tot += 0



	if e13.get() == "O": 
		
		# grid method is used for placing 
		# the widgets at respective positions 
		# in table like structure . 
		tk.Label(master, text ="20").grid(row=13, column=4) 
		tot += 20
		
 
	if e13.get() == "A": 
		tk.Label(master, text ="18").grid(row=13, column=4) 
		tot += 18
		
 
	if e13.get() == "B": 
		tk.Label(master, text ="16").grid(row=13, column=4) 
		tot += 16
		
	 
	if e13.get() == "C": 
		tk.Label(master, text ="14").grid(row=13, column=4) 
		tot += 14
		
	 
	if e13.get() == "D": 
		tk.Label(master, text ="12").grid(row=13, column=4) 
		tot += 12
		
	 
	if e13.get() == "E": 
		tk.Label(master, text ="10").grid(row=13, column=4) 
		tot += 10

	 
	if e13.get() == "P": 
		tk.Label(master, text ="8").grid(row=13, column=4) 
		tot += 8

	 
	if e13.get() == "F": 
		tk.Label(master, text ="0").grid(row=13, column=4)
		tot += 0

#1
	if e4.get() == "F": 
		tk.Label(master, text ="Unsucessfull").grid(row=17, column=4)
	elif e5.get() == "F": 
		tk.Label(master, text ="Unsucessfull").grid(row=17, column=4)
	elif e6.get() == "F": 
		tk.Label(master, text ="Unsucessfull").grid(row=17, column=4)
	elif e7.get() == "F": 
		tk.Label(master, text ="Unsucessfull").grid(row=17, column=4)
	elif e8.get() == "F": 
		tk.Label(master, text ="Unsucessfull").grid(row=17, column=4)
	elif e9.get() == "F": 
		tk.Label(master, text ="Unsucessfull").grid(row=17, column=4)
	elif e10.get() == "F": 
		tk.Label(master, text ="Unsucessfull").grid(row=17, column=4)
	elif e11.get() == "F": 
		tk.Label(master, text ="Unsucessfull").grid(row=17, column=4)
	elif e12.get() == "F": 
		tk.Label(master, text ="Unsucessfull").grid(row=17, column=4)
	elif e13.get() == "F": 
		tk.Label(master, text ="Unsucessfull").grid(row=17, column=4)
	else: 
		tk.Label(master, text ="sucessfull").grid(row=17, column=4)



 
	tk.Label(master, text=str(tot)).grid(row=14, column=4) 
	

	tk.Label(master, text=str(tot/27)).grid(row=15, column=4)

	tk.Label(master, text=float((tot/27)*10)-7.5).grid(row=16, column=4)



 
tk.Label(master, text="Name").grid(row=1, column=0) 

 
tk.Label(master, text="COMPUTER BRANCH").grid(row=0, column=3) 

 
tk.Label(master, text="SEAT.No").grid(row=1, column=4) 

 
tk.Label(master, text="Srl.No").grid(row=3, column=0) 
tk.Label(master, text="1").grid(row=4, column=0) 
tk.Label(master, text="2").grid(row=5, column=0) 
tk.Label(master, text="3").grid(row=6, column=0) 
tk.Label(master, text="4").grid(row=7, column=0)
tk.Label(master, text="5").grid(row=8, column=0)
tk.Label(master, text="6").grid(row=9, column=0)
tk.Label(master, text="7").grid(row=10, column=0)
tk.Label(master, text="8").grid(row=11, column=0)
tk.Label(master, text="9").grid(row=12, column=0)
tk.Label(master, text="10").grid(row=13, column=0) 


 
tk.Label(master, text="Subject").grid(row=3, column=1) 
tk.Label(master, text="CS201").grid(row=4, column=1) 
tk.Label(master, text="CS202").grid(row=5, column=1) 
tk.Label(master, text="CS203").grid(row=6, column=1) 
tk.Label(master, text="CS204").grid(row=7, column=1)
tk.Label(master, text="CS205").grid(row=8, column=1)
tk.Label(master, text="CSL201").grid(row=9, column=1)
tk.Label(master, text="CSL202").grid(row=10, column=1)
tk.Label(master, text="CSL203").grid(row=11, column=1)
tk.Label(master, text="CSL204").grid(row=12, column=1)
tk.Label(master, text="CSL205").grid(row=13, column=1) 

	
 
tk.Label(master, text="Credit").grid(row=3, column=2) 
e4.grid(row=4, column=3) 
e5.grid(row=5, column=3) 
e6.grid(row=6, column=3) 
e7.grid(row=7, column=3)
e8.grid(row=8, column=3)
e9.grid(row=9, column=3)
e10.grid(row=10, column=3)
e11.grid(row=11, column=3)
e12.grid(row=12, column=3)
e13.grid(row=13, column=3) 

 
tk.Label(master, text="Overall Grade").grid(row=3, column=3) 
tk.Label(master, text="5").grid(row=4, column=2) 
tk.Label(master, text="4").grid(row=5, column=2) 
tk.Label(master, text="4").grid(row=6, column=2) 
tk.Label(master, text="4").grid(row=7, column=2)
tk.Label(master, text="4").grid(row=8, column=2)
tk.Label(master, text="1").grid(row=9, column=2)
tk.Label(master, text="1").grid(row=10, column=2)
tk.Label(master, text="1").grid(row=11, column=2)
tk.Label(master, text="1").grid(row=12, column=2)
tk.Label(master, text="2").grid(row=13, column=2) 

tk.Label(master, text="Credit obtained cxg").grid(row=3, column=4) 
tk.Label(master, text="").grid(row=2, column=4) 

 
e1=tk.Entry(master) 
e2=tk.Entry(master) 
e3=tk.Entry(master) 


e1.grid(row=1, column=1) 

e3.grid(row=1, column=5) 

 
button1=tk.Button(master, text="submit", bg="blue", command=display) 
button1.grid(row=15, column=1) 



tk.Label(master, text="Total credit").grid(row=14, column=3) 
tk.Label(master, text="SGPI").grid(row=15, column=3)
tk.Label(master, text="percentage").grid(row=16, column=3)
tk.Label(master, text="Remark").grid(row=17, column=3)


        

button2=tk.Button(master, text="Exit", bg="red", command=master.destroy) 
button2.grid(row=16, column=1)
        



master.mainloop() 

