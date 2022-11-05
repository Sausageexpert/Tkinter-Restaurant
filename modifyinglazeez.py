from msilib.schema import CheckBox
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

# Main Screen Setup


root  = tk.Tk()
root.geometry('1500x650+0+0') # Length by width, x position + y position
root.resizable(False, False) # X direction and y direction (0,1 works too)
root.title('The Incredible Spice: Invoicing System')

img=(Image.open('C:\\Users\\soham\\Desktop\\Tkinter\\background.jpg'))
resized=img.resize((1500, 650))
newimg=ImageTk.PhotoImage(resized)
#root.config(image=img)
root.config(bg='#3a5311')

# Background

label = Label(root, image=newimg)
label.place(x=0, y=0)

# Top Panel

topPanel = Frame(root, bd=1, relief=RAISED) # Container to organise widgets, relief can be raised, sunken, groove, ridge, flat
topPanel.pack(side=TOP)
top_title = Label(topPanel, text='The Incredible Spice', fg='#ffd700', font=('Dosis', 58), bg='#234f1e', width=25) # fg = foreground
top_title.grid(row=0, column=0)


# Left Panel (with food, drinks, dessert and cost)

leftPanel = Frame(root, bd=1, relief=RAISED)
leftPanel.pack(side=LEFT)

# Cost Panel

costPanel = Frame(leftPanel, bd=1, relief=RAISED, bg='black', padx=50)
costPanel.pack(side=BOTTOM)

# Food Panel

foodPanel = LabelFrame(leftPanel, bd=1, relief=FLAT, text='Food', fg='#2e1503', font=('Dosis', 22, 'bold', 'underline'), bg='#74b72e')
foodPanel.pack(side=LEFT)

# Drink Panel

drinkPanel = LabelFrame(leftPanel, bd=1, relief=FLAT, text='Drinks', fg='#2e1503', font=('Dosis', 22, 'bold', 'underline'), padx=10, bg='#74b72e')
drinkPanel.pack(side=LEFT)

# Dessert Panel

dessertPanel = LabelFrame(leftPanel, bd=1, relief=FLAT, text='Dessert', fg='#2e1503', font=('Dosis', 22, 'bold', 'underline'), padx=10, bg='#74b72e')
dessertPanel.pack(side=LEFT)

# Right Panel

rightPanel = Frame(root, bd=1, relief=RAISED, bg='burlywood')
rightPanel.pack(side=RIGHT)

# Calculator

calculator = Frame(rightPanel, bd=1, relief=FLAT, bg='white')
calculator.pack() # Top by default

# Invoice Panel

invoicePanel = Frame(rightPanel, bd=1, relief=FLAT, bg='burlywood')
invoicePanel.pack()

# Buttons 

buttonPanel = Frame(rightPanel, bd=1, relief=FLAT, bg='burlywood')
buttonPanel.pack() # Specify only from left to right

# Back-End Stuff

foods = ['Lazeez Biriyani', 'Paneer Roll', 'Fried Lettuce', 'Boiled Ice Cream', 'Khuska', 'Kebabs', 'Fried Rice', 'Cinnamon Toast']
drinks = ['Juice', 'Lemonade', 'Soda', 'Ginger ale', 'Coke', 'Liquid Cake', 'Milkshake', 'Water']
desserts = ['Dragonfruit Curd', 'Paneer Milk', 'Sugared Almonds', 'Cheesecake', 'Brownies', 'Pudding', 'Candyfloss', 'Pie']

# Check boxes

# Creating food items

counter=0
food_variables=[]
foodBox=[]
foodText=[]

for food in foods:
    food_variables.append('')
    food_variables[counter]=IntVar() # Creates an integer variable (type-casting)
    food=Checkbutton(foodPanel, text=food.title(), font=('Dosis', 19, 'bold'), onvalue=1, offvalue=0, variable=food_variables[counter], bg='#74b72e') # Every element becomes a check button; when checked, check's value is 1 else 0    # Creates a variable (checkbox) for every item                                                                                                                                 
    food.grid(row=counter, column=0, sticky=W) # West
    # Creating input boxes (no. of items), food box is a list which stores the food input boxes, food text stores the text in those boxes
    foodBox.append('')
    foodText.append('')
    foodText[counter]=StringVar()
    foodText[counter].set('0') # When using the value, use an integer, when entering, use a string
    foodBox[counter]=Entry(foodPanel, bd=1, font=('Dosis', 19, 'bold'), width=6, state=DISABLED, textvariable=foodText[counter]) # Until checking the checkbox, the input is disabled
    foodBox[counter].grid(row=counter, column=1)
    counter+=1

# Creating drink items

counter=0
drink_variables=[]
drinkBox=[]
drinkText=[]

for drink in drinks:
    drink_variables.append('')
    drink_variables[counter]=IntVar() # Creates an integer variable (type-casting)
    drinkvar = IntVar()
    drink=Checkbutton(drinkPanel, text=drink.title(), font=('Dosis', 19, 'bold'), onvalue=1, offvalue=0, variable=drinkvar, bg='#74b72e') # Every element becomes a check button; when checked, check's value is 1 else 0
                                                                                                                                        # Creates a variable (checkbox) for every item                                                                                                                                   
    drink.grid(row=counter, column=0, sticky=W) # West
    # Creating input boxes (no. of items), food box is a list which stores the food input boxes, food text stores the text in those boxes
    drinkBox.append('')
    drinkText.append('')
    drinkText[counter]=StringVar()
    drinkText[counter].set('0')
    drinkBox[counter]=Entry(drinkPanel, bd=1, font=('Dosis', 19, 'bold'), width=6, state=DISABLED, textvariable=drinkText[counter]) # Until checking the checkbox, the input is disabled
    drinkBox[counter].grid(row=counter, column=1)
    if int(drinkvar.get())==1:
        drinkBox[counter].config(state=NORMAL)
    else:
        drinkBox[counter].config(state=DISABLED)
    counter+=1
    
# Creating dessert items

counter=0
dessert_variables=[]
dessertBox=[]
dessertText=[]

for dessert in desserts:
    dessert_variables.append('placeholder') # All the placeholders are going to be changed later, these are checkboxes
    dessert_variables[counter]=IntVar() # Creates an integer variable (type-casting)
    dessert=Checkbutton(dessertPanel, text=dessert.title(), font=('Dosis', 19, 'bold'), onvalue=1, offvalue=0, variable=dessert_variables[counter], bg='#74b72e') # Every element becomes a check button; when checked, check's value is 1 else 0
                                                                                                                                        # Creates a variable (checkbox) for every item                                                                                                                                   
    dessert.grid(row=counter, column=0, sticky=W) # West
    # Creating input boxes (no. of items), food box is a list which stores the food input boxes, food text stores the text in those boxes
    dessertBox.append('')
    dessertText.append('')
    dessertText[counter]=StringVar()
    dessertText[counter].set('0')
    dessertBox[counter]=Entry(dessertPanel, bd=1, font=('Dosis', 19, 'bold'), width=6, state=DISABLED, textvariable=dessertText[counter]) # Until checking the checkbox, the input is disabled
    dessertBox[counter].grid(row=counter, column=1)
    counter+=1
    
food_cost_var=StringVar()
food_cost_label = Label(costPanel, text='Food Costs', font=('Dosis', 12, 'bold'), bg='black', fg='#ffd700')
food_cost_label.grid(row=0, column=0)
food_cost_text = Entry(costPanel, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly', textvariable=food_cost_var)
food_cost_text.grid(row=0, column=1, padx=60)

drink_cost_var=StringVar()
drink_cost_label = Label(costPanel, text='Drink Costs', font=('Dosis', 12, 'bold'), fg='#ffd700', bg='black')
drink_cost_label.grid(row=1, column=0)
drink_cost_text=Entry(costPanel, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly', textvariable=drink_cost_var)
drink_cost_text.grid(row=1, column=1)

dessert_cost_var=StringVar()
dessert_cost_label = Label(costPanel, text='Dessert Costs', font=('Dosis', 12, 'bold'), fg='#ffd700', bg='black')
dessert_cost_label.grid(row=2, column=0)
dessert_cost_text=Entry(costPanel, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly', textvariable=dessert_cost_var)
dessert_cost_text.grid(row=2, column=1)

subtotal_cost_label = Label(costPanel, text='Subtotal', font=('Dosis', 12, 'bold'), fg='#ffd700', bg='black')
subtotal_cost_label.grid(row=0, column=2, padx=60)
subtotal_cost_text=Entry(costPanel, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly')
subtotal_cost_text.grid(row=0, column=3)

taxes_cost_label = Label(costPanel, text='Taxes', font=('Dosis', 12, 'bold'), fg='#ffd700', bg='black')
taxes_cost_label.grid(row=1, column=2)
taxes_cost_text=Entry(costPanel, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly')
taxes_cost_text.grid(row=1, column=3)

total_cost_label = Label(costPanel, text='Total', font=('Dosis', 12, 'bold'), fg='#ffd700', bg='black')
total_cost_label.grid(row=2, column=2)
total_cost_text=Entry(costPanel, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly')
total_cost_text.grid(row=2, column=3)

buttonsList = ['Total', 'Invoice', 'Save', 'Clear']
for button in range(len(buttonsList)):
    createButton=Button(buttonPanel, text=buttonsList[button], relief=RAISED, font=('Dosis', 19, 'bold'), fg='white', bg='azure4', bd=1, width=9)
    createButton.grid(row=0, column=button)

root.mainloop()


