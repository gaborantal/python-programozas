import fire


class Cake(object):
    def __init__(self, slices=10, flavour='chocolate'):
        self._slices = slices
        self._flavour = flavour

    def price(self):
        return self.slices * 390

    def like(self, favorite_flavour):
        f1 = set(self._flavour)
        f2 = set(favorite_flavour)
        res = f1 & f2
        return len(res) >= ((len(f1) + len(f2)) // 2)

    @property
    def slices(self):
        print('# Accessed to Cake#_slices via slices property')
        return self._slices

    @slices.setter
    def slices(self, new_slices):
        if new_slices > 0:
            print('# New number of slices is ok, updated')
            self._slices = new_slices
        else:
            print('# Cannot update number of slices, invalid value was', new_slices)

    def __str__(self):
        return '[Cake, slices=%d, flavour=%s]' % (self._slices, self._flavour)


if __name__ == '__main__':
    fire.Fire(Cake)
