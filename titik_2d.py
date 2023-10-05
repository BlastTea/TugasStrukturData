class Titik2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def geserHorizontal(self, dx):
        self.x += dx

    def geserVertikal(self, dy):
        self.y += dy

    def hitungJarak(self, titik_lain):
        return ((self.x - titik_lain.x).__abs__()**2) + ((self.y - titik_lain.y).__abs__()**2)**0.5
        
    def getX(self):
        return self.x

    def getY(self):
        return self.y

t1 = Titik2D(2, 3)
t2 = Titik2D(4, 5)

t1.geserHorizontal(-3)
t1.geserVertikal(-7)

print(f't1: {t1.x}, {t1.y}')

t2.geserHorizontal(15)
t2.geserVertikal(9)

print(f't2: {t2.x}, {t2.y}')

jarak = t1.hitungJarak(t2)
print(f'jarak: {jarak}')