class Image():
    """Image is a list of values"""
    def __init__(self, xsize, ysize, zsize):
        self.val = [0 for i in range(xsize * ysize * zsize)]
        self.xsize = xsize
        self.ysize = ysize
        self.zsize = zsize

    def __repr__(self):
        img = ''

        if self.zsize == 1:
            for i, px in enumerate(self.val):
                if i % self.xsize == 0 and i != 0:
                    img += "\n"
                img += "%d   " % (self.val[i])
            img += "\n"
        img += "(%d, %d, %d)\n" % (self.xsize, self.ysize, self.zsize)
        img += "N: %d" % (self.n())
        return img

    def create_simple_image(self):
        self.val = [0, 0, 0, 0, 0, 0,
                    0, 1, 1, 1, 0, 0,
                    0, 1, 0, 1, 0, 0,
                    0, 1, 0, 1, 0, 0,
                    0, 1, 1, 1, 0, 0,
                    0, 0, 0, 0, 0, 0]
        self.zsize = 1
        self.xsize = 6
        self.ysize = 6

    @staticmethod
    def read_file(filename):
        with open(filename) as f:
            if next(f).strip() != 'P2':
                print 'Not a valid .pgm'
                return None
            else:
                w, h = [int(x) for x in next(f).split()]
                I = Image(w, h, 1)
                next(f)
                pos = 0
                for line in f:
                    for x in line.split():
                        I.val[pos] = int(x)
                        pos += 1
        return I

    def write_to_file(self, filename):
        img = ''
        Imax = int(max(self.val))

        img += "P2\n"
        img += "{} {}\n".format(self.xsize, self.ysize)
        img += "{}\n".format(Imax)

        for i in range(self.n()):
            img += "%d " % (self.val[i])
            if (((i+1)%17) == 0):
                img += "\n"

        with open(filename + ".pgm", 'w') as f:
            f.write(img)

    @staticmethod
    def create_complex_image(filename):
        return Image.read_file(filename)

    def valid_index(self, index):
        if index >= 0 and index < self.n():
            return True
        return False

    def assign(self, value):
        self.val = [value for i in range(self.n())]

    def x_coord(self, idx):
        return (idx % (self.xsize * self.ysize)) % self.xsize

    def y_coord(self, idx):
        return (idx % (self.xsize * self.ysize)) / self.xsize

    def z_coord(self, idx):
        return (idx / (self.xsize * self.ysize))

    def xyz_coord(self, idx):
        return (self.x_coord(idx), self.y_coord(idx), self.z_coord(idx))

    def n(self):
        return len(self.val)


if __name__ == "__main__":
    pass
