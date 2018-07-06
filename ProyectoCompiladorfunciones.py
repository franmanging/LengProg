import ply.lex as lex
import ply.yacc


tokens=['VARIABLE', 'CONSTANTE', 'NULL','INICIOFUNCION', 'ZERO','EMPTY','QUOT', 'DEC', 'IF',
'NUMERO', 'SUMA', 'RESTA', 'TIMES', 'DIVIDIR', 'IGUAL', 'DOBLEIGUAL', 
'MENOR', 'MAYOR', 'PARENTESISIZQ', 'PARENTESISDER','CORCHETEIZQ','CORCHETEDER']

t_ignore='\t'
t_SUMA=r'\+'
t_RESTA=r'-'
t_TIMES=r'\*'
t_DIVIDIR=r'/'
t_IGUAL=r'='
t_MENOR=r'\<'
t_MAYOR=r'\>'
t_PARENTESISIZQ=r'\('
t_PARENTESISDER=r'\)'
t_CORCHETEIZQ=r'\['
t_CORCHETEDER=r'\]'
t_INICIOFUNCION= r'^defn'
t_ZERO= r'^zero?'
t_EMPTY= r'^empty?'
t_QUOT= r'^quot'
t_DEC= r'^dec'
t_IF= r'^if'
t_DOBLEIGUAL= r'^=='

t_VARIABLE = r'$[a-zA-Z ][=]|[a-zA-Z_][a-zA-Z0-9_]*'



def t_CONSTANTE(t):
r'\d+'
t.value= int.(t.value)
t.value= float.(t.value)
t.value= str.(t.value)
return t

def t_NUMERO(t):
 r'\d+'
 t.value= int.(t.value)
 return t

 
 def t_NULL(t):
 r'\d+'
 t.value= str.(t.value)
 t='NULL'
 return t

 def t_saltolinea(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Caracter no válido '%s'" % t.value[0])
    t.lexer.skip(1)

lex.lex()

def p_parametro(p):
	'''parametrofuncion: CORCHETEIZQ VARIABLE CORCHETEDER
	| CORECHETEIZQ VARIABLE VARIABLE CORCHETEDER'''

def p_constente(p):
'''valor: CONSTANTE'''


def p_expresionfuncion(p):
	'''expresion: INICIOFUNCION VARIABLE parametrofuncion'''

def p_expresionesnombre(p):
	'''expresiones: ZERO valor
	| EMPTY VARIABLE
	| QUOT VARIABLE NUMERO
	| QUOT NUMERO NUMERO
	| QUOT valor valor
	| QUOT valor NUMERO'''



def p_operaciones(p):
	'''operacion: SUMA valor valor 
		| SUMA VARIABLE valor
		| SUMA VARIABLE VARIABLE
		| RESTA valor valor
		| RESTA VARIABLE valor
		| RESTA VARIABLE VARIABLE
		| TIMES valor valor
		| TIMES VARIABLE valor
		| TIMES VARIABLE VARIABLE
		| DIVIDIR valor valor
		| DIVIDIR VARIABLE valor
		| DIVIDIR VARIABLE VARIABLE
		| MENOR VARIABLE VARIABLE
		| MENOR VARIABLE valor
		| MENOR valor valor
		| MAYOR VARIABLE VARIABLE
		| MAYOR VARIABLE valor
		| MAYOR valor valor
		| EQUALS VARIABLE valor
		| EQUALS VARIABLE VARIABLE
		| DOBLEIGUAL VARIBALE VARIABLE
		| DOBLEIGUAL VARIABLE VALOR
		| DOBLEIGUAL VALOR VALOR'''




def p_funcionif(p):
	'''validarif: IF operacion
	| IF expresiones '''


def p_dec(p):
	'''decv: DEC valor'''

def p_parentesisdec(p):
	'''exp2: PARENTESISIZQ decv PARENTESISDER'''

def p_expresionrecursiva1(p):
	'''recursiva1: VARIABLE exp2'''

def p_expresionrecursivacompleta(p):
	'''recursiva2: TIMES valor recursiva1
	| recursiva2: SUMA valor recursiva1'''


def p_expresiontotal(p):
	'''exp: PARENTESISIZQ expresion PARENTESISDER
	| PARENTESISIZQ operacion PARENTESISDER
	| PARENTESISIZQ expresiones PARENTESISDER
	| PARENTESISIZQ validarif PARENTESISDER
	| PARENTESISIZQ recursiva1 PARENTESISDER
	| PARENTESISIZQ recursiva2 PARENTESISDER'''
