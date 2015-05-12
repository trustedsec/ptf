#!/usr/bin/python
##########################
# After commands module
##########################
import pexpect
# this will execute after everything is over
def after_commands(command):
    # if there is more than one command iterate through
    if "," in command:
        command = command.split(",")
	child = pexpect.spawn("/bin/sh")
	print "[!] Note that this will drop into a bash shell to execute commands. You will need to type exit once completed."
        for commands in command:
		try:
			child.sendline(commands)
		except: pass

	# need to pass an exception here if the install has more things like psexec installer, etc.
	try:
		child.interact()

	except: pass

            #subprocess.Popen(commands, shell=True).wait()

    else:
        child = pexpect.spawn("/bin/sh")
        print "[!] Note that this will drop into a bash shell to execute commands. You will need to type exit once completed."
        try:
        	child.sendline(command)
        except: pass
        # need to pass an exception here if the install has more things like psexec installer, etc.
        try:
                child.interact()

        except: pass

