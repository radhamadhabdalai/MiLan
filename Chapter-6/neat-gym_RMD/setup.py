######################################################################################
'''Copyright (c) 2023, 2024 , Prof. Radhamadhab Dalai, ITER , Siksha O Aanusandhan University, 
Odisha, India
Author's email address :  radhamadhabdalai@soa.ac.in'''
###################################################################################

from setuptools import setup

setup(
    name='neat_gym',
    version='0.1',
    install_requires=['gym', 'numpy'],
    description='NEAT a GA implementations to learn OpenAI Gym environment',
    packages=['neat_gym', 'neat_gym.novelty'],
    author='Radhamadhab Dalai',
    author_email='radhamadhabdalai@soa.ac.in',
    url='https://github.com/Radhaadhabdalai/Milan',
    license='RMD',
    platforms='Linux; Windows; OS X'
    )
