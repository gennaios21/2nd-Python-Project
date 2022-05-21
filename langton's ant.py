#############################################
#                                           #
#     Ατομική Εργασία  "Langton's Ant"      #
#                                           #
#############################################

from turtle import*
from tkinter import *
from tkinter import messagebox

#---------------------MAIN--------------------------------------------------------------

def main():
  main=Tk()                                                                                                                                                             
  main.title('Langton')                       
  main.configure(bg='white')

  text=Label(main,text="Εισάγετε το μέγεθος\nτων τετραγώνων:")
  text.pack(expand=1, fill="both")
  
  frame=Frame(main)
  frame.pack()

  a = IntVar()
  entry=Entry(frame,textvariable=a,width=35)
  entry.pack(side=LEFT)
  
  def Get():
    b=float(entry.get())
  
    if 0.25<=b<=5 and b!=0:
      f=open('size.txt','w')
      f.write(str(b))
      f.close
      v.set('Έναρξη Langton\'s Ant\n(με το νέο μέγεθος τετραγώνου)')
    else:
      a=messagebox.showinfo('Προσοχή!','Το επιτρεπόμενο μέγεθος τετραγώνων\nείναι μεταξύ 0.25 και 5')
    
  get=Button(frame,text="OK",bg="light sky blue",command=Get)
  get.pack(side=RIGHT)

  def Start():
    v.set('Έναρξη Langton\'s Ant\n(με το προηγούμενο μέγεθος τετραγώνου)')
    main.destroy()
    ant()
  
  v=StringVar()
  v.set('Έναρξη Langton\'s Ant\n(με το προηγούμενο μέγεθος τετραγώνου)')
  start=Button(main,bg='light green',textvariable=v,command=Start)
  start.pack(expand=1, fill="both")
  
  cancel=Button(main,bg='light coral',text='Άκυρο',command=main.destroy)
  cancel.pack(expand=1, fill="both")

  main.mainloop()

#---------------------ΚΙΝΗΣΗ-ΚΑΝΟΝΕΣ------------------------------------------------  
  
def ant():
  size=[]
  for line in open('size.txt','r'):
    size.append(line)
  a=size[0]
  
  main2=Screen() 
  main2.bgcolor('light grey') 
  main2.screensize(1000,1000)
  space={}
  ant=Turtle()
  ant.shape('square')
  ant.shapesize(float(a))
  ant.speed(1000)
  position=(round(ant.xcor()),round(ant.ycor()))

  while True:
    step=20*float(a)
    
    if position not in space or space[position]=="white": 
      ant.fillcolor("black")
      ant.stamp()
      position=(round(ant.xcor()),round(ant.ycor()))
      space[position]="black"
      ant.right(90)
      ant.forward(step)                          
      position = (round(ant.xcor()),round(ant.ycor()))
    elif space[position]=="black": 
      ant.fillcolor("white")
      ant.stamp()
      position=(round(ant.xcor()),round(ant.ycor()))
      space[position]="white"
      ant.left(90)
      ant.forward(step) 
      position = (round(ant.xcor()),round(ant.ycor()))
   

#---------------------ΚΑΛΩ ΤΗΝ MAIN--------------------------------------------
main()




  
