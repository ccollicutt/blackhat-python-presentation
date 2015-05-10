#!/usr/bin/env python
# The most simple fuzzer for Fusil: just starts the command:
#    echo "Hello World"
#
# Since the process is not watched, Fusil will kills the process after the
# timeout (10 seconds by default).

# Reuse objets from Fusil library
from fusil.application import Application
from fusil.process.create import ProjectProcess

# Any fuzzer have to create a class based on Application
class Fuzzer(Application):
    # Fuzzer name: short alphanumeric string
    NAME = "hello"

    # setupProject() is the main fuzzer function:
    # it creates the fuzzer agents
    def setupProject(self):
        # Create an agent: don't store the object, it's already done
        # in the agent constructor
        ProjectProcess(self.project, ['echo', 'Hello World!'])

if __name__ == "__main__":
    # Create the fuzzer application and call its method main()
    # Fusil will parse the command line, create all agents, and start the
    # fuzzing project
    Fuzzer().main()
