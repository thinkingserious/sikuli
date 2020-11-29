from sikuli import type, mouseMove, mouseDown, click

type("d", Key.ALT + Key.CMD) # show the dock, if hidden
mouseMove("trash.png")
mouseDown(Button.RIGHT)
click("empty_trash.png")
click("empty_trash_button.png")
mouseDown(Button.LEFT)
