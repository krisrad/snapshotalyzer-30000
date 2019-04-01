from setuptools import setup

setup(
    name='snapshotalyzer-30000',
    version='0.1',
    author='RK Meiappan',
    author_email='RK_meiappan@geniusworld.com',
    description="snapshotalyzer-30000 is a tool to manage AWS EC2 snapshots",
    license='None',
    packages=['shotty'],
    url="https://github.com/krisrad/snapshotalyzer-30000",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.ec2main:cli
    '''
)
