import pygame, random

pygame.init()
win = pygame.display.set_mode(
    (0,0), pygame.FULLSCREEN)
W,H = win.get_size()
font = pygame.font.SysFont(
    "courier", 30, bold=True)

cols = W // 30
drops = [random.randint(-40, 0)
         for _ in range(cols)]

fade = pygame.Surface((W,H))
fade.set_alpha(35)

while True:
    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN:
            raise SystemExit
        
        win.blit(fade, (0,0))
        for i, y in enumerate(drops):
            c = random.choice("01ABCXYZ#*")
            img = font.render(c, 1, "lime")
            win.blit(img,(i * 30, y * 30))
            bottom = y * 30 > H
            if bottom and random.random() > .97:
                drops[i] = 0
            else:
                drops[i] += 1
    pygame.display.flip()
    pygame.time.wait(50)