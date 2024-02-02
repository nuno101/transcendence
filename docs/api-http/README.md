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

<table>

<tr><th>POST</th><th></th></tr>

<tr><td>Body Parameters</td><td>
<table>

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

</td></tr>

<tr><td>Query Parameters</td><td>
<table>

<tr><td>remember</td><td>
<table>

<tr><td>type</td><td>boolean</td></tr>

<tr><td>required</td><td>False</td></tr>

<tr><td>default</td><td>False</td></tr>

<tr><td>description</td><td>If false, the session will be deleted after the browser is closed</td></tr>

</table>

</td></tr>

</table>

</td></tr>

<tr><td>Response</td><td>
None
</td></tr>

</table>

## logout

<table>

<tr><th>POST</th><th></th></tr>

<tr><td>Body Parameters</td><td>
None
</td></tr>

<tr><td>Query Parameters</td><td>
None
</td></tr>

<tr><td>Response</td><td>
None
</td></tr>

</table>

## users-me

<table>

<tr><th>GET</th><th></th></tr>

<tr><td>Body Parameters</td><td>
None
</td></tr>

<tr><td>Query Parameters</td><td>
None
</td></tr>

<tr><td>Response</td><td>
None
</td></tr>

</table>

<table>

<tr><th>PATCH</th><th></th></tr>

<tr><td>Body Parameters</td><td>
<table>

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

</td></tr>

<tr><td>Query Parameters</td><td>
None
</td></tr>

<tr><td>Response</td><td>
None
</td></tr>

</table>

<table>

<tr><th>DELETE</th><th></th></tr>

<tr><td>Body Parameters</td><td>
None
</td></tr>

<tr><td>Query Parameters</td><td>
None
</td></tr>

<tr><td>Response</td><td>
None
</td></tr>

</table>

## users-me-avatar

<table>

<tr><th>POST</th><th></th></tr>

<tr><td>Body Parameters</td><td>
None
</td></tr>

<tr><td>Query Parameters</td><td>
None
</td></tr>

<tr><td>Response</td><td>
None
</td></tr>

</table>

## users-me-blocked

<table>

<tr><th>GET</th><th></th></tr>

<tr><td>Body Parameters</td><td>
None
</td></tr>

<tr><td>Query Parameters</td><td>
None
</td></tr>

<tr><td>Response</td><td>
None
</td></tr>

</table>

<table>

<tr><th>POST</th><th></th></tr>

<tr><td>Body Parameters</td><td>
<table>

<tr><td>user_id</td><td>
<table>

<tr><td>type</td><td>id</td></tr>

<tr><td>required</td><td>True</td></tr>

<tr><td>description</td><td>ID of the user to block</td></tr>

</table>

</td></tr>

</table>

</td></tr>

<tr><td>Query Parameters</td><td>
None
</td></tr>

<tr><td>Response</td><td>
None
</td></tr>

</table>

## users-me-blocked-USER_ID

<table>

<tr><th>DELETE</th><th></th></tr>

<tr><td>Body Parameters</td><td>
None
</td></tr>

<tr><td>Query Parameters</td><td>
None
</td></tr>

<tr><td>Response</td><td>
None
</td></tr>

</table>

## users-me-channels

<table>

<tr><th>GET</th><th></th></tr>

<tr><td>Body Parameters</td><td>
None
</td></tr>

<tr><td>Query Parameters</td><td>
None
</td></tr>

<tr><td>Response</td><td>
None
</td></tr>

</table>

## users-me-friends

<table>

<tr><th>GET</th><th></th></tr>

<tr><td>Body Parameters</td><td>
None
</td></tr>

<tr><td>Query Parameters</td><td>
None
</td></tr>

<tr><td>Response</td><td>
None
</td></tr>

</table>

## users-me-friends-USER_ID

<table>

<tr><th>DELETE</th><th></th></tr>

<tr><td>Body Parameters</td><td>
None
</td></tr>

<tr><td>Query Parameters</td><td>
None
</td></tr>

<tr><td>Response</td><td>
None
</td></tr>

</table>

## users-me-friends-requests

<table>

<tr><th>GET</th><th></th></tr>

<tr><td>Body Parameters</td><td>
None
</td></tr>

<tr><td>Query Parameters</td><td>
<table>

<tr><td>type</td><td>
<table>

<tr><td>type</td><td>string</td></tr>

<tr><td>required</td><td>False</td></tr>

<tr><td>default</td><td>all</td></tr>

<tr><td>description</td><td>Type of the friend requests returned (all, sent, received)</td></tr>

</table>

</td></tr>

</table>

</td></tr>

<tr><td>Response</td><td>
None
</td></tr>

</table>

<table>

<tr><th>POST</th><th></th></tr>

<tr><td>Body Parameters</td><td>
<table>

<tr><td>username</td><td>
<table>

<tr><td>type</td><td>string</td></tr>

<tr><td>required</td><td>True</td></tr>

<tr><td>description</td><td>Username of the user to send the friend request to</td></tr>

</table>

</td></tr>

</table>

</td></tr>

<tr><td>Query Parameters</td><td>
None
</td></tr>

<tr><td>Response</td><td>
None
</td></tr>

</table>

## users-me-friends-requests-REQUEST_ID

<table>

<tr><th>POST</th><th></th></tr>

<tr><td>Body Parameters</td><td>
None
</td></tr>

<tr><td>Query Parameters</td><td>
None
</td></tr>

<tr><td>Response</td><td>
None
</td></tr>

</table>

<table>

<tr><th>DELETE</th><th></th></tr>

<tr><td>Body Parameters</td><td>
None
</td></tr>

<tr><td>Query Parameters</td><td>
None
</td></tr>

<tr><td>Response</td><td>
None
</td></tr>

</table>

## users-me-notifications

<table>

<tr><th>GET</th><th></th></tr>

<tr><td>Body Parameters</td><td>
None
</td></tr>

<tr><td>Query Parameters</td><td>
None
</td></tr>

<tr><td>Response</td><td>
None
</td></tr>

</table>

## users-me-notifications-NOTIFICATION_ID

<table>

<tr><th>DELETE</th><th></th></tr>

<tr><td>Body Parameters</td><td>
None
</td></tr>

<tr><td>Query Parameters</td><td>
None
</td></tr>

<tr><td>Response</td><td>
None
</td></tr>

</table>

## users

<table>

<tr><th>GET</th><th></th></tr>

<tr><td>Body Parameters</td><td>
None
</td></tr>

<tr><td>Query Parameters</td><td>
None
</td></tr>

<tr><td>Response</td><td>
None
</td></tr>

</table>

<table>

<tr><th>POST</th><th></th></tr>

<tr><td>Body Parameters</td><td>
<table>

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

</td></tr>

<tr><td>Query Parameters</td><td>
None
</td></tr>

<tr><td>Response</td><td>
None
</td></tr>

</table>

## users-USER_ID

<table>

<tr><th>GET</th><th></th></tr>

<tr><td>Body Parameters</td><td>
None
</td></tr>

<tr><td>Query Parameters</td><td>
None
</td></tr>

<tr><td>Response</td><td>
None
</td></tr>

</table>

<table>

<tr><th>PATCH</th><th></th></tr>

<tr><td>Body Parameters</td><td>
<table>

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

</td></tr>

<tr><td>Query Parameters</td><td>
None
</td></tr>

<tr><td>Response</td><td>
None
</td></tr>

</table>

<table>

<tr><th>DELETE</th><th></th></tr>

<tr><td>Body Parameters</td><td>
None
</td></tr>

<tr><td>Query Parameters</td><td>
None
</td></tr>

<tr><td>Response</td><td>
None
</td></tr>

</table>

## users-USER_ID-avatar

<table>

<tr><th>GET</th><th></th></tr>

<tr><td>Body Parameters</td><td>
None
</td></tr>

<tr><td>Query Parameters</td><td>
None
</td></tr>

<tr><td>Response</td><td>
None
</td></tr>

</table>

## users-USER_ID-stats

<table>

<tr><th>GET</th><th></th></tr>

<tr><td>Body Parameters</td><td>
None
</td></tr>

<tr><td>Query Parameters</td><td>
None
</td></tr>

<tr><td>Response</td><td>
None
</td></tr>

</table>

## users-USER_ID-games

<table>

<tr><th>GET</th><th></th></tr>

<tr><td>Body Parameters</td><td>
None
</td></tr>

<tr><td>Query Parameters</td><td>
None
</td></tr>

<tr><td>Response</td><td>
None
</td></tr>

</table>

## tournaments

<table>

<tr><th>GET</th><th></th></tr>

<tr><td>Body Parameters</td><td>
None
</td></tr>

<tr><td>Query Parameters</td><td>
None
</td></tr>

<tr><td>Response</td><td>
None
</td></tr>

</table>

<table>

<tr><th>POST</th><th></th></tr>

<tr><td>Body Parameters</td><td>
<table>

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

</td></tr>

<tr><td>Query Parameters</td><td>
None
</td></tr>

<tr><td>Response</td><td>
None
</td></tr>

</table>

## tournaments-TOURNAMENT_ID

<table>

<tr><th>GET</th><th></th></tr>

<tr><td>Body Parameters</td><td>
None
</td></tr>

<tr><td>Query Parameters</td><td>
None
</td></tr>

<tr><td>Response</td><td>
None
</td></tr>

</table>

<table>

<tr><th>PATCH</th><th></th></tr>

<tr><td>Body Parameters</td><td>
<table>

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

</table>

</td></tr>

<tr><td>Query Parameters</td><td>
None
</td></tr>

<tr><td>Response</td><td>
None
</td></tr>

</table>

## games

<table>

<tr><th>GET</th><th></th></tr>

<tr><td>Body Parameters</td><td>
None
</td></tr>

<tr><td>Query Parameters</td><td>
None
</td></tr>

<tr><td>Response</td><td>
None
</td></tr>

</table>

<table>

<tr><th>POST</th><th></th></tr>

<tr><td>Body Parameters</td><td>
<table>

<tr><td>tournament_id</td><td>
<table>

<tr><td>type</td><td>id</td></tr>

<tr><td>required</td><td>False</td></tr>

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

</td></tr>

<tr><td>Query Parameters</td><td>
None
</td></tr>

<tr><td>Response</td><td>
None
</td></tr>

</table>

## games-GAME_ID

<table>

<tr><th>GET</th><th></th></tr>

<tr><td>Body Parameters</td><td>
None
</td></tr>

<tr><td>Query Parameters</td><td>
None
</td></tr>

<tr><td>Response</td><td>
None
</td></tr>

</table>

<table>

<tr><th>PATCH</th><th></th></tr>

<tr><td>Body Parameters</td><td>
<table>

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

</td></tr>

<tr><td>Query Parameters</td><td>
None
</td></tr>

<tr><td>Response</td><td>
None
</td></tr>

</table>

<table>

<tr><th>DELETE</th><th></th></tr>

<tr><td>Body Parameters</td><td>
None
</td></tr>

<tr><td>Query Parameters</td><td>
None
</td></tr>

<tr><td>Response</td><td>
None
</td></tr>

</table>

## channels

<table>

<tr><th>GET</th><th></th></tr>

<tr><td>Body Parameters</td><td>
None
</td></tr>

<tr><td>Query Parameters</td><td>
None
</td></tr>

<tr><td>Response</td><td>
None
</td></tr>

</table>

<table>

<tr><th>POST</th><th></th></tr>

<tr><td>Body Parameters</td><td>
<table>

<tr><td>name</td><td>
<table>

<tr><td>type</td><td>string</td></tr>

<tr><td>required</td><td>True</td></tr>

<tr><td>description</td><td>Name of the channel</td></tr>

</table>

</td></tr>

</table>

</td></tr>

<tr><td>Query Parameters</td><td>
None
</td></tr>

<tr><td>Response</td><td>
None
</td></tr>

</table>

## channels-CHANNEL_ID

<table>

<tr><th>GET</th><th></th></tr>

<tr><td>Body Parameters</td><td>
None
</td></tr>

<tr><td>Query Parameters</td><td>
None
</td></tr>

<tr><td>Response</td><td>
None
</td></tr>

</table>

<table>

<tr><th>PATCH</th><th></th></tr>

<tr><td>Body Parameters</td><td>
<table>

<tr><td>name</td><td>
<table>

<tr><td>type</td><td>string</td></tr>

<tr><td>required</td><td>False</td></tr>

<tr><td>description</td><td>Name of the channel</td></tr>

</table>

</td></tr>

</table>

</td></tr>

<tr><td>Query Parameters</td><td>
None
</td></tr>

<tr><td>Response</td><td>
None
</td></tr>

</table>

<table>

<tr><th>DELETE</th><th></th></tr>

<tr><td>Body Parameters</td><td>
None
</td></tr>

<tr><td>Query Parameters</td><td>
None
</td></tr>

<tr><td>Response</td><td>
None
</td></tr>

</table>

## channels-CHANNEL_ID-members

<table>

<tr><th>GET</th><th></th></tr>

<tr><td>Body Parameters</td><td>
None
</td></tr>

<tr><td>Query Parameters</td><td>
None
</td></tr>

<tr><td>Response</td><td>
None
</td></tr>

</table>

<table>

<tr><th>POST</th><th></th></tr>

<tr><td>Body Parameters</td><td>
<table>

<tr><td>user_id</td><td>
<table>

<tr><td>type</td><td>id</td></tr>

<tr><td>required</td><td>True</td></tr>

<tr><td>description</td><td>ID of the user to add to the channel</td></tr>

</table>

</td></tr>

</table>

</td></tr>

<tr><td>Query Parameters</td><td>
None
</td></tr>

<tr><td>Response</td><td>
None
</td></tr>

</table>

## channels-CHANNEL_ID-members-USER_ID

<table>

<tr><th>DELETE</th><th></th></tr>

<tr><td>Body Parameters</td><td>
None
</td></tr>

<tr><td>Query Parameters</td><td>
None
</td></tr>

<tr><td>Response</td><td>
None
</td></tr>

</table>

## channels-CHANNEL_ID-messages

<table>

<tr><th>GET</th><th></th></tr>

<tr><td>Body Parameters</td><td>
None
</td></tr>

<tr><td>Query Parameters</td><td>
None
</td></tr>

<tr><td>Response</td><td>
None
</td></tr>

</table>

<table>

<tr><th>POST</th><th></th></tr>

<tr><td>Body Parameters</td><td>
<table>

<tr><td>content</td><td>
<table>

<tr><td>type</td><td>string</td></tr>

<tr><td>required</td><td>True</td></tr>

<tr><td>description</td><td>Content of the message</td></tr>

</table>

</td></tr>

</table>

</td></tr>

<tr><td>Query Parameters</td><td>
None
</td></tr>

<tr><td>Response</td><td>
None
</td></tr>

</table>

## messages

<table>

<tr><th>GET</th><th></th></tr>

<tr><td>Body Parameters</td><td>
None
</td></tr>

<tr><td>Query Parameters</td><td>
None
</td></tr>

<tr><td>Response</td><td>
None
</td></tr>

</table>

## messages-MESSAGE_ID

<table>

<tr><th>PATCH</th><th></th></tr>

<tr><td>Body Parameters</td><td>
<table>

<tr><td>content</td><td>
<table>

<tr><td>type</td><td>string</td></tr>

<tr><td>required</td><td>True</td></tr>

<tr><td>description</td><td>Content of the message</td></tr>

</table>

</td></tr>

</table>

</td></tr>

<tr><td>Query Parameters</td><td>
None
</td></tr>

<tr><td>Response</td><td>
None
</td></tr>

</table>

<table>

<tr><th>DELETE</th><th></th></tr>

<tr><td>Body Parameters</td><td>
None
</td></tr>

<tr><td>Query Parameters</td><td>
None
</td></tr>

<tr><td>Response</td><td>
None
</td></tr>

</table>

