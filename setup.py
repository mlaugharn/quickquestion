from setuptools import setup

setup(
    name='quickquestion',
    version='0.1.0',
    py_modules=['qq'],
    install_requires=[
        'openai',
        'click',
        'langchain',
        'rich',
        'binaryornot'
    ],
    entry_points={
        'console_scripts': [
            'qq=qq:answer',
        ],
    },
)
