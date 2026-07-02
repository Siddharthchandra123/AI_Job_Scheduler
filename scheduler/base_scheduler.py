from abc import ABC, abstractmethod


class BaseScheduler(ABC):

    @abstractmethod
    def schedule(self):
        pass
