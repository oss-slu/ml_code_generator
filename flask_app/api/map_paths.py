from flask import render_template

next_actions = dict()
next_actions['upload'] = [('describe', 'actions/describe_data.html'), ('clean', 'actions/clean_data.html')]