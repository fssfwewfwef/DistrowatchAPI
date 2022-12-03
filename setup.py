from setuptools import setup, find_packages

setup(name='distrowatchapi',

      version='0.1',

      url='https://github.com/vovsss/DistrowatchAPI',

      license='MIT',

      author='vovsss',

      author_email='vova4ka@internet.ru',

      description='Take a top of distributions from distrowatch.com',

      packages=find_packages(exclude=['beautifulsoap4', 'aiohttp']),

      long_description=open('README.md').read(),

      zip_safe=False,

      setup_requires=["aiohttp~=3.8.3", "beautifulsoup4~=4.11.1"]
    )