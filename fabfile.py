from fabric.api import *
import os
import fabric.contrib.project as project

PROD = 'shackman@shackmanpress.com'
DEST_PATH = '/home/shackman/www/portfolio/'
ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
DEPLOY_PATH = os.path.join(ROOT_PATH, 'deploy')

def clean():
    local('rm -rf ./deploy')

def generate():
    local('hyde -g -s .')

def regen():
    clean()
    generate()

def serve():
    local('hyde -w -s . -k')

def reserve():
    regen()
    serve()

def smush():
    local('smusher ./media/images')

@hosts(PROD)
def publish():
    regen()
    project.rsync_project(
        remote_dir=DEST_PATH,
        local_dir=DEPLOY_PATH.rstrip('/') + '/',
        exclude='.htaccess',
        delete=True
    )

