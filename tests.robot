*** Settings ***
Library             Library.py

*** Test Cases ***
First example
    Example keyword

Arguments
    One argument    Robot
    One Argument    Mimmit
    Three arguments    a    b    c
    Default values    Robot
    Default values    Robot    !!!
    Default values    Robot    ending=!?!?
    Default values    Kitty    separator=${SPACE}

Returning values
    ${value} =    Upper    Robot
    Should be equal    ${value}    ROBOT
