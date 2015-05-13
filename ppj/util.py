#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Modulo que contem classes e funções utilitarias"""
from datetime import date

def enum(**enums):
    """Simula um enum Java
    """
    return type('Enum', (), enums)

def formata_data(data_nascimento):
    """formata data de nascimento para o tipo date
    """
    result = data_nascimento
    if not isinstance(data_nascimento, date):
        data_split = data_nascimento.split('-')
        result = date(int(data_split[0]), int(data_split[1]), int(data_split[2]) )
        
    return result