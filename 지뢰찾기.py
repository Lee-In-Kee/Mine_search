import random

CELL_MINE = '●'
CELL_COVER = '□'
CELL_EMPTY = 'X'
WIDTH = 8
HEIGHT = 10
NUM_MINE = 10
SURROUND = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]


class MineSearch:
    def __init__(self):
        self.row = [[CELL_COVER for i in range(WIDTH)] for j in range(HEIGHT)]
        self.visual = [[CELL_COVER for i in range(WIDTH)] for j in range(HEIGHT)]
        self.rn = []

    def print_result(self,visual):
        #최종 출력
        for i in range(HEIGHT):
            print(' '.join(visual[i]), i)
        print('0 1 2 3 4 5 6 7 !')

    # 지뢰 생성
    def position_mine(self):
        keep = []
        keep.append(random.randrange(HEIGHT))
        keep.append(random.randrange(WIDTH))
        self.rn.append(keep)
        cnt = 1
        while cnt < NUM_MINE:
            cnt += 1
            while keep in self.rn:
                keep = []
                keep.append(random.randrange(HEIGHT))
                keep.append(random.randrange(WIDTH))
            self.rn.append(keep)
    
    # 숫자 정보
    def generate_number(self):
        self.position_mine()
        for i in self.rn:
            self.row[i[0]][i[1]] = CELL_MINE
        
        for j in range(HEIGHT):
            for i in range(WIDTH):
                cnt = 0
                for k in SURROUND:
                    if k[0] + j >= 0 and k[0] + j < HEIGHT and k[1] + i >= 0 and k[1] + i < WIDTH and self.row[j][i] != CELL_MINE:
                        if self.row[k[0] + j][k[1] + i] == CELL_MINE:
                            cnt += 1
                if cnt != 0:
                    self.row[j][i] = str(cnt)
                elif cnt == 0 and self.row[j][i] != CELL_MINE:
                    self.row[j][i] = CELL_EMPTY
        return self.row

    def play(self):
        self.generate_number()

        # 첫 화면
        self.print_result(self.visual)

        while True:
            while True:
                while True:
                    x = input('x: ')
                    if x != '' and int(x) >= 0 and int(x) < WIDTH:
                        x = int(x)
                        break
                while True:
                    y = input('y: ')
                    if y != '' and int(y) >= 0 and int(y) < HEIGHT:
                        y = int(y)
                        break       
                if self.visual[y][x] == CELL_COVER or self.visual[y][x] == CELL_EMPTY:
                    break
            
            # 실패조건
            if self.row[y][x] == CELL_MINE:
                self.visual[y][x] = self.row[y][x]
                self.print_result(self.visual)
                print('Fail')
                self.print_result(self.row)
                break
            
            # 출력
            elif self.row[y][x] == CELL_EMPTY:
                self.visual[y][x] = self.row[y][x]
                for k in SURROUND:
                    if k[0] + y >= 0 and k[0] + y < HEIGHT and k[1] + x >= 0 and k[1] + x < WIDTH:
                        self.visual[k[0] + y][k[1] + x] = self.row[k[0] + y][k[1] + x]
                self.print_result(self.visual)

            else :
                self.visual[y][x] = self.row[y][x]
                self.print_result(self.visual)

            # Clear
            num = 0
            for i in self.visual:
                num += i.count(CELL_COVER)
            if num == NUM_MINE:
                print('Clear')
                
new_game = MineSearch()
new_game.play()
