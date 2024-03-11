#! /usr/bin/env python3

"""The main file where everything begins."""

import sys

try:
    from direct.showbase.ShowBase import ShowBase
    from direct.task.Task import Task
except ModuleNotFoundError:
    sys.stderr.write("Panda3d not found.\n")
    exit()


import controls
from physics import Physics
from tpp_camera import TPPCamera
from world import World


class Application(ShowBase):
    """Start the app using the Panda3D API."""

    def __init__(self):
        """Create the window and start the main loop."""

        ShowBase.__init__(self)
        controls.setup_mouse()
        self.tpp_camera = TPPCamera()

        try:
            self.world = World()
        except OSError:
            raise

        self.physics = Physics(self.world.player)
        base.taskMgr.add(self.__main_loop, "__main_loop")

    def __del__(self):
        """Clean resources."""

        del self.physics
        del self.world
        del self.tpp_camera

    def __main_loop(self, task: Task) -> Task:
        """Refresh between frames.

        Parameters:
        task -- task form a task manager that is also returned to loop
                the function.
        """

        controls.handle_events()
        self.physics(self.world.player, self.world.terrain)

        self.tpp_camera.fly_over_terrain(self.world.player,
                                         self.world.terrain)
        self.world.player.control(self.tpp_camera)

        return Task.cont


if __name__ == "__main__":
    try:
        Application().run()
    except OSError:
        pass
else:
    sys.stderr.write("Do not import the main file.\n")
