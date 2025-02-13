from setuptools import setup, find_packages

setup(
    name='EmotionDetection',  # This is the name your package will be installed under
    version='0.1.0',  # You can choose a version number
    packages=find_packages(), # Automatically find all packages and subpackages
    install_requires=['requests'], # Dependencies
)
