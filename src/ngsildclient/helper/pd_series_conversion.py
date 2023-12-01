"""
converts time-series data into pandas series
"""
import pandas as pd
import numpy as np
from ngsildclient import constants


class PdSeriesConversion:
    """
    This class is to convert temporal data into Pandas series conversion
    """

    def __init__(self, payload_attribute, index):
        """
        This function is used to create an object for prediction attribute.
        @param payload_attribute: payload_attribute
        """
        self.payload_attribute = payload_attribute
        self.index = index

    def _get_series_data(self):
        """
        This function is used to get converted Pandas series data.
        @return:converted Pandas series data
        """
        return pd.DataFrame(self.payload_attribute)

    def _pd_datetime(self):
        """
        This function is used to get datetime for Pandas series data.
        @return:datetime
        """
        series_data = self._get_series_data()
        if series_data is None and self.index not in series_data:
            raise Exception("Time-Series attribute is not exist")
        return pd.to_datetime(series_data[self.index])

    def _get_value(self):
        """
        This function is used to get values from series data.
        @return:values
        """
        return self._get_series_data().get(constants.VALUE, None)

    def _dataset_value_list(self):
        """
        This function is used to get values list in numPy from series data.
        @return:values list
        """
        return np.array(self._get_value())

    def get_pd_series(self):
        """
        This function is used to get Pandas series data
        @return:Pandas series data
        """
        return pd.Series(self._dataset_value_list(), index=self._pd_datetime(), dtype=float)
