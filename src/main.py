#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Enrique Plata

#from __init__ import DataLoader, TablesDataFrame, DDLsDataFrame
from utilities import dump_file_to_json, dump_file_to_pickle

# This can be delete later
from pandas import DataFrame
import pandas as pd

if __name__ == '__main__':

    # data_loader = DataLoader()

    # tables = TablesDataFrame(data_loader.get_all_tables())
    
    # ddls = DDLsDataFrame(data_loader.get_ddl_tables(tables.get_list_of_tables()))

    # ddls.clean_up_ddl_column()

    data = {'Product': ['Desktop Computer','Tablet','iPhone','Laptop'],
        'Price': [700,250,800,1200]
        }

    df = DataFrame(data, columns= ['Product', 'Price'])

    dump_file_to_pickle(df)

