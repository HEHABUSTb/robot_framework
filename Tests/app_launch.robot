*** Settings ***
Library     AppiumLibrary

*** Variables ***
${LOGIN-BUTTON}     chat21.android.demo:id/login
*** Test Cases ***
open application
    open application  http://localhost:4723    platformName=Android    appActivity=chat21.android.demo  automationName=Uiautomator2  deviceName=emulator-5554
    Wait Until Page Contains Element    ${LOGIN-BUTTON}