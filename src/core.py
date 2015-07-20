#!/usr/bin/env python
################################
# Core functions for PTF
################################
import os
import subprocess
import select

# color scheme for core
class bcolors:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERL = '\033[4m'
    ENDC = '\033[0m'
    backBlack = '\033[40m'
    backRed = '\033[41m'
    backGreen = '\033[42m'
    backYellow = '\033[43m'
    backBlue = '\033[44m'
    backMagenta = '\033[45m'
    backCyan = '\033[46m'
    backWhite = '\033[47m'

# get the main SET path
def definepath():
    if os.path.isfile("ptf"):
        return os.getcwd()

    else:
        if os.path.isdir("/usr/share/ptf/"):
                return "/usr/share/ptf/"
        else:
                return os.getcwd()

# main status calls for print functions
def print_status(message):
    print bcolors.GREEN + bcolors.BOLD + "[*] " + bcolors.ENDC + str(message)

def print_info(message):
    print bcolors.BLUE + bcolors.BOLD + "[-] " + bcolors.ENDC + str(message)

def print_info_spaces(message):
    print bcolors.BLUE + bcolors.BOLD + "  [-] " + bcolors.ENDC + str(message)

def print_warning(message):
    print bcolors.YELLOW + bcolors.BOLD + "[!] " + bcolors.ENDC + str(message)

def print_error(message):
    print bcolors.RED + bcolors.BOLD + "[!] " + bcolors.ENDC + bcolors.RED + str(message) + bcolors.ENDC

# count all of the modules
def count_modules():
        modules_path = definepath() + "/modules/"
        counter = 0
        for path, subdirs, files in os.walk(modules_path):
                for name in files:
                        filename = os.path.join(path, name)
                        if not "__init__.py" in filename:
                                counter = counter + 1
        return counter

# version information
grab_version = "0.8"

# banner
banner = bcolors.RED + r"""

                     ______  __ __    ___                                   
                    |      T|  T  T  /  _]                                  
                    |      ||  l  | /  [_                                   
                    l_j  l_j|  _  |Y    _]                                  
                      |  |  |  |  ||   [_                                   
                      |  |  |  |  ||     T                                  
                      l__j  l__j__jl_____j                                  
                                                                            
 ____     ___  ____   ______    ___   _____ ______    ___  ____    _____    
|    \   /  _]|    \ |      T  /  _] / ___/|      T  /  _]|    \  / ___/    
|  o  ) /  [_ |  _  Y|      | /  [_ (   \_ |      | /  [_ |  D  )(   \_     
|   _/ Y    _]|  |  |l_j  l_jY    _] \__  Tl_j  l_jY    _]|    /  \__  T    
|  |   |   [_ |  |  |  |  |  |   [_  /  \ |  |  |  |   [_ |    \  /  \ |    
|  |   |     T|  |  |  |  |  |     T \    |  |  |  |     T|  .  Y \    |    
l__j   l_____jl__j__j  l__j  l_____j  \___j  l__j  l_____jl__j\_j  \___j    
                                                                            
 _____  ____    ____  ___ ___    ___  __    __   ___   ____   __  _         
|     ||    \  /    T|   T   T  /  _]|  T__T  T /   \ |    \ |  l/ ]        
|   __j|  D  )Y  o  || _   _ | /  [_ |  |  |  |Y     Y|  D  )|  ' /         
|  l_  |    / |     ||  \_/  |Y    _]|  |  |  ||  O  ||    / |    \         
|   _] |    \ |  _  ||   |   ||   [_ l  `  '  !|     ||    \ |     Y        
|  T   |  .  Y|  |  ||   |   ||     T \      / l     !|  .  Y|  .  |        
l__j   l__j\_jl__j__jl___j___jl_____j  \_/\_/   \___/ l__j\_jl__j\_j    
"""

banner += bcolors.ENDC + """
		     The"""
banner += bcolors.BOLD + """ PenTesters """
banner += bcolors.ENDC + """Framework\n\n"""

banner += """        		  """ + bcolors.backBlue + """Version: %s""" % (grab_version) + bcolors.ENDC + "\n"

banner += bcolors.YELLOW + bcolors.BOLD + """		     Codename: """ + bcolors.BLUE + """GitDatShiny""" + "\n"

banner += """			""" + bcolors.ENDC + bcolors.backRed + """Red Team Approved""" + bcolors.ENDC + "\n"

banner += """        	     A project by """ + bcolors.GREEN + bcolors.BOLD + """Trusted""" + bcolors.ENDC + bcolors.BOLD + """Sec""" + bcolors.ENDC + "\n"

banner += """		 Written by: """ + bcolors.BOLD + """Dave Kennedy (ReL1K)""" + bcolors.ENDC + "\n"
banner += """		Twitter: """ + bcolors.BOLD + """@HackingDave, @TrustedSec""" + bcolors.ENDC + "\n"
banner += """                  """ + bcolors.BOLD + """https://www.trustedsec.com
        """ + bcolors.ENDC
banner += bcolors.BOLD + """\n              The easy way to get the new and shiny.
""" + bcolors.ENDC + "\n"
banner += "             Total module/tool count within PTF: " + bcolors.BOLD + str(count_modules()) + bcolors.ENDC + "\n" 

# check the config file and return value
def check_config(param):
    fileopen = file("%s/config/ptf.config" % (definepath()), "r")
    for line in fileopen:
        # if the line starts with the param we want then we are set, otherwise if it starts with a # then ignore
        if line.startswith(param) != "#":
            if line.startswith(param):
                line = line.rstrip()
                # remove any quotes or single quotes
                line = line.replace('"', "")
                line = line.replace("'", "")
                line = line.split("=")
                return line[1]

# parser module for module and term
def module_parser(filename, term):

    # if the file exists
    if os.path.isfile(filename):

        # set a base counter
        counter = 0

        # open the file
        fileopen = file(filename)
        # iterate through the file
        for line in fileopen:
            # strip any bogus stuff
            line = line.rstrip()
            # if the line starts with the term
            if line.startswith(term):
                line = line.replace(term + "=", "")
                line = line.replace('"', "", 2)
                # reflect we hit this and our search term was found
                counter = 1
                return line

        # if there was no search term identified for the module
        if counter == 0:
            filename_short = filename.replace(definepath() + "/", "")
            filename_short = filename_short.replace(".py", "")
            print_error("Warning, module %s was found but contains no %s field." % (filename_short,term))
            print_error("Check the module again for errors and try again.")
            print_error("Module has been removed from the list.")
            return None

    # if the file isn't there
    if not os.path.isfile(filename):
        return None

# help menu for PTF
def show_help_menu():
    print "Available from main prompt: " + bcolors.BOLD + "show modules" + bcolors.ENDC + "," + bcolors.BOLD + " show <module>" + bcolors.ENDC + "," + bcolors.BOLD + " search <name>" + bcolors.ENDC + "," + bcolors.BOLD + " use <module>" + bcolors.ENDC
    print "Inside modules:" + bcolors.BOLD + " show options" + bcolors.ENDC + "," + bcolors.BOLD + " set <option>" + bcolors.ENDC + "," + bcolors.BOLD + "run" + bcolors.ENDC
    print "Additional commands: " + bcolors.BOLD + "back" + bcolors.ENDC+ "," + bcolors.BOLD + " help" + bcolors.ENDC + "," + bcolors.BOLD + " ?" + bcolors.ENDC + "," + bcolors.BOLD + " exit" + bcolors.ENDC + "," + bcolors.BOLD + " quit" + bcolors.ENDC
    print "Update or Install: "+ bcolors.BOLD + "update" + bcolors.ENDC + "," + bcolors.BOLD + " upgrade" + bcolors.ENDC + "," + bcolors.BOLD + " install" + bcolors.ENDC

# exit message for PTF
def exit_ptf():
    print_status("Exiting PTF - the easy pentest platform creation framework.")


# this is the main handler to check what distribution we are using
# if it can't find it, will default to manual install base
def profile_os():
    # if we are running a debian variant
    if os.path.isfile("/etc/apt/sources.list"):
        return "DEBIAN"

    # will add support for more operating systems later

    # else use custom
    else:
        return "CUSTOM"


# standard log write out
def logging(log):
    # grab the log path
    logpath = check_config("LOG_PATH=")
    # if the file isn't there, create it
    if not os.path.isfile(logpath):
        filewrite = file(logpath, "w")
        filewrite.write("")
        filewrite.close()
    # open for append
    filewrite = file(logpath, "a")
    # write it out
    filewrite.write(log)
    # close the file
    filewrite.close()

# this will install all the proper locations for 
def prep_install():
    if not os.path.isfile(os.getenv("HOME") + "/.ptf"):
        print_status("This appears to be your first time using PTF.")
        print_status("Creating output directory to: " + os.getenv("HOME") + "/.ptf")
        os.makedirs(os.getenv("HOME") + "/.ptf")

def home_directory():
         return os.getenv("HOME") + "/.ptf"

# get tab completion to work
class Completer:
    def __init__(self, words):
        self.words = words
        self.prefix = None
    def complete(self, prefix, index):
        if prefix != self.prefix:
	    # start and find with prefix
            self.matching_words = [
                w for w in self.words if w.startswith(prefix)
                ]
            self.prefix = prefix
        try:
            return self.matching_words[index]
        except IndexError:
            return None

import readline
# our known tab list
base_list = ["?", "help", "run", "show modules", "show options", "set", "install", "upgrade", "use", "use modules"]
# dynamically generate modules
module_files = []
for dirpath, subdirs, files in os.walk("modules/"):
    for x in files:
        if x.endswith(".py"):
            if not "__init__.py" in x:
		    x = x.replace(".py", "")
                    module_files.append("use " + os.path.join(dirpath, x))
words = base_list + module_files


completer = Completer(words)
readline.parse_and_bind("tab: complete")
readline.set_completer(completer.complete)

# this will run commands after an install or update on a module
def after_commands(filename,install_location):
	from src.commands import after_commands
	commands = module_parser(filename, "AFTER_COMMANDS")
	if commands != "":
		# here we check if install location needs to be added
		if "{INSTALL_LOCATION}" in commands:
			commands = commands.replace("{INSTALL_LOCATION}", install_location)
		print_status("Running after commands for post installation requirements.")
		after_commands(commands)
		print_status("Completed running after commands routine..")


