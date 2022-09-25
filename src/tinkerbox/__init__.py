"""Stub for running the ipython kernel inside of Thinkbox Deadline. When run as
main, it will locate `deadlinecommand` on the system and execute itself inside
Deadline's sandbox. Any command line arguments are forwarded directly to the
kernel.

When this package is in the load path, it can be invoked like so:

python -m deadline_ipy_kernel -f path/to/connection_file.json

See the ipython documentation for more details, or run this package with a
--help argument.

"""
