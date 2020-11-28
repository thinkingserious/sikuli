from sikuli import App, click, dragDrop

App.open("System Preferences.app")
click("accessibility.png")
click("spoken_content.png")
dragDrop("slider.png","slow.png")
