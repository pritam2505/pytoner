from distutils.core import setup

setup(name="pytoner",
      version='svn',
      description='Printer toner stock',
      url="http://code.google.com/p/pytoner",
      author='Mathieu Gauthier-Lafaye',
      author_email='mathgl@freesurf.fr',
      packages=['toner', 'toner.core', 'toner.dao', 'toner.models',
                'toner.views', 'toner.views.qt', 'toner.views.console', 
                'toner.controlers', 'toner.controlers.qt', 'toner.controlers.console']
      )

