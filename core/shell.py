#!/usr/bin/env python3
# coding=utf-8

"""
Copyright (c) 2019 ares developers (http://github.com/clownsonyou/ares)
See the file 'LICENSE' for copying permission
"""

from fancycmd import Cmd
import os
import json

from utils import log


class Shell(Cmd):
    def __init__(self):
        Cmd.__init__(self)
        with open("profile.json", "rt") as f:
            self.profile = json.loads(f.read())
        self.prompt = "shell > "

    def complete_help(self, *arg):
        pass

    def emptyline(self):
        pass
