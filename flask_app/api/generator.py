from flask import session

from application import code_generator
from pandas_code.mapping import template_mapping
from pandas_code.parse_template import parse_template

generators = list()

def get_generator():
   if not 'generator' in session:
      session['generator'] = add_generator()
   return retrieve_generator(session['generator'])

def add_generator():
   generator = code_generator.CodeGenerator(template_mapping, parse_template)
   generators.append(generator)
   return(len(generators)-1)

def retrieve_generator(index):
   return generators[index]
