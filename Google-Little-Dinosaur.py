# 导入pygame模块
import pygame

# 初始化pygame
pygame.init()

# 设置窗口大小和标题
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Google Dinosaur Game")

# 加载图片资源
background = pygame.image.load("background.png")
dinosaur = pygame.image.load("dinosaur.png")
cactus = pygame.image.load("cactus.png")

# 设置图片位置和速度
background_x = 0
background_speed = -5
dinosaur_x = 100
dinosaur_y = 400
dinosaur_speed = 0
cactus_x = 800
cactus_y = 400
cactus_speed = -10

# 设置游戏状态和分数
running = True
game_over = False
score = 0

# 设置字体和颜色
font = pygame.font.SysFont("arial", 32)
white = (255, 255, 255)
black = (0, 0, 0)

# 主循环
while running:

    # 处理事件
    for event in pygame.event.get():

        # 如果点击关闭按钮，退出游戏
        if event.type == pygame.QUIT:
            running = False

        # 如果按下空格键，让恐龙跳起来
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and dinosaur_y == 400:
                dinosaur_speed = -15

    # 更新图片位置
    background_x += background_speed
    dinosaur_y += dinosaur_speed
    cactus_x += cactus_speed

    # 如果背景图片移出屏幕，让它回到初始位置
    if background_x <= -800:
        background_x = 0

    # 如果恐龙跳起来，让它受重力影响下落
    if dinosaur_y < 400:
        dinosaur_speed += 1

    # 如果仙人掌移出屏幕，让它回到初始位置，并增加分数和速度
    if cactus_x <= -100:
        cactus_x = 800
        score += 1
        cactus_speed -= 1

    # 检测恐龙和仙人掌是否碰撞，如果是，游戏结束
    if dinosaur_x + dinosaur.get_width() > cactus_x and dinosaur_y + dinosaur.get_height() > cactus_y:
        game_over = True

    # 绘制背景图片
    screen.blit(background, (background_x, 0))
    screen.blit(background, (background_x + 800, 0))

    # 绘制恐龙和仙人掌图片
    screen.blit(dinosaur, (dinosaur_x, dinosaur_y))
    screen.blit(cactus, (cactus_x, cactus_y))

    # 绘制分数和游戏结束提示文字
    score_text = font.render("Score: " + str(score), True, white)
    screen.blit(score_text, (10, 10))
    if game_over:
        game_over_text = font.render("Game Over", True, black)
        screen.blit(game_over_text, (350, 250))

    # 更新屏幕显示
    pygame.display.flip()
