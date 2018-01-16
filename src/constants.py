# Defines the constants the theGarrison will use, such as GPIO pins and TIME
# constants

# GPIO PINS
PUMP_0                          = None
PUMP_1                          = None
PUMP_2                          = None
PUMP_3                          = None

PUMP_RELAY_PINS = [ PUMP_0,
                    PUMP_1,
                    PUMP_2,
                    PUMP_3]

ACTUATOR_UP                     = 1
ACTUATOR_DOWN                   = 0


# TIME UNITS
SECONDS_PER_MIL                 = 0.1
TIME_TO_WAIT_BETWEEN_PRESSES    = 0.5
TIME_TO_EMPTY_OPTIC             = 2.0
ACTUATOR_TRAVEL_TIME            = 2.5

# Stepper Settings
STEPS_PER_CM                    = 810
MOTOR_NUMBER                    = 0
MAX_RIGHT                       = 88
HOME_POSITION                   = 45.5


# Dispenser Locations
# Left
OPTIC_0_LOC                 = 0
PUMP_0_LOC                  = None
OPTIC_1_LOC                 = 18
PUMP_1_LOC                  = None
OPTIC_2_LOC                 = 36
# Center
OPTIC_3_LOC                 = 54
PUMP_2_LOC                  = None
OPTIC_4_LOC                 = 72
PUMP_3_LOC                  = None
OPTIC_5_LOC                 = 88
# Right

PUMP_TO_PIN = { 1: PUMP_0,
                3: PUMP_1,
                6: PUMP_2,
                8: PUMP_3 }

DISPENSER_LOCATIONS             = [ DISPENSER_0_LOC,
                                    PUMP_0_LOC,
                                    DISPENSER_1_LOC,
                                    PUMP_1_LOC,
                                    DISPENSER_2_LOC,
                                    DISPENSER_3_LOC,
                                    PUMP_2_LOC,
                                    DISPENSER_4_LOC,
                                    PUMP_3_LOC,
                                    DISPENSER_5_LOC]
