from assets.scripts.ecology import *
ecosystem = EcoSytem()
async def main():
    while True:
        win.fill((0, 0, 0))
        ecosystem.update()
        pygame.display.update()
        await asyncio.sleep(0)
asyncio.run( main() )