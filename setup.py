from setuptools import setuptools

setup(name='wordsearch',
      version='0.1.0',
      description='find them words',
      url='https://github.com/amclen/wordsearch',
      author='amclen',
      author_email='andrew.mclenigan@gmail.com',
      packages=['src'],
      entry_points=(
          'console_scripts': ['wordsearch=src.__main__:main']
      ),
      include_package_data=True,
      zip_safe=False
)
