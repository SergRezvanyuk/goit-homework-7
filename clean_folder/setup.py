from setuptools import setup, find_namespace_packages


setup(
    name='clean_folder',
    version='1.1.3',
    description='T.7 Clean_folder',
    url='http://github.com/dummy_user/useful',
    author='Sergii Rezvaniuk',
    author_email='o_serg@ukr.net',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean-folder=clean_folder.clean:main']}
)