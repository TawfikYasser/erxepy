from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

 
setup(
  name='erxepy',
  version='0.0.1',
  description='Easy Regular Expression Python Module',
  long_description=long_description,
  url='https://github.com/TawfikYasser/erxepy',  
  author='Tawfik Yasser',
  author_email='tawfekyassertawfek@gmail.com',
  license='MIT', 
  project_urls={
    "Bug Tracker": "https://github.com/TawfikYasser/erxepy/issues",
  },
  classifiers=classifiers,
  keywords='regex', 
  packages=find_packages(),
  install_requires=[''] 
)