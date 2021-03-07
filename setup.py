from setuptools import setup

setup(
    name='BoltzTraP_Tools',
    version='1.0b0',
    author='Hilal BALOUT',
    author_email='hilal_balout@hotmail.com',
    package_dir={'BoltzTraP_Tools': 'src'},
    packages=['BoltzTraP_Tools'],
    url='https://github.com/K4ys4r/BoltzTraP_Tools',
    license=open('LICENSE.txt').read(),
    description='BoltzTraP Plotting DATA',
    long_description=open('README.md').read(),
    classifiers=[
       'Development Status :: 4 - Beta',
       'License :: OSI Approved :: MIT License',
       'Intended Audience :: Science/Research',
       'Natural Language :: English',
       'Programming Language :: Python :: 2',
       'Programming Language :: Python :: 2.3',
       'Programming Language :: Python :: 2.4',
       'Programming Language :: Python :: 2.5',
       'Programming Language :: Python :: 2.6',
       'Programming Language :: Python :: 2.7',
       'Programming Language :: Python :: 3',
       'Programming Language :: Python :: 3.6',
       'Programming Language :: Python :: 3.7',
       'Programming Language :: Python :: 3.8',
       'Programming Language :: Python :: 3.9'
     ],
    install_requires=[
        'BoltzTraP_Tools',
        'numpy',
        'matplotlib',
    ],
)

