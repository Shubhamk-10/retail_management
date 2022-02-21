from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in retail_management/__init__.py
from retail_management import __version__ as version

setup(
	name="retail_management",
	version=version,
	description="Retail Management System",
	author="Shubham",
	author_email="shubham@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
