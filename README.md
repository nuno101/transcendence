# transcendence
Pong game as single-page web application 

FIXME: Delete .env 
FIXME: Remove debug template html files in ./backend/transc/*/templates/*

The project requires 7🔺 major modules to be validated.
🔺 Major module, 🔸 Minor module : 1🔺 = 2🔸


## Technologies
- backend: Django 4.2 🔺 use a Framework as backend. See https://docs.djangoproject.com/en/4.2/intro/
- frontend: vue.js 🔸 use a Front-end framework or toolkit
- database: Postgres 🔸 Use a database
  - protect against SQL injection

## Application overview/ required features
- single-page application
- handle back/fwd buttons
- store credentials in .env file and do not committ this file
- support 2 browsers: Chrome and Firefox
- docker-compose up --build

## User management
  - 🔺 Standard user management, authentication, users across tournaments.
  - has contacts, blocked contacts
  - statistics
  - match history

## Pong Game and user experience
  - matchmaking
  - queue
  - 🔸 Game Customization Options
  - pause game?



## Summary of scores

**Web 2**
- 🔺 **Use a Framework as backend.**
- 🔸 **Use a front-end framework or toolkit.**
- 🔸 **Use a database for the backend.**
- 🔺 Store the score of a tournament in the Blockchain.
  
**User management 2+1**
- 🔺 **Standard user management, authentication, users across tournaments.**
- 🔺 Implementing a remote authentication.
  
**Gameplay and user experience 3+1.5**
- 🔺 Remote players
- 🔺 Multiplayers (more than 2 in the same game).
- 🔺 Add Another Game with User History and Matchmaking.
- 🔸 **Game Customization Options.**
- 🔺 **Live chat.**

**IA-Algo 4.5+0.5**
- 🔺 Introduce an AI Opponent.
- 🔸 User and Game Stats Dashboards

**Cybersecurity 5+0**
- 🔺 Implement WAF/ModSecurity with Hardened Configuration and HashiCorp Vault for Secrets Management.
- 🔸 GDPR Compliance options with user anonymizations, local data management and account deletion
- 🔺 Implement Two-Factor Authentication (2FA) and JWT.

**Devops 5+1**
- 🔺 Infrastructure Setup for Log Management.
- 🔸 Monitoring system.
- 🔺 Designing the Backend as Microservices.

**Graphics 6**
- 🔺 Use of advanced 3D techniques.
  
**Accessibility 6+1**
- 🔸 Support on all devices
- 🔸 **Expanding browser compatibility**
- 🔸 **Multiple language supports.**
- 🔸 Add accessibility for Visually Impaired Users.
- 🔸 Server-Side Rendering (SSR) Integration.
  
**Object oriented 7+0**
- 🔺 Replacing Basic Pong with Server-Side Pong and Implementing an API.
- 🔺 Enabling Pong Gameplay via CLI against Web Users with API Integration.
