from sikuli import *
click("spotlight_menu.png")
for x in findAll("checkbox.png"):
    click(x)