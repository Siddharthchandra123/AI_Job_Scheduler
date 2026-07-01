"""
Base Generator for all synthetic generators.

Every generator should inherit from this class to provide
consistent logging, random seeding, validation and iteration.
"""

from abc import ABC, abstractmethod
from typing import List, Any
import random
import logging


logger = logging.getLogger(__name__)


class BaseGenerator(ABC):
    """
    Base class for all generators.
    """

    def __init__(self, seed: int | None = None):

        self.seed = seed

        if seed is not None:
            random.seed(seed)

    @abstractmethod
    def generate(self):
        """
        Generate a single object.
        """
        pass

    def generate_many(self, count: int) -> List[Any]:

        logger.info(
            "Generating %s objects using %s",
            count,
            self.__class__.__name__,
        )

        return [
            self.generate()
            for _ in range(count)
        ]
