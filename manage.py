import os
from flask.ext import script
from bbs import create_app
from bbs.models import db

manager = script.Manager(create_app)

# Override the default `runserver` command, to monitor the change of
# the configuration file.
# XXX: `Config.root_path` is an undocumented attribute.
class Server(script.Server):
    def handle(self, app, *args, **kwargs):
        config_path = os.path.join(app.config.root_path, 'config.py')
        self.server_options['extra_files'] = [config_path]
        super(Server, self).handle(app, *args, **kwargs)
manager.add_command('runserver', Server())


db_manager = script.Manager()

@db_manager.command
def create_all():
    db.create_all()

@db_manager.command
def drop_all():
    if script.prompt_bool('This action will DESTROY ALL DATA. Continue'):
        db.drop_all()

manager.add_command('db', db_manager)


if __name__ == '__main__':
    manager.run()
