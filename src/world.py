from player import Player


class World:
    """Just player and terrain inside."""

    def __init__(self):
        """Load an environment."""

        try:
            self.terrain = base.loader.loadModel("../assets/terrain.egg")
            self.player = Player()
            self.player.setZ(1)  # Set higher to "fall" on the terrain.
        except OSError:  # Error during a model/texture loading.
            raise

        self.__render()

    def __del__(self):
        """Clean the environment."""

        del self.player
        del self.terrain

    def __render(self):
        """Show the world."""

        self.terrain.reparentTo(base.render)
        self.player.reparentTo(self.terrain)
