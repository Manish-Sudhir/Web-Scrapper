from ensurepip import version
from setuptools import setup, find_packages

setup(name="scrapper",
      version='1.0',
      packages=find_packages(),
      install_requires=[
        'selenium',
        'webdriver_manager',
      ])
# setup(name="dashboards",
#       version='1.0',
#       packages=find_packages(),
#       install_requires=[
#         'pandas',
#         'numpy',
#         'requests',
#         'psycopg2-binary',
#         'sqlalchemy',
#         'PyYaml',
#         'hubspot-api-client',
#         'dateparser',
#         'analytics-python',
#         'plotly',
#         'dash',
#         'dash_auth',
#       ])