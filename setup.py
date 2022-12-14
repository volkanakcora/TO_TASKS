import os
from setuptools import find_packages
from distutils.core import setup


# User-friendly description from README.md
current_directory = os.path.dirname(os.path.abspath(__file__))
try:
    with open(os.path.join(current_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except Exception:
    long_description = ''


requirements = [
	'requests',
	'schedule',
    'dash',
    'pandas',
	'gunicorn'

] 

setup(
	# Name of the package 
	name='chucknorris',
	entry_points= {
		'console_scripts': ['run_chucknorris = chuchnorris:main', 'run_web = web:main']
        
	},	
	# Packages to include into the distribution 
	packages=find_packages('.'),
	# Start with a small number and increase it with 
	# every change you make https://semver.org 
	version='1.0.0',
	# Chose a license from here: https: // 
	# help.github.com / articles / licensing - a - 
	# repository. For example: MIT 
	license='',
	# Short description of your library 
	description='',
	# Long description of your library 
	long_description=long_description,
	long_description_content_type='text/markdown',
	# Your name 
	author='volkan akcora',
	# Your email 
	author_email='volkan.eymir.akcora@deutsche-boerse.com',
	# Either the link to your github or to your website 
	url='',
	# Link from which the project can be downloaded 
	download_url='',
	# List of keywords 
	keywords=[],
	# List of packages to install with this one 
	install_requires= requirements,
	# https://pypi.org/classifiers/ 
	classifiers=[]
)
