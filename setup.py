from setuptools import setup, find_packages

setup(
  name="tinkerbox",
  version="0.0.1",
  description="A Jupyter kernel for interacting with Thinkbox Deadline",
  url="https://github.com/jjsullivan5196/tinkerbox.git",
  author="John Sullivan",
  package_dir={"": "src/"},
  packages=find_packages(where="src"),
  python_requires=">=3.7, <4",
  data_files=[
    ("share/jupyter/kernels/tinkerbox/kernel.json", ["jupyter/kernels/tinkerbox/kernel.json"])
  ]
)
