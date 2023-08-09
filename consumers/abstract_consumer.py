import abc
import pandas as pd


class AbstractConsumer(abc.ABC):
    @abc.abstractmethod
    def get(self, **options) -> pd.DataFrame:
        """
        Abstract method that receive some options and return a pandas dataframe as the implementation.
        Returns:
            df (pd.Dataframe): dataframa with the consumed data
        """
        pass
