# transcendence
Pong game as single-page web application 

## Technologies
- backend: use NestJS
- frontend: choose a Typescript framework - vue.js? react.js ?
- database: Postgres
  - protect against SQL injection

## Application overview/ required features
- single-page application
- handle back/fwd buttons
- store credentials in .env file and do not committ this file
- support 2 browsers: Chrome and Firefox
- docker-compose up --build
- Login using the OAuth system of 42 intranet
  - two-factor authentication. For instance, Google Authenticator or sending a text message to their phone
  - user login status

- User accounts
  - Password hashing using SHA512
  - has contacts, blocked contacts
  - statistics
  - match history

- Chat
  - channels
  - channel admin
  - see contacts status
  - invite to play Pong

- Pong Game
  - matchmaking
  - queue
  - customisation options
  - handle network issues
    - pause game?
