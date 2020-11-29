#!/usr/bin/env python3
""" A simple flast app """
from flask import Flask

app = Flask(__name__)

from app import routes