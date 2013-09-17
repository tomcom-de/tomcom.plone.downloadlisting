from setuptools import setup, find_packages

version = '4.3.0.1'

tests_require = [
    'plone.app.testing',
    'pyquery'
    ]

setup(name='tomcom.plone.downloadlisting',
      version=version,
      description='A folder listing with recursive content included.. With listing an detail view.',
      long_description=open("README.rst").read() + '\n' +
                       open('CHANGES.rst').read(),
      classifiers=[
        'Framework :: Plone',
        'Framework :: Plone :: 4.3',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
      keywords='tomcom download listing view plone',
      author='tomcom GmbH',
      author_email='mailto:info@tomcom.de',
      url='http://eggserver.tcis.de/tomcom.plone.downloadlisting',
      license='GPL2',
      packages=find_packages(),
      namespace_packages=['tomcom','tomcom.plone'],
      include_package_data=True,
      install_requires=[
        'setuptools',
        'tomcom.plone.ptregistry'

      ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require,
                     ),
      zip_safe=False,
      entry_points='''
[z3c.autoinclude.plugin]
target = plone
''',
)