# plugins/sleep_plugin.py
import asyncio

async def slow_hello(*args):
    await asyncio.sleep(2)
    return "👋 Hello after 2 seconds"

def get_commands():
    return {
        "slow": slow_hello
    }
