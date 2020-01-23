# -*- coding: UTF-8 -*-
from utils.path import *
import os
import logging
from Model.DAL import DAL




class DAO() :

    __slots__ = [ "logger","registry", "params","query", "instance", "data_to_insert"]

    def __init__(self, connection_parameters, query=None):
        self.logger = logging.getLogger(__name__)
        self.params = connection_parameters
        self.query = query
        self.instance = None
        self.data_to_insert = None

    def exec(self, args):
        connector = DAL(self.params.get('INSTANCE'))
        if connector :
            if args :
                self.data_to_insert = args
            self.instance = connector.connect()
            action = getattr(self, self.params.get('ACTION'))
            action()



    def insert(self):
        for key, listvalues in self.data_to_insert.items() :
            for valuesDict in listvalues:
                ins_qry = "INSERT INTO {tablename} ({columns}) VALUES {values};".format(
                    tablename='stop_times',
                    columns=', '.join(valuesDict.keys()),
                    values=tuple(valuesDict.values())
                )
                self.instance.cursor.execute(ins_qry)

        self.instance.connection.commit()

    def insertGeo(self):
        for key, listvalues in self.data_to_insert.items() :
            for valuesDict in listvalues:

                ins_qry = "INSERT INTO {tablename} ({columns}) VALUES {values};".format(
                    tablename='stop_times',
                    columns=', '.join(valuesDict.keys()),
                    values=tuple(valuesDict.values())
                )
                self.instance.cursor.execute(ins_qry)

        self.instance.connection.commit()





