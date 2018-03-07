from setuptools import setup

setup(
    name='kucoin_export',
    version='0.2.1',
    py_modules=['kucoin'],
    install_requires=[
        'pandas',
        'ccxt==1.10.1271',
        'privy',
        'cfscrape',
        'click'
    ],
    python_requires='>=3',
    entry_points='''
    [console_scripts]
    kucoin=kucoin:cli
    '''
)
