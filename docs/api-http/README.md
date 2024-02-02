# Statistics

Total number of urls: 29

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
- [/users/USER_ID/stats](#users-USER_ID-stats)
- [/users/USER_ID/games](#users-USER_ID-games)
- [/tournaments](#tournaments)
- [/tournaments/TOURNAMENT_ID](#tournaments-TOURNAMENT_ID)
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
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr>
<td>
<table>
<tr>
<th>username</th>
<th>password</th>
</tr><tr>
<td>
<table>
<tr>
<th>type</th>
<th>required</th>
<th>description</th>
</tr><tr>
<td>string</td>
<td>True</td>
<td>Username of the user</td>
</tr></table>

</td>
<td>
<table>
<tr>
<th>type</th>
<th>required</th>
<th>description</th>
</tr><tr>
<td>string</td>
<td>True</td>
<td>Password of the user</td>
</tr></table>

</td>
</tr></table>

</td>
<td>
<table>
<tr>
<th>remember</th>
</tr><tr>
<td>
<table>
<tr>
<th>type</th>
<th>required</th>
<th>default</th>
<th>description</th>
</tr><tr>
<td>boolean</td>
<td>False</td>
<td>False</td>
<td>If false, the session will be deleted after the browser is closed</td>
</tr></table>

</td>
</tr></table>

</td>
<td>
None
</td>
</tr></table>

## logout

### POST

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr>
<td>
None
</td>
<td>
None
</td>
<td>
None
</td>
</tr></table>

## users-me

### GET

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr>
<td>
None
</td>
<td>
None
</td>
<td>
None
</td>
</tr></table>

### PATCH

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr>
<td>
<table>
<tr>
<th>nickname</th>
<th>password</th>
</tr><tr>
<td>
<table>
<tr>
<th>type</th>
<th>required</th>
<th>description</th>
</tr><tr>
<td>string</td>
<td>False</td>
<td>Nickname of the user</td>
</tr></table>

</td>
<td>
<table>
<tr>
<th>type</th>
<th>required</th>
<th>description</th>
</tr><tr>
<td>string</td>
<td>False</td>
<td>Password of the user</td>
</tr></table>

</td>
</tr></table>

</td>
<td>
None
</td>
<td>
None
</td>
</tr></table>

### DELETE

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr>
<td>
None
</td>
<td>
None
</td>
<td>
None
</td>
</tr></table>

## users-me-avatar

### POST

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr>
<td>[]</td>
<td>
None
</td>
<td>
None
</td>
</tr></table>

## users-me-blocked

### GET

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr>
<td>
None
</td>
<td>
None
</td>
<td>
None
</td>
</tr></table>

### POST

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr>
<td>
<table>
<tr>
<th>user_id</th>
</tr><tr>
<td>
<table>
<tr>
<th>type</th>
<th>required</th>
<th>description</th>
</tr><tr>
<td>id</td>
<td>True</td>
<td>ID of the user to block</td>
</tr></table>

</td>
</tr></table>

</td>
<td>
None
</td>
<td>
None
</td>
</tr></table>

## users-me-blocked-USER_ID

### DELETE

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr>
<td>
None
</td>
<td>
None
</td>
<td>
None
</td>
</tr></table>

## users-me-channels

### GET

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr>
<td>
None
</td>
<td>
None
</td>
<td>
None
</td>
</tr></table>

## users-me-friends

### GET

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr>
<td>
None
</td>
<td>
None
</td>
<td>
None
</td>
</tr></table>

## users-me-friends-USER_ID

### DELETE

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr>
<td>
None
</td>
<td>
None
</td>
<td>
None
</td>
</tr></table>

## users-me-friends-requests

### GET

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr>
<td>[]</td>
<td>
<table>
<tr>
<th>type</th>
</tr><tr>
<td>
<table>
<tr>
<th>type</th>
<th>required</th>
<th>default</th>
<th>description</th>
</tr><tr>
<td>string</td>
<td>False</td>
<td>all</td>
<td>Type of the friend requests returned (all, sent, received)</td>
</tr></table>

</td>
</tr></table>

</td>
<td>
None
</td>
</tr></table>

### POST

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr>
<td>
<table>
<tr>
<th>username</th>
</tr><tr>
<td>
<table>
<tr>
<th>type</th>
<th>required</th>
<th>description</th>
</tr><tr>
<td>string</td>
<td>True</td>
<td>Username of the user to send the friend request to</td>
</tr></table>

</td>
</tr></table>

</td>
<td>
None
</td>
<td>
None
</td>
</tr></table>

## users-me-friends-requests-REQUEST_ID

### POST

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr>
<td>
None
</td>
<td>
None
</td>
<td>
None
</td>
</tr></table>

### DELETE

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr>
<td>
None
</td>
<td>
None
</td>
<td>
None
</td>
</tr></table>

## users-me-notifications

### GET

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr>
<td>
None
</td>
<td>
None
</td>
<td>
None
</td>
</tr></table>

## users-me-notifications-NOTIFICATION_ID

### DELETE

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr>
<td>
None
</td>
<td>
None
</td>
<td>
None
</td>
</tr></table>

## users

### GET

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr>
<td>
None
</td>
<td>
None
</td>
<td>
None
</td>
</tr></table>

### POST

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr>
<td>
<table>
<tr>
<th>username</th>
<th>password</th>
</tr><tr>
<td>
<table>
<tr>
<th>type</th>
<th>required</th>
<th>description</th>
</tr><tr>
<td>string</td>
<td>True</td>
<td>Username of the user</td>
</tr></table>

</td>
<td>
<table>
<tr>
<th>type</th>
<th>required</th>
<th>description</th>
</tr><tr>
<td>string</td>
<td>True</td>
<td>Password of the user</td>
</tr></table>

</td>
</tr></table>

</td>
<td>
None
</td>
<td>
None
</td>
</tr></table>

## users-USER_ID

### GET

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr>
<td>
None
</td>
<td>
None
</td>
<td>
None
</td>
</tr></table>

### PATCH

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr>
<td>
<table>
<tr>
<th>nickname</th>
<th>password</th>
</tr><tr>
<td>
<table>
<tr>
<th>type</th>
<th>required</th>
<th>description</th>
</tr><tr>
<td>string</td>
<td>False</td>
<td>Nickname of the user</td>
</tr></table>

</td>
<td>
<table>
<tr>
<th>type</th>
<th>required</th>
<th>description</th>
</tr><tr>
<td>string</td>
<td>False</td>
<td>Password of the user</td>
</tr></table>

</td>
</tr></table>

</td>
<td>
None
</td>
<td>
None
</td>
</tr></table>

### DELETE

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr>
<td>
None
</td>
<td>
None
</td>
<td>
None
</td>
</tr></table>

## users-USER_ID-avatar

### GET

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr>
<td>
None
</td>
<td>
None
</td>
<td>
None
</td>
</tr></table>

## users-USER_ID-stats

### GET

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr>
<td>
None
</td>
<td>
None
</td>
<td>
None
</td>
</tr></table>

## users-USER_ID-games

### GET

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr>
<td>
None
</td>
<td>
None
</td>
<td>
None
</td>
</tr></table>

## tournaments

### GET

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr>
<td>
None
</td>
<td>
None
</td>
<td>
None
</td>
</tr></table>

### POST

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr>
<td>
<table>
<tr>
<th>title</th>
<th>description</th>
</tr><tr>
<td>
<table>
<tr>
<th>type</th>
<th>required</th>
<th>description</th>
</tr><tr>
<td>string</td>
<td>True</td>
<td>Title of the tournament</td>
</tr></table>

</td>
<td>
<table>
<tr>
<th>type</th>
<th>required</th>
<th>description</th>
</tr><tr>
<td>string</td>
<td>False</td>
<td>Description of the tournament</td>
</tr></table>

</td>
</tr></table>

</td>
<td>
None
</td>
<td>
None
</td>
</tr></table>

## tournaments-TOURNAMENT_ID

### GET

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr>
<td>
None
</td>
<td>
None
</td>
<td>
None
</td>
</tr></table>

### PATCH

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr>
<td>
<table>
<tr>
<th>title</th>
<th>description</th>
</tr><tr>
<td>
<table>
<tr>
<th>type</th>
<th>required</th>
<th>description</th>
</tr><tr>
<td>string</td>
<td>False</td>
<td>Title of the tournament</td>
</tr></table>

</td>
<td>
<table>
<tr>
<th>type</th>
<th>required</th>
<th>description</th>
</tr><tr>
<td>string</td>
<td>False</td>
<td>Description of the tournament</td>
</tr></table>

</td>
</tr></table>

</td>
<td>
None
</td>
<td>
None
</td>
</tr></table>

## games

### GET

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr>
<td>
None
</td>
<td>
None
</td>
<td>
None
</td>
</tr></table>

### POST

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr>
<td>
<table>
<tr>
<th>tournament_id</th>
<th>player1_id</th>
<th>player2_id</th>
<th>player1_score</th>
<th>player2_score</th>
</tr><tr>
<td>
<table>
<tr>
<th>type</th>
<th>required</th>
<th>description</th>
</tr><tr>
<td>id</td>
<td>False</td>
<td>ID of the tournament</td>
</tr></table>

</td>
<td>
<table>
<tr>
<th>type</th>
<th>required</th>
<th>description</th>
</tr><tr>
<td>id</td>
<td>True</td>
<td>ID of the first player</td>
</tr></table>

</td>
<td>
<table>
<tr>
<th>type</th>
<th>required</th>
<th>description</th>
</tr><tr>
<td>id</td>
<td>True</td>
<td>ID of the second player</td>
</tr></table>

</td>
<td>
<table>
<tr>
<th>type</th>
<th>required</th>
<th>description</th>
</tr><tr>
<td>integer</td>
<td>True</td>
<td>Score of the first player</td>
</tr></table>

</td>
<td>
<table>
<tr>
<th>type</th>
<th>required</th>
<th>description</th>
</tr><tr>
<td>integer</td>
<td>True</td>
<td>Score of the second player</td>
</tr></table>

</td>
</tr></table>

</td>
<td>
None
</td>
<td>
None
</td>
</tr></table>

## games-GAME_ID

### GET

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr>
<td>
None
</td>
<td>
None
</td>
<td>
None
</td>
</tr></table>

### PATCH

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr>
<td>
<table>
<tr>
<th>player1_score</th>
<th>player2_score</th>
<th>status</th>
</tr><tr>
<td>
<table>
<tr>
<th>type</th>
<th>required</th>
<th>description</th>
</tr><tr>
<td>integer</td>
<td>False</td>
<td>Score of the first player</td>
</tr></table>

</td>
<td>
<table>
<tr>
<th>type</th>
<th>required</th>
<th>description</th>
</tr><tr>
<td>integer</td>
<td>False</td>
<td>Score of the second player</td>
</tr></table>

</td>
<td>
<table>
<tr>
<th>type</th>
<th>required</th>
<th>description</th>
</tr><tr>
<td>string</td>
<td>False</td>
<td>Status of the game</td>
</tr></table>

</td>
</tr></table>

</td>
<td>
None
</td>
<td>
None
</td>
</tr></table>

### DELETE

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr>
<td>
None
</td>
<td>
None
</td>
<td>
None
</td>
</tr></table>

## channels

### GET

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr>
<td>
None
</td>
<td>
None
</td>
<td>
None
</td>
</tr></table>

### POST

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr>
<td>
<table>
<tr>
<th>name</th>
</tr><tr>
<td>
<table>
<tr>
<th>type</th>
<th>required</th>
<th>description</th>
</tr><tr>
<td>string</td>
<td>True</td>
<td>Name of the channel</td>
</tr></table>

</td>
</tr></table>

</td>
<td>
None
</td>
<td>
None
</td>
</tr></table>

## channels-CHANNEL_ID

### GET

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr>
<td>
None
</td>
<td>
None
</td>
<td>
None
</td>
</tr></table>

### PATCH

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr>
<td>
<table>
<tr>
<th>name</th>
</tr><tr>
<td>
<table>
<tr>
<th>type</th>
<th>required</th>
<th>description</th>
</tr><tr>
<td>string</td>
<td>False</td>
<td>Name of the channel</td>
</tr></table>

</td>
</tr></table>

</td>
<td>
None
</td>
<td>
None
</td>
</tr></table>

### DELETE

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr>
<td>
None
</td>
<td>
None
</td>
<td>
None
</td>
</tr></table>

## channels-CHANNEL_ID-members

### GET

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr>
<td>
None
</td>
<td>
None
</td>
<td>
None
</td>
</tr></table>

### POST

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr>
<td>
<table>
<tr>
<th>user_id</th>
</tr><tr>
<td>
<table>
<tr>
<th>type</th>
<th>required</th>
<th>description</th>
</tr><tr>
<td>id</td>
<td>True</td>
<td>ID of the user to add to the channel</td>
</tr></table>

</td>
</tr></table>

</td>
<td>
None
</td>
<td>
None
</td>
</tr></table>

## channels-CHANNEL_ID-members-USER_ID

### DELETE

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr>
<td>
None
</td>
<td>
None
</td>
<td>
None
</td>
</tr></table>

## channels-CHANNEL_ID-messages

### GET

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr>
<td>
None
</td>
<td>
None
</td>
<td>
None
</td>
</tr></table>

### POST

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr>
<td>
<table>
<tr>
<th>content</th>
</tr><tr>
<td>
<table>
<tr>
<th>type</th>
<th>required</th>
<th>description</th>
</tr><tr>
<td>string</td>
<td>True</td>
<td>Content of the message</td>
</tr></table>

</td>
</tr></table>

</td>
<td>
None
</td>
<td>
None
</td>
</tr></table>

## messages

### GET

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr>
<td>
None
</td>
<td>
None
</td>
<td>
None
</td>
</tr></table>

## messages-MESSAGE_ID

### PATCH

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr>
<td>
<table>
<tr>
<th>content</th>
</tr><tr>
<td>
<table>
<tr>
<th>type</th>
<th>required</th>
<th>description</th>
</tr><tr>
<td>string</td>
<td>True</td>
<td>Content of the message</td>
</tr></table>

</td>
</tr></table>

</td>
<td>
None
</td>
<td>
None
</td>
</tr></table>

### DELETE

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr>
<td>
None
</td>
<td>
None
</td>
<td>
None
</td>
</tr></table>

