class Observable(object):

    def __init__(self):
        self.__observations = {}

    def subscribe(self, subject, observer):
        if not subject in self.__observations:
            self.__observations[subject] = [observer]
        elif observer not in self.__observations[subject]:
            self.__observations[subject].append(observer)

    def _notify(self, subject):
        if subject in self.__observations:
            observers = self.__observations[subject]
            for observer in observers:
                observer.Notify(subject, self)