from flask import session

from application import code_generator
from pandas_code.mapping import template_mapping
from pandas_code.parse_template import parse_template

# this is kind of a dirty hack
# there is one generator per client session
# we keep all generators in a list
# this is not thread safe and needs to be fixed

generators = []

def get_generator():
   if 'generator' not in session:
      session['generator'] = add_generator()
   return retrieve_generator(session['generator'])

def add_generator():
   generator = code_generator.CodeGenerator(template_mapping, parse_template)
   generators.append(generator)
   return len(generators)-1

def retrieve_generator(index):
   return generators[index]
