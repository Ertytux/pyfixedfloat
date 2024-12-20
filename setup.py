from setuptools import setup, find_packages

setup(
    name='pyfixedfloat',
    version='0.1',
    packages=find_packages(),
    install_requires=[
       ' requests'
        # Aquí puedes listar las dependencias, por ejemplo:
        # 'numpy',
    ],
    author='Ertytux Tux',
    author_email='hivep2p@gmail.com',
    description='Paquete para el manejo de FixedFloat',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Ertytux/pyfixedfloat',  # URL del repositorio
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
