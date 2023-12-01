from __future__ import annotations

from multipledispatch import dispatch
from ngsildclient import constants
from ngsildclient.exception import *
from typing import Union, Any
from ngsildclient.helper.client_entity import ClientEntity
from ngsildclient.helper.temporal import Temporal
from ngsildclient.helper.batch import Batch
from ngsildclient.entity import Entity as E


class Client:

    @dispatch(dict)
    def __init__(self, config):
        """
        Parameter
        ---------------------
        config : dict ----> it contain following two key
        ip : str    ---> NGSI-LD Broker IP
        PORT : str  ---> NGSI-LD Broker Port
        Example :
        ----------------------
        1- client = Client({"ip":"127.0.0.1", "port": "9090")
        2- client = Client({"ip":"127.0.0.1", "port": 9090)
        """
        ip = config.get(constants.NGSILD_IP, "")
        port = config.get(constants.NGSILD_PORT, "")
        if (ip == None) or (isinstance(ip, str) and ip.replace(" ", "") == ""):
            raise IPError("NGSI-LD Broker IP must be required")
        if (port == None) or (isinstance(port, str) and port.replace(" ", "") == ""):
            raise PortError("NGSI-LD Broker Port must be required")

        self.base_url = constants.HTTP_OBJECT + \
            config[constants.NGSILD_IP] + ":" + \
            str(config[constants.NGSILD_PORT])

    @dispatch(str, str)
    def __init__(self, ip: str = None, port: str = None):
        """
        Parameter
        ---------------------
        ip : str    ---> NGSI-LD Broker IP
        PORT : str  ---> NGSI-LD Broker Port

        Example :
        ----------------------
        client = Client("127.0.0.1", "9090")
        """
        self.__ip = ip
        self.__port = port
        self.__init__({constants.NGSILD_IP: self.__ip,
                      constants.NGSILD_PORT: self.__port})

    @dispatch(str, int)
    def __init__(self, ip: str = None, port: int = None):
        """
        Parameter
        ---------------------
        ip : str    ---> NGSI-LD Broker IP
        PORT : int  ---> NGSI-LD Broker Port

        Example :
        ----------------------
        client = Client("127.0.0.1", 9090)
        """
        self.__ip = ip
        self.__port = port
        self.__init__({constants.NGSILD_IP: self.__ip,
                      constants.NGSILD_PORT: self.__port})

    @dispatch(object, object)
    def __init__(self, id, type):
        raise NameError(
            "supported Type for IP is str and suppored type for port is either string or int")

    @dispatch(object)
    def __init__(self, ip):
        raise NameError(
            "To make connection with NGSILD-Broker IP and PORT both are required")

    def create(
        self,
        entity,
        entityID=None,
        context: bool = False,
        NGSILD_Tenant: str = None,
        NGSILD_Path: str = None,
        *options
    ):
        """
        Description
        -----------------------------
        This function is responsible to create normal entity and append attribute into existing entity.

        parameter
        -----------------------------
        entity:Mandatory               ----->  The entity to be saved in scorpio broker.
        entityID:Not mandatory         ----->  Entity Id is required if any attribute is to be added to existing entity.
        context:Not mandatory          ----->  It has two value True and False , True repersent the entity body have the
                                          The context itself and False repersent that there is no conetxt in the body
                                          The default value of conetxt is False.
        NGSILD_Tenant:Not Mandatory     -----> This is a multi-tenancy feature that allows different organizations.
        NGSILD_Path:Not mandatory       -----> NGSILD-Path is a feature of NGSI-LD architecture that sepcify subset of entity.

        Example
        -----------------------------------
        """
        return ClientEntity.create(self.base_url, entity, entityID, context=context, ngsild_tenant=NGSILD_Tenant, ngsild_path=NGSILD_Path)

    def partial_update(
        self,
        entity,
        entityID,
        attribute=None,
        context: bool = True,
        NGSILD_Tenant: str = None,
        NGSILD_Path: str = None,
        **options
    ):
        """
        Description
        ------------------------------
        This finction is responsible to update a NGSILD entity fully and partially

        Parameter:
        -------------------------------
        entity :Mandatory           ---> data to be update into Scorpio Broker.
        entityId:Mandatory          ----> This is id of entity to be updated.
        attribute : not Mandatroy   ---->  This parameter is required for partial update.
        context:Not mandatory       ----->  It has two value True and False , True repersent the entity body have the
                                          The context itself and False repersent that there is no conetxt in the body
                                          The default value of conetxt is False.
        NGSILD_Tenant:Not Mandatory  -----> This is a multi-tenancy feature that allows different organizations.
        NGSILD_Path:Not mandatory    -----> NGSILD-Path is a feature of NGSI-LD architecture that sepcify subset of entity.
        """
        return ClientEntity.partial_update(self.base_url, entity, entityID, attribute=attribute, context=context,
                                           ngsild_tenant=NGSILD_Tenant, ngsild_path=NGSILD_Path)

    def delete(
        self,
        entityId,
        context: bool = False,
        NGSILD_Tenant: str = None,
        NGSILD_Path: str = None,
        **options
    ):
        """
        Description
        ------------------------------
        This finction is responsible to delete existing entity based on entityId.

        Parameter:
        -------------------------------
        entityId:Mandatory          ----> Id of entity to be deleted.
        context:Not mandatory       -----> It has two value True and False , True repersent the entity body have the
                                          The context itself and False repersent that there is no conetxt in the body
                                          The default value of conetxt is False.
        NGSILD_Tenant:Not Mandatory  -----> This is a multi-tenancy feature that allows different organizations.
        NGSILD_Path:Not mandatory    -----> NGSILD-Path is a feature of NGSI-LD architecture that sepcify subset of entity.
        """
        return ClientEntity.delete(self.base_url, entityId, context=context, ngsild_tenant=NGSILD_Tenant, ngsild_path=NGSILD_Path)

    def query(
        self,
        entityids=None,
        context: bool = False,
        NGSILD_Tenant: str = None,
        NGSILD_Path: str = None,
        **param
    ):
        """
        Description
        ------------------------------
        This finction is responsible to query for entity from NGSI-LD Broker.

        Parameter:
        -------------------------------
        entityids        ----> List of ids.
        context:Not mandatory       -----> It has two value True and False , True repersent the entity body have the
                                          The context itself and False repersent that there is no conetxt in the body
                                          The default value of conetxt is False.
        NGSILD_Tenant:Not Mandatory  -----> This is a multi-tenancy feature that allows different organizations.

        NGSILD_Path:Not mandatory    -----> NGSILD-Path is a feature of NGSI-LD architecture that sepcify subset of entity.

        param : ----> contain other parameter(like type, limit , offset , attribute) for query.
        """
        json_obj = ClientEntity.query(
            self.base_url, entityids, param, context=context, ngsild_tenant=NGSILD_Tenant, ngsild_path=NGSILD_Path)
        if isinstance(json_obj, list):
            entity_object = []
            for entity in json_obj:
                entity_object.append(E(entity))
            return entity_object
        else:
            return [E(json_obj)]
        
    def temporal_create(
        self,
        entity,
        context: bool = False,
        NGSILD_Tenant: str = None,
        NGSILD_Path: str = None,
        *options
    ):
        """
        Description
        -----------------------------
        This function is responsible to create temporal entity using temporal api of NGSILD-Broker.

        parameter
        -----------------------------
        entity:Mandatory               ----->  The entity to be saved in scorpio broker using temporal API. 
        context:Not mandatory          ----->  It has two value True and False , True repersent the entity body have the
                                          The context itself and False repersent that there is no conetxt in the body
                                          The default value of conetxt is False.
        NGSILD_Tenant:Not Mandatory     -----> This is a multi-tenancy feature that allows different organizations.
        NGSILD_Path:Not mandatory       -----> NGSILD-Path is a feature of NGSI-LD architecture that sepcify subset of entity.

        Example
        -----------------------------------
        """
        return Temporal.temporal_create(self.base_url, entity, context=context, ngsild_tenant=NGSILD_Tenant,
                                        ngsild_path=NGSILD_Path)

    def temporal_delete(
        self,
        entityId,
        context: bool = False,
        NGSILD_Tenant: str = None,
        NGSILD_Path: str = None,
        **options
    ):
        """
        Description
        ------------------------------
        This finction is responsible to delete existing tempoarl entity based on entityId using temporal
        API of Scorpio Broker.

        Parameter:
        -------------------------------
        entityId:Mandatory          ----> Id of entity to be deleted.
        context:Not mandatory       -----> It has two value True and False , True repersent the entity body have the
                                          The context itself and False repersent that there is no conetxt in the body
                                          The default value of conetxt is False.
        NGSILD_Tenant:Not Mandatory  -----> This is a multi-tenancy feature that allows different organizations.
        NGSILD_Path:Not mandatory    -----> NGSILD-Path is a feature of NGSI-LD architecture that sepcify subset of entity.
        """
        return Temporal.temporal_delete(self.base_url, entityId, context=context, ngsild_tenant=NGSILD_Tenant, ngsild_path=NGSILD_Path)

    def get_temporal(
        self,
        entityID=None,
        entityType=None,
        pandasSeries=False,
        attribute=None,
        index=None,
        context: bool = False,
        NGSILD_Tenant: str = None,
        NGSILD_Path: str = None,
        **options,
    ):
        if pandasSeries == True and attribute == None:
            raise Exception("attribute parameter is importent")

        if entityID == None and entityType == None:
            raise Exception("Id or Type must be required")

        return Temporal.temporal_query(self.base_url, options, ids=entityID, entity_type=entityType, pandas_series=pandasSeries, attribute=attribute, index=index, context=context, ngsild_tenant=NGSILD_Tenant, ngsild_path=NGSILD_Path)

    def batch_create(
        self,
        entity,
        context: bool = False,
        NGSILD_Tenant: str = None,
        NGSILD_Path: str = None,
        **options
    ):
        """
        Description
        -----------------------------
        This function is responsible to create batch entity using batch api of NGSILD-Broker.

        parameter
        -----------------------------
        entity:Mandatory               ----->  The entity to be saved in scorpio broker using batch API. 
        context:Not mandatory          ----->  It has two value True and False , True repersent the entity body have the
                                          The context itself and False repersent that there is no conetxt in the body
                                          The default value of conetxt is False.
        NGSILD_Tenant:Not Mandatory     -----> This is a multi-tenancy feature that allows different organizations.
        NGSILD_Path:Not mandatory       -----> NGSILD-Path is a feature of NGSI-LD architecture that sepcify subset of entity.

        Example
        -----------------------------------
        """
        return Batch.batch_create(self.base_url, entity, context=context, ngsild_tenant=NGSILD_Tenant, ngsild_path=NGSILD_Path)

    def batch_upsert(
        self,
        entity,
        context: bool = False,
        NGSILD_Tenant: str = None,
        NGSILD_Path: str = None,
        **options
    ):
        """
        Description
        -----------------------------
        This function is responsible to create batch entity using batch upsert api of NGSILD-Broker.
        The upsert API of NGSILD-Broker can create the entity if entity does not exist into NGSILD-Broker

        parameter
        -----------------------------
        entity:Mandatory               ----->  The entity to be saved in scorpio broker using upsert batch API. 
        context:Not mandatory          ----->  It has two value True and False , True repersent the entity body have the
                                          The context itself and False repersent that there is no conetxt in the body
                                          The default value of conetxt is False.
        NGSILD_Tenant:Not Mandatory     -----> This is a multi-tenancy feature that allows different organizations.
        NGSILD_Path:Not mandatory       -----> NGSILD-Path is a feature of NGSI-LD architecture that sepcify subset of entity.

        Example
        -----------------------------------
        """
        return Batch.batch_upsert(self.base_url, entity, context=context, ngsild_tenant=NGSILD_Tenant, ngsild_path=NGSILD_Path)

    def batch_update(
        self,
        entity,
        context: bool = False,
        NGSILD_Tenant: str = None,
        NGSILD_Path: str = None,
        **options
    ):
        """
        Description
        -----------------------------
        This function is responsible to update batch entity using batch api of NGSILD-Broker. 
        This API can update only existing entity into NGSILD-Brokert.

        parameter
        -----------------------------
        entity:Mandatory               ----->  The entity to be update in NGSILD Broker using batch API. 
        context:Not mandatory          ----->  It has two value True and False , True represent the entity body have the
                                         The context itself and False represent that there is no conetxt in the body
                                         The default value of conetxt is False.
        NGSILD_Tenant:Not Mandatory     -----> This is a multi-tenancy feature that allows different organizations.
        NGSILD_Path:Not mandatory       -----> NGSILD-Path is a feature of NGSI-LD architecture that sepcify subset of entity.

        Example
        -----------------------------------
        """
        return Batch.batch_update(self.base_url, entity, context=context, ngsild_tenant=NGSILD_Tenant, ngsild_path=NGSILD_Path)

    def batch_delete(
            self,
            entity,
            context: bool = False,
            NGSILD_Tenant: str = None,
            NGSILD_Path: str = None,
            **options
    ):
        """
        Description
        ------------------------------
        This finction is responsible to delete existing entity based on entityIds using batch
        API of Scorpio Broker.

        Parameter:
        -------------------------------
        entity:Mandatory            ----> list of Ids of existing entity to be deleted.
        context:Not mandatory       -----> It has two value True and False , True repersent the entity body have the
                                          The context itself and False repersent that there is no conetxt in the body
                                          The default value of conetxt is False.
        NGSILD_Tenant:Not Mandatory  -----> This is a multi-tenancy feature that allows different organizations.
        NGSILD_Path:Not mandatory    -----> NGSILD-Path is a feature of NGSI-LD architecture that sepcify subset of entity.
        """
        return Batch.batch_delete(self.base_url, entity, context=context, ngsild_tenant=NGSILD_Tenant, ngsild_path=NGSILD_Path)
