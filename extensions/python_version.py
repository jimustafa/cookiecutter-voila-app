import platform

from jinja2.ext import Extension


class PythonVersion():
    def __str__(self):
        version = platform.python_version_tuple()

        return f'{version[0]}.{version[1]}'


class PythonVersionExtension(Extension):
    def __init__(self, environment):
        super(PythonVersionExtension, self).__init__(environment)

        environment.globals['python_version'] = PythonVersion()
