#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import typing

import commands2
import commands2.button
import wpilib
import romi

from commands.arcadedrive import ArcadeDrive
from commands.drivedistance import DriveDistance

from subsystems.drivetrain import Drivetrain


class RobotContainer:
    """
    This class is where the bulk of the robot should be declared. Since Command-based is a
    "declarative" paradigm, very little robot logic should actually be handled in the :class:`.Robot`
    periodic methods (other than the scheduler calls). Instead, the structure of the robot (including
    subsystems, commands, and button mappings) should be declared here.
    """

    def __init__(self) -> None:
        # The robot's subsystems are defined here
        self.drivetrain = Drivetrain()

        # You can put robot's commands here, but you don't have to

        # Assume that joystick "j0" is plugged into channnel 0
        self.j0 = wpilib.Joystick(0)

        self._configureButtonBindings()

    def _configureButtonBindings(self):
        """Use this method to define your button->command mappings. Buttons can be created by
        instantiating a :class:`.GenericHID` or one of its subclasses (:class`.Joystick or
        :class:`.XboxController`), and then passing it to a :class:`.JoystickButton`.
        """

        # 1. Here is a command to drive forward 10 inches with speed 0.5
        cmd_drive_forward_10inch = DriveDistance(0.5, 10, self.drivetrain)
        #  - a trigger attached to joystick button "A" pressed *later* (therefore "lambda")
        btn_a = commands2.button.Trigger(lambda: self.j0.getRawButton(1))
        #  - hooking the command to whenever the trigger turns "true" (button becomes pressed)
        btn_a.onTrue(cmd_drive_forward_10inch)

        # 2. Here is a command to drive back 10 inches with speed 0.5
        cmd_drive_back_10inch = DriveDistance(-0.5, 10, self.drivetrain)
        #  - exercise A1: can you make a trigger for button "B" pressed *later* ??

        #  - exercise A2: can you hook this command to drive back 10 inches to that button?

        # 3. Finally, a command to take input from joystick *later* (lambda) and drive using that input as signal
        cmd_arcade_drive = ArcadeDrive(
            self.drivetrain,
            lambda: self.j0.getRawAxis(0),
            lambda: self.j0.getRawAxis(1),
        )
        # It will be running *by default* on drivetrain
        # ("by default" means it will stop running once some other command is asked is "using" drivetrain
        # , and will restart running again after this)
        self.drivetrain.setDefaultCommand(cmd_arcade_drive)

    def getAutonomousCommand(self) -> typing.Optional[commands2.Command]:
        # - exercise B1: can you make a command to drive 20 inches forward at max speed?

        # - exercise B2: can you return this command instead of None?
        return None
