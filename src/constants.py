# Defines the constants the theGarrison will use, such as GPIO pins and TIME
# constants

# GPIO PINS
PUMP_1                          = None
PUMP_2                          = None
PUMP_3                          = None
PUMP_4                          = None
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


# Dispenser Locations
DISPENSER_0_LOC                 = 0
DISPENSER_1_LOC                 = 18
DISPENSER_2_LOC                 = 36
DISPENSER_3_LOC                 = 54
DISPENSER_4_LOC                 = 72
DISPENSER_5_LOC                 = 88
DISPENSER_LOCATIONS             = [ DISPENSER_0_LOC,
                                    DISPENSER_1_LOC,
                                    DISPENSER_2_LOC,
                                    DISPENSER_3_LOC,
                                    DISPENSER_4_LOC,
                                    DISPENSER_5_LOC] 
