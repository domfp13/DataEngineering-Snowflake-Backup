#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Enrique Plata

import pandas as pd
from pandas import DataFrame
import os, contextlib, json
from pathlib import Path

@contextlib.contextmanager
def this_directory(path:str):
    """Change working directroy to the path(within the src) specified. Then change back to original path.

    Args:
        path (str): Path to move to
    """

    original_workdir = os.getcwd()    
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(original_workdir)

def dump_file_to_pickle(df:DataFrame):
    with this_directory(path=Path('..','data')):
        df.to_pickle('data.pkl')

def dump_file_to_json(df:DataFrame):
    with this_directory(path=Path('..','data')):
        df.to_json('ddls.json', orient="table")
