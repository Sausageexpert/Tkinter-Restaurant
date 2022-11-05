

from msilib.schema import CheckBox
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

# Main Screen Setup

root = tk.Tk()
root.geometry('1550x700+0+0')  # Length by width, x position + y position
root.resizable(False, False)  # X direction and y direction (0,1 works too)
root.title('The Incredible Spice: Invoicing System')

img = (
  Image.open('C:\\Users\\soham\\Desktop\\Tkinter\\background.jpg'))
resized = img.resize((1500, 650))
newimg = ImageTk.PhotoImage(resized)
#root.config(image=img)
root.config(bg='#3a5311')

# Background

label = Label(root, image=newimg)
label.place(x=0, y=0)

# Top Panel

topPanel = Frame(
  root, bd=1, relief=RAISED
)  # Container to organise widgets, relief can be raised, sunken, groove, ridge, flat
topPanel.pack(side=TOP)
top_title = Label(topPanel,
                  text='The Incredible Spice',
                  fg='#ffd700',
                  font=('Dosis', 58),
                  bg='#234f1e',
                  width=25)  # fg = foreground
top_title.grid(row=0, column=0)

# Left Panel (with food, drinks, dessert and cost)

leftPanel = Frame(root, bd=1, relief=RAISED)
leftPanel.pack(side=LEFT)

# Cost Panel

costPanel = Frame(leftPanel, bd=1, relief=RAISED, bg='black', padx=50)
costPanel.pack(side=BOTTOM)

# Food Panel

foodPanel = LabelFrame(leftPanel,
                       bd=1,
                       relief=FLAT,
                       text='Food',
                       fg='#2e1503',
                       font=('Dosis', 22, 'bold', 'underline'),
                       bg='#74b72e')
foodPanel.pack(side=LEFT)

# Drink Panel

drinkPanel = LabelFrame(leftPanel,
                        bd=1,
                        relief=FLAT,
                        text='Drinks',
                        fg='#2e1503',
                        font=('Dosis', 22, 'bold', 'underline'),
                        padx=10,
                        bg='#74b72e')
drinkPanel.pack(side=LEFT)

# Dessert Panel

dessertPanel = LabelFrame(leftPanel,
                          bd=1,
                          relief=FLAT,
                          text='Dessert',
                          fg='#2e1503',
                          font=('Dosis', 22, 'bold', 'underline'),
                          padx=10,
                          bg='#74b72e')
dessertPanel.pack(side=LEFT)

# Right Panel

rightPanel = Frame(root, bd=1, relief=RAISED, bg='burlywood')
rightPanel.pack(side=RIGHT)

# Calculator

calculator = Frame(rightPanel, bd=1, relief=FLAT, bg='white')
calculator.pack()  # Top by default

# Invoice Panel

invoicePanel = Frame(rightPanel, bd=1, relief=FLAT, bg='burlywood')
invoicePanel.pack()

# Buttons

buttonPanel = Frame(rightPanel, bd=1, relief=FLAT, bg='burlywood')
buttonPanel.pack()  # Specify only from left to right

# Back-End Stuff

foods = [
  'Lazeez Biriyani', 'Paneer Roll', 'Fried Lettuce', 'Boiled Ice Cream',
  'Khuska', 'Kebabs', 'Fried Rice', 'Cinnamon Toast'
]
foodCosts = [100, 200, 100, 200, 100, 200, 100, 200]
drinks = [
  'Juice', 'Lemonade', 'Soda', 'Ginger ale', 'Coke', 'Liquid Cake',
  'Milkshake', 'Water'
]
drinkCosts = [100, 200, 100, 200, 100, 200, 100, 200]
desserts = [
  'Dragonfruit Curd', 'Paneer Milk', 'Sugared Almonds', 'Cheesecake',
  'Brownies', 'Pudding', 'Candyfloss', 'Pie'
]
dessertCosts = [100, 200, 100, 200, 100, 200, 100, 200]

food_cost_var = StringVar()
drink_cost_var = StringVar()
dessert_cost_var = StringVar()
subtotal_cost_var = StringVar()
taxes_var = StringVar()
total_var = StringVar()

# Check boxes

# Creating food items

counter = 0
food_variables = []
foodBox = []
foodText = []


def checkFoodClicked():
  for i in range(len(food_variables)):
    if food_variables[i].get() == 1:
      foodBox[i].config(state=NORMAL)
    else:
      foodBox[i].config(state=DISABLED)

def addEverything():
    foodCost=0
    drinkCost=0
    dessertCost=0
    for i in range(len(foodText)):
        foodCost+=int(foodText[i].get())*foodCosts[i]
    for j in range(len(drinkText)):
        drinkCost+=int(drinkText[j].get())*foodCosts[j]
    for k in range(len(dessertText)):
        dessertCost+=int(dessertText[k].get())*foodCosts[k]
    food_cost_var.set(str(foodCost))
    drink_cost_var.set(str(drinkCost))
    dessert_cost_var.set(str(dessertCost))
    subtotal_cost_var.set(str(foodCost+drinkCost+dessertCost))
    taxes_var.set(str((foodCost+drinkCost+dessertCost)/10))
    total_var.set(str(1.1*(foodCost+drinkCost+dessertCost)))
            


for food in foods:
  food_variables.append('')
  food_variables[counter] = IntVar(
  )  # Creates an integer variable (type-casting)
  food = Checkbutton(
    foodPanel,
    text=food.title(),
    font=('Dosis', 19, 'bold'),
    onvalue=1,
    offvalue=0,
    variable=food_variables[counter],
    bg='#74b72e',
    command=checkFoodClicked
  )  # Every element becomes a check button; when checked, check's value is 1 else 0
  # Creates a variable (checkbox) for every item
  food.grid(row=counter, column=0, sticky=W)  # West
  # Creating input boxes (no. of items), food box is a list which stores the food input boxes, food text stores the text in those boxes
  foodBox.append('')
  foodText.append('')
  foodText[counter] = StringVar()
  foodText[counter].set('0')  # When using the value, use an integer, when entering, use a string
  foodBox[counter] = Entry(
    foodPanel,
    bd=1,
    font=('Dosis', 19, 'bold'),
    width=6,
    state=DISABLED,
    textvariable=foodText[counter],
  )  # Until checking the checkbox, the input is disabled
  foodBox[counter].grid(row=counter, column=1)
  counter += 1

# Creating drink items

counter = 0
drink_variables = []
drinkBox = []
drinkText = []


def checkDrinkClicked():
  for i in range(len(drink_variables)):
    if drink_variables[i].get() == 1:
      drinkBox[i].config(state=NORMAL)
    else:
      drinkBox[i].config(state=DISABLED)


for drink in drinks:
  drink_variables.append('')
  drink_variables[counter] = IntVar(
  )  # Creates an integer variable (type-casting)
  drink = Checkbutton(
    drinkPanel,
    text=drink.title(),
    font=('Dosis', 19, 'bold'),
    onvalue=1,
    offvalue=0,
    variable=drink_variables[counter],
    bg='#74b72e',
    command=checkDrinkClicked
  )  # Every element becomes a check button; when checked, check's value is 1 else 0
  # Creates a variable (checkbox) for every item
  drink.grid(row=counter, column=0, sticky=W)  # West
  # Creating input boxes (no. of items), food box is a list which stores the food input boxes, food text stores the text in those boxes
  drinkBox.append('')
  drinkText.append('')
  drinkText[counter] = StringVar()
  drinkText[counter].set('0')
  drinkBox[counter] = Entry(
    drinkPanel,
    bd=1,
    font=('Dosis', 19, 'bold'),
    width=6,
    state=DISABLED,
    textvariable=drinkText[counter]
  )  # Until checking the checkbox, the input is disabled
  drinkBox[counter].grid(row=counter, column=1)
  counter += 1

# Creating dessert items

counter = 0
dessert_variables = []
dessertBox = []
dessertText = []


def checkDessertClicked():
  for i in range(len(dessert_variables)):
    if dessert_variables[i].get() == 1:
      dessertBox[i].config(state=NORMAL)
    else:
      dessertBox[i].config(state=DISABLED)


for dessert in desserts:
  dessert_variables.append(
    'placeholder'
  )  # All the placeholders are going to be changed later, these are checkboxes
  dessert_variables[counter] = IntVar(
  )  # Creates an integer variable (type-casting)
  dessert = Checkbutton(
    dessertPanel,
    text=dessert.title(),
    font=('Dosis', 19, 'bold'),
    onvalue=1,
    offvalue=0,
    variable=dessert_variables[counter],
    bg='#74b72e',
    command=checkDessertClicked
  )  # Every element becomes a check button; when checked, check's value is 1 else 0
  # Creates a variable (checkbox) for every item
  dessert.grid(row=counter, column=0, sticky=W)  # West
  # Creating input boxes (no. of items), food box is a list which stores the food input boxes, food text stores the text in those boxes
  dessertBox.append('')
  dessertText.append('')
  dessertText[counter] = StringVar()
  dessertText[counter].set('0')
  dessertBox[counter] = Entry(
    dessertPanel,
    bd=1,
    font=('Dosis', 19, 'bold'),
    width=6,
    state=DISABLED,
    textvariable=dessertText[counter]
  )  # Until checking the checkbox, the input is disabled
  dessertBox[counter].grid(row=counter, column=1)
  counter += 1
  
submitButton = Button(costPanel, width = 20, height=1, bg='green', text='Submit', font = ('Dosis', 19, 'bold'), command=addEverything)
submitButton.grid(row = 0, column = 1)


food_cost_label = Label(costPanel,
                        text='Food Costs',
                        font=('Dosis', 12, 'bold'),
                        bg='black',
                        fg='#ffd700')
food_cost_label.grid(row=1, column=0)
food_cost_text = Entry(costPanel,
                       font=('Dosis', 12, 'bold'),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=food_cost_var)
food_cost_text.grid(row=1, column=1, padx=60)

drink_cost_label = Label(costPanel,
                         text='Drink Costs',
                         font=('Dosis', 12, 'bold'),
                         fg='#ffd700',
                         bg='black')
drink_cost_label.grid(row=2, column=0)
drink_cost_text = Entry(costPanel,
                        font=('Dosis', 12, 'bold'),
                        bd=1,
                        width=10,
                        state='readonly',
                        textvariable=drink_cost_var)
drink_cost_text.grid(row=2, column=1)

dessert_cost_label = Label(costPanel,
                           text='Dessert Costs',
                           font=('Dosis', 12, 'bold'),
                           fg='#ffd700',
                           bg='black')
dessert_cost_label.grid(row=3, column=0)
dessert_cost_text = Entry(costPanel,
                          font=('Dosis', 12, 'bold'),
                          bd=1,
                          width=10,
                          state='readonly',
                          textvariable=dessert_cost_var)
dessert_cost_text.grid(row=3, column=1)

subtotal_cost_label = Label(costPanel,
                            text='Subtotal',
                            font=('Dosis', 12, 'bold'),
                            fg='#ffd700',
                            bg='black')
subtotal_cost_label.grid(row=1, column=2, padx=60)
subtotal_cost_text = Entry(costPanel,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=subtotal_cost_var)
subtotal_cost_text.grid(row=1, column=3)

taxes_cost_label = Label(costPanel,
                         text='Taxes',
                         font=('Dosis', 12, 'bold'),
                         fg='#ffd700',
                         bg='black')
taxes_cost_label.grid(row=2, column=2)
taxes_cost_text = Entry(costPanel,
                        font=('Dosis', 12, 'bold'),
                        bd=1,
                        width=10,
                        state='readonly',
                        textvariable=taxes_var)
taxes_cost_text.grid(row=2, column=3)

total_cost_label = Label(costPanel,
                         text='Total',
                         font=('Dosis', 12, 'bold'),
                         fg='#ffd700',
                         bg='black')
total_cost_label.grid(row=3, column=2)
total_cost_text = Entry(costPanel,
                        font=('Dosis', 12, 'bold'),
                        bd=1,
                        width=10,
                        state='readonly',
                        textvariable = total_var)
total_cost_text.grid(row=3, column=3)

buttonsList = ['Total', 'Invoice', 'Save', 'Clear']
for button in range(len(buttonsList)):
  createButton = Button(buttonPanel,
                        text=buttonsList[button],
                        relief=RAISED,
                        font=('Dosis', 19, 'bold'),
                        fg='white',
                        bg='azure4',
                        bd=1,
                        width=9)
  createButton.grid(row=0, column=button)
  
# Calculator

expression=""

def press(val):
    global expression
    expression+=str(val)
    equation.set(expression)

def equate():
    try:
        equation.set(eval(equation.get()))
    except:
        equation.set("error")
        expression=""

def clear():
    equation.set("")
    expression = ""

equation = StringVar()

box = Entry(calculator, textvariable=equation, width=50)
box.place(relx=0.3, rely=0)

button1 = Button(calculator, bg = '#652a0e', fg='black', text='1', width=10, height=2, command=lambda: press(1))
button1.place(x=120, y=80)

'''
button2 = Button(calculator, bg = '#652a0e', fg='black', text='2', width=10, height=2, command=lambda: press(2))
button2.place(x = 220, y = 80)
button3 = Button(calculator, bg = '#652a0e', fg='black', text='3', width=10, height=2, command=lambda: press(3))
button3.place(x = 320, y=80)
button4 = Button(calculator, bg = '#652a0e', fg='black', text='4', width=10, height=2, command=lambda: press(4))
button4.place(x=420, y=80)
button5 = Button(calculator, bg = '#652a0e', fg='black', text='5', width=10, height=2, command=lambda: press(5))
button5.place(x = 520, y=80)
button6 = Button(calculator, bg = '#652a0e', fg='black', text='6', width=10, height=2, command=lambda: press(6))
button6.place(x=120, y = 130)
button7 = Button(calculator, bg = '#652a0e', fg='black', text='7', width=10, height=2, command=lambda: press(7))
button7.place(x = 220, y = 130)
button8 = Button(calculator, bg = '#652a0e', fg='black', text='8', width=10, height=2, command=lambda: press(8))
button8.place(x = 320, y = 130)
button9 = Button(calculator, bg = '#652a0e', fg='black', text='9', width=10, height=2, command=lambda: press(9))
button9.place(x = 420, y = 130)
button0 = Button(calculator, bg = '#652a0e', fg='black', text='0', width=10, height=2, command=lambda: press(0))
button0.place(x = 520, y = 130)

add = Button(calculator, bg = '#652a0e', fg='black', text='+', width=10, height=2, command=lambda: press('+'))
add.place(x=120, y=180)
subtract = Button(calculator, bg = '#652a0e', fg='black', text='-', width=10, height=2, command=lambda: press('-'))
subtract.place(x=220, y=180)
multiply = Button(calculator, bg = '#652a0e', fg='black', text='x', width=10, height=2, command=lambda: press('*'))
multiply.place(x=320, y=180)
divide = Button(calculator, bg = '#652a0e', fg='black', text='/', width=10, height=2, command=lambda: press('/'))
divide.place(x=420, y=180)
equal = Button(calculator, bg = '#652a0e', fg='black', text='=', width=10, height=2, command=equate)
equal.place(x=520, y=180)
clear = Button(calculator, bg = '#652a0e', fg='black', text='clear', width=10, height=2, command=clear)
clear.place(x=320, y=230)

                  '''                                                                                                                                

root.mainloop()





