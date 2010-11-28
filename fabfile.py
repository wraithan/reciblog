from fabric.api import env, run, cd, sudo, local, get


env.hosts = ['wraithan.net', ]
deploy_dir = '/srv/wsgi/reciblog/'

dumpdata_apps = 'admin blog auth messages recipes sites south tagging webdesign'
json_fixture = 'live_data.json'

def virtualenv_run(cmd):
    run('workon reciblog && ' + cmd)


def virtualenv_local(cmd):
    local('workon reciblog && ' + cmd)


def deploy():
    git_pull()
    install_requirements()
    sync_db()
    reload_code()


def install():
    make_deploy_dir()
    git_clone()
    make_virtualenv()
    install_requirements()
    start_gunicorn()
    install_nginx_conf()
    enable_nginx_conf()
    reload_nginx_conf()
    create_db()
    sync_db()

def load_data_from_live():
    reset_data()
    dump_live_data()
    load_live_data()


def full_restart_gunicorn():
    stop_gunicorn()
    start_gunicorn()


def make_deploy_dir():
    sudo('mkdir ' + deploy_dir)
    sudo('chown wraithan:users ' + deploy_dir)


def git_clone():
    with cd('/srv/wsgi/'):
        run('git clone git@github.com:wraithan/reciblog.git')


def git_pull():
    with cd(deploy_dir):
        run('git pull')


def make_virtualenv():
    run('mkvirtualenv --no-site-packages reciblog')


def install_requirements():
    with cd(deploy_dir):
        virtualenv_run('pip install -r deploy-requirements.txt')


def start_gunicorn():
    with cd(deploy_dir):
        virtualenv_run('gunicorn_django --pid=' + deploy_dir +
                       '/gunicorn.pid --workers=8 -b 127.0.0.1:8002 --daemon deploy_settings.py')

def stop_gunicorn():
    with cd(deploy_dir):
        sudo('kill `cat gunicorn.pid`')


def install_nginx_conf():
    sudo('cp ' + deploy_dir +
         '/conf/reciblog /etc/nginx/sites-available/reciblog')


def enable_nginx_conf():
    sudo('ln -s /etc/nginx/sites-available/reciblog'
         '/etc/nginx/sites-enabled/reciblog')


def reload_nginx_conf():
    sudo('/etc/rc.d/nginx check')
    sudo('/etc/rc.d/nginx reload')


def create_db():
    run('createdb reciblog')


def sync_db():
    with cd(deploy_dir):
        virtualenv_run('./manage.py migrate')


def reload_code():
    with cd(deploy_dir):
        sudo('kill -HUP `cat gunicorn.pid`')


def reset_data():
    local('./manage.py flush', capture=False)


def dump_live_data():
    with cd(deploy_dir):
        virtualenv_run('./manage.py dumpdata %s > %s' % (dumpdata_apps, json_fixture))
    get('%s/%s' % (deploy_dir, json_fixture), '/home/wraithan/devel/reciblog/')


def load_live_data():
    with cd('/home/wraithan/devel/reciblog'):
        local('./manage.py loaddata %s' % json_fixture)
        local('rm %s' % json_fixture)
    with cd(deploy_dir):
        virtualenv_run('rm %s' % json_fixture)
