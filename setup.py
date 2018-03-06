from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='cli',
      version='0.1',
      description='simple command line interface module for program menus',
      long_description=readme(),
      url='',
      author='Vinzenz G Eck',
      author_email='vinzenz@eck-mail.eu',
      classifiers=[
        'Development Status :: 1 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
      ],
      license='MIT',
      packages=['cli'],
      install_requires=[], # add dependencies
      include_package_data=True,
      zip_safe=False)

