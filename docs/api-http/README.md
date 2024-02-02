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
</tr><tr><td>

<table>
<tr><th>Parameter</th><th>Type</th><th>Required</th><th>Description</th></tr>
<tr><td>username</td><td>string</td><td>True</td><td>Username of the user</td></tr>
<tr><td>password</td><td>string</td><td>True</td><td>Password of the user</td></tr>
</table>

</td><td>
<table>
<tr><th>Parameter</th><th>Type</th><th>Required</th><th>Description</th></tr>
<tr><td>remember</td><td>boolean</td><td>False</td><td>If false, the session will be deleted after the browser is closed</td></tr>
</table>

</td><td>
None
</td></tr>
</td></tr>
</td></tr>
</table>

## logout

### POST

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

None
</td><td>
None
</td><td>
None
</td></tr>
</td></tr>
</td></tr>
</table>

## users-me

### GET

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

None
</td><td>
None
</td><td>
None
</td></tr>
</td></tr>
</td></tr>
</table>

### PATCH

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

<table>
<tr><th>Parameter</th><th>Type</th><th>Required</th><th>Description</th></tr>
<tr><td>nickname</td><td>string</td><td>False</td><td>Nickname of the user</td></tr>
<tr><td>password</td><td>string</td><td>False</td><td>Password of the user</td></tr>
</table>

</td><td>
None
</td><td>
None
</td></tr>
</td></tr>
</td></tr>
</table>

### DELETE

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

None
</td><td>
None
</td><td>
None
</td></tr>
</td></tr>
</td></tr>
</table>

## users-me-avatar

### POST

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

None
</td><td>
None
</td><td>
None
</td></tr>
</td></tr>
</td></tr>
</table>

## users-me-blocked

### GET

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

None
</td><td>
None
</td><td>
None
</td></tr>
</td></tr>
</td></tr>
</table>

### POST

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

<table>
<tr><th>Parameter</th><th>Type</th><th>Required</th><th>Description</th></tr>
<tr><td>user_id</td><td>id</td><td>True</td><td>ID of the user to block</td></tr>
</table>

</td><td>
None
</td><td>
None
</td></tr>
</td></tr>
</td></tr>
</table>

## users-me-blocked-USER_ID

### DELETE

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

None
</td><td>
None
</td><td>
None
</td></tr>
</td></tr>
</td></tr>
</table>

## users-me-channels

### GET

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

None
</td><td>
None
</td><td>
None
</td></tr>
</td></tr>
</td></tr>
</table>

## users-me-friends

### GET

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

None
</td><td>
None
</td><td>
None
</td></tr>
</td></tr>
</td></tr>
</table>

## users-me-friends-USER_ID

### DELETE

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

None
</td><td>
None
</td><td>
None
</td></tr>
</td></tr>
</td></tr>
</table>

## users-me-friends-requests

### GET

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

None
</td><td>
<table>
<tr><th>Parameter</th><th>Type</th><th>Required</th><th>Description</th></tr>
<tr><td>type</td><td>string</td><td>False</td><td>Type of the friend requests returned (all, sent, received)</td></tr>
</table>

</td><td>
None
</td></tr>
</td></tr>
</td></tr>
</table>

### POST

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

<table>
<tr><th>Parameter</th><th>Type</th><th>Required</th><th>Description</th></tr>
<tr><td>username</td><td>string</td><td>True</td><td>Username of the user to send the friend request to</td></tr>
</table>

</td><td>
None
</td><td>
None
</td></tr>
</td></tr>
</td></tr>
</table>

## users-me-friends-requests-REQUEST_ID

### POST

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

None
</td><td>
None
</td><td>
None
</td></tr>
</td></tr>
</td></tr>
</table>

### DELETE

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

None
</td><td>
None
</td><td>
None
</td></tr>
</td></tr>
</td></tr>
</table>

## users-me-notifications

### GET

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

None
</td><td>
None
</td><td>
None
</td></tr>
</td></tr>
</td></tr>
</table>

## users-me-notifications-NOTIFICATION_ID

### DELETE

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

None
</td><td>
None
</td><td>
None
</td></tr>
</td></tr>
</td></tr>
</table>

## users

### GET

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

None
</td><td>
None
</td><td>
None
</td></tr>
</td></tr>
</td></tr>
</table>

### POST

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

<table>
<tr><th>Parameter</th><th>Type</th><th>Required</th><th>Description</th></tr>
<tr><td>username</td><td>string</td><td>True</td><td>Username of the user</td></tr>
<tr><td>password</td><td>string</td><td>True</td><td>Password of the user</td></tr>
</table>

</td><td>
None
</td><td>
None
</td></tr>
</td></tr>
</td></tr>
</table>

## users-USER_ID

### GET

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

None
</td><td>
None
</td><td>
None
</td></tr>
</td></tr>
</td></tr>
</table>

### PATCH

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

<table>
<tr><th>Parameter</th><th>Type</th><th>Required</th><th>Description</th></tr>
<tr><td>nickname</td><td>string</td><td>False</td><td>Nickname of the user</td></tr>
<tr><td>password</td><td>string</td><td>False</td><td>Password of the user</td></tr>
</table>

</td><td>
None
</td><td>
None
</td></tr>
</td></tr>
</td></tr>
</table>

### DELETE

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

None
</td><td>
None
</td><td>
None
</td></tr>
</td></tr>
</td></tr>
</table>

## users-USER_ID-avatar

### GET

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

None
</td><td>
None
</td><td>
None
</td></tr>
</td></tr>
</td></tr>
</table>

## users-USER_ID-stats

### GET

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

None
</td><td>
None
</td><td>
None
</td></tr>
</td></tr>
</td></tr>
</table>

## users-USER_ID-games

### GET

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

None
</td><td>
None
</td><td>
None
</td></tr>
</td></tr>
</td></tr>
</table>

## tournaments

### GET

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

None
</td><td>
None
</td><td>
None
</td></tr>
</td></tr>
</td></tr>
</table>

### POST

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

<table>
<tr><th>Parameter</th><th>Type</th><th>Required</th><th>Description</th></tr>
<tr><td>title</td><td>string</td><td>True</td><td>Title of the tournament</td></tr>
<tr><td>description</td><td>string</td><td>False</td><td>Description of the tournament</td></tr>
</table>

</td><td>
None
</td><td>
None
</td></tr>
</td></tr>
</td></tr>
</table>

## tournaments-TOURNAMENT_ID

### GET

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

None
</td><td>
None
</td><td>
None
</td></tr>
</td></tr>
</td></tr>
</table>

### PATCH

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

<table>
<tr><th>Parameter</th><th>Type</th><th>Required</th><th>Description</th></tr>
<tr><td>title</td><td>string</td><td>False</td><td>Title of the tournament</td></tr>
<tr><td>description</td><td>string</td><td>False</td><td>Description of the tournament</td></tr>
</table>

</td><td>
None
</td><td>
None
</td></tr>
</td></tr>
</td></tr>
</table>

## games

### GET

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

None
</td><td>
None
</td><td>
None
</td></tr>
</td></tr>
</td></tr>
</table>

### POST

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

<table>
<tr><th>Parameter</th><th>Type</th><th>Required</th><th>Description</th></tr>
<tr><td>tournament_id</td><td>id</td><td>False</td><td>ID of the tournament</td></tr>
<tr><td>player1_id</td><td>id</td><td>True</td><td>ID of the first player</td></tr>
<tr><td>player2_id</td><td>id</td><td>True</td><td>ID of the second player</td></tr>
<tr><td>player1_score</td><td>integer</td><td>True</td><td>Score of the first player</td></tr>
<tr><td>player2_score</td><td>integer</td><td>True</td><td>Score of the second player</td></tr>
</table>

</td><td>
None
</td><td>
None
</td></tr>
</td></tr>
</td></tr>
</table>

## games-GAME_ID

### GET

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

None
</td><td>
None
</td><td>
None
</td></tr>
</td></tr>
</td></tr>
</table>

### PATCH

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

<table>
<tr><th>Parameter</th><th>Type</th><th>Required</th><th>Description</th></tr>
<tr><td>player1_score</td><td>integer</td><td>False</td><td>Score of the first player</td></tr>
<tr><td>player2_score</td><td>integer</td><td>False</td><td>Score of the second player</td></tr>
<tr><td>status</td><td>string</td><td>False</td><td>Status of the game</td></tr>
</table>

</td><td>
None
</td><td>
None
</td></tr>
</td></tr>
</td></tr>
</table>

### DELETE

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

None
</td><td>
None
</td><td>
None
</td></tr>
</td></tr>
</td></tr>
</table>

## channels

### GET

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

None
</td><td>
None
</td><td>
None
</td></tr>
</td></tr>
</td></tr>
</table>

### POST

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

<table>
<tr><th>Parameter</th><th>Type</th><th>Required</th><th>Description</th></tr>
<tr><td>name</td><td>string</td><td>True</td><td>Name of the channel</td></tr>
</table>

</td><td>
None
</td><td>
None
</td></tr>
</td></tr>
</td></tr>
</table>

## channels-CHANNEL_ID

### GET

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

None
</td><td>
None
</td><td>
None
</td></tr>
</td></tr>
</td></tr>
</table>

### PATCH

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

<table>
<tr><th>Parameter</th><th>Type</th><th>Required</th><th>Description</th></tr>
<tr><td>name</td><td>string</td><td>False</td><td>Name of the channel</td></tr>
</table>

</td><td>
None
</td><td>
None
</td></tr>
</td></tr>
</td></tr>
</table>

### DELETE

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

None
</td><td>
None
</td><td>
None
</td></tr>
</td></tr>
</td></tr>
</table>

## channels-CHANNEL_ID-members

### GET

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

None
</td><td>
None
</td><td>
None
</td></tr>
</td></tr>
</td></tr>
</table>

### POST

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

<table>
<tr><th>Parameter</th><th>Type</th><th>Required</th><th>Description</th></tr>
<tr><td>user_id</td><td>id</td><td>True</td><td>ID of the user to add to the channel</td></tr>
</table>

</td><td>
None
</td><td>
None
</td></tr>
</td></tr>
</td></tr>
</table>

## channels-CHANNEL_ID-members-USER_ID

### DELETE

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

None
</td><td>
None
</td><td>
None
</td></tr>
</td></tr>
</td></tr>
</table>

## channels-CHANNEL_ID-messages

### GET

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

None
</td><td>
None
</td><td>
None
</td></tr>
</td></tr>
</td></tr>
</table>

### POST

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

<table>
<tr><th>Parameter</th><th>Type</th><th>Required</th><th>Description</th></tr>
<tr><td>content</td><td>string</td><td>True</td><td>Content of the message</td></tr>
</table>

</td><td>
None
</td><td>
None
</td></tr>
</td></tr>
</td></tr>
</table>

## messages

### GET

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

None
</td><td>
None
</td><td>
None
</td></tr>
</td></tr>
</td></tr>
</table>

## messages-MESSAGE_ID

### PATCH

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

<table>
<tr><th>Parameter</th><th>Type</th><th>Required</th><th>Description</th></tr>
<tr><td>content</td><td>string</td><td>True</td><td>Content of the message</td></tr>
</table>

</td><td>
None
</td><td>
None
</td></tr>
</td></tr>
</td></tr>
</table>

### DELETE

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

None
</td><td>
None
</td><td>
None
</td></tr>
</td></tr>
</td></tr>
</table>

