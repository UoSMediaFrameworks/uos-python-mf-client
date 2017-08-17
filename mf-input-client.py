import click

from click_repl import register_repl
from mf_client.MF_API_Client import *

# dev scenes
# "586f8524b8678acc10b1595c"
# "596636589d6362d01a6374d9"

# Setup an authenticated connection to a controller
mf_ws_in_client = MF_API_Client('http://localhost', 6000, 'kittens')
session_roomid = ""

@click.group()
def cli():
    pass


@cli.command()
def hello():
    """Hello world."""
    click.echo("Hello world!")


@cli.command()
@click.option('--roomid', prompt='Set a display id for REPL session',
              help='If you wish to set a roomid for a session use this command')
def set_display_room_for_session(roomid):
    """Set a display room for the session."""
    global session_roomid
    session_roomid = roomid
    click.echo('Set room id for session (roomid:' + session_roomid + ')')


@cli.command()
@click.option('--roomid', prompt='Enter display id', help='Display room identifier')
@click.option('--sceneid', prompt='Enter scene id', help='Scene identifier you wish to play')
def play_scene(roomid, sceneid):
    """Play a scene on a display."""
    # APEP testing out a concept of setting a roomid for the command console session, we may wish to improve this
    if len(roomid) == 0 and len(session_roomid) != 0:
        roomid = session_roomid

    mf_ws_in_client.sendScene(roomid, sceneid)
    click.echo('Sent command')


@cli.command()
@click.option('--roomid', prompt='Enter display id')
@click.option('--sceneid', prompt='Enter a scene id')
@click.option('--theme', prompt='Enter a theme')
def play_scene_theme(roomid, sceneid, theme):
    """Play a scene and specific theme on a display."""
    mf_ws_in_client.sendScenesAndThemes(roomid, [sceneid], [theme])
    click.echo('Sent command')


@cli.command()
@click.option('--sceneName', help='Find a scene identifier by scene name')
def find_scene_by_name(scene_name):
    """Not yet implemented."""
    click.echo('Not implemented in client library yet')

register_repl(cli)

if __name__ == '__main__':
    cli()
