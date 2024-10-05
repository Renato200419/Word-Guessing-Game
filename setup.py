from setuptools import setup, find_packages

setup(
    name='word_guessing_game',
    version='3.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'word-guessing-game = src.main:main',
        ],
    },
    description='Juego de adivinanza de palabras desarrollado en Python.',
    author='Renato Olivera',
    author_email='renato.olivera.c@uni.pe',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
