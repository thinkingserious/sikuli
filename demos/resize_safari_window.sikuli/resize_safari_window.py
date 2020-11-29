from sikuli import switchApp, find, dragDrop

def resizeApp(app, dx, dy):
    switchApp(app)
    corner = find(Pattern("corner.png").targetOffset(3,14))
    drop_point = corner.getTarget().offset(dx, dy)
    dragDrop(corner, drop_point)

resizeApp("Safari", 50, 50)
