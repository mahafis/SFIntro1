import os


PATH = os.getcwd()
GROUND = 585
print(PATH)


class Fighter:
    
    def __init__(self, x, y, r, img, slice_w, slice_h, num_slices, dir):
        self.x = x
        self.y = y
        self.g = GROUND
        self.r = r
        self.vx = 0
        self.vy = 1
        self.images = {
            "idle": loadImage(PATH + "/images/ryu/ryu_idle.png"),
            "walk": loadImage(PATH + "/images/ryu/ryu_walk.png"),
            "jump": loadImage(PATH + "/images/ryu/ryu_jump.png"),
            "crouch": loadImage(PATH + "/images/ryu/ryu_crouch.png")
        }
        self.img = self.images[img]  # Use the passed img key to set the initial image
        self.key_handler = {LEFT: False, RIGHT: False, UP: False, DOWN: False}
        self.slice_w = slice_w
        self.slice_h = slice_h
        self.num_slices = num_slices
        self.slice = 0
        self.dir = dir
        self.is_crouching = False
        
    def gravity(self):
        if self.y + self.r >= self.g:
            self.vy = 0
        else:
            self.vy += 0.6
            if self.y + self.r + self.vy > self.g:
                self.y = self.g - self.r
                self.vy = 0
    
    def update(self):
        self.gravity()
    
        if self.key_handler[LEFT]:
            self.vx = -7
            self.dir = LEFT
        elif self.key_handler[RIGHT]:
            self.vx = 7
            self.dir = RIGHT
        else:
            self.vx = 0
            
        if self.key_handler[UP] and self.y >= GROUND - self.r:
            self.vy = -15
            
        if self.vy != 0:
            self.key_handler[UP] = False
            
        self.x += self.vx
        self.y += self.vy
        
        if self.key_handler[DOWN] and self.vy == 0 and not self.is_crouching and self.vx == 0:
            self.img = self.images["crouch"]
            self.is_crouching = True
            self.slice = (self.slice) % (self.num_slices - 1)
        elif not self.key_handler[DOWN] and self.is_crouching:
            self.is_crouching = False
            self.img = self.images["idle"]
            self.slice = (self.slice + 1) % (self.num_slices - 1)

        if self.x - self.r < 0:
            self.x = self.r
        elif self.x + self.r > width:
            self.x = width - self.r
        
        if frameCount % 10 == 0 and not self.is_crouching:
            if self.vx != 0 and self.vy == 0:
                self.img = self.images["walk"]
                self.slice = (self.slice + 1) % (self.num_slices - 1)
            elif self.vy != 0:
                self.img = self.images["jump"]
                self.slice = (self.slice + 1) % (self.num_slices - 1)
            elif self.vy == 0 and self.vx == 0 and not self.is_crouching:
                self.img = self.images["idle"]
                self.slice = (self.slice + 1) % (self.num_slices - 1)
                
        

    def display(self):
        self.update()
        
        vertical_offset = 0
        if self.vy < 0:
            vertical_offset = -100
        elif self.vy > 0:
            vertical_offset = -130
        else:
            if self.vx != 0:
                vertical_offset = -25
                
        if self.is_crouching == True:
            vertical_offset = 50

        if self.dir == RIGHT:
            image(self.img, self.x - self.slice_w//2, self.y - self.slice_h//2 + vertical_offset, self.slice_w, self.slice_h, self.slice * self.slice_w, 0, (self.slice + 1) * self.slice_w, self.slice_h)
        elif self.dir == LEFT:
            image(self.img, self.x - self.slice_w//2, self.y - self.slice_h//2 + vertical_offset, self.slice_w, self.slice_h, (self.slice + 1) * self.slice_w, 0, self.slice * self.slice_w, self.slice_h)


class Ken(Fighter):
    def __init__(self, x, y, r, img, slice_w, slice_h, num_slices, dir):
        Fighter.__init__(self, x, y, r, img, slice_w, slice_h, num_slices, dir)
        self.images = {
            "idle": loadImage(PATH + "/images/ken/ken_idle.png"),
            "walk": loadImage(PATH + "/images/ken/ken_walk.png"),
            "jump": loadImage(PATH + "/images/ken/ken_jump.png"),
            "crouch": loadImage(PATH + "/images/ken/ken_crouch.png")
        }
        
        self.dir = LEFT
        
        self.img = self.images[img]
        
        self.key_handler = {LEFT: False, RIGHT: False, UP: False, DOWN: False}
        
    def update(self):
        self.gravity()
    
        if self.key_handler[LEFT]:
            self.vx = -7
            self.dir = LEFT
        elif self.key_handler[RIGHT]:
            self.vx = 7
            self.dir = RIGHT
        else:
            self.vx = 0
            
        if self.key_handler[UP] and self.y >= GROUND - self.r:
            self.vy = -15
            
        if self.vy != 0:
            self.key_handler[UP] = False
            
        self.x += self.vx
        self.y += self.vy
        
        if self.key_handler[DOWN] and self.vy == 0 and not self.is_crouching and self.vx == 0:
            self.img = self.images["crouch"]
            self.is_crouching = True
            self.slice = (self.slice) % (self.num_slices - 1)
        elif not self.key_handler[DOWN] and self.is_crouching:
            self.is_crouching = False
            self.img = self.images["idle"]
            self.slice = (self.slice + 1) % (self.num_slices - 1)

        if self.x - self.r < 0:
            self.x = self.r
        elif self.x + self.r > width:
            self.x = width - self.r
        
        if frameCount % 10 == 0 and not self.is_crouching:
            if self.vx != 0 and self.vy == 0:
                self.img = self.images["walk"]
                self.slice = (self.slice + 1) % (self.num_slices - 1)
            elif self.vy != 0:
                self.img = self.images["jump"]
                self.slice = (self.slice + 1) % (self.num_slices - 1)
            elif self.vy == 0 and self.vx == 0 and not self.is_crouching:
                self.img = self.images["idle"]
                self.slice = (self.slice + 1) % (self.num_slices - 1)
                
    def display(self):
        self.update()
        
        vertical_offset = 0
        if self.vy < 0:
            vertical_offset = -50
        elif self.vy > 0:
            vertical_offset = -60
        else:
            if self.vx != 0:
                vertical_offset = 25
                
        if self.is_crouching == True:
            vertical_offset = 50

        if self.dir == RIGHT:
            image(self.img, self.x - self.slice_w//2, self.y - self.slice_h//2 + vertical_offset, self.slice_w, self.slice_h, self.slice * self.slice_w, 0, (self.slice + 1) * self.slice_w, self.slice_h)
        elif self.dir == LEFT:
            image(self.img, self.x - self.slice_w//2, self.y - self.slice_h//2 + vertical_offset, self.slice_w, self.slice_h, (self.slice + 1) * self.slice_w, 0, self.slice * self.slice_w, self.slice_h)

        
        


class Game:
    
    def __init__(self, w, h, g):
        self.w = w
        self.h = h
        self.g = g
        self.ryu = Fighter(160, GROUND-50, 20, "idle", 160, 400, 5, dir = RIGHT)
        self.ken = Ken(1120, GROUND-50, 20, "idle", 160, 400, 5, dir = LEFT)
    
    def display(self):
        noStroke()
        fill(0,125,0)
        self.ryu.display()
        self.ken.display()
        rect(0, GROUND, 1280, 500)
        
        
    
    
game = Game(1280,800,585)
        
def setup():
    size(1280, 800)
    background(255,255,255)
    
def draw():
    background(255,255,255)
    game.display()
    
def keyPressed():
    if keyCode == LEFT:
        game.ryu.key_handler[LEFT] = True
    elif keyCode == RIGHT:
        game.ryu.key_handler[RIGHT] = True
    elif keyCode == UP:
        game.ryu.key_handler[UP] = True
    elif keyCode == DOWN:
        game.ryu.key_handler[DOWN] = True
        
    if key == 'w' or key == 'W':
        game.ken.key_handler[UP] = True
    elif key == 's' or key == 'S':
        game.ken.key_handler[DOWN] = True
    elif key == 'a' or key == 'A':
        game.ken.key_handler[LEFT] = True
    elif key == 'd' or key == 'D':
        game.ken.key_handler[RIGHT] = True
    
    
def keyReleased():
    if keyCode == LEFT:
        game.ryu.key_handler[LEFT] = False
    elif keyCode == RIGHT:
        game.ryu.key_handler[RIGHT] = False    
    elif keyCode == UP:
        game.ryu.key_handler[UP] = False
    elif keyCode == DOWN:
        game.ryu.key_handler[DOWN] = False
        
    if key == 'w' or key == 'W':
        game.ken.key_handler[UP] = False
    elif key == 's' or key == 'S':
        game.ken.key_handler[DOWN] = False
    elif key == 'a' or key == 'A':
        game.ken.key_handler[LEFT] = False
    elif key == 'd' or key == 'D':
        game.ken.key_handler[RIGHT] = False
