*** Settings ***
Library    RequestsLibrary

*** Test Cases ***
GET an existing user, notice how the schema gets more accurate
    GET         /users/1                  # this creates a new instance
    Output schema   response body
    Object      response body             # values are fully optional
    Integer     response body id          1
    String      response body name        nuno
    String      response body fullname    Nuno
    [Teardown]  Output schema             # note the updated response schema
