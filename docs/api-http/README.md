# Statistics

Total number of urls: 31

Total number of methods: 52
# Table of Contents

- [/login](#login)
- [/logout](#logout)
- [/users/me](#users-me)
- [/users/me/avatar](#users-me-avatar)
- [/users/me/blocked](#users-me-blocked)
- [/users/me/blocked/USER_ID](#users-me-blocked-USER_ID)
- [/users/me/channels](#users-me-channels)
- [/users/me/friends](#users-me-friends)
- [/users/me/friends/USER_ID](#users-me-friends-USER_ID)
- [/users/me/friends/requests](#users-me-friends-requests)
- [/users/me/friends/requests/REQUEST_ID](#users-me-friends-requests-REQUEST_ID)
- [/users/me/notifications](#users-me-notifications)
- [/users/me/notifications/NOTIFICATION_ID](#users-me-notifications-NOTIFICATION_ID)
- [/users](#users)
- [/users/USER_ID](#users-USER_ID)
- [/users/USER_ID/avatar](#users-USER_ID-avatar)
- [/users/USER_ID/games](#users-USER_ID-games)
- [/users/USER_ID/games_upcoming](#users-USER_ID-games_upcoming)
- [/tournaments](#tournaments)
- [/tournaments/TOURNAMENT_ID](#tournaments-TOURNAMENT_ID)
- [/tournaments/TOURNAMENT_ID/play](#tournaments-TOURNAMENT_ID-play)
- [/tournaments/TOURNAMENT_ID/games](#tournaments-TOURNAMENT_ID-games)
- [/games](#games)
- [/games/GAME_ID](#games-GAME_ID)
- [/channels](#channels)
- [/channels/CHANNEL_ID](#channels-CHANNEL_ID)
- [/channels/CHANNEL_ID/members](#channels-CHANNEL_ID-members)
- [/channels/CHANNEL_ID/members/USER_ID](#channels-CHANNEL_ID-members-USER_ID)
- [/channels/CHANNEL_ID/messages](#channels-CHANNEL_ID-messages)
- [/messages](#messages)
- [/messages/MESSAGE_ID](#messages-MESSAGE_ID)

# Endpoint description

## login

### POST

<table>

<tr><th>Query Parameters</th><th></th></tr>

<tr><td>remember</td><td>
<table>

<tr><td>type</td><td>boolean</td></tr>

<tr><td>required</td><td>False</td></tr>

<tr><td>default</td><td>False</td></tr>

<tr><td>description</td><td>If false, the session will be deleted after the browser is closed</td></tr>

</table>

</td></tr>

</table>

<table>

<tr><th>Body Parameters</th><th></th></tr>

<tr><td>username</td><td>
<table>

<tr><td>type</td><td>string</td></tr>

<tr><td>required</td><td>True</td></tr>

<tr><td>description</td><td>Username of the user</td></tr>

</table>

</td></tr>

<tr><td>password</td><td>
<table>

<tr><td>type</td><td>string</td></tr>

<tr><td>required</td><td>True</td></tr>

<tr><td>description</td><td>Password of the user</td></tr>

</table>

</td></tr>

</table>

## logout

### POST

## users-me

### GET

### PATCH

<table>

<tr><th>Body Parameters</th><th></th></tr>

<tr><td>nickname</td><td>
<table>

<tr><td>type</td><td>string</td></tr>

<tr><td>required</td><td>False</td></tr>

<tr><td>description</td><td>Nickname of the user</td></tr>

</table>

</td></tr>

<tr><td>password</td><td>
<table>

<tr><td>type</td><td>string</td></tr>

<tr><td>required</td><td>False</td></tr>

<tr><td>description</td><td>Password of the user</td></tr>

</table>

</td></tr>

<tr><td>tournament_id</td><td>
<table>

<tr><td>type</td><td>integer</td></tr>

<tr><td>required</td><td>False</td></tr>

<tr><td>description</td><td>ID of the tournament joined</td></tr>

</table>

</td></tr>

</table>

### DELETE

## users-me-avatar

### POST

## users-me-blocked

### GET

### POST

<table>

<tr><th>Body Parameters</th><th></th></tr>

<tr><td>user_id</td><td>
<table>

<tr><td>type</td><td>id</td></tr>

<tr><td>required</td><td>True</td></tr>

<tr><td>description</td><td>ID of the user to block</td></tr>

</table>

</td></tr>

</table>

## users-me-blocked-USER_ID

### DELETE

## users-me-channels

### GET

## users-me-friends

### GET

## users-me-friends-USER_ID

### DELETE

## users-me-friends-requests

### GET

<table>

<tr><th>Query Parameters</th><th></th></tr>

<tr><td>type</td><td>
<table>

<tr><td>type</td><td>string</td></tr>

<tr><td>required</td><td>False</td></tr>

<tr><td>default</td><td>all</td></tr>

<tr><td>description</td><td>Type of the friend requests returned (all, sent, received)</td></tr>

</table>

</td></tr>

</table>

### POST

<table>

<tr><th>Body Parameters</th><th></th></tr>

<tr><td>nickname</td><td>
<table>

<tr><td>type</td><td>string</td></tr>

<tr><td>required</td><td>True</td></tr>

<tr><td>description</td><td>Nickname of the user to send the friend request to</td></tr>

</table>

</td></tr>

</table>

## users-me-friends-requests-REQUEST_ID

### POST

### DELETE

## users-me-notifications

### GET

### POST

<table>

<tr><th>Body Parameters</th><th></th></tr>

<tr><td>type</td><td>
<table>

<tr><td>type</td><td>string</td></tr>

<tr><td>required</td><td>True</td></tr>

<tr><td>description</td><td>Type of the notification</td></tr>

</table>

</td></tr>

<tr><td>content</td><td>
<table>

<tr><td>type</td><td>string</td></tr>

<tr><td>required</td><td>True</td></tr>

<tr><td>description</td><td>Content of the notification</td></tr>

</table>

</td></tr>

</table>

## users-me-notifications-NOTIFICATION_ID

### DELETE

## users

### GET

### POST

<table>

<tr><th>Body Parameters</th><th></th></tr>

<tr><td>username</td><td>
<table>

<tr><td>type</td><td>string</td></tr>

<tr><td>required</td><td>True</td></tr>

<tr><td>description</td><td>Username of the user</td></tr>

</table>

</td></tr>

<tr><td>password</td><td>
<table>

<tr><td>type</td><td>string</td></tr>

<tr><td>required</td><td>True</td></tr>

<tr><td>description</td><td>Password of the user</td></tr>

</table>

</td></tr>

</table>

## users-USER_ID

### GET

### PATCH

<table>

<tr><th>Body Parameters</th><th></th></tr>

<tr><td>nickname</td><td>
<table>

<tr><td>type</td><td>string</td></tr>

<tr><td>required</td><td>False</td></tr>

<tr><td>description</td><td>Nickname of the user</td></tr>

</table>

</td></tr>

<tr><td>password</td><td>
<table>

<tr><td>type</td><td>string</td></tr>

<tr><td>required</td><td>False</td></tr>

<tr><td>description</td><td>Password of the user</td></tr>

</table>

</td></tr>

</table>

### DELETE

## users-USER_ID-avatar

### GET

## users-USER_ID-games

### GET

## users-USER_ID-games_upcoming

### GET - Games with status created, i.e. not yet started

## tournaments

### GET

### POST

<table>

<tr><th>Body Parameters</th><th></th></tr>

<tr><td>title</td><td>
<table>

<tr><td>type</td><td>string</td></tr>

<tr><td>required</td><td>True</td></tr>

<tr><td>description</td><td>Title of the tournament</td></tr>

</table>

</td></tr>

<tr><td>description</td><td>
<table>

<tr><td>type</td><td>string</td></tr>

<tr><td>required</td><td>False</td></tr>

<tr><td>description</td><td>Description of the tournament</td></tr>

</table>

</td></tr>

</table>

## tournaments-TOURNAMENT_ID

### GET

### DELETE

### PATCH

<table>

<tr><th>Body Parameters</th><th></th></tr>

<tr><td>title</td><td>
<table>

<tr><td>type</td><td>string</td></tr>

<tr><td>required</td><td>False</td></tr>

<tr><td>description</td><td>Title of the tournament</td></tr>

</table>

</td></tr>

<tr><td>description</td><td>
<table>

<tr><td>type</td><td>string</td></tr>

<tr><td>required</td><td>False</td></tr>

<tr><td>description</td><td>Description of the tournament</td></tr>

</table>

</td></tr>

<tr><td>status</td><td>
<table>

<tr><td>type</td><td>string</td></tr>

<tr><td>required</td><td>False</td></tr>

<tr><td>description</td><td>'next' -> advance to next tournament status, 'cancelled' -> cancel tournament</td></tr>

</table>

</td></tr>

</table>

## tournaments-TOURNAMENT_ID-play

### POST

<table>

<tr><th>Body Parameters</th><th></th></tr>

<tr><td>play</td><td>
<table>

<tr><td>type</td><td>string</td></tr>

<tr><td>required</td><td>True</td></tr>

<tr><td>description</td><td>join on unjoin the tournament</td></tr>

</table>

</td></tr>

</table>

## tournaments-TOURNAMENT_ID-games

### GET

## games

### GET

### POST

<table>

<tr><th>Body Parameters</th><th></th></tr>

<tr><td>tournament_id</td><td>
<table>

<tr><td>type</td><td>id</td></tr>

<tr><td>required</td><td>False</td></tr>

<tr><td>default</td><td>null</td></tr>

<tr><td>description</td><td>ID of the tournament</td></tr>

</table>

</td></tr>

<tr><td>player1_id</td><td>
<table>

<tr><td>type</td><td>id</td></tr>

<tr><td>required</td><td>True</td></tr>

<tr><td>description</td><td>ID of the first player</td></tr>

</table>

</td></tr>

<tr><td>player2_id</td><td>
<table>

<tr><td>type</td><td>id</td></tr>

<tr><td>required</td><td>True</td></tr>

<tr><td>description</td><td>ID of the second player</td></tr>

</table>

</td></tr>

<tr><td>player1_score</td><td>
<table>

<tr><td>type</td><td>integer</td></tr>

<tr><td>required</td><td>True</td></tr>

<tr><td>description</td><td>Score of the first player</td></tr>

</table>

</td></tr>

<tr><td>player2_score</td><td>
<table>

<tr><td>type</td><td>integer</td></tr>

<tr><td>required</td><td>True</td></tr>

<tr><td>description</td><td>Score of the second player</td></tr>

</table>

</td></tr>

</table>

## games-GAME_ID

### GET

### PATCH

<table>

<tr><th>Body Parameters</th><th></th></tr>

<tr><td>player1_score</td><td>
<table>

<tr><td>type</td><td>integer</td></tr>

<tr><td>required</td><td>False</td></tr>

<tr><td>description</td><td>Score of the first player</td></tr>

</table>

</td></tr>

<tr><td>player2_score</td><td>
<table>

<tr><td>type</td><td>integer</td></tr>

<tr><td>required</td><td>False</td></tr>

<tr><td>description</td><td>Score of the second player</td></tr>

</table>

</td></tr>

<tr><td>status</td><td>
<table>

<tr><td>type</td><td>string</td></tr>

<tr><td>required</td><td>False</td></tr>

<tr><td>description</td><td>Status of the game</td></tr>

</table>

</td></tr>

</table>

### DELETE

## channels

### GET

### POST

<table>

<tr><th>Body Parameters</th><th></th></tr>

<tr><td>name</td><td>
<table>

<tr><td>type</td><td>string</td></tr>

<tr><td>required</td><td>True</td></tr>

<tr><td>description</td><td>Name of the channel</td></tr>

</table>

</td></tr>

</table>

## channels-CHANNEL_ID

### GET

### PATCH

<table>

<tr><th>Body Parameters</th><th></th></tr>

<tr><td>name</td><td>
<table>

<tr><td>type</td><td>string</td></tr>

<tr><td>required</td><td>False</td></tr>

<tr><td>description</td><td>Name of the channel</td></tr>

</table>

</td></tr>

</table>

### DELETE

## channels-CHANNEL_ID-members

### GET

### POST

<table>

<tr><th>Body Parameters</th><th></th></tr>

<tr><td>user_id</td><td>
<table>

<tr><td>type</td><td>id</td></tr>

<tr><td>required</td><td>True</td></tr>

<tr><td>description</td><td>ID of the user to add to the channel</td></tr>

</table>

</td></tr>

</table>

## channels-CHANNEL_ID-members-USER_ID

### DELETE

## channels-CHANNEL_ID-messages

### GET

### POST

<table>

<tr><th>Body Parameters</th><th></th></tr>

<tr><td>content</td><td>
<table>

<tr><td>type</td><td>string</td></tr>

<tr><td>required</td><td>True</td></tr>

<tr><td>description</td><td>Content of the message</td></tr>

</table>

</td></tr>

</table>

## messages

### GET

## messages-MESSAGE_ID

### PATCH

<table>

<tr><th>Body Parameters</th><th></th></tr>

<tr><td>content</td><td>
<table>

<tr><td>type</td><td>string</td></tr>

<tr><td>required</td><td>True</td></tr>

<tr><td>description</td><td>Content of the message</td></tr>

</table>

</td></tr>

</table>

### DELETE

