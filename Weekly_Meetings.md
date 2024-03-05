# 2024-02-28 Discord meeting:
Attended by all.

Jan:
- wants to improve the game physics
- another week and it should be done

Julia:
- welcome page footer added
- dashboard removed
- websockets based notifications working
- statistics of users to be updated to remove restrictions (all users can see all statistics)
- Online Status on FriendsView
- UserStatsView instead of ProfileView
- * [ ] create reusable avatar component
- * [ ] create reusable component for FriendsView tables
- * [ ] All StatsTables in one component
* [ ] Implement second player authentication for onsite game

Anouk:
- tournament logic implementation
- rendering of tournaments

Nuno:
- added pull requests review with Robert: everyone fine with it
- wants to finalise the games logic 
- suggests freezing each module when good enough and asking someone who was not involved in its development to do some  independent testing/ review


Robert:
- will work in the chat also to learn Vue.js
* [ ] Implement automatic check for user serialization to decide if private output should be included, e.g. online status in case requesting user is a friend 
* [ ] Fix avatars not updating
* [ ] ~~Fix/Fully implement user online status -> current state enough?~~
* [ ] Implement chat
  * [x] Implement listing of channels
  * [x] Implement feature to select the channel to view the messages of
  * [x] Implement feature to send messages in a channel
  * [x] Implement feature to delete messages in a channel
  * [ ] Implement feature to create new channel
  * [ ] Implement feature to delete (or leave?) channels
  * [ ] Implement feature to add users to channels
  * [ ] Implement feature to remove users from channels
  * [ ] Implement feature to block/unblock user
* [ ] Add endpoint/feature to check if user credentials are correct without logging in


# 2024-02-20 Discord meeting:
Attended by all.

Jan:
* bug fixing on header component
* working on collision detection and ball speed issues game in separate branch to improve current game

Jmatheis:
* avatar working. Nuno reports some issues
* working on notifications but not yet ready to push to main

Amechain:
* working on the tournaments page
* added users.tournaments join table to keep track of users joining a tournament
* some discussion with Nuno about state handling logic. Only creator can change a tournament state/status. To change state use PATCH /tournamnets/tournament_id/ with payload { status: "next" } of { status: "cancel" }

Nuno:
* added simple tournaments state handling. Robert has reviewed patched some issues
* tournament.status to allow changes only by the creator
* asked Robert about how to use Postman with authentication (demo after the meeting)
  
Robert:
* [ ] Check and implement where websocket events are still missing
* [ ] Add avatar functionality in backend
  * [ ] Implement system so that if user updates the old image deleted so that the user can't create unused avatars on the server file system
  * [ ] Fix avatars not updating correctly
* [x] ~~Add parameter type verification/validation in endpoint structure~~ --> Can be implemented via model field limit
* [x] ~~Add parameter min/max validation in endpoint structure~~ --> Can be implemented via model field limit
* [x] Implement max/min limits for game score --> Limits set at django model level


# 2024-02-13 Discord meeting:

Jan:
* Header and Login improved, some bug-fixing and features
* Plans to work in the game.

Julia:
* worked in the friends page
* few bugs on the game edges
* scores are POSTed to the backend
* avatar to be added to pages. Some issue prefix
* plans to work in the notifications

Nuno:
* adding logic or a state-machine for managing the tournaments & games.

Robert:
* [ ] Add avatar functionality in backend
  * [x] Implement working default avatar
  * [ ] Implement system so that if user updates the old image deleted so that the user can't create unused avatars on the server file system
* [x] to check with Julia about the avatars
* [x] Improve error checking/exception handling for PATCH endpoints updating database models
* [ ] ~~Add parameter type verification/validation~~
* [ ] ~~Extend/Improve functionality of automatic http api documentation generation?~~
* [ ] ~~Implement creating of notifications in database for relevant things like friend requests, etc.~~
* [ ] ~~Make use of notification system, e.g. for the creation of a friend request, etc~~ -> Creating notifications will be moved to the frontend

# 2024-02-06 Discord meeting:
Attended by Anouk, Jan, Julia, Robert

Robert:
* [ ] Add avatar functionality in backend
  * [x] Add basic avatar implementation in database, filesystem and endpoints
  * [ ] Implement system so that if user updates the old image deleted so that the user can't create unused avatars on the server file system
  * [ ] Implement working default avatar
* [ ] Implement creating of notifications in database for relevant things like friend requests, etc.
* [ ] Make use of notification system, e.g. for the creation of a friend request, etc
* [x] Add websocket event for notification creation
* [ ] Extend/Improve functionality of automatic http api documentation generation
  * [ ] ~~Endpoint method description~~
  * [ ] ~~Response code documentation (and description?)~~
  * [ ] ~~Min/Max checking for integer values?~~
* [ ] ~~Add documentation for valid endpoint responses in endpoint structure (code, description, return format?, etc.)~~
  * [ ] ~~Activate response code check middleware once responses are documented~~

# 2024-01-30 Discord meeting:
Attended by Anouk, Jan, Julia, Robert

Robert:
* [x] Implement basic notification system/endpoints to inform user about new events
* [ ] Make use of notification system, e.g. for the creation of a friend request, etc
* [x] Add notification endpoints for frontend
* [ ] Add websocket event for notification creation
* [x] Change game model so that it doesn't need a relationship with a tournament
* [ ] Extend/Improve functionality of automatic http api documentation generation
  * [ ] Endpoint method description
  * [x] Query-/Body parameter tables
  * [ ] Response code documentation (and description?)
  * [ ] Min/Max checking for integer values?
* [x] Extend/Fully implement middleware used verify request query and body parameters
  * [x] Implemented it instead as global method_decorator that should be used for every endpoint class because I was not able to determine the endpoint url in middleware
* [x] Implement middleware to verify valid response(-code) is sent
  * [x] Is only active if django is in debug mode
* [ ] Add documentation for valid endpoint responses in endpoint structure (code, description, return format?, etc.)
  * [ ] Activate response code check middleware once responses are documented

Julia:
* working on FriendsView.vue
* finish Game with requests
* implement notification for friends requests/general messages

# 2024-01-24 Discord meeting:
Attended by all.

Jan:
* new nginx container configured as a proxy
* to be checked again when the SSL certificate is used
* working on authentication and some discussion about cookie management

Anouk:
* working on the tournament
* registration for tournament to be performed by each user separately
* add property display_name/ nickname for playing tournaments
* tournaments visible to all

Nuno:
* will try to add API tests to check the entry-points

Julia:
* some discussion about the remote games
* working on the profile & friends page
* fix edge cases ball collision (game)

Robert:
* [ ] Try to find out how to do the remote authentication module
* [x] Will look at the modules that are currently not being worked on (Log management, Monitoring system, etc.)
* [x] Work on game and tournament endpoints to fit needs of frontend team

# 2024-01-16 Slack meeting:
Attended by all.

## Weekly Meetings:
- weekly meeting agreed for every Tuesday at 10am.

## Goals for next week:

Jan:
* work in the frontend
* unavailable Friday

Julia:
* wants to check Pong Game in vanilla Javascript

Nuno:
* documentation about how to initialise application
* API documentation
* automatic tests and load DB
* will be more available after week 6.

Anouk:
* asks to share info when meeting onsite

## Blackhole status:
* Julia: 22nd of March + 1 freeze
* Anouk: has 2? freezes and about 30? days left
* Nuno: 124 days (May)
* Jan and Robert: August…
