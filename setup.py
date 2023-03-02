from setuptools import setup

setup(
    name='quickquestion',
    version='0.1.0',
    py_modules=['how', 'why', 'where'],
    install_requires=[
        'openai',
        'click'
    ],
    entry_points={
        'console_scripts': [
            'how=how:main',
            'why=why:main',
            'where=where:main',
        ],
    },
)
