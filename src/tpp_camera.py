import math
import sys

try:
    from direct.actor.Actor import Actor
    from panda3d.core import CollisionHandlerQueue
    from panda3d.core import CollideMask
    from panda3d.core import CollisionNode
    from panda3d.core import CollisionRay
    from panda3d.core import CollisionSphere
    from panda3d.core import CollisionTraverser
    from panda3d.core import ModelRoot
    from panda3d.core import Vec3
except ModuleNotFoundError:
    sys.stderr.write("Panda3d not found.\n")
    exit()


import controls
import rotation


class TPPCamera:
    """As in the name.."""

    def __init__(self):
        """Adjust the third-person perspective and camera collision
        models.
        """

        self.__DEFAULT_Y_OFFSET_M = 2.5
        self.__MIN_Y_OFFSET_M = 0.0
        self.__MIN_PITCH_DEG = -90  # Down.
        self.__max_pitch_deg = 0  # Up.

        self.__relative_offset_m = Vec3(1, self.__DEFAULT_Y_OFFSET_M, 1.7)
        self.__ROTATION_RADIUS_M = math.sqrt(
            self.__relative_offset_m.getX()**2 + self.__DEFAULT_Y_OFFSET_M**2
            + self.__relative_offset_m.getZ()**2)

        base.camera.setPos(self.__relative_offset_m)
        base.camLens.setFov(90)

        self.coll_checker = CollisionTraverser()
        self.coll_handler = CollisionHandlerQueue()

        self.vertical_coll_ray = base.camera.attachNewNode(CollisionNode(
            "camera_coll_node"))

        # Look down straight on the terrain to check for collisions.
        self.vertical_coll_ray.node().addSolid(CollisionRay(0, 0, 0, 0, 0, -1))
        self.vertical_coll_ray.node().setFromCollideMask(CollideMask.allOn())

        self.horizontal_coll_sphere = base.camera.attachNewNode(CollisionNode(
            "camera_coll_node"))

        self.horizontal_coll_sphere.node().addSolid(
            CollisionSphere(Vec3(0), 1))
        self.horizontal_coll_sphere.node().setFromCollideMask(
            CollideMask.allOn())

    def change_position(self, player_delta_vector_m: Vec3):
        """Relatively change the camera position.

        Parameters:
        player_delta_vector_m -- 3D vector that describes how
                                 the player has moved in the last
                                 frame.
        """

        base.camera.setPos(base.camera.getX() + player_delta_vector_m.getX(),
                           base.camera.getY() + player_delta_vector_m.getY(),
                           base.camera.getZ() + player_delta_vector_m.getZ())

    def fly_over_terrain(self, player: Actor, terrain: ModelRoot):
        """Set the max_pitch_deg to block the camere if is near
        the terrain to prevent overlapping.

        Parameters:
        player -- player's model.
        terrain -- terrain's model.
        """

        safety_angle_deg = 10

        self.coll_checker.addCollider(self.vertical_coll_ray,
                                      self.coll_handler)
        self.coll_checker.traverse(terrain)
        terrain_colls = list(self.coll_handler.getEntries())

        if terrain_colls:
            terrain_coll_z = terrain_colls[0].getSurfacePoint(terrain).getZ() \
                - player.getZ() - self.__relative_offset_m.getZ()

            negative_max_pitch_radians = math.atan2(
                terrain_coll_z, self.__relative_offset_m.getY())

            self.__max_pitch_deg = -math.degrees(negative_max_pitch_radians) \
                                   - safety_angle_deg
        self.coll_checker.clearColliders()

    def rotate(self, player_delta_vector_m: Vec3):
        """Rotate the camera relatively to the player using the magical
        trigonometry.

        Parameters:
        player_delta_vector_m -- 3D vector that describes how
                                 the player has moved in the last
                                 frame.
        """

        base.camera.setH(-controls.mouse_pos['x']
                         * controls.MOUSE_SENSITIVITY_DEG)

        controls.limit_mouse_pos(self.__MIN_PITCH_DEG, self.__max_pitch_deg)

        if controls.mouse_pos['y'] * controls.MOUSE_SENSITIVITY_DEG \
                < self.__MIN_PITCH_DEG:
            base.camera.setP(self.__MIN_PITCH_DEG)

        elif controls.mouse_pos['y'] * controls.MOUSE_SENSITIVITY_DEG \
                > self.__max_pitch_deg:
            base.camera.setP(self.__max_pitch_deg)

        else:
            base.camera.setP(controls.mouse_pos['y']
                             * controls.MOUSE_SENSITIVITY_DEG)

        camera_yaw_deg = base.camera.getH()
        camera_yaw_rad = math.radians(camera_yaw_deg)
        camera_yaw_quarter = rotation.get_angle_quarter(camera_yaw_deg)

        pos_x_of_x_offset_m = 0
        pos_y_of_x_offset_m = 0

        if camera_yaw_quarter == 1 or 2:
            pos_x_of_x_offset_m = math.cos(camera_yaw_rad) \
                * self.__relative_offset_m.getX()

            pos_y_of_x_offset_m = math.sin(camera_yaw_rad) \
                * self.__relative_offset_m.getX()

        elif camera_yaw_quarter == 3:
            angle_rad = math.radians(camera_yaw_deg - 90)

            pos_x_of_x_offset_m = -math.sin(angle_rad) \
                * self.__relative_offset_m.getX()

            pos_y_of_x_offset_m = math.cos(angle_rad) \
                * self.__relative_offset_m.getX()

        elif camera_yaw_quarter == 4:
            angle_rad = math.radians(camera_yaw_deg - 180)

            pos_x_of_x_offset_m = -math.cos(angle_rad) \
                * self.__relative_offset_m.getX()

            pos_y_of_x_offset_m = -math.sin(angle_rad) \
                * self.__relative_offset_m.getX()

        camera_pitch_rad = math.radians(base.camera.getP())

        # Pitch cosinus - looking down.
        x = player_delta_vector_m.getX() + pos_x_of_x_offset_m \
            + (math.sin(camera_yaw_rad) * self.__relative_offset_m.getY()
               * math.cos(camera_pitch_rad))

        y = player_delta_vector_m.getY() + pos_y_of_x_offset_m \
            + (math.cos(camera_yaw_rad) * -self.__relative_offset_m.getY()
               * math.cos(camera_pitch_rad))

        z = player_delta_vector_m.getZ() + self.__relative_offset_m.getZ() \
            + (math.sin(-camera_pitch_rad) * self.__relative_offset_m.getY())

        base.camera.setPos(x, y, z)
