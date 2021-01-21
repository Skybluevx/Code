import random
import pygame

# 设置屏幕大小
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新的帧率
FRAME_PER_SEC = 100
# 创建敌机定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 创建子弹定时器常量
HERO_FIRE_EVENT = pygame.USEREVENT + 1
# 创建敌机时间间隔
CREATE_ENEMY_TIME = 500
# 开火时间间隔
FIRE_TIME = 100


class GameSprite(pygame.sprite.Sprite):
    """
        飞机大战游戏精灵
    """
    def __init__(self, image_name, speed=1):
        # 调用父类的初始化方法
        super().__init__()

        # 定义属性
        # 定义所传递的图像名称的图像
        self.image = pygame.image.load(image_name)
        # 定义图像属性
        self.rect = self.image.get_rect()

        self.speed = speed

    def update(self, *args):
        self.rect.y += self.speed


class Background(GameSprite):
    """
        游戏背景精灵
    """
    def __init__(self, is_alt=False):
        super().__init__("Image/background.png")
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self, *args):
        super().update()
        # 增加新的方法：判断背景图片是否移出屏幕，是，把背景图片移动到屏幕上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """
        敌机精灵
    """
    count = 0

    def __init__(self):
        super().__init__("Image/enemy1.png")
        # 指定敌机的随机速度
        self.speed = random.randint(1, 8)
        # 制定敌机的随机位置
        self.rect.bottom = 0
        self.rect.x = random.randint(110, SCREEN_RECT.width - self.rect.width)

    def update(self, *args):
        super().update()
        # 敌机飞出屏幕后，删除敌机
        if self.rect.y > SCREEN_RECT.height:
            # kill 方法会将精灵从精灵组中移出，然后精灵就会被销毁
            self.kill()

    def __del__(self):
        Enemy.count += 1
        # print("我挂了 %d 次了" % Enemy.count)


class Hero(GameSprite):
    """
        英雄精灵
    """
    def __init__(self):
        super().__init__("Image/hero1.png", 0)

        # 英雄初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        # 创建子弹精灵组
        self.bullets = pygame.sprite.Group()

        # 爆炸图片列表
        self.bomb_image_list = []

    def update(self, *args):
        # 英雄水平移动
        # self.rect.x += self.speed
        # 英雄不能离开屏幕设置
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
        elif self.rect.bottom > SCREEN_RECT.bottom:
            self.rect.bottom = SCREEN_RECT.bottom
        elif self.rect.y < 0:
            self.rect.y = 0

    def fire(self):
        # 创建子弹精灵
        bullet = Bullet()
        # 设置子弹精灵的初始位置
        bullet.rect.bottom = self.rect.y
        bullet.rect.centerx = self.rect.centerx
        # 把子弹精灵添加到子弹精灵组中
        self.bullets.add(bullet)

    def bomb(self):
        # 创建爆炸图片列表
        for i in range(1, 4):
            im_path = "Image/hero_blowup_n" + str(1) + ".png"
            self.bomb_image_list.append(pygame.image.load(im_path))
        # 设置爆炸的初始位置


class Bullet(GameSprite):
    """
        子弹精灵
    """
    def __init__(self):
        super().__init__("Image/bullet1.png", -6)

    def update(self, *args):
        super().update()
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        # print("子弹被销毁...")
        pass
