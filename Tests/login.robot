*** Settings ***
Library     AppiumLibrary
Resource    ../Resources/password.robot

*** Variables ***
#***Test Variables ***
&{USER1-DETAILS}  email=${EMAIL}  password=${PASSWORD}
#*** Login Page ***
${LOGIN-BUTTON}          chat21.android.demo:id/login
${LOGIN-EMAIL-FIELD}     chat21.android.demo:id/email
${LOGIN-PASSWORD-FIELD}  chat21.android.demo:id/password

#*** Main Page ***
${MAIN-HOME-TAB}  //android.widget.TextView[@text="HOME"]
*** Test Cases ***
open application
    open application  http://localhost:4723    platformName=Android    appActivity=chat21.android.demo  automationName=Uiautomator2  deviceName=emulator-5554
    Wait Until Page Contains Element    ${LOGIN-EMAIL-FIELD}
    Input Text  ${LOGIN-EMAIL-FIELD}  ${USER1-DETAILS}[email]
    Input Text  ${LOGIN-PASSWORD-FIELD}  ${USER1-DETAILS}[password]
    Click Element
        ${LOGIN-BUTTON}
    Wait Until Page Contains Element    ${MAIN-HOME-TAB}