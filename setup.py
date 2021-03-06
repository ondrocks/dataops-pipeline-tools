from setuptools import setup, find_packages

long_description = '''
DataOps Pipeline Tools is a library that contains functions used regularly in
data ETL jobs by the DataOps team
'''

setup(
    name='dataops_pipeline_tools',
    version='0.0.5',
    url='https://github.com/puppetlabs/dataops-pipeline-tools',
    author_email='bizappdev@puppet.com',
    packages=['dataops_pipeline_tools'],
    license='Apache License 2.0',
    install_requires=[
        'requests==2.23.0',
        'bigquery-schema-generator==0.5.1',
        'jsonlines==1.2.0'
    ],
    keywords=['DataOps', 'Pipeline'],
    description='Python Library for DataOps functions',
    long_description=long_description,
)
