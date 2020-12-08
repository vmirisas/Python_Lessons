from abc import ABC, abstractmethod


class Resizable(ABC):
    @abstractmethod
    def resize(self, param):
        pass
