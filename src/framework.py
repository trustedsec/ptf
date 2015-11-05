#!/usr/bin/env python
#######################################
# PTF Main framework look and feel
#######################################

# main module imports
from src.core import *
import sys
import readline
import os
import time

# print the main welcome banner
print banner

# funny random banner
import random
funny = random.sample(["Aliens","Clowns", "Mr. Robot", "Zero Cool", "Goats", "Hackers", "Unicorns"], 1)[0]

print_status("Operating system detected as: " + bcolors.BOLD + profile_os() + bcolors.ENDC)
# main intro here
if profile_os() == "DEBIAN":
    subprocess.Popen("sudo dpkg --add-architecture i386", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
print_status("Welcome to PTF - where everything just works...Because.." + bcolors.BOLD + funny + bcolors.ENDC)
print """
For a list of available commands type ? or help
"""

ignore_these = []
if check_config("IGNORE_THESE_MODULES") is not None:
    ignore_these = check_config("IGNORE_THESE_MODULES").split(",")

def ignore_module(module):
    result = False
    for check in ignore_these:
        if check == module:
            print_warning("Ignoring module: " + module)
            result = True
    result

# check the folder structure
def show_module():
    modules_path = os.getcwd() + "/modules/"
    print "\n"
    print bcolors.BOLD + "The PenTesters Framework Modules" + bcolors.ENDC
    print ("""=================================

   """ + bcolors.BOLD + """Name                                                 Description """ + bcolors.ENDC + """
   ----                                                 ---------------
    """)

    print "   modules/install_update_all                           This will install or update all tools with modules within PTF"
    for path, subdirs, files in os.walk(modules_path):
        for name in files:
            # join the structure
            filename = os.path.join(path, name)
            # strip un-needed files
            if not "__init__.py" in filename or not "install_update_all":
                # shorten it up a little bit
                filename_short = filename.replace(os.getcwd() + "/", "")
                filename_short = filename_short.replace(".py", "")
                description = module_parser(filename, "DESCRIPTION")
                # print the module name
                if description != None:
                    temp_number = 53 - len(filename_short)
                    print "   " + filename_short + " " * temp_number + description
    print "\n"


# this is when a use <module> command is initiated
def use_module(module, all_trigger):

    # if we aren't using all
    if not "install_update_all" in module:

        # if we are using a normal module
        if int(all_trigger) == 0 or int(all_trigger) == 1:
            filename = definepath() + "/" + module + ".py"

            # grab the author
            try:
                author = module_parser(filename, "AUTHOR")

            except TypeError: author = "Invalid"

            # grab the description
            description = module_parser(filename, "DESCRIPTION")

            # grab install type
            install_type = module_parser(filename, "INSTALL_TYPE")

            # grab repository location
            repository_location = module_parser(filename, "REPOSITORY_LOCATION")

            # here we check if we need to do x86 or x64
            if module_parser(filename, "X64_LOCATION") != None:
                # grab architecture
                # print module_parser(filename, "X64_LOCATION")
                arch_detect = arch()
                if "64bit" in arch_detect:
                    repository_location = module_parser(filename, "X64_LOCATION")

            # grab install path
            base_install = check_config("BASE_INSTALL_PATH=")
            install_base_location = module_parser(filename, "INSTALL_LOCATION")
            module_split = module.split("/")
            module_split = module_split[1]
            install_location = base_install + "/" + module_split + "/" + install_base_location + "/"

        while 1:

            # if we aren't doing update/install all
            if int(all_trigger) == 0:
                try:
                    prompt = raw_input(bcolors.BOLD + "ptf:" + bcolors.ENDC + "(" + bcolors.RED + "%s" % module + bcolors.ENDC + ")>")
                except EOFError:
                    prompt = "back"
                    print("")

                # exit if we need to
                if prompt == "back" or prompt == "quit" or prompt == "exit": break
                # show the help menu
                if prompt == "?" or prompt == "help":
                    show_help_menu()

                if prompt == "show modules": print_warning("In order to show modules, you must type 'back' first")

                # if we are searching for something
                if "search " in prompt: search(prompt)

                # options menu - was a choice here to load upon initial load of dynamically pull each time
                # if changes are made, it makes sense to keep it loading each time
                if prompt.lower() == "show options":
                    print "Module options (%s):" % module

                # if we are using a normal module
                if module != "modules/install_update_all":

                    print "\n\n"
                    print bcolors.BOLD + "Module Author:         " + bcolors.ENDC + author
                    print bcolors.BOLD + "Module Description:    " + bcolors.ENDC + description
                    print "-------------------------------------------------------------------------------------"
                    print bcolors.BOLD + "INSTALL_TYPE:           " + bcolors.ENDC + install_type
                    print bcolors.BOLD + "REPOSITORY_LOCATION:    " + bcolors.ENDC + repository_location
                    print bcolors.BOLD + "INSTALL_LOCATION:       " + bcolors.ENDC + install_location
                    print "-------------------------------------------------------------------------------------"

                # if we are setting the command now
                if prompt.lower().startswith("set"):
                    # need to grab the options
                    set_breakout = prompt.split(" ")
                    # here we rewrite the options for the menu
                    if set_breakout[1].upper() == "INSTALL_TYPE": install_type = set_breakout[2]
                    if set_breakout[1].upper() == "REPOSITORY_LOCATION": repository_location = set_breakout[2]
                    if set_breakout[1].upper() == "INSTALL_LOCATION": install_location = set_breakout[2]

            if int(all_trigger) == 1: prompt = "run"

            # if we are using run, check first to see if its there, if so, do an upgrade
            if prompt.lower() == "run":

                # check if empty directory - if so purge it before anything else
                check_blank_dir(install_location)

                if os.path.isdir(install_location):
                    print_status("Detected installation already. Going to upgrade for you.")
                    prompt = "update"
                else:
                    print_status("Tool not installed yet, will run through install routine")
                    prompt = "install"

            # check to see if we need to bypass after commands for certain files - this is needed when using FILE and others where after commands need to be run
            if module_parser(filename, "BYPASS_UPDATE") == "YES":
                if prompt.lower() == "update":
                    prompt = "install"

            # if we are updating the tools
            if prompt.lower() == "update" or prompt.lower() == "upgrade":

                # move to the location
                if os.path.isdir(install_location):
                    if install_type.lower() == "git":
                        print_status("Updating the tool, be patient while git pull is initiated.")
                        proc = subprocess.Popen("cd %s;git pull" % (install_location), stderr=subprocess.PIPE, shell=True).wait()
                        print_status("Finished Installing! Enjoy the tool installed under: " + (install_location))

                        # run after commands
                        if prompt != "update":
                            after_commands(filename,install_location)
                            # special metasploit voodoo needed here
                            if os.path.isfile(install_location + "/msfconsole"):
                                cwd = os.getcwd()
                                os.chdir("/usr/local/bin")
                                print_status("Needing to perform special Metasploit voodoo to get launcher to work.. Wait for another bundle install...")
                                subprocess.Popen("cd %s;bundle install;rm -rf /usr/local/rvm/gems/ruby-2.*/bin/msf*" % (install_location), shell=True).wait()
                                print_status("Sacrifice to the ruby Gods complete. MSF should now work outside of the msf directory structure..")
                                os.chdir(cwd)

                        # check launcher
                        launcher(filename, install_location)

                        # special for Metasploit
                        if "metasploit" in filename:
                            if prompt == "update":
                                print_status("Ensuring libgmp-dev is installed for ffi...")
                                subprocess.Popen("apt-get --force-yes -y install libgmp-dev", shell=True).wait()
                                print_status("Updating gem packages for Metasploit....")
                                subprocess.Popen("cd %s;bundle update;bundle install" % (install_location), shell=True).wait()
                                print_status("Killing ruby gem launchers as this breaks launchers...")
                                subprocess.Popen("rm /usr/local/rvm/gems/ruby-2.*/bin/msf*", shell=True).wait()
                                print_status("Finished updating Metasploit.... Enjoy!")

                    if install_type.lower() == "svn":
                        print_status("Updating the tool, be patient while git pull is initiated.")
                        proc = subprocess.Popen("cd %s;svn update" % (install_location), stderr=subprocess.PIPE, shell=True)
                        print_status("Finished Installing! Enjoy the tool installed under: " + (install_location))
                        # run after commands
                        if prompt != "update":
                            after_commands(filename,install_location)

                        # check launcher
                        launcher(filename, install_location)

                if not os.path.isdir(install_location):
                    print_error("The tool was not found in the install location. Try running install first!")


            # if we want to install it
            if prompt.lower() == "install":

                # grab the OS type, DEBIAN, FEDORA, CUSTOM, BSD!!!! WOW!!, ETC
                ostype = profile_os()

                # if OSTYPE is DEBIAN
                if ostype == "DEBIAN":
                    print_status("Preparing dependencies for module: " + module)
                    from src.platforms.debian import base_install_modules
                    # grab all the modules we need
                    deb_modules = module_parser(filename, "DEBIAN")
                    base_install_modules(deb_modules)
                    print_status("Pre-reqs for %s have been installed." % (module))

                    # do some stuff to add metasploit
                    if "metasploit" in filename:
                        print_status("Installing additional ruby2 libraries for MSF...")
                        subprocess.Popen("echo y | apt-add-repository ppa:brightbox/ruby-ng;apt-get update;apt-get --force-yes -y install ruby2.2 ruby2.2-dev", shell=True).wait()

                # if OSTYPE is ARCHLINUX
                if ostype == "ARCHLINUX":
                    print_status("Preparing dependencies for module: " + module)
                    from src.platforms.archlinux import base_install_modules
                    # grab all the modules we need
                    arch_modules = module_parser(filename, "ARCHLINUX")
                    base_install_modules(arch_modules)
                    print_status("Pre-reqs for %s have been installed." % (module))

                # if OSTYPE is FEDORA
                if ostype == "FEDORA":
                    print_status("Preparing dependencies for module: " + module)
                    from src.platforms.fedora import base_install_modules
                    # grab all the modules we need
                    fedora_modules = module_parser(filename, "FEDORA")
                    base_install_modules(fedora_modules)
                    print_status("Pre-reqs for %s have been installed." % (module))

                # if OSTYPE is OPENBSD
                if ostype == "OPENBSD":
                    print_status("Preparing dependencies for module: " + module)
                    from src.platforms.openbsd import base_install_modules
                    # grab all the modules we need
                    openbsd_modules = module_parser(filename, "OPENBSD")
                    base_install_modules(openbsd_modules)
                    print_status("Pre-reqs for %s have been installed." % (module))

                print_status("Making the appropriate directory structure first")
                subprocess.Popen("mkdir -p %s" % install_location, shell=True).wait()

                # if we are using git
                if install_type.lower() == "git":
                    print_status("GIT was the selected method for installation... Using GIT to install.")
                    print_status("Installing now.. be patient...")
                    proc = subprocess.Popen("git clone %s %s" % (repository_location, install_location), stderr=subprocess.PIPE, shell=True).wait()
                    print_status("Finished Installing! Enjoy the tool located under: " + install_location)
                    after_commands(filename,install_location)
                    launcher(filename, install_location)

                # if we are using svn
                if install_type.lower() == "svn":
                    print_status("SVN was the selected method for installation... Using SVN to install.")
                    proc = subprocess.Popen("svn co %s %s" % (repository_location, install_location), stderr=subprocess.PIPE, shell=True).wait()
                    print_status("Finished Installing! Enjoy the tool located under: " + install_location)
                    after_commands(filename,install_location)
                    launcher(filename, install_location)

                # if we are using file
                if install_type.lower() == "file":
                    print_status("FILE was the selected method for installation... Using curl -o to install.")
                    repository_file = repository_location.split("/")[-1]
                    proc = subprocess.Popen('curl -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.112 Safari/534.30" -o %s%s %s' % (install_location, repository_file, repository_location), stderr=subprocess.PIPE, shell=True).wait()
                    print_status("Finished Installing! Enjoy the tool located under: " + install_location)
                    after_commands(filename,install_location)
                    launcher(filename, install_location)

                    # if we are using wget
                if install_type.lower() == "wget":
                    print_status("WGET was the selected method for installation because it plays better that curl -l with Sourceforge.")
                    proc = subprocess.Popen("cd %s && wget -q %s" % (install_location, repository_location), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
                    print_status("Finished Installing! Enjoy the tool located under: " + install_location)
                    after_commands(filename,install_location)
                    launcher(filename, install_location)

                # if we update all we need to break out until finished
            if int(all_trigger) == 1: break

# start the main loop
while 1:

    # specify no commands, if counter increments then a command was found
    base_counter = 0

    try:
        prompt = raw_input(bcolors.BOLD + "ptf" + bcolors.ENDC + "> ")
    except EOFError:
        prompt = "quit"
        print("")

    # main help menu
    if prompt == "?" or prompt == "help":
        show_help_menu()
        base_counter = 1

    # if we want to exit out
    if prompt == "quit" or prompt == "exit" or prompt == "back":
        base_counter = 1
        exit_ptf()
        sys.exit()

    # if we want to see the modules
    if prompt == "show modules":
        base_counter = 1
        show_module()

    # inside joke
    if prompt == "install sleeves":
        print_error("Scott White? Sleeves? F Sleeves. Scott Rules.")
        base_counter = 1

    # search functionality here
    if prompt.startswith("search"):
        base_counter = 1
        search(prompt)

    # if we want to use a module
    if prompt.startswith("use"):
        base_counter = 1
        counter = 0
        prompt = prompt.split(" ")

        # do a quick sanity check to see if the module is there first
        if "install_update_all" in prompt[1]:
            counter = 3
            try:
                install_query = raw_input("[*] You are about to install/update everything. Proceed? [yes/no]:")
            except EOFError:
                install_query = "no"
                print("")
            if install_query.lower() == "yes" or install_query.lower() == "y":

                # do auto update check first
                auto_update()

                modules_path = definepath() +"/"+ (prompt[1])[:-18]
                # base holder for all debian packages
                deb_modules = ""
                # first we install all depends for all applications
                print_status("We are going to first install all prereqs using apt before installing..")
                print_status("Cycling through modules and grabbing requirements...")
                for path, subdirs, files in os.walk(modules_path):
                    for name in files:
                        # join the structure
                        filename = os.path.join(path, name)
                        # strip un-needed files
                        if not "__init__.py" in filename and not ignore_module(filename):
                            # shorten it up a little bit
                            filename_short = filename.replace(os.getcwd() + "/", "")
                            # update depend modules
                            ostype = profile_os()
                            if ostype == "DEBIAN":
                                if not "install_update_all" in filename_short:
                                    from src.platforms.debian import base_install_modules
                                    # grab all the modules we need
                                    deb_modules = deb_modules + "," + module_parser(filename_short, "DEBIAN")
                            # archlinux
                            if ostype == "ARCHLINUX":
                                if not "install_update_all" in filename_short:
                                    from src.platforms.archlinux import base_install_modules
                                    # grab all the modules we need
                                    arch_modules = arch_modules + "," + module_parser(filename_short, "ARCHLINUX")
                            # fedora
                            if ostype == "FEDORA":
                                if not "install_update_all" in filename_short:
                                    from src.platforms.fedora import base_install_modules
                                    # grab all the modules we need
                                    fedora_modules = fedora_modules + "," + module_parser(filename_short, "FEDORA")
                            # openbsd
                            if ostype == "OPENSBD":
                                if not "install_update_all" in filename_short:
                                    from src.platforms.openbsd import base_install_modules
                                    # grab all the modules we need
                                    openbsd_modules = openbsd_modules + "," + module_parser(filename_short, "OPENBSD")


                # install all of the packages at once
                ostype = profile_os()
                if ostype == "DEBIAN":
                    deb_modules = deb_modules.replace(",", " ")
                    if deb_modules != None:
                        base_install_modules(deb_modules)
                    print_status("Finished updating depends for modules.")

                if ostype == "ARCHLINUX":
                    arch_modules = arch_modules.replace(",", " ")
                    if arch_modules != None:
                        base_install_modules(arch_modules)
                    print_status("Finished updating depends for modules.")

                if ostype == "FEDORA":
                    fedora_modules = fedora_modules.replace(",", " ")
                    if fedora_modules != None:
                        base_install_modules(fedora_modules)
                    print_status("Finished updating depends for modules.")

                if ostype == "OPENBSD":
                    openbsd_modules = openbsd_modules.replace(",", " ")
                    if openbsd_modules != None:
                        base_install_modules(openbsd_modules)
                    print_status("Finished updating depends for modules.")

                for path, subdirs, files in os.walk(modules_path):
                    for name in files:
                        # join the structure
                        filename = os.path.join(path, name)
                        # strip un-needed files
                        if not "__init__.py" in filename:
                            # shorten it up a little bit
                            filename_short = filename.replace(os.getcwd() + "/", "")
                            filename_short = filename_short.replace(".py", "")
                            # check if empty directory - if so purge it before anything else
                            check_blank_dir(path)
                            print_status("Installing and/or updating: " + filename_short)
                            # run the module for install
                            use_module(filename_short, "1")
                            # sleep a sec
                            time.sleep(0.2)

                # clear the screen
                os.system("clear")
                print "\n"
                print (""" _   _            _      _   _            ____  _                  _""")
                print ("""| | | | __ _  ___| | __ | |_| |__   ___  |  _ \| | __ _ _ __   ___| |_""")
                print ("""| |_| |/ _` |/ __| |/ / | __| '_ \ / _ \ | |_) | |/ _` | '_ \ / _ \ __|""")
                print ("""|  _  | (_| | (__|   <  | |_| | | |  __/ |  __/| | (_| | | | |  __/ |_ """)
                print ("""|_| |_|\__,_|\___|_|\_\  \__|_| |_|\___| |_|   |_|\__,_|_| |_|\___|\__|\n\n""")
                print_status("All finished installing/and or updating.. All shiny again.\n")

            else: print_status("Alright boss. Not installing right now. Tell me when. I want that shiny. I want it now.")

        if os.path.isfile(definepath() + "/" + prompt[1] + ".py"): counter = 1
        if counter == 1:
            use_module(prompt[1], "0")

        if counter == 0:
            print_error("Module name was not found, try retyping it again.")

    # if blanks are used
    if prompt == "":
        base_counter = 1

    if base_counter == 0:
        print_warning("Command was not found, try help or ? for more information.")
