#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import date

def enum(**enums):
    return type('Enum', (), enums)

def formata_data(data_nascimento):
    result = data_nascimento 
    if type(data_nascimento) is not date:
        data_split = data_nascimento.split('-')
        result = date(int(data_split[0]),int(data_split[1]),int(data_split[2]) )
        
    return result