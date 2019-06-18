#!/usr/bin/env python3
# coding=utf-8

"""
Copyright (c) 2019 ares developers (http://github.com/clownsonyou/ares)
See the file 'LICENSE' for copying permission
"""

from fancycmd.data_types import *


class Log:
    def __init__(self, profile):
        self.logger = open("debug.log", "a+")
        self.profile = profile

    def fire(self, s):
        self.logger.write("[fire] {}\n".format(s))
        if self.profile["use_emojies"]:
            print("🔥 {}".format(s))
        else:
            print("[FIRE] {}".format(s))

    def thinking(self, s):
        self.logger.write("[thinking] {}\n".format(s))
        if self.profile["use_emojies"]:
            print("🤔 {}".format(s))
        else:
            print("[THINKING] {}".format(s))

    def nerd(self, s):
        self.logger.write("[nerd] {}\n".format(s))
        if self.profile["use_emojies"]:
            print("🤓 {}".format(s))
        else:
            print("[NERD] {}".format(s))

    def status(self, s):
        self.logger.write("[*] {}\n".format(s))
        print("[{}] {}".format("*", s))

    def success(self, s):
        self.logger.write("[+] {}\n".format(s))
        print("[{}] {}".format("+", s))

    def error(self, s):
        self.logger.write("[-] {}\n".format(s))
        print("[{}] {}".format("-", s))

    def warning(self, s):
        self.logger.write("[!] {}\n".format(s))
        print("[{}] {}".format("!", s))
