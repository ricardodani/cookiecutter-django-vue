import os
from fabric.api import local{% if cookiecutter.use_travis == 'y' -%}, env, cd, run, hosts{% endif %}


{% if cookiecutter.use_travis == 'y' -%}
@hosts('root@{{cookiecutter.domain}}')
def deploy():
    """
    Travis is using this function to deploy project
    """
    project_root = '/var/www/{{cookiecutter.project_slug}}/'
    env.user = os.environ['PRODUCTION_USER']
    env.password = os.environ['PRODUCTION_PASSWORD']

    with cd(project_root):
        run("git pull")
        run("docker-compose -f docker-compose-prod.yml up -d --no-deps --build")
        run("docker system prune -af"){% endif %}


def up():
    """
    Locally updates project
    """
    local('docker-compose down')
    local('git pull')
    local('docker-compose up --build')
