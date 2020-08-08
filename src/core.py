#!/usr/bin/env python
# -*- coding: utf-8 -*-
################################
# Core functions for PTF
################################
import os
import subprocess
import select
import readline
import glob
import platform
import urllib.request
import sys

# Import PTF internal logging module
#from src.ptflogger import info, error, debug, log

# tab completion
def complete(text, state):
    a = (glob.glob(text + '*') + [None])[state].replace("__init__.py", "").replace(".py", "").replace("LICENSE", "").replace("README.md", "").replace("config", "").replace("ptf", "").replace("readme", "").replace("src", "").replace("         ", "").replace(".txt","") + "/"
    a = a.replace("//", "/")
    if os.path.isfile(a[:-1] + ".py") or os.path.isfile(a[:-1] + ".txt"): return a[:-1]
    else:
        return a

readline.set_completer_delims(' \t\n;')
readline.parse_and_bind("tab: complete")
readline.set_completer(complete)
# end tab completion

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

# custom parser for zaproxy
def zaproxy():
    if sys.version_info > (3,0):
        file = urllib.request.urlopen('https://raw.githubusercontent.com/zaproxy/zap-admin/master/ZapVersions.xml')
        data = file.readlines()
        file.close()
        for url in data:
            if b'Linux.tar.gz' in url and b'<url>' in url: return url.decode('utf-8').replace("<url>", "").replace("</url>", "").strip()
    else:
        file = urllib.urlopen('https://raw.githubusercontent.com/zaproxy/zap-admin/master/ZapVersions.xml')
        data = file.readlines()
        file.close()
        for url in data:
            if "Linux.tar.gz" in url and "<url>" in url: return url.rstrip().replace("<url>", "").replace("</url>", "").strip()


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
    print((bcolors.GREEN) + (bcolors.BOLD) + \
        ("[*] ") + (bcolors.ENDC) + (str(message)))


def print_info(message):
    print((bcolors.BLUE) + (bcolors.BOLD) + \
        ("[-] ") + (bcolors.ENDC) + (str(message)))


def print_info_spaces(message):
    print((bcolors.BLUE) + (bcolors.BOLD) + \
        ("  [-] ") + (bcolors.ENDC) + (str(message)))


def print_warning(message):
    print((bcolors.YELLOW) + (bcolors.BOLD) + \
        ("[!] ") + (bcolors.ENDC) + (str(message)))


def print_error(message):
    print((bcolors.RED) + (bcolors.BOLD) + \
        ("[!] ") + (bcolors.ENDC) + (bcolors.RED) + \
        (str(message)) + (bcolors.ENDC))

def set_title(title):
	sys.stdout.write("\x1b]2;%s\x07" % title)

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
grab_version = "2.4.5"

# banner
banner = bcolors.RED + r"""
                ████████╗██╗  ██╗███████╗                                     
                ╚══██╔══╝██║  ██║██╔════╝                                     
                   ██║   ███████║█████╗                                       
                   ██║   ██╔══██║██╔══╝                                       
                   ██║   ██║  ██║███████╗                                     
                   ╚═╝   ╚═╝  ╚═╝╚══════╝                                     
                                                                              
██████╗ ███████╗███╗   ██╗████████╗███████╗███████╗████████╗███████╗██████╗   
██╔══██╗██╔════╝████╗  ██║╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝██╔════╝██╔══██╗  
██████╔╝█████╗  ██╔██╗ ██║   ██║   █████╗  ███████╗   ██║   █████╗  ██████╔╝  
██╔═══╝ ██╔══╝  ██║╚██╗██║   ██║   ██╔══╝  ╚════██║   ██║   ██╔══╝  ██╔══██╗  
██║     ███████╗██║ ╚████║   ██║   ███████╗███████║   ██║   ███████╗██║  ██║  
╚═╝     ╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝  
                                                                              
███████╗██████╗  █████╗ ███╗   ███╗███████╗██╗    ██╗ ██████╗ ██████╗ ██╗  ██╗
██╔════╝██╔══██╗██╔══██╗████╗ ████║██╔════╝██║    ██║██╔═══██╗██╔══██╗██║ ██╔╝
█████╗  ██████╔╝███████║██╔████╔██║█████╗  ██║ █╗ ██║██║   ██║██████╔╝█████╔╝ 
██╔══╝  ██╔══██╗██╔══██║██║╚██╔╝██║██╔══╝  ██║███╗██║██║   ██║██╔══██╗██╔═██╗ 
██║     ██║  ██║██║  ██║██║ ╚═╝ ██║███████╗╚███╔███╔╝╚██████╔╝██║  ██║██║  ██╗
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
                                                                              
"""

banner += bcolors.ENDC + """
		     The"""
banner += bcolors.BOLD + """ PenTesters """
banner += bcolors.ENDC + """Framework\n\n"""

banner += """        		   """ + bcolors.backBlue + \
    """Version: %s""" % (grab_version) + bcolors.ENDC + "\n"

banner += bcolors.YELLOW + bcolors.BOLD + """		        Codename: """ + \
    bcolors.BLUE + """Toolsmith""" + "\n"

banner += """		         """ + bcolors.ENDC + bcolors.backRed + \
    """Red Team Approved""" + bcolors.ENDC + "\n"

banner += """        	      A project by """ + bcolors.GREEN + bcolors.BOLD + \
    """Trusted""" + bcolors.ENDC + bcolors.BOLD + """Sec""" + bcolors.ENDC + "\n"

banner += """		 Written by: """ + bcolors.BOLD + \
    """Dave Kennedy (ReL1K)""" + bcolors.ENDC + "\n"
banner += """		Twitter: """ + bcolors.BOLD + \
    """@HackingDave, @TrustedSec""" + bcolors.ENDC + "\n"
banner += """\n                    """ + bcolors.BOLD + """https://www.trustedsec.com
        """ + bcolors.ENDC
banner += bcolors.BOLD + """\n              The easy way to get the new and shiny.
""" + bcolors.ENDC + "\n"
banner += "             Total module/tool count within PTF: " + \
    bcolors.BOLD + str(count_modules()) + bcolors.ENDC + "\n"
banner += """
All tools are downloaded directly from the developers websites as-is.  PTF 
doesn't perform any type of source code analysis or verification on the tools.
You should run these after performing your own analysis of the tools and ensure 
you trust the parties. PTF only adds tools that are well-known typically in the 
security industry but that does not negate the risk. This is no different than 
any other tool distribution platform, operating system, or anything you would 
download from the Internet.\n"""

# check the config file and return value
def check_config(param):
    fileopen = open("%s/config/ptf.config" % (definepath()), "r")
    for line in fileopen:
        # if the line starts with the param we want then we are set, otherwise
        # if it starts with a # then ignore
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
    if os.path.isfile(filename) and not "install_update_all" in filename and ".py" in filename and not ".pyc" in filename:

        # set a base counter
        counter = 0

        # open the file
        fileopen = open(filename, "r")
        # iterate through the file
        for line in fileopen:
            # strip any bogus stuff
            line = line.rstrip()
            # if the line starts with the term
            if line.startswith(term):
                line = line.replace(term + '="', "")
                line = line.replace(term + "='", "")
                line = line.replace(term + "=", "")
                if str(line).endswith('"'): line = line[:-1]
                if str(line).endswith("'"): line = line[:-1]
                # reflect we hit this and our search term was found
                counter = 1
                return line

        # if there was no search term identified for the module
        if counter == 0:
            filename_short = filename.replace(definepath() + "/", "")
            filename_short = filename_short.replace(".py", "")
            if term not in "BYPASS_UPDATE|LAUNCHER|TOOL_DEPEND|X64_LOCATION|install_update_all|FEDORA|OPENBSD|ARCHLINUX":
                              if filename_short not in "__init__|msfdb.sh|modules/custom_list/list":
                                        print_error("Warning, module %s was found but contains no %s field." % (filename_short, term))
                                        print_error("Check the module again for errors and try again.")
                                        print_error("Module has been removed from the list.")

            return ""

    # if the file isn't there
    if not os.path.isfile(filename):
        return None

# help menu for PTF
def show_help_menu():
    print(("Available from main prompt: " + bcolors.BOLD + "show modules" + bcolors.ENDC + "," + bcolors.BOLD + " show <module>" +
           bcolors.ENDC + "," + bcolors.BOLD + " search <name>" + bcolors.ENDC + "," + bcolors.BOLD + " use <module>" + bcolors.ENDC))
    print(("Inside modules:" + bcolors.BOLD + " show options" + bcolors.ENDC + "," +
           bcolors.BOLD + " set <option>" + bcolors.ENDC + "," + bcolors.BOLD + "run" + bcolors.ENDC))
    print(("Additional commands: " + bcolors.BOLD + "back" + bcolors.ENDC + "," + bcolors.BOLD + " help" + bcolors.ENDC + "," +
           bcolors.BOLD + " ?" + bcolors.ENDC + "," + bcolors.BOLD + " exit" + bcolors.ENDC + "," + bcolors.BOLD + " quit" + bcolors.ENDC))
    print(("Update or Install: " + bcolors.BOLD + "update" + bcolors.ENDC + "," + bcolors.BOLD + " upgrade" +
           bcolors.ENDC + "," + bcolors.BOLD + " install" + bcolors.ENDC + "," + bcolors.BOLD + " run" + bcolors.ENDC))

# exit message for PTF
def exit_ptf():
    print_status("Exiting PTF - the easy pentest platform creation framework.")
    set_title("Hack the Planet!")


# this is the main handler to check what distribution we are using
# if it can't find it, will default to manual install base
def profile_os():
    # if we are running a debian variant
    if os.path.isfile("/usr/bin/apt-get"):
        return "DEBIAN"

    if os.path.isfile("/usr/bin/aptitude"):
        return "DEBIAN"

    if os.path.isfile("/etc/arch-release"):
        return "ARCHLINUX"

    if os.path.isfile("/etc/fedora-release"):
        return "FEDORA"

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
        filewrite = open(logpath, "w")
        filewrite.write("")
        filewrite.close()
    # open for append
    filewrite = open(logpath, "a")
    # write it out
    filewrite.write(log)
    # close the file
    filewrite.close()

# this will install all the proper locations for
def prep_install():
    if not os.path.isfile(os.getenv("HOME") + "/.ptf"):
        print_status("This appears to be your first time using PTF.")
        print_status("Creating output directory to: " +
                     os.getenv("HOME") + "/.ptf")
        os.makedirs(os.getenv("HOME") + "/.ptf")


def home_directory():
    return os.getenv("HOME") + "/.ptf"

# this will run commands after an install or update on a module
def after_commands(filename, install_location):
    from src.commands import after_commands
    commands = module_parser(filename, "AFTER_COMMANDS")
    if commands != "":
        # here we check if install location needs to be added
        if "{INSTALL_LOCATION}" in commands:
            commands = commands.replace("{INSTALL_LOCATION}", install_location)
        # ptf location
        if "{PTF_LOCATION}" in commands:
            commands = commands.replace("{PTF_LOCATION}", os.getcwd())
        print_status(
            "Running after commands for post installation requirements.")
        after_commands(commands, install_location)
        print_status("Completed running after commands routine..")

# launcher - create launcher under /usr/local/bin
def launcher(filename, install_location):
    launcher = module_parser(filename, "LAUNCHER")

    # if its optional
    if launcher == None:
        launcher = ""
    if launcher != "":
        # create a launcher if it doesn't exist
        base_launcher = 0
        if "," in launcher:
            launcher = launcher.split(",")
        for launchers in launcher:

            # means there was just one launcher
            if len(launchers) == 1:
                launchers = launcher
                base_launcher = 1

            if os.path.isfile("/usr/local/bin/" + launchers):
                os.remove("/usr/local/bin/" + launchers)
            if not os.path.isfile("/usr/local/bin/" + launchers):

                # base launcher filename
                point = ""

                # make sure the actual launcher is there with known filetypes
                if os.path.isfile(install_location + "/" + launchers):
                    # specific launcher file
                    point = "./" + launchers
                    file_point = launchers

                # check for Python
                if os.path.isfile(install_location + "/" + launchers + ".py"):
                    point = "./" + launchers + ".py"
                    file_point = launchers + ".py"

                # check for Ruby
                if os.path.isfile(install_location + "/" + launchers + ".rb"):
                    point = "./" + launchers + ".rb"
                    file_point = launchers + ".rb"

                # check for Perl - ew Perl. Ew ew ew ew ew ew =)
                if os.path.isfile(install_location + "/" + launchers + ".pl"):
                    point = "./" + launchers + ".pl"
                    file_point = launchers + ".pl"

                # check for bash
                if os.path.isfile(install_location + "/" + launchers + ".sh"):
                    point = "./" + launchers + ".sh"
                    file_point = launchers + ".sh"

                # check of executable, then flag wine
                if os.path.isfile(install_location + "/" + launchers + ".exe"):
                    point = "wine cmd /c start " + launchers + ".exe"
                    file_point = launchers + ".exe"

                # normal launcher
                if os.path.isfile(install_location + "/" + launchers):
                    point = "./" + launchers
                    file_point = launchers

                # if we found filetype
                if point != "":
                    filewrite = open("/usr/local/bin/" + launchers, "w")
                    filewrite.write('#!/bin/sh\n[ -x %s%s ] || chmod +x %s%s\n%s%s "$@"\n' %
                                    (install_location, file_point, install_location, file_point, install_location, file_point))
                    filewrite.close()
                    subprocess.Popen("chmod +x /usr/local/bin/%s" %
                                     (launchers), shell=True).wait()
                    msg = "Created automatic launcher, you can run the tool from anywhere by typing: " + launchers
                    print_status(msg)
                    with open("ptf-output.log","a") as ee:
                        ee.write(msg+"\n")
            # just need to do this once
            if base_launcher == 1:
                break

# search functionality here
def search(term):
    term = term.replace("search ", "").lower() # Make the text in search lower for case sensitive
    module_files = []
    if "update" in term or "install" in term:
        module_files.append("modules/install_update_all")

    else:
        for dirpath, subdirs, files in os.walk("modules/"):
            for x in files:
                if x.endswith(".py"):
                    if not "__init__.py" in x:
                        path = os.path.join(dirpath, x)
                        if term in path:
                            x = x.replace(".py", "")
                            module_files.append(os.path.join(dirpath, x))

                        if not term in path:
                            data = open(path, "r", encoding="utf-8").readlines()
                            # normally just searched entire file, but we don't
                            # want to search # lines
                            for line in data:
                                line = line.rstrip()
                                if term in line:
                                    if not line.startswith("#"):
                                        x = x.replace(".py", "")
                                        module_files.append(
                                            os.path.join(dirpath, x))
                                        break
    if module_files != []:
        print_status("Search results below:")
        for modules in module_files:
            print (modules)

    else:
        print_warning("Search found no results.")


# auto update packages
def auto_update():
    # if we want to do auto update
    check = check_config("AUTO_UPDATE=").lower()
    if check == "on":
        print_status(
            "Auto updating is turned to on, this will install normal package updates for you...")
        print_status(
            "If you want to turn this off, go to the PTF directory and go to config and change AUTO_UPDATE")
        if profile_os() == "DEBIAN":
            subprocess.Popen(
                "sudo apt-get update && sudo apt-get -y upgrade && sudo apt-get dist-upgrade -y && apt-get -q --allow-downgrades --allow-remove-essential --allow-change-held-packages -y install build-essential && sudo apt-get autoremove -y && apt-get autoclean -y && updatedb", shell=True).wait()
        print_status(
            "Finished with normal package updates, moving on to the tools section..")
    else:
        print_status(
            "Auto updating for packages is turned off, to enable go to PTF and config directory and turn AUTO_UPDATE to ON.")

# check if a blank directory exists
def check_blank_dir(path):
    if os.path.isdir(path):
        if os.listdir(path) == []:
            print_status("Detected an empty folder, purging and re-checking out...")
            subprocess.Popen("rm -rf %s" % (path), shell=True).wait()

        # we put a second one in there in case the path was removed from above
        if os.path.isdir(path):
            if os.listdir(path) == ['.git', '.gitignore']:
                print_status(
                    "Detected an empty folder, purging and re-checking out...")
                subprocess.Popen("rm -rf %s" % (path), shell=True).wait()

# do platform detection on 32 or 64 bit
def arch():
    return str(platform.architecture()[0])

# check to see if we are running kali linux
def check_kali():
    if os.path.isfile("/etc/apt/sources.list"):
        kali = open("/etc/apt/sources.list", "r")
        kalidata = kali.read()
        if "kali" in kalidata:
            return "Kali"
        # if we aren't running kali
        else:
            return "Non-Kali"
    else:
        print("[!] Not running a Debian variant..")
        return "Non-Kali"
