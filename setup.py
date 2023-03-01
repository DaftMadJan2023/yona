from setuptools import setup, find_packages

setup(
    # metadatos del proyecto
    name='yona',
    version='0.1',
    description='Una libreria academica y divertida',
    author='DAFT Madrid JAN 2023',
    author_email='daftjan23@gmail.com',
    url='https://github.com/DaftMadJan23/yona',

    # lista de paquetes incluidos
    packages=find_packages(),

    # dependencias requeridas
    install_requires=[
        'numpy>=1.19.5',
        'matplotlib>=3.4.2',
    ],

    # scripts incluidos
    scripts=['scripts/mi_script.py'],

    # datos adicionales incluidos
    package_data={
        'mi_libreria': ['datos/*'],
    },

    
)
