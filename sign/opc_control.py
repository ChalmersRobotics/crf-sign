from discord.ext import commands
import opc


class OpcControl(commands.Cog):
    def __init__(self, bot, address):
        self.bot = bot

        self.opcClient = opc.Client(address)

        if self.opcClient.can_connect():
            print('connected to %s' % address)
        else:
            # We could exit here, but instead let's just print a warning
            # and then keep trying to send pixels in case the server
            # appears later
            print('WARNING: could not connect to %s' % address)

