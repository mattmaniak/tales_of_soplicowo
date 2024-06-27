import sys

import errors

try:
    from direct.actor.Actor import Actor
    from panda3d.core import CollisionHandlerQueue
    from panda3d.core import CollideMask
    from panda3d.core import CollisionNode
    from panda3d.core import CollisionRay
    from panda3d.core import CollisionTraverser
    from panda3d.core import ModelRoot
except ModuleNotFoundError:
    sys.stderr.write(errors.PANDA3D_MISSING_ERROR)
    exit()


class Physics:
    """Walk on a terrain support."""

    def __init__(self, player: Actor):
        """Collosion handling and physical models creation."""

        self.coll_checker = CollisionTraverser()
        self.coll_handler = CollisionHandlerQueue()  # Collisions list.

        self.player_gravity_ray = player.attachNewNode(
            CollisionNode("player_coll_node"))

        self.player_gravity_ray.node().addSolid(
            CollisionRay(0, 0, 5, 0, 0, -1))
        self.player_gravity_ray.node().setIntoCollideMask(
            CollideMask.allOff())

    def __del__(self):
        """Physical model deletion."""
        self.player_gravity_ray.removeNode()

    def __call__(self, player: Actor, terrain: ModelRoot):
        """Walk on the terrain.

        Parameters:
        terrain -- terrain model to walk on.
        player -- movable human-like model.
        """

        self.coll_checker.addCollider(self.player_gravity_ray,
                                      self.coll_handler)

        self.coll_checker.traverse(terrain)
        terrain_colls = list(self.coll_handler.getEntries())

        if terrain_colls:
            terrain_coll_z = player.RELATIVE_Z_OFFSET_M \
                - player.getZ() \
                + terrain_colls[0].getSurfacePoint(terrain).getZ()

            player.delta_vector_m.setZ(terrain_coll_z)
        self.coll_checker.clearColliders()
