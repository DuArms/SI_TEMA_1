import cripto
import key_manager
import constants

vec = [cripto, constants, key_manager]

string = ""

for module in vec:
    help(module)
