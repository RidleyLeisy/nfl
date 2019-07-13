# script to create a file directory for an ml project
import os

# collect user information on project name
project_name = input(f'Create project folder name: {os.getcwd()}/')
path = os.getcwd() + f'/{project_name}'

#create project folder
os.mkdir(path)

#create top layer files
f = open(path + '/Makefile','x')
f.write('Makefile with commands like `make data` or `make train`')
f.close()

f = open(path + '/LICENSE','x')
f.write('Proper documentation for License')
f.close()

f = open(path + '/README.md','x')
f.write('The top-level README for developers using this project.')
f.close()

f = open(path + '/docs','x')
f.write('A default Sphinx project; see sphinx-doc.org for details')
f.close()

f = open(path + '/references', 'x')
f.write('Data dictionaries, manuals, and all other explanatory materials.')
f.close()

f = open(path + '/requirements.txt','x')
f.write('The requirements file for reproducing the analysis environment, e.g.')
f.close()

f = open(path + '/setup.py','x')
f.write('Make this project pip installable with `pip install -e`')
f.close()

f = open(path + '/.env', 'x')
f.write('Local file for env variables')
f.close()

# create data folder
os.mkdir(path + '/data')
f = open(path + '/data/external', 'x')
f.write('Data from third party sources.')
f.close()

f = open(path + '/data/internal', 'x')
f.write('Intermediate data that has been transformed.')
f.close()

f = open(path + '/data/processed', 'x')
f.write('The final, canonical data sets for modeling.')
f.close()

f = open(path + '/data/raw', 'x')
f.write('The original, immutable data dump.')
f.close()

# create model folder
os.mkdir(path + '/models')
# create notebook folder
os.mkdir(path + '/notebooks')
# create reports folder
os.mkdir(path + '/reports')
open(path + '/reports/figures', 'x')

#create src folder
os.mkdir(path + '/src')
f = open(path + '/src/__init__.py', 'x')
f.write('Makes src a Python module')
f.close()

os.mkdir(path + '/src/data')
os.mkdir(path + '/src/features')
os.mkdir(path + '/src/models')