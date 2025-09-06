#entlib
# Licensed under the GPL 2.0 license

import colorama
class Logs():
    '''Logging functions'''
    def info(text):
        print(colorama.Fore.GREEN+text+colorama.Fore.RESET)
    def error(text):
        print(colorama.Fore.RED+text+colorama.Fore.RESET)
    def warning(text):
        print(colorama.Fore.YELLOW+text+colorama.Fore.RESET)