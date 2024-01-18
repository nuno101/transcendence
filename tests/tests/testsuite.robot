*** Settings ***
Library    RequestsLibrary

*** Variables ***

*** Test Cases ***
Quick Get Request Test
    ${response}=    GET  http://localhost:8000

GET an existing user, notice how the schema gets more accurate
    ${response}=    GET  http://localhost:8000/users/1                  # this creates a new instance
    Should Be Equal As Strings    1  ${response.json()}[user][id]

