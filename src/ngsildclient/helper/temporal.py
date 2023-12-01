from __future__ import annotations
from ngsildclient.rest.rest import Rest
from ngsildclient import constants
from ngsildclient.helper import client_utils as u
from ngsildclient.helper.pd_series_conversion import PdSeriesConversion


class Temporal:
    """
    This class is to responsible to generate data for temporal APIs.
    """

    def __init__(self) -> None:
        pass

    @classmethod
    def temporal_create(
        cls,
        base_url: str,
        entity,
        context=False,
        ngsild_tenant=None,
        ngsild_path=None,
        **options
    ):
        """
        This method is responsible to push temporal data into Scorpio Broker
        """
        url = base_url+constants.NGSILD_TEMPORAL_ENDPOINT
        headers = u.add_header(context, ngsild_tenant, ngsild_path)
        return Rest.post(entity, url, headers)

    @classmethod
    def temporal_delete(
        cls,
        base_url,
        entity_id: str,
        context=False,
        ngsild_tenant=None,
        ngsild_path=None
    ):
        """
        This method is responsible to delete temporal data from Scorpio Broker
        """
        url = base_url+constants.NGSILD_TEMPORAL_ENDPOINT+"/"+entity_id
        headers = u.add_header(context, ngsild_tenant, ngsild_path)
        return Rest.delete(url, headers)

    @classmethod
    def series_to_pd_series(cls, temporal_dataset, index):
        """
        This function is used to convert the prediction temporal data set
        into Pandas series data set.
        @param temporal_dataset:prediction temporal data set
        @return:Pandas series data set
        """
        pd_series_obj = PdSeriesConversion(temporal_dataset, index)
        return pd_series_obj.get_pd_series()

    @classmethod
    def temporal_query(
            cls,
            base_url,
            param,
            ids: str = None,
            entity_type: str = None,
            context=False,
            ngsild_tenant=None,
            ngsild_path=None,
            pandas_series=False,
            attribute=None,
            index="observedAt"
    ):
        """
        This method is responsible for querying temporal data from Scorpio Broker
        """
        url_string = ""
        if ids is not None:
            url_string = u.tuple_to_string(ids)
            if url_string != "":
                url_string = "/" + url_string
        if entity_type is not None:
            param["type"] = entity_type
        if len(param) > 0:
            option_string = u.to_string(param)
            url_string = url_string+"?"+option_string
        if url_string == "":
            raise Exception("some parameter is missing")

        url = base_url+constants.NGSILD_TEMPORAL_ENDPOINT + url_string
        headers = u.add_header(context, ngsild_tenant, ngsild_path)
        historical_data = Rest.get(url, headers)
        if pandas_series is False:
            return historical_data
        return cls.get_pandas_series(historical_data, pandas_series, attribute, index)

    @classmethod
    def get_pandas_series(cls, historical_data, pandas_series, attribute, index):
        if index == None:
            index = "observedAt"
        if isinstance(historical_data, list):
            pandas_list = []
            for historical_data_ins in historical_data:
                if attribute in historical_data_ins:
                    result = cls.series_to_pd_series(
                        historical_data_ins[attribute], index)
                    pandas_list.append(result)
            return pandas_list
        return cls.series_to_pd_series(historical_data[attribute], index)
