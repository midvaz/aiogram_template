
from aiogram import Dispatcher

from abc import ABC, abstractmethod

class Handler(ABC):
    """Interface for any storage saving weather"""
    def __init__(self):
        pass
    @abstractmethod
    def regisetr_handlers(self, dp: Dispatcher) -> None:
        """Реализация метода регистрации хендлера"""
        pass