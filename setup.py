from setuptools import setup, find_packages

setup(
    name='word_guessing_game',
    version='1.0.0',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        'console_scripts': [
            'word-guessing-game = src.main:main',
        ],
    },
    description='Juego de adivinanza de palabras desarrollado en Python.',
    author='Renato Olivera',
    author_email='renato.olivera.c@uni.pe',
    install_requires=[],
)
