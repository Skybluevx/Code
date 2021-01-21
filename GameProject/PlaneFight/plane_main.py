import pygame
from plane_sprites import *

from plane_sprites import Background, SCREEN_RECT, CREATE_ENEMY_EVENT, FRAME_PER_SEC, HERO_FIRE_EVENT, \
    Enemy, Hero, CREATE_ENEMY_TIME, FIRE_TIME


class PlaneGame(object):
    """
        飞机大战游戏
    """

    def __init__(self):
        print("游戏初始化！")
        # 设置游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 创建游戏时钟
        self.clock = pygame.time.Clock()
        # 通过私有方法，创建精灵
        self.__create_sprites()
        # 设置定时器 -> 创建敌机, 发射子弹
        pygame.time.set_timer(CREATE_ENEMY_EVENT, CREATE_ENEMY_TIME)
        pygame.time.set_timer(HERO_FIRE_EVENT, FIRE_TIME)

    def __create_sprites(self):
        # 创建背景精灵和精灵组
        bg1 = Background()
        bg2 = Background(True)

        self.black_group = pygame.sprite.Group(bg1, bg2)

        # 创建敌机精灵组
        self.enemy_group = pygame.sprite.Group()

        # 创建英雄精灵和精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print("游戏开始啦...")
        while True:
            # 1.设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 2.监听事件
            self.__event_handler()
            # 3.碰撞检测
            self.__check_collide()
            # 4.更新/绘制精灵组
            self.__update_sprites()
            # 5.更新屏幕显示
            pygame.display.update()

    def __event_handler(self):
        for event in pygame.event.get():

            # 游戏退出
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            # 创建敌机
            elif event.type == CREATE_ENEMY_EVENT:
                # print("敌机出场。。。")
                # 创建敌机精灵
                enemy = Enemy()

                # 把敌机精灵添加到敌机精灵组中
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("向右移动...")

        # 使用提供的方法监听键盘
        keys_pressd = pygame.key.get_pressed()
        # 判断元组中对应的索引值 - 1
        # if keys_pressd[pygame.K_RIGHT]:
        #     # print("向右移动...")
        #     self.hero.speed = 4
        # elif keys_pressd[pygame.K_LEFT]:
        #     self.hero.speed = -4
        # else:
        #     self.hero.speed = 0

        # 改进：上下左右移动
        if keys_pressd[pygame.K_LEFT] or keys_pressd[pygame.K_RIGHT] or \
                keys_pressd[pygame.K_UP] or keys_pressd[pygame.K_DOWN]:
            self.hero.speed = 4
            if keys_pressd[pygame.K_RIGHT]:
                self.hero.rect.x += self.hero.speed
            elif keys_pressd[pygame.K_LEFT]:
                self.hero.rect.x -= self.hero.speed
            elif keys_pressd[pygame.K_UP]:
                self.hero.rect.y -= self.hero.speed
            elif keys_pressd[pygame.K_DOWN]:
                self.hero.rect.y += self.hero.speed
        else:
            self.hero.speed = 0

    def __check_collide(self):
        # 子弹摧毁敌机
        pygame.sprite.groupcollide(
            self.hero.bullets, self.enemy_group, True, True)
        # 敌机摧毁英雄
        enemies = pygame.sprite.spritecollide(
            self.hero, self.enemy_group, True)
        if len(enemies) > 0:
            # print(enemies)
            self.hero.kill()
            PlaneGame.__game_over()
        # 无敌状态
        # pygame.sprite.groupcollide(
        #     self.hero_group, self.enemy_group, False, True)

    def __update_sprites(self):
        self.black_group.update()
        self.black_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        print("游戏结束啦...")

        pygame.quit()
        exit()


if __name__ == '__main__':
    # 创建游戏对象
    game = PlaneGame()
    # 开始游戏
    game.start_game()
