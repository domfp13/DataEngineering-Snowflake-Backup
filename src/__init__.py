#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Enrique Plata

import pandas as pd
import snowflake.connector
from os import environ
import re

class AbstractClass:
    def values(self):
        return self.__dict__
    def __del__(self):
        pass

class DatabaseObject(AbstractClass):
    def __init__(self, table_name:str):
        self.table_name = table_name

class DDL(AbstractClass):
    def __init__(self, table_name, ddl_statement:str):
        self.table_name = table_name
        self.ddl_statement = ddl_statement

class TablesDataFrame:
    def __init__(self, list_database_objects:list):
        self.df = pd.DataFrame(list_database_objects)
    
    def get_list_of_tables(self):
        return self.df['table_name'].to_list()

class DDLsDataFrame:
    def __init__(self, list_ddl_objects:list):
        self.df = pd.DataFrame(list_ddl_objects)

    def clean_up_ddl_column(self)->None:
        self.df['ddl_statement'].replace(to_replace=[r"\\t|\\n|\\r", "\t|\n|\r"], value=[" "," "], regex=True, inplace=True)
    
    def get_list_of_ddls(self):
        return self.df['ddl_statement'].to_list()

class SnowflakeConn:
    def __init__(self):
        self.snowflake_accountname:str = environ.get('SNOWFLAKE_ACCOUNTNAME')
        self.snowflake_username:str = environ.get('SNOWFLAKE_USERNAME')
        self.snowflake_password:str = environ.get('SNOWFLAKE_PASSWORD')
        self.snowflake_dbname:str = environ.get('SNOWFLAKE_DBNAME')
        self.snowflake_warehousename:str = environ.get('SNOWFLAKE_WAREHOUSENAME')
        self.snowflake_rolename:str = environ.get('SNOWFLAKE_ROLENAME')
        self.snowflake_schemaname:str = environ.get('SNOWFLAKE_SCHEMANAME')
    
    def values(self):
        return self.__dict__

class DataLoader(SnowflakeConn):
    def __init__(self):
        super(DataLoader, self).__init__()
    
    def __get_data_from_db(self, query:str)->list:
        try:  
            conn = snowflake.connector.connect(
                account=self.snowflake_accountname,
                user=self.snowflake_username,
                password=self.snowflake_password,
                warehouse=self.snowflake_warehousename,
                database=self.snowflake_dbname,
                schema=self.snowflake_schemaname,
                role=self.snowflake_rolename
                )
            
            cursor = conn.cursor()
            cursor.execute(query)
            
            return cursor.fetchall()
        except Exception as e:
            print(e)
        finally:
            if conn:
                cursor.close()
                conn.close()

    def get_all_tables(self)->list:
        
        tables = self.__get_data_from_db(f"select table_name from information_schema.tables where table_schema = '{self.snowflake_schemaname}' AND table_type LIKE '%TABLE%'")
        
        return [DatabaseObject(table[0]).values() for table in tables]

    def get_ddl_tables(self, table_list:list)->list:
        
        ddl_list = []
        
        for table in table_list:
            ddl_list.append(self.__get_data_from_db(f"select '{table}', get_ddl('table', '{table}')")[0])

        return [DDL(ddl[0], ddl[1]).values() for ddl in ddl_list]
