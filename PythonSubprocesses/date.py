#!/usr/bin/env python3

import subprocess

# while running the child process, the parent isn't able to run any commands
print(subprocess.run(["date"]))
# flow control continues

print(subprocess.run(["sleep", "2"]))

result = subprocess.run(["ls", "this_file_does_not_exist"])
# when you only care for the return code of the command
print(result.returncode)
