import jerrygame
from setuptools import setup

setup(name = 'jerrygame', version = 1.0, packages=['jerrygame', 'jerrygame.dominio', 'jerrygame.dominio.spritesdesign'],
 console_point = {
     'gui_scripts': ['jerrygame = jerrygame.__main__:main']
})