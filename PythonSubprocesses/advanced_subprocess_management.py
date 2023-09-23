import os
import subprocess

my_env = os.environ.copy()
my_env["PATH"] = os.pathsep.join(["/opt/myapp/", my_env["PATH"]])

result = subprocess.run(["myapp"], env=my_env)

# If we're automating a one-off, well-defined task, we're developing a solution 
# quickly is the biggest requirement, then using system commands and 
# subprocesses can help a lot.