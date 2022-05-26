from random import randint


class _Support:
    def __init__(self):
        self.link = 'Нет ссылки('

    def support(self):
        return 'Техническая поддержка: ' + self.link


class _ArseniySupport(_Support):
    def __init__(self):
        self.link = '@theorly'

    def support(self):
        return f'Привет, я {self.link}, я знаю квадраты чисел {[x**2 for x in range(4)]}.'


class _MaximSupport(_Support):
    def __init__(self):
        self.link = '@maxon4444ik'

    def support(self):
        return f'Привет, я {self.link}, я сделал форк.'

supports = [_MaximSupport(), _ArseniySupport()]
