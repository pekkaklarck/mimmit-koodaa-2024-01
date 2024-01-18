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

Status
    Should be positive    1
    Should be positive    7.4
    Should be positive    -2

Errors
    Should be positive    bad

Argument conversion
    Mimmit    koodaa
    Mimmit    BAILAA
    Mimmit    tiskaa

Deprecation
    Deprecated keyword
