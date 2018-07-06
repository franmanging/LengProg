import ply.lex as lex
import re
import codecs
import os
import sys

tokens = ['ID', 'NUMBER', 'PLUS', 'MINUS', 'TIMES',
          'DIVIDE,', 'ODD', 'ASSIGN', 'NE', 'LT',
          'LTE', 'GT', 'GTE', 'LPARENT', 'RPARENT', 'COMMA',
          'SEMMICOLOM', 'DOT', 'UPDATE'
          ]

reservadas = {
    'begin' : 'BEGIN',
    'end' : 'END',
    'then' : 'THEN',
    'if' : 'IF',
    'while' : 'WHILE',
    'do' : 'DO',
    'call' : 'CALL',
    'const' : 'CONST',
    'int' : 'INT',
    'procedure' : 'PROCEDURE',
    'out' : 'OUT',
    'in' : 'INT',
    'else' : 'ELSE',
}


tokens = tokens+list(reservadas.values())

t_ignore = '\t'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'\\'
t_ODD = r'ODD'
t_ASSIGN = r'='
t_NE = r'<>'
t_LT = r'<'
t_LTE = r'<='
t_GT = r'>'
t_GTE = r'>='
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_COMMA = r','
t_SEMMICOLOM =  r';'
t_DOT = r'\.'
t_UPDATE = r':='

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.upper() in keywords:
        t.value = t.value.upper()
        t.type = t.value
    
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_COMMENT(t):
    r'\#.*'
    pass

def t_dec(t):
    r'[dec][(][a-z][)]*'
    t.value=t.value-1
    return t

def t_ifzero(t):
    r'[if(zero?][a-z][)]+'
    t.value=0
    t.value=int(t.value)
    return t

def t_ntrfactorial (t):
    r'[ntrfactorial][(][dec(][a-z][)][)]*'
    t.value=1
    t.value=int((* t (ntrfactorial (dec (t)))))
    return t
