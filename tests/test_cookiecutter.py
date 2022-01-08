import contextlib
import os

import pytest
import sh


@contextlib.contextmanager
def chdir(new_dir):
    old_dir = os.getcwd()
    try:
        os.chdir(new_dir)
        yield
    finally:
        os.chdir(old_dir)


@pytest.fixture
def project_name():
    return 'My Voila App'


@pytest.mark.parametrize('preset', ['basic', 'scientific'])
def test_integration(cookies, project_name, preset, venv):
    result = cookies.bake(extra_context=dict(project_name=project_name, preset=preset))

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == 'my-voila-app'
    assert result.project_path.is_dir()

    sh2 = sh.bake(_env={
            'LC_ALL': 'C.UTF-8',
            'LANG': 'C.UTF-8',
            'PATH': f'{venv.bin}:{os.environ["PATH"]}'
            })

    with chdir(result.project_path):
        venv.install('pip-tools')
        with chdir('requirements'):
            try:
                output = sh2.make(
                    ['all', 'install']
                )
            except sh.ErrorReturnCode as e:
                print(e.stderr)
                print(output.exit_code)
        sh2.make(
                ['check']
            )
