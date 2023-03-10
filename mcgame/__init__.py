__version__ = "0.0.1"


from beet import Context
from beet.contrib.load import load
from bolt import bolt


def beet_default(ctx: Context):
    ctx.require(
        load(
            data_pack={
                "data/mcgame/modules": "@mcgame/modules",
            },
        ),
    )
