# import logging.config
# from os import path
#
# lof_file_path = path.join(path.dirname(path.abspath(__file__)),'logging.ini')
# logging.config.fileConfig(lof_file_path)

pytest_plugins = [
    'src.browser'
]
