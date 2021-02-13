"""PKONE servo implementation."""
from collections import namedtuple

from mpf.platforms.interfaces.servo_platform_interface import ServoPlatformInterface

PKONEServoNumber = namedtuple("PKONEServoNumber", ["board_address_id", "servo_number"])


class PKONEServo(ServoPlatformInterface):

    """A servo in the PKONE platform."""

    __slots__ = ["number", "platform"]

    def __init__(self, number: PKONEServoNumber, platform: "PKONEHardwarePlatform"):
        """Initialise servo."""
        self.number = number
        self.platform = platform

    def go_to_position(self, position):
        """Set a servo position."""
        if position < 0 or position > 1:
            raise AssertionError("Position has to be between 0 and 1")

        # convert from [0,1] to [0, 250]
        position_numeric = int(position * 255)

        cmd = 'PSC{}{}{}'.format(
            self.number.board_address_id,
            self.number.servo_number,
            position_numeric)

        self.platform.send(cmd)

    def set_speed_limit(self, speed_limit):
        """Not implemented."""

    def set_acceleration_limit(self, acceleration_limit):
        """Not implemented."""
