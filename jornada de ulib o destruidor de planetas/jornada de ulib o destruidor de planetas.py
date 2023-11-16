import pygame, sys
import time
from button import Button
import math
from pygame.locals import *
from random import *

pygame.init()

display_size = 1280, 720
screen = pygame.display.set_mode(display_size)
fonte = pygame.font.SysFont("Times New Roman", 32)
fonte_ending = pygame.font.SysFont("Times New Roman", 72)
button_sound = pygame.mixer.Sound("button.MP3")
background_menu_original = pygame.image.load("menu_background.png").convert()
background_menu = pygame.transform.scale(background_menu_original, (720,720))
background_cutscene_1 = pygame.transform.scale(background_menu_original, (1280,720))
imagem = pygame.image.load("img/image_lv1.png")
bg_width = background_menu.get_width()
bg_rect = background_menu.get_rect()
ulib_som = pygame.mixer.Sound("ulib urro.MP3")
vulcao_som = pygame.mixer.Sound("vulcao explodindo.MP3")
passaro_som = pygame.mixer.Sound("som passaro.MP3")
passaro_raiva_som = pygame.mixer.Sound("som passaro com raiva.MP3")
starter_music = pygame.mixer.Sound("starter_music.MP3")

imagem_ulib_dialogo_original = pygame.image.load(r'ulib dialogo.png')
imagem_ulib_dialogo_scaled = pygame.transform.scale(imagem_ulib_dialogo_original, (180, 180))

imagem_chico_dialogo_original = pygame.image.load(r'chico dialogo.png')
imagem_chico_dialogo_scaled = pygame.transform.scale(imagem_chico_dialogo_original, (180,180))

imagem_opium_dialogo_original = pygame.image.load(r'opium bird dialogo.png')
imagem_opium_dialogo_scaled = pygame.transform.scale(imagem_opium_dialogo_original, (180,180))

def display_text(surface, text, pos, fonte, color):
    collection = [word.split(' ') for word in text.splitlines()]
    space = fonte.size(' ')[0]
    x,y = pos
    for lines in collection:
        for words in lines:
            word_surface = fonte.render(words, True, color)
            word_width , word_height = word_surface.get_size()
            if x + word_width >= 800:
                x = pos[0]
                y += word_height
            surface.blit(word_surface, (x,y))
            x += word_width + space
        x = pos[0]
        y += word_height

def fase_1():

    chico_ost = pygame.mixer.music.load("guarda_chico_ost.MP3")
    pygame.mixer.music.set_volume(0.5)  

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)
    RED = (255, 0, 0)
    BLUE= (0,0,255)

    font = pygame.font.SysFont('sans', 20)
    player_lives = 20
    enemy_lives = 5

    posicaoUlib = [30, 300]
    velocidadeUlib = [0, 10]

    criar = True
    X_vermelho = 0
    Y_vermelho = 0
    fall = True 

    X_branco = 0
    Y_branco = 0

    posicaoInimigo = [1180, 300]
    velocidadeInimigo = [0, 5]
    vertical_direction = 1
    vertical_speed = 5

    clock = pygame.time.Clock()
    CLOCKTICK = pygame.USEREVENT + 1
    pygame.time.set_timer(CLOCKTICK, 1000)

    last_red_ball_time = 0

    font_game_over = pygame.font.SysFont('sans', 60)
    game_over_text = font_game_over.render('Game Over', True, RED)
    game_over_rect = game_over_text.get_rect(center=(display_size[0] // 2, display_size[1] // 2))

    font_victory = pygame.font.SysFont('sans', 60)
    victory_text = font_victory.render('Você venceu!', True, BLUE)
    victory_rect = victory_text.get_rect(center=(display_size[0] // 2, display_size[1] // 2))

    vitoria_tempo = 0

    class Sprite_chars(pygame.sprite.Sprite):
        def __init__(self,image_path, x, y):
            super().__init__()
            self.image = pygame.image.load(image_path).convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)

        def update(self, y_pos):
            self.rect.y = y_pos

    ulib_path = "img/alt_Ulib.png"
    ulib_spr = Sprite_chars(ulib_path, posicaoUlib[0], posicaoUlib[1])

    chico_path = "img/alt_guarda_chico.png"
    chico_sprt = Sprite_chars(chico_path, posicaoInimigo[0], posicaoInimigo[1])

    all_sprites = pygame.sprite.Group()
    all_sprites.add(ulib_spr)
    all_sprites.add(chico_sprt)

    image = pygame.image.load(r'cutscene fase 1.png')
    image_size = image.get_rect().size
    centered_image = [(display_size[0] - image_size[0])/2, (display_size[1] - image_size[1])/2]

    for i in range (255):
        screen.fill((0,0,0))    
        image.set_alpha(i)    
        screen.blit(image, centered_image)    
        pygame.display.update()    
        time.sleep(0.002)

    time.sleep(2)

    pygame.draw.rect(screen, (0,0,0), pygame.Rect(240,520,800,200))
    screen.blit(imagem_chico_dialogo_scaled, (250, 530))
    pygame.display.update()
    time.sleep(0.25)
    display_text(screen, "Com licença colega verde não permitimos estacionamento de naves dentro do vulcão", (450, 540), fonte, "white")
    pygame.display.update()

    time.sleep(3)

    pygame.draw.rect(screen, (0,0,0), pygame.Rect(240,520,800,200))
    screen.blit(imagem_ulib_dialogo_scaled, (250, 530))
    ulib_som.play()
    display_text(screen, "*Incompreensível*", (450, 540), fonte, "white")
    pygame.display.update()

    vulcao_som.play()

    time.sleep(1.5)

    pygame.draw.rect(screen, (0,0,0), pygame.Rect(240,520,800,200))
    screen.blit(imagem_chico_dialogo_scaled, (250, 530))
    display_text(screen, "O qu-", (450, 540), fonte, "white")
    pygame.display.update()

    time.sleep(0.2)

    image = pygame.image.load(r'cutscene fase 1 vulcao.png')
    image_size = image.get_rect().size
    centered_image = [(display_size[0] - image_size[0])/2, (display_size[1] - image_size[1])/2]
    screen.blit(image, centered_image)  
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(240,520,800,200))
    display_text(screen, "!!!", (270, 540), fonte, "white")
    pygame.display.update()

    time.sleep(1)

    pygame.draw.rect(screen, (0,0,0), pygame.Rect(240,520,800,200))
    screen.blit(imagem_chico_dialogo_scaled, (250, 530))
    display_text(screen, "MEU DEUS O VULCÃO", (450, 540), fonte, "white")
    pygame.display.update()

    time.sleep(2)

    pygame.draw.rect(screen, (0,0,0), pygame.Rect(240,520,800,200))
    screen.blit(imagem_chico_dialogo_scaled, (250, 530))
    display_text(screen, "A HUMANIDADE VAI MORRER E A CULPA É SUA", (450, 540), fonte, "white")
    pygame.display.update()

    time.sleep(2)

    pygame.draw.rect(screen, (0,0,0), pygame.Rect(240,520,800,200))
    screen.blit(imagem_ulib_dialogo_scaled, (250, 530))
    display_text(screen, "(Visivelmente desinteressado)", (450, 540), fonte, "white")
    pygame.display.update()

    time.sleep(2)

    pygame.draw.rect(screen, (0,0,0), pygame.Rect(240,520,800,200))
    display_text(screen, "O combate vai começar!", (270, 540), fonte, "white")
    pygame.display.update()

    time.sleep(2)

    pygame.draw.rect(screen, (0,0,0), pygame.Rect(240,520,800,200))
    display_text(screen, "Desvie dos tiros brancos, eles te dão dano, e depois de 5 tiros, você perde", (270, 540), fonte, "white")
    pygame.display.update()

    time.sleep(4)

    pygame.draw.rect(screen, (0,0,0), pygame.Rect(240,520,800,200))
    display_text(screen, "Os vermelhos são seu meio de ataque, rebata para causar dano ao inimigo", (270, 540), fonte, "white")
    pygame.display.update()

    time.sleep(4)

    pygame.draw.rect(screen, (0,0,0), pygame.Rect(240,520,800,200))
    display_text(screen, "O combate vai começar em 3!", (270, 540), fonte, "white")
    pygame.display.update()

    time.sleep(1.5)

    pygame.draw.rect(screen, (0,0,0), pygame.Rect(240,520,800,200))
    display_text(screen, "2!", (270, 540), fonte, "white")
    pygame.display.update()

    time.sleep(1.5)

    pygame.draw.rect(screen, (0,0,0), pygame.Rect(240,520,800,200))
    display_text(screen, "1!", (270, 540), fonte, "white")
    pygame.display.update()

    time.sleep(1.5)

    pygame.draw.rect(screen, (0,0,0), pygame.Rect(240,520,800,200))
    display_text(screen, "Comece!", (270, 540), fonte, "white")
    pygame.display.update()

    time.sleep(1.5)

    #jogo comeca aqui

    pygame.mixer.music.play(-1, 0.0)  

    while True:

        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_r:
                # Reiniciar a fase
                player_lives = 20
                enemy_lives = 5
                posicaoUlib = [30, 300]
                posicaoInimigo = [1180, 300]
                X_vermelho = 0
                Y_vermelho = 0
                fall = True
                X_branco = 0
                Y_branco = 0
                pressed = pygame.key.get_pressed()

        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP] and posicaoUlib[1] > 0:
            posicaoUlib[1] -= velocidadeUlib[1]
        if pressed[pygame.K_DOWN] and posicaoUlib[1] < display_size[1] - 130:
            posicaoUlib[1] += velocidadeUlib[1]
        if pressed[pygame.K_LEFT] and posicaoUlib[0] > 0:
            posicaoUlib[0] -= velocidadeUlib[0]
        if pressed[pygame.K_RIGHT] and posicaoUlib[0] < display_size[0] - 50:
            posicaoUlib[0] += velocidadeUlib[0]

        posicaoInimigo[0] += velocidadeInimigo[0]

        if posicaoInimigo[0] < -50:
            posicaoInimigo[0] = 1280

        if posicaoInimigo[1] < 0:
            posicaoInimigo[1] = 0
            vertical_direction = 1
        elif posicaoInimigo[1] > display_size[1] - 130:
            posicaoInimigo[1] = display_size[1] - 130
            vertical_direction = -1

        posicaoInimigo[1] += vertical_direction * vertical_speed

        if randint(0, 100) < 2:
            vertical_direction = -vertical_direction




        ulib_spr.update(posicaoUlib[1])
        chico_sprt.update(posicaoInimigo[1])
        screen.blit(imagem, (0, 0))
        all_sprites.draw(screen)





        if current_time - last_red_ball_time >= 3000:
            X_vermelho = 1240
            Y_vermelho = randint(40, 680)
            last_red_ball_time = current_time

        if fall == True:
            X_vermelho -= 25
        if fall == False:
            X_vermelho += 25

        posicaoBolasVermelhas = [X_vermelho, Y_vermelho]
        pygame.draw.circle(screen, RED, posicaoBolasVermelhas, 10)

        if X_vermelho < 0:
            criar = True
        if X_vermelho > 1280:
            criar = True
            fall = True

        if (
            (posicaoUlib[1] + 130 >= Y_vermelho - 10 and posicaoUlib[1] <= Y_vermelho + 10)
            and (posicaoUlib[0] + 50 >= X_vermelho - 10 and posicaoUlib[0] - 50 <= X_vermelho + 20)
        ):
            if fall:  
                enemy_lives -= 1
                bonk_sound = pygame.mixer.Sound('som/bonk.mp3')
                bonk_sound.play()
                fall = False
        player_score = font.render('HP Ulib ' + str(player_lives), True, (BLUE))
        enemy_score = font.render('HP inimigo: ' + str(enemy_lives), True, (RED))
        screen.blit(player_score, (20, 20))  
        screen.blit(enemy_score, (display_size[0] - 200, 20))  

        X_branco -= 25
        if X_branco < 0:
            criar = True
            X_branco = 1280
            Y_branco = randint(40, 680)

        posicaoBolasBrancas = [X_branco, Y_branco]
        pygame.draw.circle(screen, WHITE, posicaoBolasBrancas, 10)

        if (
            (posicaoUlib[1] + 130 >= Y_branco - 10 and posicaoUlib[1] <= Y_branco + 10)
            and (posicaoUlib[0] + 50 >= X_branco - 10 and posicaoUlib[0] - 50 <= X_branco + 20)
        ):
            player_lives -= 1

        if player_lives <= 0:
            screen.blit(game_over_text, game_over_rect)
            restart_text = font.render('Pressione R para recomeçar.', True, WHITE)
            restart_rect = restart_text.get_rect(center=(display_size[0] // 2, display_size[1] // 2 + 60))
            screen.blit(restart_text, restart_rect)       
            pygame.display.flip()
            pygame.time.delay(3000)  

        if enemy_lives <= 0:
            
            if vitoria_tempo == 0:
                vitoria_tempo = current_time
                

            if current_time - vitoria_tempo >= 1000:  
                screen.blit(victory_text, victory_rect)
                info_text = font.render('A jornada de Ulib segue.', True, RED)
                restart_rect = info_text.get_rect(center=(display_size[0] // 2, display_size[1] // 2 + 60))
                screen.blit(info_text, restart_rect)
                pygame.display.flip()
                pygame.mixer.fadeout(3000)
                pygame.time.delay(3000)

                fase_2()

        pygame.display.flip()
        clock.tick(60)

def fase_2():

    imagem = pygame.image.load("img/alt_fundo_fase2.png")
    bonfire = pygame.image.load("img/bonfire_ds3.png")

    opium_bird = pygame.mixer.music.load("opium_bird_ost.MP3")
    pygame.mixer.music.set_volume(0.5) 

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)
    RED = (255, 0, 0)
    BLUE= (0,0,255)

    font = pygame.font.SysFont('sans', 20)
    player_lives = 20
    enemy_lives = 5

    posicaoUlib = [30, 650]
    velocidadeUlib = [0, 10]

    criar = True
    X_vermelho = 0
    Y_vermelho = 0
    fall = True 

    X_branco = 0
    Y_branco = 0

    posicaoInimigo = [1050  , 300]
    velocidadeInimigo = [0, 5]
    vertical_direction = 1
    vertical_speed = 5

    clock = pygame.time.Clock()
    CLOCKTICK = pygame.USEREVENT + 1
    pygame.time.set_timer(CLOCKTICK, 1000)

    # Initialize a variable to keep track of the time for red balls
    last_red_ball_time = 0

    font_game_over = pygame.font.SysFont('sans', 60)
    game_over_text = font_game_over.render('Game Over', True, RED)
    game_over_rect = game_over_text.get_rect(center=(display_size[0] // 2, display_size[1] // 2))

    font_victory = pygame.font.SysFont('sans', 60)
    victory_text = font_victory.render('Você venceu!', True, BLUE)
    victory_rect = victory_text.get_rect(center=(display_size[0] // 2, display_size[1] // 2))

    vitoria_tempo = 0

    area_recuperacao = pygame.Rect(10, display_size[1] - 70, 100, 60)
    cor_area_recuperacao = YELLOW

    font_calor = pygame.font.SysFont('sans', 40)
    calor=70

    pygame.time.set_timer(USEREVENT + 1, 1000)

    recuperacao_timer = pygame.time.get_ticks()

    class Sprite_chars(pygame.sprite.Sprite):
        def __init__(self,image_path, x, y):
            super().__init__()
            self.image = pygame.image.load(image_path).convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)

        def update(self, y_pos):
            self.rect.y = y_pos

    ulib_path = "img/alt_Ulib.png"
    ulib_spr = Sprite_chars(ulib_path, posicaoUlib[0], posicaoUlib[1])

    opium_path = "img/alt_opium_bird.png"
    opium_sprt = Sprite_chars(opium_path, posicaoInimigo[0], posicaoInimigo[1])

    all_sprites = pygame.sprite.Group()
    all_sprites.add(ulib_spr)
    all_sprites.add(opium_sprt)

    image = pygame.image.load(r'cutscene fase 2.png')
    image_scaled = pygame.transform.scale(image, (1280,720))
    image_size = image_scaled.get_rect().size
    centered_image = [(display_size[0] - image_size[0])/2, (display_size[1] - image_size[1])/2]

    frase_cutscene1 = fonte.render("Após derrotar o guarda florestal, ulib continuou sua jornada rumo à casa branca.", True, (255,255,255))
    frase_cutscene2 = fonte.render("Conforme avançava, as temperaturas pareciam cair cada vez mais,", True, (255,255,255))
    frase_cutscene2_2 = fonte.render("e foi aí que o nosso protagonista se deu conta.", True, (255,255,255))
    frase_cutscene3 = fonte.render("Um inverno vulcânico havia começado.", True, (255,255,255))
    frase_cutscene4 = fonte.render("Cada vez mais fraco, ulib busca desesperadamente por fontes de calor para se aquecer.", True, (255,255,255))
    frase_cutscene5 = fonte.render("No último momento, havia finalmente achado uma fogueira para se esquentar.", True, (255,255,255))
    frase_cutscene6 = fonte.render("Só que ele não foi o único.", True, (255,0,0))

    time.sleep(1.5)

    starter_music.play()
    screen.fill("black")
    pygame.display.update()

    time.sleep(1.5)

    for i in range (255):
        screen.fill((0,0,0))    
        frase_cutscene1.set_alpha(i)    
        screen.blit(frase_cutscene1, (60, 60)) 
        pygame.display.update()    
        time.sleep(0.001)

    time.sleep(2.5)

    for i in range (255, 0, -1):
        screen.fill((0,0,0))       
        frase_cutscene1.set_alpha(i)    
        screen.blit(frase_cutscene1, (60, 60))  
        pygame.display.update()    
        time.sleep(0.001)

    time.sleep(1.5)

    for i in range (255):
        screen.fill((0,0,0))    
        frase_cutscene2.set_alpha(i)    
        screen.blit(frase_cutscene2, (60, 60)) 
        frase_cutscene2_2.set_alpha(i)    
        screen.blit(frase_cutscene2_2, (60, 110)) 
        pygame.display.update()    
        time.sleep(0.001)

    time.sleep(3.5)

    for i in range (255, 0, -1):
        screen.fill((0,0,0))       
        frase_cutscene2.set_alpha(i)    
        screen.blit(frase_cutscene2, (60, 60))  
        frase_cutscene2_2.set_alpha(i)    
        screen.blit(frase_cutscene2_2, (60, 110)) 
        pygame.display.update()    
        time.sleep(0.001)

    time.sleep(1.5)

    for i in range (255):
        screen.fill((0,0,0))    
        frase_cutscene3.set_alpha(i)    
        screen.blit(frase_cutscene3, (60, 60)) 
        pygame.display.update()    
        time.sleep(0.001)

    time.sleep(2.5)

    for i in range (255, 0, -1):
        screen.fill((0,0,0))       
        frase_cutscene3.set_alpha(i)    
        screen.blit(frase_cutscene3, (60, 60))  
        pygame.display.update()    
        time.sleep(0.001)

    time.sleep(1.5)

    for i in range (255):
        screen.fill((0,0,0))    
        frase_cutscene4.set_alpha(i)    
        screen.blit(frase_cutscene4, (60, 60)) 
        pygame.display.update()    
        time.sleep(0.001)

    time.sleep(3)

    for i in range (255, 0, -1):
        screen.fill((0,0,0))       
        frase_cutscene4.set_alpha(i)    
        screen.blit(frase_cutscene4, (60, 60))  
        pygame.display.update()    
        time.sleep(0.001)

    time.sleep(1.5)

    for i in range (255):
        screen.fill((0,0,0))    
        frase_cutscene5.set_alpha(i)    
        screen.blit(frase_cutscene5, (60, 60)) 
        pygame.display.update()    
        time.sleep(0.001)

    time.sleep(2.5)

    for i in range (255, 0, -1):
        screen.fill((0,0,0))       
        frase_cutscene5.set_alpha(i)    
        screen.blit(frase_cutscene5, (60, 60))  
        pygame.display.update()    
        time.sleep(0.001)

    time.sleep(1.5)

    for i in range (255):
        screen.fill((0,0,0))    
        frase_cutscene6.set_alpha(i)    
        screen.blit(frase_cutscene6, (60, 60)) 
        pygame.display.update()    
        time.sleep(0.001)

    time.sleep(2.5)

    for i in range (255, 0, -1):
        screen.fill((0,0,0))       
        frase_cutscene6.set_alpha(i)    
        screen.blit(frase_cutscene6, (60, 60))  
        pygame.display.update()    
        time.sleep(0.001)

    starter_music.fadeout(1500)
    time.sleep(1.5)

    for i in range (255):
        screen.fill((0,0,0))    
        image_scaled.set_alpha(i)    
        screen.blit(image_scaled, centered_image)    
        pygame.display.update()    
        time.sleep(0.002)

    time.sleep(2)

    pygame.draw.rect(screen, (0,0,0), pygame.Rect(240,520,800,200))
    screen.blit(imagem_opium_dialogo_scaled, (250, 530))
    pygame.display.update()
    time.sleep(0.25)
    display_text(screen, "(som de pássaro amigável)", (450, 540), fonte, "white")
    pygame.display.update()
    passaro_som.play()

    time.sleep(2.5)

    pygame.draw.rect(screen, (0,0,0), pygame.Rect(240,520,800,200))
    display_text(screen, "As aves parecem querer dividir a fogueira com você.", (270, 540), fonte, "white")
    pygame.display.update()

    time.sleep(3)

    pygame.draw.rect(screen, (0,0,0), pygame.Rect(240,520,800,200))
    screen.blit(imagem_ulib_dialogo_scaled, (250, 530))
    ulib_som.play()
    display_text(screen, "(Ulib faz um sinal um tanto quanto rude com as maõs)", (450, 540), fonte, "white")
    pygame.display.update()

    time.sleep(3)

    pygame.draw.rect(screen, (0,0,0), pygame.Rect(240,520,800,200))
    screen.blit(imagem_opium_dialogo_scaled, (250, 530))
    pygame.display.update()
    passaro_raiva_som.set_volume(0.1)
    passaro_raiva_som.play()
    display_text(screen, "(som de pássaro com raiva)", (450, 540), fonte, "white")
    pygame.display.update()

    time.sleep(2.5)

    pygame.draw.rect(screen, (0,0,0), pygame.Rect(240,520,800,200))
    display_text(screen, "parece que essa discussão não vai levar a lugar nenhum...", (270, 540), fonte, "white")
    pygame.display.update()

    time.sleep(3)

    pygame.draw.rect(screen, (0,0,0), pygame.Rect(240,520,800,200))
    display_text(screen, "O combate vai começar em 3!", (270, 540), fonte, "white")
    pygame.display.update()

    time.sleep(1.5)

    pygame.draw.rect(screen, (0,0,0), pygame.Rect(240,520,800,200))
    display_text(screen, "2!", (270, 540), fonte, "white")
    pygame.display.update()

    time.sleep(1.5)

    pygame.draw.rect(screen, (0,0,0), pygame.Rect(240,520,800,200))
    display_text(screen, "1!", (270, 540), fonte, "white")
    pygame.display.update()

    time.sleep(1.5)

    pygame.draw.rect(screen, (0,0,0), pygame.Rect(240,520,800,200))
    display_text(screen, "Comece!", (270, 540), fonte, "white")
    pygame.display.update()

    time.sleep(1.5)

    pygame.mixer.music.play(-1, 0.0)  

    while True:
        
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_r:
                # Reiniciar a fase
                player_lives = 20
                enemy_lives = 5
                posicaoUlib = [30, 300]
                posicaoInimigo = [1050, 300]
                X_vermelho = 0
                Y_vermelho = 0
                fall = True
                X_branco = 0
                Y_branco = 0
                calor=5
                pressed = pygame.key.get_pressed()
                
            elif event.type == USEREVENT + 1:
                calor -= 1
                calor = max(calor, -1)
                
                if calor == 0:
                    screen.blit(game_over_text, game_over_rect)
                    restart_text = font.render('Pressione R para recomeçar.', True, BLACK)
                    restart_rect = restart_text.get_rect(center=(display_size[0] // 2, display_size[1] // 2 + 60))
                    screen.blit(restart_text, restart_rect)
                    pygame.display.flip()
                    pygame.time.delay(3000)  

        pressed = pygame.key.get_pressed()
        
        if area_recuperacao.colliderect(pygame.Rect(posicaoUlib[0], posicaoUlib[1], 50, 130)):
            if current_time - recuperacao_timer >= 400:
                calor += 1
                recuperacao_timer = current_time


        if pressed[pygame.K_UP] and posicaoUlib[1] > 0:
            posicaoUlib[1] -= velocidadeUlib[1]
        if pressed[pygame.K_DOWN] and posicaoUlib[1] < display_size[1] - 130:
            posicaoUlib[1] += velocidadeUlib[1]
        if pressed[pygame.K_LEFT] and posicaoUlib[0] > 0:
            posicaoUlib[0] -= velocidadeUlib[0]
        if pressed[pygame.K_RIGHT] and posicaoUlib[0] < display_size[0] - 50:
            posicaoUlib[0] += velocidadeUlib[0]

        posicaoInimigo[0] += velocidadeInimigo[0]

        if posicaoInimigo[0] < -50:
            posicaoInimigo[0] = 1280

        if posicaoInimigo[1] < 0:
            posicaoInimigo[1] = 0
            vertical_direction = 1
        elif posicaoInimigo[1] > display_size[1] - 130:
            posicaoInimigo[1] = display_size[1] - 130
            vertical_direction = -1

        posicaoInimigo[1] += vertical_direction * vertical_speed

        if randint(0, 100) < 2:
            vertical_direction = -vertical_direction

        ulib_spr.update(posicaoUlib[1])
        opium_sprt.update(posicaoInimigo[1])
        screen.blit(imagem, (0, 0))
        all_sprites.draw(screen)

        if current_time - last_red_ball_time >= 3000:
            X_vermelho = 1240
            Y_vermelho = randint(40, 680)
            last_red_ball_time = current_time
        
        calor = max(calor, 0)
        
        calor_text = font_calor.render('Calor: ' + str(calor), True, YELLOW)
        calor_rect = calor_text.get_rect(center=(display_size[0] // 2, display_size[1] - 20))
        screen.blit(calor_text, calor_rect)
        
        screen.blit(bonfire, (10, 600))

        if fall == True:
            X_vermelho -= 25
        if fall == False:
            X_vermelho += 25

        posicaoBolasVermelhas = [X_vermelho, Y_vermelho]
        pygame.draw.circle(screen, RED, posicaoBolasVermelhas, 10)

        if X_vermelho < 0:
            criar = True
        if X_vermelho > 1280:
            criar = True
            fall = True

        if (
            (posicaoUlib[1] + 130 >= Y_vermelho - 10 and posicaoUlib[1] <= Y_vermelho + 10)
            and (posicaoUlib[0] + 50 >= X_vermelho - 10 and posicaoUlib[0] - 50 <= X_vermelho + 20)
        ):
            if fall:  
                enemy_lives -= 1
                bonk_sound = pygame.mixer.Sound('som/bonk.mp3')
                bonk_sound.play()
                fall = False
        player_score = font.render('HP Ulib ' + str(player_lives), True, (BLUE))
        enemy_score = font.render('HP inimigo: ' + str(enemy_lives), True, (RED))
        screen.blit(player_score, (20, 20))  
        screen.blit(enemy_score, (display_size[0] - 200, 20))  

        X_branco -= 25
        if X_branco < 0:
            criar = True
            X_branco = 1280
            Y_branco = randint(40, 680)

        posicaoBolasBrancas = [X_branco, Y_branco]
        pygame.draw.circle(screen, WHITE, posicaoBolasBrancas, 10)

        if (
            (posicaoUlib[1] + 130 >= Y_branco - 10 and posicaoUlib[1] <= Y_branco + 10)
            and (posicaoUlib[0] + 50 >= X_branco - 10 and posicaoUlib[0] - 50 <= X_branco + 20)
        ):
            player_lives -= 1

        if player_lives <= 0:
            screen.blit(game_over_text, game_over_rect)
            restart_text = font.render('Pressione R para recomeçar.', True, RED)
            restart_rect = restart_text.get_rect(center=(display_size[0] // 2, display_size[1] // 2 + 60))
            screen.blit(restart_text, restart_rect)       
            pygame.display.flip()
            pygame.time.delay(3000) 

        if enemy_lives <= 0:
            
            if vitoria_tempo == 0:
                vitoria_tempo = current_time
                

            if current_time - vitoria_tempo >= 1000:  
                screen.blit(victory_text, victory_rect)
                info_text = font.render('A jornada de Ulib segue.', True, RED)
                restart_rect = info_text.get_rect(center=(display_size[0] // 2, display_size[1] // 2 + 60))
                screen.blit(info_text, restart_rect)
                pygame.display.flip()
                pygame.mixer.music.fadeout(3000)
                pygame.time.delay(3000) 
                fase_3()

        pygame.display.flip()
        clock.tick(60)

def fase_3():

    imagem = pygame.image.load("img/alt_casa_branca.jpg")
    

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)

    font = pygame.font.SysFont('sans', 20)
    player_lives = 40
    enemy_lives = 1

    posicaoUlib = [30, 300]
    velocidadeUlib = [0, 10]

    criar = True
    X_vermelho = 0
    Y_vermelho = 0
    fall = True 

    X_branco = 0
    Y_branco = 0

    posicaoInimigo = [1100, 300]
    velocidadeInimigo = [0, 5]
    vertical_direction = 1
    vertical_speed = 5

    clock = pygame.time.Clock()
    CLOCKTICK = pygame.USEREVENT + 1
    pygame.time.set_timer(CLOCKTICK, 1000)

    last_red_ball_time = 0

    font_game_over = pygame.font.SysFont('sans', 60)
    game_over_text = font_game_over.render('Game Over', True, RED)
    game_over_rect = game_over_text.get_rect(center=(display_size[0] // 2, display_size[1] // 2))

    font_victory = pygame.font.SysFont('sans', 60)
    victory_text = font_victory.render('Você venceu!', True, BLACK)
    victory_rect = victory_text.get_rect(center=(display_size[0] // 2, display_size[1] // 2))

    vitoria_tempo = 0

    class Sprite_chars(pygame.sprite.Sprite):
        def __init__(self,image_path, x, y):
            super().__init__()
            self.image = pygame.image.load(image_path).convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)

        def update(self, y_pos):
            self.rect.y = y_pos

    ulib_path = "img/alt_Ulib_chutambo.png"
    ulib_chutambo_spr = Sprite_chars(ulib_path, posicaoUlib[0], posicaoUlib[1])

    opium_path = "img/alt_souza_mansur.png"
    souza_mansur_sprt = Sprite_chars(opium_path, posicaoInimigo[0], posicaoInimigo[1])

    all_sprites = pygame.sprite.Group()
    all_sprites.add(ulib_chutambo_spr)
    all_sprites.add(souza_mansur_sprt)

    image = pygame.image.load(r'cutscene fase 3.png')
    image_scaled = pygame.transform.scale(image, (1280,720))
    image_size = image_scaled.get_rect().size
    centered_image = [(display_size[0] - image_size[0])/2, (display_size[1] - image_size[1])/2]
    musica_cutscene3 = pygame.mixer.Sound("cutscene 3 musica.MP3")

    frase_cutscene1 = fonte.render("Vitorioso e aquecido, ulib segue sua jornada.", True, (255,255,255))
    frase_cutscene2 = fonte.render("Porém mal sabia ele o que o aguardava...", True, (255,255,255))
    frase_cutscene3 = fonte.render("Chegando na casa branca, ulib se depara com o inigualável,", True, (255,255,255))
    frase_cutscene4 = fonte.render("O imparável,", True, (255,255,255))
    frase_cutscene5 = fonte.render("O invencível,", True, (255,255,255))
    frase_cutscene6 = fonte.render("Mestre Souza mansur.", True, (255,0,0))

    musica_cutscene3.play()
    time.sleep(1.5)
    
    screen.fill("black")
    pygame.display.update()

    time.sleep(1.5)

    for i in range (255):
        screen.fill((0,0,0))    
        frase_cutscene1.set_alpha(i)    
        screen.blit(frase_cutscene1, (60, 60)) 
        pygame.display.update()    
        time.sleep(0.001)

    time.sleep(2.5)

    for i in range (255, 0, -1):
        screen.fill((0,0,0))       
        frase_cutscene1.set_alpha(i)    
        screen.blit(frase_cutscene1, (60, 60))  
        pygame.display.update()    
        time.sleep(0.001)

    time.sleep(1.5)

    for i in range (255):
        screen.fill((0,0,0))    
        frase_cutscene2.set_alpha(i)    
        screen.blit(frase_cutscene2, (60, 60)) 
        pygame.display.update()    
        time.sleep(0.001)

    time.sleep(2.5)

    for i in range (255, 0, -1):
        screen.fill((0,0,0))       
        frase_cutscene2.set_alpha(i)    
        screen.blit(frase_cutscene2, (60, 60))  
        pygame.display.update()    
        time.sleep(0.001)

    time.sleep(1.5)

    for i in range (255):
        screen.fill((0,0,0))    
        frase_cutscene3.set_alpha(i)    
        screen.blit(frase_cutscene3, (60, 60)) 
        pygame.display.update()    
        time.sleep(0.001)

    time.sleep(2.5)

    for i in range (255, 0, -1):
        screen.fill((0,0,0))       
        frase_cutscene3.set_alpha(i)    
        screen.blit(frase_cutscene3, (60, 60))  
        pygame.display.update()    
        time.sleep(0.001)

    time.sleep(1.5)

    for i in range (255):
        screen.fill((0,0,0))    
        frase_cutscene4.set_alpha(i)    
        screen.blit(frase_cutscene4, (60, 60)) 
        pygame.display.update()    
        time.sleep(0.001)

    time.sleep(1)

    for i in range (255, 0, -1):
        screen.fill((0,0,0))       
        frase_cutscene4.set_alpha(i)    
        screen.blit(frase_cutscene4, (60, 60))  
        pygame.display.update()    
        time.sleep(0.001)

    time.sleep(1.5)

    for i in range (255):
        screen.fill((0,0,0))    
        frase_cutscene5.set_alpha(i)    
        screen.blit(frase_cutscene5, (60, 60)) 
        pygame.display.update()    
        time.sleep(0.001)

    time.sleep(1)

    for i in range (255, 0, -1):
        screen.fill((0,0,0))       
        frase_cutscene5.set_alpha(i)    
        screen.blit(frase_cutscene5, (60, 60))  
        pygame.display.update()    
        time.sleep(0.001)

    time.sleep(1.5)

    for i in range (255):
        screen.fill((0,0,0))    
        frase_cutscene6.set_alpha(i)    
        screen.blit(frase_cutscene6, (60, 60)) 
        pygame.display.update()    
        time.sleep(0.001)

    time.sleep(3)

    for i in range (255, 0, -1):
        screen.fill((0,0,0))       
        frase_cutscene6.set_alpha(i)    
        screen.blit(frase_cutscene6, (60, 60))  
        pygame.display.update()    
        time.sleep(0.001)

    time.sleep(1.5)

    for i in range (255):
        screen.fill((0,0,0))    
        image_scaled.set_alpha(i)    
        screen.blit(image_scaled, centered_image)    
        pygame.display.update()    
        time.sleep(0.002)

    time.sleep(2)

    pygame.draw.rect(screen, (0,0,0), pygame.Rect(240,520,800,200))
    pygame.display.update()
    time.sleep(0.25)
    display_text(screen, "conversas são desnecessárias", (270, 540), fonte, "white")
    pygame.display.update()

    time.sleep(3)

    pygame.draw.rect(screen, (0,0,0), pygame.Rect(240,520,800,200))
    display_text(screen, "ele veio para impedi-lo e isso é tudo que importa", (270, 540), fonte, "white")
    pygame.display.update()

    time.sleep(3.5)

    pygame.draw.rect(screen, (0,0,0), pygame.Rect(240,520,800,200))
    display_text(screen, "porém ulib não se renderá facilmente", (270, 540), fonte, "white")
    pygame.display.update()

    time.sleep(3)

    pygame.draw.rect(screen, (0,0,0), pygame.Rect(240,520,800,200))
    display_text(screen, "a casa branca está repleta de argônio", (270, 540), fonte, "white")
    pygame.display.update()

    time.sleep(3)

    pygame.draw.rect(screen, (0,0,0), pygame.Rect(240,520,800,200))
    display_text(screen, "gás que coincidentalmente é o respirado por ulib em sua terra natal", (270, 540), fonte, "white")
    pygame.display.update()

    time.sleep(4)

    pygame.draw.rect(screen, (0,0,0), pygame.Rect(240,520,800,200))
    display_text(screen, "elevando assim suas capacidades ao máximo", (270, 540), fonte, "white")
    pygame.display.update()

    time.sleep(3)

    pygame.draw.rect(screen, (0,0,0), pygame.Rect(240,520,800,200))
    display_text(screen, "O combate final irá começar", (270, 540), fonte, "white")
    pygame.display.update()

    time.sleep(2.5)

    pygame.draw.rect(screen, (0,0,0), pygame.Rect(240,520,800,200))
    display_text(screen, "Subitamente, sua consciência te recorda dos ensinamentos passados por gerações por sua família", (270, 540), fonte, "white")
    pygame.display.update()

    time.sleep(4.5)

    pygame.draw.rect(screen, (0,0,0), pygame.Rect(240,520,800,200))
    display_text(screen, "\"No chutambô você entra no ringue com a perna bamba pra ficar mais fácil do seu adversário te derrubar porque...\"", (270, 540), fonte, "white")
    pygame.display.update()

    time.sleep(5)

    pygame.draw.rect(screen, (0,0,0), pygame.Rect(240,520,800,200))
    display_text(screen, "\"O fracasso é o sucesso do chutambô.\"", (270, 540), fonte, "red")
    pygame.display.update()

    time.sleep(4)

    pygame.draw.rect(screen, (0,0,0), pygame.Rect(240,520,800,200))
    display_text(screen, "3.", (270, 540), fonte, "white")
    pygame.display.update()

    time.sleep(2)

    pygame.draw.rect(screen, (0,0,0), pygame.Rect(240,520,800,200))
    display_text(screen, "2.", (270, 540), fonte, "white")
    pygame.display.update()

    time.sleep(2)

    pygame.draw.rect(screen, (0,0,0), pygame.Rect(240,520,800,200))
    display_text(screen, "1.", (270, 540), fonte, "white")
    pygame.display.update()

    time.sleep(2)
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(240,520,800,200))
    display_text(screen, "Comece.", (270, 540), fonte, "white")
    pygame.display.update()

    time.sleep(2)


    while True:

        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_r:
                # Reiniciar a fase
                player_lives = 20
                enemy_lives = 5
                posicaoUlib = [30, 300]
                posicaoInimigo = [1100, 300]
                X_vermelho = 0
                Y_vermelho = 0
                fall = True
                X_branco = 0
                Y_branco = 0
                pressed = pygame.key.get_pressed()

        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP] and posicaoUlib[1] > 0:
            posicaoUlib[1] -= velocidadeUlib[1]
        if pressed[pygame.K_DOWN] and posicaoUlib[1] < display_size[1] - 130:
            posicaoUlib[1] += velocidadeUlib[1]
        if pressed[pygame.K_LEFT] and posicaoUlib[0] > 0:
            posicaoUlib[0] -= velocidadeUlib[0]
        if pressed[pygame.K_RIGHT] and posicaoUlib[0] < display_size[0] - 50:
            posicaoUlib[0] += velocidadeUlib[0]

        posicaoInimigo[0] += velocidadeInimigo[0]

        if posicaoInimigo[0] < -50:
            posicaoInimigo[0] = 1280

        if posicaoInimigo[1] < 0:
            posicaoInimigo[1] = 0
            vertical_direction = 1
        elif posicaoInimigo[1] > display_size[1] - 130:
            posicaoInimigo[1] = display_size[1] - 130
            vertical_direction = -1

        posicaoInimigo[1] += vertical_direction * vertical_speed

        if randint(0, 100) < 2:
            vertical_direction = -vertical_direction

        ulib_chutambo_spr.update(posicaoUlib[1])
        souza_mansur_sprt.update(posicaoInimigo[1])
        screen.blit(imagem, (0, 0))
        all_sprites.draw(screen)

        if current_time - last_red_ball_time >= 3000:
            X_vermelho = 1240
            Y_vermelho = randint(40, 680)
            last_red_ball_time = current_time

        if fall == True:
            X_vermelho -= 25
        if fall == False:
            X_vermelho += 25

        posicaoBolasVermelhas = [X_vermelho, Y_vermelho]
        pygame.draw.circle(screen, RED, posicaoBolasVermelhas, 10)

        if X_vermelho < 0:
            criar = True
        if X_vermelho > 1280:
            criar = True
            fall = True

        if (
            (posicaoUlib[1] + 130 >= Y_vermelho - 10 and posicaoUlib[1] <= Y_vermelho + 10)
            and (posicaoUlib[0] + 50 >= X_vermelho - 10 and posicaoUlib[0] - 50 <= X_vermelho + 20)
        ):
            if fall:  
                enemy_lives -= 1
                bonk_sound = pygame.mixer.Sound('som/bonk.mp3')
                bonk_sound.play()
                fall = False

        player_score = font.render('Player Lives: ' + str(player_lives), True, (BLUE))
        enemy_score = font.render('Enemy Lives: ' + str(enemy_lives), True, (WHITE))
        screen.blit(player_score, (20, 20))  
        screen.blit(enemy_score, (display_size[0] - 200, 20))  

        X_branco -= 25
        if X_branco < 0:
            criar = True
            X_branco = 1280
            Y_branco = randint(40, 680)

        posicaoBolasBrancas = [X_branco, Y_branco]
        pygame.draw.circle(screen, WHITE, posicaoBolasBrancas, 10)

        if (
            (posicaoUlib[1] + 130 >= Y_branco - 10 and posicaoUlib[1] <= Y_branco + 10)
            and (posicaoUlib[0] + 50 >= X_branco - 10 and posicaoUlib[0] - 50 <= X_branco + 20)
        ):
            player_lives -= 1

        if player_lives <= 0:
            screen.blit(game_over_text, game_over_rect)
            restart_text = font.render('Você perdeu, parabéns, ISSO É CHUTAMBÔ', True, BLUE)
            restart_rect = restart_text.get_rect(center=(display_size[0] // 2, display_size[1] // 2 + 60))
            screen.blit(restart_text, restart_rect)       
            pygame.display.flip()




            pygame.time.delay(3000)
            musica_cutscene3.stop()
            ending()

        if enemy_lives <= 0:
            
            if vitoria_tempo == 0:
                vitoria_tempo = current_time
                

            if current_time - vitoria_tempo >= 1000:  
                screen.blit(victory_text, victory_rect)
                info_text = font.render('Tente de novo', True, RED)
                restart_rect = info_text.get_rect(center=(display_size[0] // 2, display_size[1] // 2 + 60))
                screen.blit(info_text, restart_rect)
                pygame.display.flip()
                pygame.time.delay(3000) 
                
        pygame.display.flip()
        clock.tick(60)

def ending():

    ending_music = pygame.mixer.Sound("ending_music.MP3")

    image = pygame.image.load(r'casa branca.png')
    image_scaled = pygame.transform.scale(image, (1280,720))
    image_size = image_scaled.get_rect().size
    centered_image = [(display_size[0] - image_size[0])/2, (display_size[1] - image_size[1])/2]

    frase_cutscene1 = fonte.render("Assim acaba a jornada de ulib.", True, (255,255,255))
    frase_cutscene2 = fonte.render("Tendo derrotado o tubarão mais insano a ter pisado no planeta,", True, (255,255,255))
    frase_cutscene2_2 = fonte.render("nosso protagonista está satisfeito com suas conquistas.", True, (255,255,255))
    frase_cutscene3 = fonte.render("E ele não está sozinho.", True, (255,255,255))
    frase_cutscene4 = fonte.render("Admirados pela vitória, os passáros elegem ulib como seu novo líder.", True, (255,255,255))
    frase_cutscene5 = fonte.render("Sem esperanças de sobreviver na terra arrasada pelo inverno absoluto,", True, (255,255,255))
    frase_cutscene5_2 = fonte.render("eles partem para uma nova jornada.", True, (255,255,255))
    frase_ending = fonte_ending.render("Obrigado por jogar!", True, (255, 255, 255))

    time.sleep(1.5)

    ending_music.play()
    screen.fill("black")
    pygame.display.update()

    time.sleep(1.5)

    for i in range (255):
        screen.fill((0,0,0))    
        frase_cutscene1.set_alpha(i)    
        screen.blit(frase_cutscene1, (60, 60)) 
        pygame.display.update()    
        time.sleep(0.001)

    time.sleep(2.5)

    for i in range (255, 0, -1):
        screen.fill((0,0,0))       
        frase_cutscene1.set_alpha(i)    
        screen.blit(frase_cutscene1, (60, 60))  
        pygame.display.update()    
        time.sleep(0.001)

    time.sleep(1.5)

    for i in range (255):
        screen.fill((0,0,0))    
        frase_cutscene2.set_alpha(i)    
        screen.blit(frase_cutscene2, (60, 60)) 
        frase_cutscene2_2.set_alpha(i)    
        screen.blit(frase_cutscene2_2, (60, 110)) 
        pygame.display.update()    
        time.sleep(0.001)

    time.sleep(2.5)

    for i in range (255, 0, -1):
        screen.fill((0,0,0))       
        frase_cutscene2.set_alpha(i)    
        screen.blit(frase_cutscene2, (60, 60))
        frase_cutscene2_2.set_alpha(i)    
        screen.blit(frase_cutscene2_2, (60, 110)) 
        pygame.display.update()    
        time.sleep(0.001)

    time.sleep(1.5)

    for i in range (255):
        screen.fill((0,0,0))    
        frase_cutscene3.set_alpha(i)    
        screen.blit(frase_cutscene3, (60, 60)) 
        pygame.display.update()    
        time.sleep(0.001)

    time.sleep(2.5)

    for i in range (255, 0, -1):
        screen.fill((0,0,0))       
        frase_cutscene3.set_alpha(i)    
        screen.blit(frase_cutscene3, (60, 60))  
        pygame.display.update()    
        time.sleep(0.001)

    time.sleep(1.5)

    for i in range (255):
        screen.fill((0,0,0))    
        frase_cutscene4.set_alpha(i)    
        screen.blit(frase_cutscene4, (60, 60)) 
        pygame.display.update()    
        time.sleep(0.001)

    time.sleep(2.5)

    for i in range (255, 0, -1):
        screen.fill((0,0,0))       
        frase_cutscene4.set_alpha(i)    
        screen.blit(frase_cutscene4, (60, 60))  
        pygame.display.update()    
        time.sleep(0.001)

    time.sleep(1.5)

    for i in range (255):
        screen.fill((0,0,0))    
        frase_cutscene5.set_alpha(i)    
        screen.blit(frase_cutscene5, (60, 60)) 
        frase_cutscene5_2.set_alpha(i)    
        screen.blit(frase_cutscene5_2, (60, 110)) 
        pygame.display.update()    
        time.sleep(0.001)

    time.sleep(2.5)

    for i in range (255, 0, -1):
        screen.fill((0,0,0))       
        frase_cutscene5.set_alpha(i)    
        screen.blit(frase_cutscene5, (60, 60))
        frase_cutscene5_2.set_alpha(i)    
        screen.blit(frase_cutscene5_2, (60, 110)) 
        pygame.display.update()    
        time.sleep(0.001)

    time.sleep(1.5)

    for i in range (255):
        screen.fill((0,0,0))    
        image_scaled.set_alpha(i)    
        screen.blit(image_scaled, centered_image)    
        pygame.display.update()    
        time.sleep(0.002)

    time.sleep(3)

    pygame.draw.rect(screen, (0,0,0), pygame.Rect(240,520,800,200))
    pygame.display.update()
    time.sleep(0.25)
    display_text(screen, "O que o futuro reserva para nossos heróis?", (270, 540), fonte, "white")
    pygame.display.update()

    time.sleep(3)

    pygame.draw.rect(screen, (0,0,0), pygame.Rect(240,520,800,200))
    pygame.display.update()
    time.sleep(0.25)
    display_text(screen, "Apenas o tempo dirá...", (270, 540), fonte, "white")
    pygame.display.update()

    time.sleep(2.5)

    for i in range (255, 0, -1):
        screen.fill((0,0,0))       
        image_scaled.set_alpha(i)    
        screen.blit(image_scaled, centered_image)  
        pygame.display.update()    
        time.sleep(0.001)

    time.sleep(5)

    for i in range (255):
        screen.fill((0,0,0))    
        frase_ending.set_alpha(i)    
        screen.blit(frase_ending, (360, 300)) 
        pygame.display.update()    
        time.sleep(5)

def menu():
     screen.fill("black")

     pygame.display.update()

     music = pygame.mixer.Sound("menu_music.MP3")
     music.play()

     time.sleep(5)

     scroll = 0
     tiles = math.ceil(1280  / bg_width) + 1

     while True:
        for i in range(0, tiles):
            screen.blit(background_menu, (i * bg_width + scroll, 0))

        scroll -= 0.5

        if abs(scroll) > bg_width:
            scroll = 0

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = fonte.render("ULIB VOLCANIC ADVENTURES", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("Play Rect.png"), pos=(640, 250), 
                            text_input="JOGAR", font=fonte, base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("Quit Rect.png"), pos=(640, 550), 
                            text_input="SAIR", font=fonte, base_color="#d7fcd4", hovering_color="White")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    music.stop()
                    button_sound.play()
                    fase_1()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def intro():
    frase_cutscene1 = fonte.render("Ulib, um contente alienígena cruzava o espaço em sua nave doida de tubarao", True, (255,255,255))
    frase_cutscene2 = fonte.render("Até que um dia...", True, (255,0,0))
    frase_cutscene3 = fonte.render("Ulib, sem conseguir resistir ao impacto causado por um míssil,", True, (255,255,255))
    frase_cutscene3_2 = fonte.render("caiu sem esperanças na Terra, desconhecida por ele.", True, (255,255,255))
    frase_cutscene4 = fonte.render("Como se não bastasse a tragédia, Ulib caiu dentro do vulcão Yellowstone.", True, (255,255,255))
    frase_cutscene5 = fonte.render("Perdido em um lugar estranho, e detectando a origem do míssil na casa branca,", True, (255,255,255))

    image = pygame.image.load(r'nave_tubarao_foda.png')
    image_size = image.get_rect().size

    frase_cutscene5_2 = fonte.render("nosso protagonista parte em busca de respostas.", True, (255,255,255))
    centered_image = [(display_size[0] - image_size[0])/2, (display_size[1] - image_size[1])/2]

    starter_music.play()

    time.sleep(1.5)

    for i in range (255):
        screen.fill((0,0,0))    
        frase_cutscene1.set_alpha(i)    
        screen.blit(frase_cutscene1, (60, 60)) 
        pygame.display.update()    
        time.sleep(0.001)

    time.sleep(1.5)

    for i in range (255, 0, -1):
        screen.fill((0,0,0))       
        frase_cutscene1.set_alpha(i)    
        screen.blit(frase_cutscene1, (60, 60))  
        pygame.display.update()    
        time.sleep(0.001)

    time.sleep(1.5)

    for i in range (255):
        screen.fill((0,0,0))    
        image.set_alpha(i)    
        screen.blit(image, centered_image)    
        pygame.display.update()    
        time.sleep(0.001)

    time.sleep(1)

    for i in range (255, 0, -1):
        screen.fill((0,0,0))       
        image.set_alpha(i)    
        screen.blit(image, centered_image)    
        pygame.display.update()    
        time.sleep(0.001)

    time.sleep(1.5)

    for i in range (255):
        screen.fill((0,0,0))    
        frase_cutscene2.set_alpha(i)    
        screen.blit(frase_cutscene2, (60, 60)) 
        pygame.display.update()    
        time.sleep(0.001)

    time.sleep(1.5)

    for i in range (255, 0, -1):
        screen.fill((0,0,0))       
        frase_cutscene2.set_alpha(i)    
        screen.blit(frase_cutscene2, (60, 60))  
        pygame.display.update()    
        time.sleep(0.001)

    time.sleep(1.5)

    image = pygame.image.load(r'explosao.webp')

    explosao = pygame.mixer.Sound("ulib explodindo.MP3")
    explosao.set_volume(0.2)
    explosao.play()

    for i in range (255):
        screen.fill((0,0,0))    
        image.set_alpha(i)    
        screen.blit(image, (150, 50))
        screen.blit(image, (340, 310)) 
        screen.blit(image, (790, 230)) 
        screen.blit(image, (920, 480))   
        pygame.display.update()    
        time.sleep(0.001)

    time.sleep(1)

    for i in range (255, 0, -1):
        screen.fill((0,0,0))       
        image.set_alpha(i)    
        screen.blit(image, (150, 50))
        screen.blit(image, (340, 310)) 
        screen.blit(image, (790, 230)) 
        screen.blit(image, (920, 480))   
        pygame.display.update()    
        time.sleep(0.001)

    time.sleep(1.5)

    for i in range (255):
        screen.fill((0,0,0))    
        frase_cutscene3.set_alpha(i)    
        screen.blit(frase_cutscene3, (60, 60))
        frase_cutscene3_2.set_alpha(i)    
        screen.blit(frase_cutscene3_2, (60,110)) 
        pygame.display.update()    
        time.sleep(0.001)

    time.sleep(3)

    for i in range (255, 0, -1):
        screen.fill((0,0,0))       
        frase_cutscene3.set_alpha(i)    
        screen.blit(frase_cutscene3, (60, 60))  
        frase_cutscene3_2.set_alpha(i)    
        screen.blit(frase_cutscene3_2, (60,110)) 
        pygame.display.update()    
        time.sleep(0.001)

    time.sleep(1.5)

    image = pygame.image.load(r'ulib_caindo.jpg')
    image_size = image.get_rect().size
    centered_image = [(display_size[0] - image_size[0])/2, (display_size[1] - image_size[1])/2]

    for i in range (255):
        screen.fill((0,0,0))    
        image.set_alpha(i)    
        screen.blit(image, centered_image)    
        pygame.display.update()    
        time.sleep(0.001)

    time.sleep(1)

    for i in range (255, 0, -1):
        screen.fill((0,0,0))       
        image.set_alpha(i)    
        screen.blit(image, centered_image)    
        pygame.display.update()    
        time.sleep(0.001)

    time.sleep(1.5)

    for i in range (255):
        screen.fill((0,0,0))    
        frase_cutscene4.set_alpha(i)    
        screen.blit(frase_cutscene4, (60, 60)) 
        pygame.display.update()    
        time.sleep(0.001)

    time.sleep(1.5)

    for i in range (255, 0, -1):
        screen.fill((0,0,0))       
        frase_cutscene4.set_alpha(i)    
        screen.blit(frase_cutscene4, (60, 60))  
        pygame.display.update()    
        time.sleep(0.001)

    time.sleep(1.5)

    image = pygame.image.load(r'yellowstone.jpg')
    image_size = image.get_rect().size
    centered_image = [(display_size[0] - image_size[0])/2, (display_size[1] - image_size[1])/2]

    for i in range (255):
        screen.fill((0,0,0))    
        image.set_alpha(i)    
        screen.blit(image, centered_image)    
        pygame.display.update()    
        time.sleep(0.001)

    time.sleep(1)

    for i in range (255, 0, -1):
        screen.fill((0,0,0))       
        image.set_alpha(i)    
        screen.blit(image, centered_image)    
        pygame.display.update()    
        time.sleep(0.001)

    time.sleep(1.5)

    for i in range (255):
        screen.fill((0,0,0))    
        frase_cutscene5.set_alpha(i)    
        screen.blit(frase_cutscene5, (60, 60))
        frase_cutscene5_2.set_alpha(i)    
        screen.blit(frase_cutscene5_2, (60,110)) 
        pygame.display.update()    
        time.sleep(0.001)

    time.sleep(3)

    for i in range (255, 0, -1):
        screen.fill((0,0,0))       
        frase_cutscene5.set_alpha(i)    
        screen.blit(frase_cutscene5, (60, 60))  
        frase_cutscene5_2.set_alpha(i)    
        screen.blit(frase_cutscene5_2, (60,110)) 
        pygame.display.update()    
        time.sleep(0.001)

    time.sleep(5)

    starter_music.fadeout(5500)

    time.sleep(3)

    menu()

screen.fill("black")

while True:
    PLAY_MOUSE_POS = pygame.mouse.get_pos()

    PLAY_TEXT = fonte.render("Deseja pular a introdução?", True, "White")
    PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
    screen.blit(PLAY_TEXT, PLAY_RECT)

    PLAY_SIM = Button(image=None, pos=(640, 460), text_input="Sim", font=fonte, base_color="White", hovering_color="Green")
    PLAY_NAO = Button(image=None, pos=(640, 600), text_input="Não", font=fonte, base_color="White", hovering_color="Green")

    PLAY_SIM.changeColor(PLAY_MOUSE_POS)
    PLAY_SIM.update(screen)

    PLAY_NAO.changeColor(PLAY_MOUSE_POS)
    PLAY_NAO.update(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if PLAY_SIM.checkForInput(PLAY_MOUSE_POS):
                button_sound.play()
                menu()
            if PLAY_NAO.checkForInput(PLAY_MOUSE_POS):
                button_sound.play()
                intro()
    
    pygame.display.update()