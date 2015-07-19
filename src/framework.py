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

print_status("Operating system detected as: " + bcolors.BOLD + profile_os() + bcolors.ENDC)
# main intro here
print_status("Welcome to PTF - where everything just works...Because.." + bcolors.BOLD + "Aliens." + bcolors.ENDC)
print """
For a list of available commands type ? or help
"""

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
            if not "__init__.py" in filename:
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

        # grab install path
        base_install = check_config("BASE_INSTALL_PATH=")
        install_base_location = module_parser(filename, "INSTALL_LOCATION")
        module_split = module.split("/")
        module_split = module_split[1]
        install_location = base_install + "/" + module_split + "/" + install_base_location + "/"

    while 1:

	# if we aren't doing update/install all
	if int(all_trigger) == 0:
	        prompt = raw_input(bcolors.BOLD + "ptf:" + bcolors.ENDC + "(" + bcolors.RED + "%s" % module + bcolors.ENDC + ")>")
	        # exit if we need to
	        if prompt == "back" or prompt == "quit" or prompt == "exit": break
	        # show the help menu
	        if prompt == "?" or prompt == "help":
	        	show_help_menu()

	        if prompt == "show modules": print_warning("In order to show modules, you must type 'back' first")

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
		if os.path.isdir(install_location):
			print_status("Detected installation already. Going to upgrade for you.")
			prompt = "update"
		else:
			print_status("Tool not installed yet, will run through install routine")
			prompt = "install"


        # if we are updating the tools
        if prompt.lower() == "update" or prompt.lower() == "upgrade":

            # update depend modules
            ostype = profile_os()
            if ostype == "DEBIAN":
                    from src.platforms.debian import base_install_modules
                    # grab all the modules we need
                    deb_modules = module_parser(filename, "DEBIAN")
                    print_status("Updating depends for %s prior to update." % (module))
                    base_install_modules(deb_modules)
                    print_status("Finished updating depends for %s" % (module))

		    # run after commands
		    after_commands(filename, install_location)

            # move to the location
            if os.path.isdir(install_location):
                if install_type.lower() == "git":
                    print_status("Updating the tool, be patient while git pull is initiated.")
                    proc = subprocess.Popen("cd %s;git pull" % (install_location), stderr=subprocess.PIPE, shell=True)
                    # if there were errors
                    error = proc.stderr.read().rstrip()
                    if error != "": 
                        print_error("Install did not complete. Printing error:\n" + error)
                    else:
                        print_status("Finished Installing! Enjoy the tool installed under: " + (install_location))

		    # run after commands
                    after_commands(filename,install_location)

                if install_type.lower() == "svn":
                    print_status("Updating the tool, be patient while git pull is initiated.")
			
                    proc = subprocess.Popen("cd %s;svn update" % (install_location), stderr=subprocess.PIPE, shell=True)
                    print_status("Finished Installing! Enjoy the tool installed under: " + (install_location))
                    # run after commands
                    after_commands(filename,install_location)

            if not os.path.isdir(install_location):
                print_error("The tool was not found in the install location. Try running install first!")

        # if we want to install it
        if prompt.lower() == "install":
                # grab the OS type, DEBIAN, CUSTOM, ETC
                ostype = profile_os()

                # if OSTYPE is DEBIAN
                if ostype == "DEBIAN":
                    print_status("Preparing dependencies for module: " + module)
                    from src.platforms.debian import base_install_modules
                    # grab all the modules we need
                    deb_modules = module_parser(filename, "DEBIAN")
                    base_install_modules(deb_modules)
                    print_status("Pre-reqs for %s have been installed." % (module))

                print_status("Making the appropriate directory structure first")
                subprocess.Popen("mkdir -p %s" % install_location, shell=True).wait()

                if install_type.lower() == "git":
                    print_status("GIT was the selected method for installation... Using GIT to install.")
                    proc = subprocess.Popen("git clone %s %s" % (repository_location, install_location), stderr=subprocess.PIPE, shell=True)

                    # if there were errors
                    error = proc.stderr.read().rstrip()
		    print error
                    if error != "":
                        print_error("Install did not complete. Printing error:\n" + error)
                    else:
                        print_status("Finished Installing! Enjoy the tool located under: " + install_location)
   			after_commands(filename,install_location)

		# if we are using svn
                if install_type.lower() == "svn":
                    print_status("SVN was the selected method for installation... Using SVN to install.")
                    proc = subprocess.Popen("svn co %s %s" % (repository_location, install_location), stderr=subprocess.PIPE, shell=True)
                    print_status("Finished Installing! Enjoy the tool located under: " + install_location)
                    after_commands(filename,install_location)

	        # if we are using file
                if install_type.lower() == "file":
                    print_status("FILE was the selected method for installation... Using curl -o to install.")
                    repository_file = repository_location.split("/")[-1]
                    proc = subprocess.Popen("curl -o %s%s %s" % (install_location, repository_file, repository_location), stderr=subprocess.PIPE, shell=True)
                    status = proc.stderr.read().rstrip()
                    if "Warning" in status:
                        print_error("Install did not complete. Printing error:\n" + error)
                    else:
                        print_status("Finished Installing! Enjoy the tool located under: " + install_location)
                        after_commands(filename,install_location)

	# if we update all we need to break out until finished
	if int(all_trigger) == 1: break	

# start the main loop
while 1:

    # specify no commands, if counter increments then a command was found
    base_counter = 0

    prompt = raw_input(bcolors.BOLD + "ptf" + bcolors.ENDC + "> ")

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

    # if we want to use a module
    if prompt.startswith("use"):
        base_counter = 1
        counter = 0
        prompt = prompt.split(" ")        
        # do a quick sanity check to see if the module is there first
        if prompt[1] == "modules/install_update_all": 
		counter = 3
		install_query = raw_input("[*] You are about to install/update everything. Proceed? [yes/no]:")
		if install_query.lower() == "yes" or install_query.lower() == "y":
			modules_path = definepath() + "/modules/"
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
	            			if not "__init__.py" in filename:
		                			# shorten it up a little bit
		                			filename_short = filename.replace(os.getcwd() + "/", "")
							# update depend modules
							ostype = profile_os()
							if ostype == "DEBIAN":
					                	from src.platforms.debian import base_install_modules
                    						# grab all the modules we need
                    						deb_modules = deb_modules + "," + module_parser(filename_short, "DEBIAN")

			# install all of the packages at once
			ostype = profile_os()
			if ostype == "DEBIAN":
				deb_modules = deb_modules.replace(",", " ")
	                    	base_install_modules(deb_modules)
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
