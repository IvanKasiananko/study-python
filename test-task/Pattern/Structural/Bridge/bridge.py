class SortAbstraction:

    def sortImpl(self, sortImpl):
        self._sortImpl = sortImpl

    def sort(self, data):
        self._sortImpl.sort(data)
        return data


class SortImpl:

    def sort(self, data):
        pass



class SlowSortImpl(SortImpl):

    def sort(self, data):
        return data.sort()  # якобы медленная сортировка


class FastSortImpl(SortImpl):

    def sort(self, data):
        return data.sort()  # якобы быстрая сортировка


if __name__ == '__main__':
    abstraction = SortAbstraction()
    abstraction.sortImpl(SlowSortImpl())
    print(abstraction.sort([2, 1, 3]))

    abstraction.sortImpl(FastSortImpl())
    print(abstraction.sort([2, 1, 3]))
