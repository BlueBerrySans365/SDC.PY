from setuptools import setup
from os.path import join, dirname

setup(name='BSDPY',
      version='1.0.0',
      description='An attempt to recreate the module to work with the server-discord.com API',
      packages=['BSDPY'],
      author='NickSaltFoxu',
      license='MPL-2.0',
      url="https://discord.gg/8Cey77R",
      author_email='senyaprojectg@gmail.com',
      long_description=open(join(dirname(__file__), 'README.MD')).read(),
      long_description_content_type="text/markdown",
      zip_safe=False)