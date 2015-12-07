import random


class Battleground:

    def __init__(self):
        self.fields = [[-1 for i in xrange(0, 10)] for j in xrange(0, 10)]
       

    def check_freedom(self, k, l):
        d = [(-1, 0), (-1, -1), (-1, 1), (0, -1), (0, 1), (1, 0), (1, 1), (1, -1)]

        if (k >= 0) and (k < 10) and (l >= 0) and (l < 10) and (self.fields[k][l] == -1):
            for i in xrange(0, 8):
                dx = k + d[i][0]
                dy = l + d[i][1]

                if (dx >= 0) and (dx < 10) and (dy >= 0) and (dy < 10) and (self.fields[dx][dy] > -1):
                    return False

            return True
        else:
            return False


    def generate_ships(self):
        for n in xrange(5, 0, -1):
            for m in xrange(0, 5-n):
                b = False

                while not b:
                    x = random.randrange(0, 10)
                    y = random.randrange(0, 10)

                    kx = random.randrange(0, 2)
                    ky = 0

                    if kx == 0:
                        ky = 1

                    b = True
                    for i in xrange(0, n):
                        if not self.check_freedom(x + kx * i, y + ky * i):
                            b = False

                    if b:
                        for i in xrange(0, n):
                            self.fields[x+kx*i][y+ky*i] = 0

        return self.fields

    def render(self):
        _table = '   a b c d e f g h j k\r\n'
        for i in xrange(0, 10):
            _row = '%2d ' % (i+1, )

            for j in xrange(0, 10):
                if self.fields[i][j] == 0:
                    _row += '+ '

                if self.fields[i][j] == -1:
                    _row += '- '

                if self.fields[i][j] == 2:
                    _row += '* '

            _table += '%s\r\n' % _row

        print _table
