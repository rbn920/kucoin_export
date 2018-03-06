from setuptools import setup

setup(
    name='kucoin_export',
    version='0.1',
    install_requires=[
        'pandas',
        'ccxt',
        'privy',
        'cfscrape',
        'click'
    ],
    entry_points='''
    [console_scripts]
    kucoin=kucoin:cli
    '''
)
