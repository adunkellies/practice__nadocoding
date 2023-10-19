import random
import pygame
##############################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init()

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Quiz")

# FPS
clock = pygame.time.Clock()
##############################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
# 배경화면
background = pygame.image.load("C:\\coding\\nadocoding\\pygame_basic\\background.png")

# 캐릭터
charater = pygame.image.load("C:\\coding\\nadocoding\\pygame_basic\\charater.png")
charater_size = charater.get_rect().size
charater_width = charater_size[0]
charater_height = charater_size[1]
charater_x_pos = (screen_width / 2) - (charater_width / 2)
charater_y_pos = screen_height - charater_height

# 이동할 좌표
to_x = 0

# 이동 속도
charater_speed = 0.5

# 적 enemy 캐릭터
enemy = pygame.image.load("C:\\coding\\nadocoding\\pygame_basic\\enemy.png")
enemy_size = enemy.get_rect().size # 이미지의 크기를 구해옴
enemy_width = enemy_size[0] # 캐릭터의 가로 크기
enemy_height = enemy_size[1] # 캐릭터의 세로 크기
enemy_x_pos = random.randint(0, screen_width - enemy_width)
enemy_y_pos = -enemy_height

# 적 이동 속도
enemy_speed = 0.5

running = True
while running:
    dt = clock.tick(30)

    # 2. 이벤트 처리 (키보드, 마우스등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                to_x -= charater_speed
            elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
                to_x += charater_speed

        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    charater_x_pos += to_x * dt
    enemy_y_pos += enemy_speed * dt

    # 3. 게임 캐릭터 위치 정의
    # 가로 경계값 처리
    if charater_x_pos < 0:
        charater_x_pos = 0
    elif charater_x_pos > screen_width - charater_width:
        charater_x_pos = screen_width - charater_width
    
    if enemy_y_pos > screen_height:
        enemy_x_pos = random.randint(0, screen_width - enemy_width)
        enemy_y_pos = 0
    
    # 4. 충돌 처리
    # 충돌 처리를 위한 rect 정보 업데이트
    charater_rect = charater.get_rect()
    charater_rect.left = charater_x_pos
    charater_rect.top = charater_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if charater_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False

    # 5. 화면에 그리기
    screen.blit(background, (0, 0)) # 배경 그리기

    screen.blit(charater, (charater_x_pos, charater_y_pos)) # 캐릭터 그리기

    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 적 그리기
    
    pygame.display.update()

pygame.quit()