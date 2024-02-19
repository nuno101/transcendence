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
* to check with Julia about the avatars
* [ ] Websocket system bugfixing
* [ ] Add avatar functionality in backend
  * [ ] Implement system so that if user updates the old image deleted so that the user can't create unused avatars on the server file system
  * [x] Implement working default avatar
* [ ] Implement creating of notifications in database for relevant things like friend requests, etc.
* [ ] Make use of notification system, e.g. for the creation of a friend request, etc
* [ ] Extend/Improve functionality of automatic http api documentation generation?

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
