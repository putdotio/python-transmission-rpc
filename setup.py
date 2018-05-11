from setuptools import setup

setup(
    name='transmission-putio',
    description='Client for Transmission RPC Server',
    version='1.0.2',
    author=u'Cenk Altı',
    author_email='cenkalti@gmail.com',
    url='https://github.com/putdotio/python-transmission-rpc',
    py_modules=['transmission'],
    include_package_data=True,
    zip_safe=True,
    platforms='any',
    install_requires=['requests'],
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
