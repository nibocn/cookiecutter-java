#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
import codecs
import subprocess


PROJECT_DIRECTORY = os.getcwd()
CODE_QUALITY_CHECK = {% if cookiecutter.code_quality_check == 'yes' %}True{% else %}False{% endif %}
CODE_QUALITY_CHECK_PATH = os.path.join(PROJECT_DIRECTORY, 'quality')
CVS = '{{ cookiecutter.cvs }}'
JACOCO_PLUGIN = '{{ cookiecutter.jacoco_plugin }}'

print('Project Directory: {}\n'.format(PROJECT_DIRECTORY))


def run(command, log=True):
    """A quick-and-dirty function that mimicks the fabric library local run.
    """
    try:
        output = codecs.decode(subprocess.check_output(command), 'utf-8')
    except subprocess.CalledProcessError as error:
        print('{}: {}\n{}'.format(error.returncode, error.cmd, error.output))
        raise error
    else:
        if output and log:
            print('{}\n{}'.format(' '.join(command), output))
        else:
            print(' '.join(command))
    return output


def init_cvs_repo():
  if CVS == 'git':
    print('Initializing Git Repo...')
    run(['git', 'init'])
    run(['git', 'add', '-A'], False)
    run(['git', 'commit', '-m', 'Initial commit'])
  elif CVS == 'svn':
    print('Initializing SVN Repo...')
    os.remove(os.path.join(PROJECT_DIRECTORY, 'gradle/install-git-hooks.gradle'))
  else:
    print('Skip CVS initial.')
    os.remove(os.path.join(PROJECT_DIRECTORY, '.gitignore'))


def remove_code_quality_file():
  if not CODE_QUALITY_CHECK:
    print("Removing '{}'...".format(CODE_QUALITY_CHECK_PATH))
    os.remove(os.path.join(PROJECT_DIRECTORY, 'gradle/checkstyle.gradle'))
    os.remove(os.path.join(PROJECT_DIRECTORY, 'gradle/findbugs.gradle'))
    os.remove(os.path.join(PROJECT_DIRECTORY, 'gradle/pmd.gradle'))
    shutil.rmtree(CODE_QUALITY_CHECK_PATH)


def remove_jacoco_file():
  if JACOCO_PLUGIN == 'no':
    jacoco_file_path = os.path.join(PROJECT_DIRECTORY, 'gradle/jacoco.gradle')
    print("Removing '{}'...".format(jacoco_file_path))
    os.remove(jacoco_file_path)


def clean_file():
  if not CODE_QUALITY_CHECK or CVS != 'git':
    os.remove(os.path.join(PROJECT_DIRECTORY, 'gradle/install-git-hooks.gradle'))
    shutil.rmtree(os.path.join(CODE_QUALITY_CHECK_PATH, 'hooks'))


def main():
  clean_file()
  remove_code_quality_file()
  remove_jacoco_file()
  init_cvs_repo()


if __name__ == '__main__':
  main()
