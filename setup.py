from distutils.core import setup

setup(
    name='notefiles',
    version='1.0',
    py_modules=['notefiles'],
    install_requires=['click', 'marko'],
    entry_points={
        'console_scripts': ['notefiles=notefiles:main'],
    },
)
