from setuptools import setup

setup(name='pbixrefresher',
      version='0.1.8',
      description='Script for refreshing and publishing Power BI workbooks',
      url='https://github.com/marv2410/pbixrefresher-python',
      author='mro',
      author_email='god.bless.ec@gmail.com',
      license='MIT',
      packages=['pbixrefresher'],
      install_requires=[
          'pywinauto',
          'psutil'
      ],
	  entry_points = {
        "console_scripts": ['pbixrefresher = pbixrefresher.pbixrefresher:main']
        },
      zip_safe=False)
