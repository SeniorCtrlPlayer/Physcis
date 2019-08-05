import pygame
import sys
import math


class Game(object):
    # 定义几个颜色
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    # 定义河岸厚度
    thickness = 5
    BACKGROUND = (255, 255, 255)
    SIZE = (600, 300)
    # 坐标原点的位置和大小
    position = [0, 0, thickness, thickness]
    varphi = math.pi/2
    r0 = SIZE[1] - 100

    def __init__(self, rey=False):
        pygame.init()
        self.screen = pygame.display.set_mode(Game.SIZE)
        self.text = pygame.font.SysFont("宋体",24)
        self.clock = pygame.time.Clock()
        self.rey = rey
        self.varphi = math.pi/4
        pygame.display.set_caption("boat")

    def ybias(self, y):
        """
        将y坐标进行对称变换
        :param y: 左上角为坐标原点的y
        :return: 左下角为坐标原点的y
        """
        if self.rey:
            return self.SIZE[1] - y
        return y

    def polar_to_d(self, rho, varphi):
        """
        将极坐标转换成笛卡尔坐标
        :param rho: 极径
        :param varphi: 极角
        :return: x,y
        """
        x = rho * math.cos(varphi)
        y = rho * math.sin(varphi)
        return x, y

    def update(self, screen):
        self.varphi -= 0.001
        if self.varphi <= 0:
            self.varphi = math.pi/2
        # 轨迹方程
        self.r = self.r0 * (math.pow(math.tan(self.varphi/2)/math.tan(math.pi/8),2)
                  * math.sin(math.pi/4)/math.sin(self.varphi))

        x, y = self.polar_to_d(self.r, self.varphi)
        self.position[0] = x
        self.position[1] = y + 50

        # 将y坐标进行对称变换
        if self.rey:
            self.position[1] = self.ybias(self.position[1])
        pygame.draw.rect(screen, self.BLUE, self.position)

    def run(self, FPS=30):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill(Game.BACKGROUND)
            # 下部河岸
            pygame.draw.line(self.screen, self.RED, [0, self.ybias(48)], [self.SIZE[0], self.ybias(48)], self.thickness)
            # 上部河岸
            pygame.draw.line(self.screen, self.GREEN, [0, self.ybias(self.SIZE[1]-50)], [self.SIZE[0], self.ybias(self.SIZE[1] - 50)], self.thickness)
            # 绘制小船
            pygame.draw.rect(self.screen, self.BLACK, [0, self.ybias(50), self.thickness, self.thickness])
            self.update(self.screen)
            self.screen.blit(self.text.render("rho: {},varphi: {}".format(round(self.r,2), round(self.varphi,2)),1,(255,0,0)), (self.SIZE[0]-200, 25))
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game(True)
    game.run()
