"""Poorly implemented invisible map border."""

import sys

import errors

try:
    from direct.actor.Actor import Actor
except ModuleNotFoundError:
    sys.stderr.write(errors.PANDA3D_MISSING_ERROR)
    exit()


MOVABLE_AREA_METERS = {"width": 200, "height": 180}


def limit_actor_movable_area(actor: Actor) -> None:
    """Reset a position if exceeded.

    Parameters:
    actor -- model that is somewhere.
    """

    global MOVABLE_AREA_METERS

    pos_x = actor.getX()
    pos_y = actor.getY()

    max_x = MOVABLE_AREA_METERS["width"] / 2
    min_x = -max_x

    max_y = MOVABLE_AREA_METERS["height"] / 2
    min_y = -max_y

    if pos_x < min_x:
        actor.setX(min_x)

    elif pos_x > max_x:
        actor.setX(max_x)

    if pos_y < min_y:
        actor.setY(min_y)

    elif pos_y > max_y:
        actor.setY(max_y)
