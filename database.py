from tortoise import Tortoise

async def init():
    await Tortoise.init(
        db_url="sqlite://./knowledge.db",
        modules={"models": ["app.models"]}
    )
    await Tortoise.generate_schemas()

async def close():
    await Tortoise.close_connections()
