from mcdreforged.api.all import *

from bud.utils import tr, logger
from bud.config import config
from bud.core import register_command


def on_unload(*args, **kwargs):
    logger.unload_file()


def on_load(server: PluginServerInterface, prev_module):
    server.register_help_message(config.primary_prefix, tr('help.mcdr'))
    register_command()
