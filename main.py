from assets.scripts.ecology import *
ecosystem = EcoSytem()

async def main():
    run = True
    while run:
        win.fill((0, 0, 0))
        ecosystem.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
        await asyncio.sleep(0)
    pygame.quit()
    sys.exit()
asyncio.run( main() )