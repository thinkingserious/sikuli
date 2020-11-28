from sikuli import click, findAll

click("spotlight_menu.png")
for x in findAll("checkbox.png"):
    click(x)
