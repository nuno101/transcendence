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
   
The project now required 7 major modules (2 minors is equals to 1 major) to be validated.
🔺 Major module, 🔸 Minor module

**Web**
- 🔺 Use a Framework as backend.
- 🔸 Use a front-end framework or toolkit.
- 🔸 Use a database for the backend.
- 🔺 Store the score of a tournament in the Blockchain.
  
**User management**
- 🔺 Standard user management, authentication, users across tournaments.
- 🔺 Implementing a remote authentication.
  
**Gameplay and user experience**
- 🔺 Remote players
- 🔺 Multiplayers (more than 2 in the same game).
- 🔺 Add Another Game with User History and Matchmaking.
- 🔸 Game Customization Options.
- 🔺 Live chat.

**IA-Algo**
- 🔺 Introduce an AI Opponent.
- 🔸 User and Game Stats Dashboards

**Cybersecurity**
- 🔺 Implement WAF/ModSecurity with Hardened Configuration and HashiCorp Vault for Secrets Management.
- 🔸 GDPR Compliance options with user anonymizations, local data management and account deletion
- 🔺 Implement Two-Factor Authentication (2FA) and JWT.

**Devops**
- 🔺 Infrastructure Setup for Log Management.
- 🔸 Monitoring system.
- 🔺 Designing the Backend as Microservices.

**Graphics**
- 🔺 Use of advanced 3D techniques.
  
**Accessibility**
- 🔸 Support on all devices
- 🔸 Expanding browser compatibility
- 🔸 Multiple language supports.
- 🔸 Add accessibility for Visually Impaired Users.
- 🔸 Server-Side Rendering (SSR) Integration.
  
**Object oriented**
- 🔺 Replacing Basic Pong with Server-Side Pong and Implementing an API.
- 🔺 Enabling Pong Gameplay via CLI against Web Users with API Integration.
