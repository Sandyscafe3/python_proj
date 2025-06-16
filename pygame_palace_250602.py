import pygame

# Pygame 초기화
pygame.init()

# 화면 크기 설정
screen_width = 600 
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("이미지로 캐릭터 움직이기")

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)        # 검은색
RED = (255, 0, 0)        # 빨간색
GREEN = (0, 255, 0)      # 초록색
BLUE = (0, 0, 255)       # 파란색
YELLOW = (255, 255, 0)   # 노란색
CYAN = (0, 255, 255)     # 청록색
MAGENTA = (255, 0, 255)  # 마젠타(보라색)

# 캐릭터 이미지 로드
# player_image = pygame.image.load("border.jpg")  # 'border' 파일을 로드합니다.
player_image = pygame.image.load("hanbok.png")  # 'border' 파일을 로드합니다.
player_width = player_image.get_width()  # 이미지의 가로 크기
player_height = player_image.get_height()  # 이미지의 세로 크기
player_image = pygame.transform.scale(player_image, (200, 250))  # 배경 크기를 화면에 맞게 조정


background_image = pygame.image.load("palace.jpg")  # 'background_image.png' 이미지를 로드합니다.
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))  # 배경 크기를 화면에 맞게 조정

hunmin =  pygame.image.load("hunmin.jpg")
hunmin = pygame.transform.scale(hunmin, (100, 100))  # 배경 크기를 화면에 맞게 조정

storm =  pygame.image.load("storm.jpg")
storm = pygame.transform.scale(storm, (100, 100))  # 배경 크기를 화면에 맞게 조정

bok =  pygame.image.load("bok.jpg")
bok = pygame.transform.scale(bok, (100, 100))  # 배경 크기를 화면에 맞게 조정

zak =  pygame.image.load("zak.png")
zak = pygame.transform.scale(zak, (100, 100))  # 배경 크기를 화면에 맞게 조정

# 캐릭터 초기 위치 설정
player_x = 0  # 화면의 중앙 위치
player_y = 0
player_speed = 5

jumping = False
jump_count = 10  # 점프 높이

# 게임 루프
game_over = False
clock = pygame.time.Clock()

# 게임 루프 시작
while not game_over:
    screen.fill(GREEN)  # 화면을 흰색으로 채움

    # 캐릭터 이미지 그리기

    screen.blit(background_image, (0, 0))  # 이미지 위치에 캐릭터를 그립니다.

    screen.blit(hunmin, (0, 300))
    screen.blit(storm, (500, 0))
    screen.blit(bok, (500, 300))
    screen.blit(zak, (0, 0))
    screen.blit(player_image, (player_x, player_y))  # 이미지 위치에 캐릭터를 그립니다.

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # 키보드 입력 처리
    keys = pygame.key.get_pressed()  # 키보드의 눌린 키들 상태를 받아옴
    if keys[pygame.K_LEFT]:  # 왼쪽 화살표
        player_x -= player_speed  # 왼쪽으로 이동
    if keys[pygame.K_RIGHT]:  # 오른쪽 화살표
        player_x += player_speed  # 오른쪽으로 이동
    if keys[pygame.K_UP]:  # 위쪽 화살표
        player_y -= player_speed  # 위로 이동
    if keys[pygame.K_DOWN]:  # 아래쪽 화살표
        player_y += player_speed  # 아래로 이동

# 점프 구현
    if not jumping:
        if keys[pygame.K_SPACE]:  # 스페이스 키로 점프
            jumping = True
    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            player_y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            jumping = False
            jump_count = 10
    # 화면 업데이트
    pygame.display.update()
    clock.tick(60)  # 초당 60프레임

# Pygame 종료
pygame.quit()
