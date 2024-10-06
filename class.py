
class gun: 
    def __init__(self,name,ammo,damage):
        self.name = name
        self.ammo = ammo
        self.damage = damage
    def load(self,ammo):
        self.ammo += ammo
    
    def crirical(self):
        self.damage *=2 
    
    def reload(self):
        if self.ammo <=30:
            self.ammo + 30
    
    def semi(self):
        self.ammo -=1 

    def fire(self,ammo):
        self.ammo -= ammo 

glock = gun('Glock',17,2)
sig = gun('Sig',19,2)
M4 = gun('M4',30,5)

M4.load(10)
M4.fire(8)
M4.semi()
M4.crirical()
print(M4.ammo,M4.damage)