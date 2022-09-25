import sys

def __main__(*args):
  "Start the ipython kernel."
  sys.argv.extend(args)

  from ipykernel.kernelapp import launch_new_instance
  launch_new_instance()

def __run_deadlinecommand():
  "Stub for execing to Deadline's sandboxed interpreter."
  import os
  import platform

  # Find deadlinecommand
  system = platform.system()
  deadline_command = None

  if system == 'Linux':
    deadline_command = f"{os.environ['DEADLINE_PATH']}/deadlinecommand"
  elif system == 'Windows':
    deadline_command = f"{os.environ['DEADLINE_PATH']}/deadlinecommand.exe"
  elif system == 'Darwin':
    with open("/Users/Shared/Thinkbox/DEADLINE_PATH", 'r') as path_file:
      deadline_path = path_file.read().strip()
      deadline_command = f"{deadline_path}/deadlinecommand"
  else:
    sys.exit("This operating system is not supported by Thinkbox Deadline.")

  # Run this script in the Deadline sandbox
  abspath = os.path.abspath(__file__)
  os.execl(deadline_command, deadline_command, "-ExecuteScript", abspath, *sys.argv[1:])
