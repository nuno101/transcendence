FIXME: Delete .env 
FIXME: Remove debug template html files in ./backend/transc/*/templates/*

Step 1: Project Initialization
Set up your project repository, create a directory structure to separate front-end and back-end code.
{
    /frontend: All the code related to the frontend part of your application.
    /backend: All the code related to the backend part of your application.
    /shared: Any code or assets shared between front-end and back-end, such as TypeScript interfaces or utility functions.
    /deploy: Any scripts, Dockerfiles, and configuration related to deployment.
    README.md: Information about the project, how to set it up, build it, run it, etc.
    .gitignore: List of files and folders to ignore in git version control.
    docker-compose.yml: Configuration to run your entire stack with Docker Compose.

    TODOO: mkdir when u need
    /frontend/src/components: Reusable UI components.
    /frontend/src/services: Services to manage API calls and other side effects.
    /frontend/src/assets: Static assets like images, icons, etc.
    /frontend/src/store: State management (if using Redux, Vuex, etc.).
    /frontend/src/types: TypeScript type definitions and interfaces.
    /backend/src/modules: Group related functionalities (controller, service, etc.) into modules to take advantage of NestJS's modular architecture.
    /backend/src/config: Configuration files and setup.
    /backend/src/middleware: Any middleware to manage HTTP requests and responses.
    /backend/src/interfaces: TypeScript interfaces for structured data in your backend.
}

Initialize npm projects (npm init) in both frontend and backend directories. (???Through docker-compose???)
Set up .gitignore to exclude node_modules and other unnecessary files from your repository.


Step 2: Back-end Setup (NestJS)
Install NestJS CLI (npm i -g @nestjs/cli).
Use nest new my-backend in the backend directory.
Connect NestJS to PostgreSQL using TypeORM.
Install necessary dependencies (npm install @nestjs/typeorm typeorm pg).
Set up a TypeORM config file with your PostgreSQL credentials and entity mappings.
Begin developing basic API endpoints for user authentication and real-time game state updates.
Implement WebSocket for real-time communication between players.


Step 3: Front-end Setup
Choose a TypeScript framework (React, Angular, Vue, etc.) and set up the project in the frontend directory.
Implement basic UI components (e.g., game board, paddle, ball).
Set up a WebSocket client to communicate with your NestJS backend.
Implement user authentication flow (if required) and game state rendering logic using the WebSocket data.


Step 4: Implement Chat
Design chat UI on the front end.
Implement chat functionality using WebSockets to send and receive messages in real-time.
Store chat messages in PostgreSQL, if persistent chat history is required.


Step 5: Implement Multiplayer Game Logic
Define game rules and logic on the backend (movement of the paddle, bouncing of the ball, scoring, etc.)
Synchronize game state among all players in real-time using WebSockets.


Step 6: Single Page Application (SPA) Compliance & Browser Compatibility
Ensure that your frontend app is an SPA. Verify that navigation doesn't reload the page.
Check the compatibility of your website with Google Chrome and another browser of your choice. Ensure all features work smoothly.


Step 7: Error Handling
Implement global error handling in both the front end and back end to manage unexpected issues.
Ensure the user gets appropriate feedback on any error (via UI notifications or alerts).


Step 8: Dockerization
Create a Dockerfile for the backend (NestJS) and frontend separately.
Set up a docker-compose.yml that includes both the frontend, backend, and PostgreSQL database services.
Ensure the application can be built and started using docker-compose up --build.


Step 9: Testing
Implement unit tests for both frontend and backend.
Perform integration and E2E tests to ensure all parts work together as expected.
Test the application in different environments (using Docker) to make sure it works universally.


Step 10: Deployment
Choose a deployment platform.
Set up CI/CD pipelines to automate testing and deployment processes.
Deploy the Dockerized app to the production environment.
Additional Tips:
Version Control: Regularly commit your changes to version control (e.g., Git).
Continuous Feedback: Test your application frequently to ensure it behaves as expected.
Documentation: Maintain clear documentation for your setup and deployment processes, API endpoints, and frontend components.