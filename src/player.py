"""Player initialization and movement."""

from enum import Enum
import math
import sys

try:
    from direct.actor.Actor import Actor
    from panda3d.core import Vec3
except ModuleNotFoundError:
    sys.stderr.write("Panda3D not found. Check your venv configuration.\n")
    exit()


import controls
import rotation
import invisible_border
from tpp_camera import TPPCamera


class States(Enum):
    STOP = 0
    MOVE = 1


class Player(Actor):
    """Same as in the file's header docstring."""

    def __init__(self):
        """Load and set the player attribiutes."""

        self.RELATIVE_Z_OFFSET_M = 0.0
        self.delta_vector_m = Vec3(0.0)

        self.__ANIM_FPS = 20
        self.__DEFAULT_RELATIVE_YAW_DEG = 180
        self.__SPEED_M_PER_S = {"walk": 2, "run": 6}

        self.__current_anim_frame_idx = 0
        self.__delta_per_frame_m = 0.0  # Normalized step per frame.
        self.__running_is_toggled = False
        self.__state = States.STOP
        self.__timer_ms = 0.0  # Finite-state machine timer.

        try:
            Actor.__init__(self, "../assets/panda3d/samples/roaming-ralph/models/ralph",
                           {"walk": "../assets/panda3d/samples/roaming-ralph/models/ralph-walk",
                            "run": "../assets/panda3d/samples/roaming-ralph/models/ralph-run"})
        except OSError:
            sys.stderr.write("Unable to load the player assets.\n")
            raise

        self.setH(self.__DEFAULT_RELATIVE_YAW_DEG)
        self.setScale(0.4)

    def control(self, tpp_camera: TPPCamera):
        """Change player pos using the "controls" module."""

        invisible_border.limit_actor_movable_area(self)
        tpp_camera.rotate(self.getPos())

        self.__set_state()
        self.__set_delta_per_frame_m()

        if controls.pressed_keys[controls.Keymap.Player.go_left] \
                or controls.pressed_keys[controls.Keymap.Player.go_right]:

            # Move left.
            if controls.pressed_keys[controls.Keymap.Player.go_left]:
                self.__delta_per_frame_m = -self.__delta_per_frame_m

            self.__follow_camera()
            self.__rotate_relatively_to_camera()
            self.__move_in_x_axis(tpp_camera)

        if controls.pressed_keys[controls.Keymap.Player.go_forward] \
                or controls.pressed_keys[controls.Keymap.Player.go_backward]:

            # Move backward.
            if controls.pressed_keys[controls.Keymap.Player.go_backward]:
                self.__delta_per_frame_m = -self.__delta_per_frame_m

            self.__follow_camera()
            self.__rotate_relatively_to_camera()
            self.__move_in_y_axis(tpp_camera)

        self.setZ(self.getZ() + self.delta_vector_m.getZ())
        self.setH(rotation.limit_angle_to_360_deg(self.getH()))

        tpp_camera.change_position(Vec3(0, 0, self.delta_vector_m.getZ()))

    def __follow_camera(self):
        """Rotate the player's back to the camera."""

        self.setH(self.__DEFAULT_RELATIVE_YAW_DEG
                  - (controls.mouse_pos['x']
                     * controls.MOUSE_SENSITIVITY_DEG))

    def __move_in_x_axis(self, tpp_camera: TPPCamera):
        """X-axis movement handling."""

        camera_yaw_deg = base.camera.getH()
        camera_yaw_rad = math.radians(camera_yaw_deg)
        camera_yaw_quarter = rotation.get_angle_quarter(camera_yaw_deg)

        delta_x_m = delta_y_m = 0.0

        if camera_yaw_quarter == 1 or 2:
            delta_x_m = math.cos(camera_yaw_rad) * self.__delta_per_frame_m
            delta_y_m = math.sin(camera_yaw_rad) * self.__delta_per_frame_m

        elif camera_yaw_quarter == 3:
            angle_rad = math.radians(camera_yaw_deg - 90)
            delta_x_m = -math.sin(angle_rad) * self.__delta_per_frame_m
            delta_y_m = math.cos(angle_rad) * self.__delta_per_frame_m

        elif camera_yaw_quarter == 4:
            angle_rad = math.radians(camera_yaw_deg - 180)
            delta_x_m = -math.cos(angle_rad) * self.__delta_per_frame_m
            delta_y_m = -math.sin(angle_rad) * self.__delta_per_frame_m

        self.delta_vector_m.set(delta_x_m, delta_y_m,
                                self.delta_vector_m.getZ())
        self.__set_position(tpp_camera)

    def __move_in_y_axis(self, tpp_camera: TPPCamera):
        """Y-axis movement handling."""

        camera_yaw_deg = base.camera.getH()
        camera_yaw_rad = math.radians(camera_yaw_deg)
        camera_yaw_quarter = rotation.get_angle_quarter(camera_yaw_deg)

        delta_x_m = delta_y_m = 0.0

        if camera_yaw_quarter == 1 or 2:
            delta_x_m = -math.sin(camera_yaw_rad) * self.__delta_per_frame_m
            delta_y_m = math.cos(camera_yaw_rad) * self.__delta_per_frame_m

        elif camera_yaw_quarter == 3:
            angle_rad = math.radians(camera_yaw_deg - 90)
            delta_x_m = -math.cos(angle_rad) * self.__delta_per_frame_m
            delta_y_m = -math.sin(angle_rad) * self.__delta_per_frame_m

        elif camera_yaw_quarter == 4:
            angle_rad = math.radians(camera_yaw_deg - 180)
            delta_x_m = math.sin(angle_rad) * self.__delta_per_frame_m
            delta_y_m = -math.cos(angle_rad) * self.__delta_per_frame_m

        self.delta_vector_m.set(delta_x_m, delta_y_m,
                                self.delta_vector_m.getZ())

        # Move both directions.
        if controls.pressed_keys[controls.Keymap.Player.go_left]:
            if controls.pressed_keys[controls.Keymap.Player.go_forward] \
                    or controls.pressed_keys[
                    controls.Keymap.Player.go_backward]:
                self.delta_vector_m.setX(-self.delta_vector_m.getX())
                self.delta_vector_m.setY(-self.delta_vector_m.getY())

        self.__set_position(tpp_camera)

    def __rotate_relatively_to_camera(self):
        """Mainly relative diagonal to camera movement handling."""

        sqrt_of_2 = math.sqrt(2)
        player_yaw = self.getH()

        if controls.pressed_keys[controls.Keymap.Player.go_left]:
            self.__delta_per_frame_m /= sqrt_of_2

            if controls.pressed_keys[controls.Keymap.Player.go_forward]:
                self.setH(player_yaw + 45)

            elif controls.pressed_keys[controls.Keymap.Player.go_backward]:
                self.setH(player_yaw + 135)

            else:
                self.setH(player_yaw + 90)

        elif controls.pressed_keys[controls.Keymap.Player.go_right]:
            self.__delta_per_frame_m /= sqrt_of_2

            if controls.pressed_keys[controls.Keymap.Player.go_forward]:
                self.setH(player_yaw + 315)

            elif controls.pressed_keys[controls.Keymap.Player.go_backward]:
                self.setH(player_yaw + 225)

            else:
                self.setH(player_yaw + 270)

        elif controls.pressed_keys[controls.Keymap.Player.go_backward]:
            self.setH(player_yaw + 180)

    def __set_delta_per_frame_m(self):
        """Set delta speed and optionally normalize it."""

        if self.__running_is_toggled:
            self.__delta_per_frame_m = self.__SPEED_M_PER_S["run"]
        else:
            self.__delta_per_frame_m = self.__SPEED_M_PER_S["walk"]
        self.__delta_per_frame_m *= globalClock.getDt()

    def __set_position(self, tpp_camera: TPPCamera):
        """Adjust the player position and normalize the main vector."""

        try:
            vector_normalization_ratio = \
                (math.fabs(self.__delta_per_frame_m)
                 - math.fabs(self.delta_vector_m.getZ())) \
                / (math.fabs(self.delta_vector_m.getX())
                   + math.fabs(self.delta_vector_m.getY()))

        except ZeroDivisionError:
            vector_normalization_ratio = 1

        self.delta_vector_m.setX(self.delta_vector_m.getX()
                                 * vector_normalization_ratio)

        self.delta_vector_m.setY(self.delta_vector_m.getY()
                                 * vector_normalization_ratio)

        self.setPos(self.getX() + self.delta_vector_m.getX(),
                    self.getY() + self.delta_vector_m.getY(), self.getZ())

        tpp_camera.change_position(Vec3(self.delta_vector_m.getX(),
                                        self.delta_vector_m.getY(), 0.0))

    def __set_state(self):
        """Set the animations of walking or running or disable it.

        Simple finite-state machine.
        """

        if controls.pressed_keys[controls.Keymap.Player.go_forward] \
                or controls.pressed_keys[controls.Keymap.Player.go_backward] \
                or controls.pressed_keys[controls.Keymap.Player.go_left] \
                or controls.pressed_keys[controls.Keymap.Player.go_right]:
            try:
                delta_frame = self.__ANIM_FPS \
                    / globalClock.getAverageFrameRate()
            except ZeroDivisionError:
                delta_frame = 0

            self.__state = States.MOVE

            if self.__running_is_toggled:
                self.pose("run", int(self.__current_anim_frame_idx))
                self.__current_anim_frame_idx += delta_frame

                if self.__current_anim_frame_idx > self.getNumFrames("run"):
                    self.__current_anim_frame_idx = 0

            else:
                self.pose("walk", int(self.__current_anim_frame_idx))
                self.__current_anim_frame_idx += delta_frame

                if self.__current_anim_frame_idx > self.getNumFrames("walk"):
                    self.__current_anim_frame_idx = 0

        else:
            self.__state = States.STOP
            self.pose("walk", 7)

        if controls.pressed_keys[controls.Keymap.Player.toggle_run]:

            if self.__timer_ms >= controls.KEYPRESS_TIMEOUT_S:
                if self.__running_is_toggled:
                    self.__running_is_toggled = False
                else:
                    self.__running_is_toggled = True
            self.__timer_ms = 0

        self.__timer_ms += globalClock.getDt()
