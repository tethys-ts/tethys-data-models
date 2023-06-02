#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 09:04:18 2023

@author: mike
"""
from datetime import datetime, date
from typing import List, Optional, Union, Dict
from pydantic import BaseModel, Field
from enum import Enum
import orjson
from .utils import orjson_dumps
from .geometry import geometry
from . import base

#########################################
### Models


class Plan(BaseModel):
    """

    """
    plan_id: str
    plan_name: str
    commencement_date: date
    plan_authority: str































































