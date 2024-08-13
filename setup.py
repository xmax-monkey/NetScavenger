from setuptools import setup, find_packages

setup(
    name='NetScavenger',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'python-whois',
        'geoip2'
    ],
    entry_points={
        'console_scripts': [
            'netscavenger=netscavenger.main:ping_website',
        ],
    },
    package_data={
        '': ['GeoLite2-City.mmdb'],
    },
    include_package_data=True,
    description='A simple tool to ping websites and retrieve information',
    author='Dein Name',
    author_email='deine.email@example.com',
    url='https://github.com/xmax-monkey/NetScavenger',
)
