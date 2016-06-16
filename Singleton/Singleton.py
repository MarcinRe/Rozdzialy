class Singleton(object):
    _instance=None
    def __new__(self):
        if self._instance is None:
            self._instance = super(Singleton, self).__new__(self)
        return self._instance
    @staticmethod
    def getInstance():
        if Singleton._instance is None:
            s=Singleton()
        return Singleton._instance





