# /usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: ./test/main.py
# Virtual Env(comamnd line.) > "python -m venv [venv name]"
# install Flask > "pip install Flask"
# 
# Please Your Application Enviroment.
import os,sys,datetime
from flask import Flask, render_template, request, redirect

# Production Server variable: debug,port,host
debug=False # True or False
port=8080 # Your Envroment to change Port Number: [1024-65535]

# Loopback Address
# host="127.0.0.1" 

# Template File Path
tmpl_file="main.html" # Path: ./test/templates/main.html

# WebApp Title
page_title='Automatic Create WebApp'

# DB Name
dbname='None'

#Table Name
tbl=[]

# Flask Instanse
app=Flask(__name__)
        
# ======================================== routing start

@app.route('/')
def index():
        
    return render_template(
        tmpl_file, 
        title=page_title
    )

# routing end ==========================================
        
# ======================================== routing start

@app.route('/main')
def main():
        
    return render_template(
        tmpl_file, 
        title=page_title
    )

# routing end ==========================================
        
# ======================================== routing start

@app.route('/test')
def test():
        
    return render_template(
        tmpl_file, 
        title=page_title
    )

# routing end ==========================================


# run to app
# browser access <Your Host&Port>
if __name__=="__main__":
    app.run(debug=debug, port=port)
