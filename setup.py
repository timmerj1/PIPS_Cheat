from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='pipscheat',
    url='https://github.com/timmerj1/PIPS_Cheat',
    author='Jeroen Timmerman',
    author_email='timmerman.jeroen@gmail.com',
    # Needed to actually package something
    packages=['pipscheat'],
    # Needed for dependencies
    install_requires=['numpy', 'importlib_resources'],
    # *strongly* suggested for sharing
    version='0.1.2',
    # The license can be anything you like
    license='MIT',
    description='Python packeage to cheat on PIPS Python assignments.',
    # We will also need a readme eventually (there will be a warning)
    long_description=open('README.md', encoding="utf8").read(),
    include_package_data=True
)