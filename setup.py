from setuptools import find_packages
from distutils.core import setup

setup(name='deer_gym_plane',
      version='1.0.0',
      author='Deer Robotics',
      license="BSD-3-Clause",
      packages=find_packages(),
      author_email='support@deer.com',
      description='Template RL environments for Deer Robots',
      install_requires=['isaacgym', 'rsl-rl', 'matplotlib', 'numpy==1.20', 'tensorboard', 'mujoco==3.2.3', 'pyyaml'])
