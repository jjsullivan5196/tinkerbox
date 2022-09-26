import sys
import platform

SYSTEM = platform.system()

def __main__(*args):
  "Start the ipython kernel."
  # Forward args from the exec wrapper
  sys.argv.extend(args)

  # Set the system python interpreter for debugpy, so it can launch the adapter server
  import debugpy
  import shutil

  # Python on Windows installs under `python.exe`, otherwise look for `python3`
  # TODO there may be a less-hacky way to find the system interpreter
  sys_python_binname = "python" if SYSTEM == 'Windows' else "python3"
  sys_python_path = shutil.which(sys_python_binname)

  debugpy.configure({"python": sys_python_path})

  # Launch the kernel
  from ipykernel.kernelapp import launch_new_instance
  launch_new_instance()

def __run_deadlinecommand():
  "Stub for execing to Deadline's sandboxed interpreter."
  import os
  import platform

  # Find deadlinecommand
  deadline_command = None

  if SYSTEM == 'Linux':
    deadline_command = f"{os.environ['DEADLINE_PATH']}/deadlinecommand"
  elif SYSTEM == 'Windows':
    deadline_command = f"{os.environ['DEADLINE_PATH']}/deadlinecommand.exe"
  elif SYSTEM == 'Darwin':
    with open("/Users/Shared/Thinkbox/DEADLINE_PATH", 'r') as path_file:
      deadline_path = path_file.read().strip()
      deadline_command = f"{deadline_path}/deadlinecommand"
  else:
    sys.exit("This operating system is not supported by Thinkbox Deadline.")

  # Run this script in the Deadline sandbox
  abspath = os.path.abspath(__file__)
  os.execl(deadline_command, deadline_command, "-ExecuteScript", abspath, *sys.argv[1:])
