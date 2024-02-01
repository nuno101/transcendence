# Endpoint documentation

## Statistics

Total number of urls: 29
- [/channels](#channels)
- [/channels/CHANNEL_ID](#channels-CHANNEL_ID)
- [/channels/CHANNEL_ID/members](#channels-CHANNEL_ID-members)
- [/channels/CHANNEL_ID/members/USER_ID](#channels-CHANNEL_ID-members-USER_ID)
- [/channels/CHANNEL_ID/messages](#channels-CHANNEL_ID-messages)
- [/games](#games)
- [/games/GAME_ID](#games-GAME_ID)
- [/login](#login)
- [/logout](#logout)
- [/messages](#messages)
- [/messages/MESSAGE_ID](#messages-MESSAGE_ID)
- [/tournaments](#tournaments)
- [/tournaments/TOURNAMENT_ID](#tournaments-TOURNAMENT_ID)
- [/users](#users)
- [/users/USER_ID](#users-USER_ID)
- [/users/USER_ID/avatar](#users-USER_ID-avatar)
- [/users/USER_ID/games](#users-USER_ID-games)
- [/users/USER_ID/stats](#users-USER_ID-stats)
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

Total number of methods: 48
- GET: 20
- POST: 11
- PATCH: 7
- DELETE: 10

## Endpoints

### channels

#### GET

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

</td></tr></table>

#### POST

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

| name | type | required | description |
| --- | --- | --- | --- |
| name | string | True | Name of the channel |
</td><td>
None

</td><td>
None

</td></tr></table>

### channels-CHANNEL_ID

#### DELETE

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

</td></tr></table>

#### GET

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

</td></tr></table>

#### PATCH

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

| name | type | required | description |
| --- | --- | --- | --- |
| name | string | False | Name of the channel |
</td><td>
None

</td><td>
None

</td></tr></table>

### channels-CHANNEL_ID-members

#### GET

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

</td></tr></table>

#### PATCH

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

| name | type | required | description |
| --- | --- | --- | --- |
| user_id | id | True | ID of the user to add to the channel |
</td><td>
None

</td><td>
None

</td></tr></table>

### channels-CHANNEL_ID-members-USER_ID

#### DELETE

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

</td></tr></table>

### channels-CHANNEL_ID-messages

#### GET

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

</td></tr></table>

#### POST

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

| name | type | required | description |
| --- | --- | --- | --- |
| content | string | True | Content of the message |
</td><td>
None

</td><td>
None

</td></tr></table>

### games

#### GET

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

</td></tr></table>

#### POST

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

| name | type | required | description |
| --- | --- | --- | --- |
| tournament_id | id | False | ID of the tournament |
| player1_id | id | True | ID of the first player |
| player2_id | id | True | ID of the second player |
| player1_score | integer | True | Score of the first player |
| player2_score | integer | True | Score of the second player |
</td><td>
None

</td><td>
None

</td></tr></table>

### games-GAME_ID

#### DELETE

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

</td></tr></table>

#### GET

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

</td></tr></table>

#### PATCH

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

| name | type | required | description |
| --- | --- | --- | --- |
| player1_score | integer | False | Score of the first player |
| player2_score | integer | False | Score of the second player |
| status | string | False | Status of the game |
</td><td>
None

</td><td>
None

</td></tr></table>

### login

#### POST

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

| name | type | required | description |
| --- | --- | --- | --- |
| username | string | True | Username of the user |
| password | string | True | Password of the user |
</td><td>
None

</td><td>
None

</td></tr></table>

### logout

#### POST

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

</td></tr></table>

### messages

#### GET

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

</td></tr></table>

### messages-MESSAGE_ID

#### DELETE

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

</td></tr></table>

#### PATCH

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

| name | type | required | description |
| --- | --- | --- | --- |
| content | string | True | Content of the message |
</td><td>
None

</td><td>
None

</td></tr></table>

### tournaments

#### GET

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

</td></tr></table>

#### POST

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

| name | type | required | description |
| --- | --- | --- | --- |
| title | string | True | Title of the tournament |
| description | string | False | Description of the tournament |
</td><td>
None

</td><td>
None

</td></tr></table>

### tournaments-TOURNAMENT_ID

#### GET

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

</td></tr></table>

#### PATCH

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

| name | type | required | description |
| --- | --- | --- | --- |
| title | string | False | Title of the tournament |
| description | string | False | Description of the tournament |
</td><td>
None

</td><td>
None

</td></tr></table>

### users

#### GET

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

</td></tr></table>

#### POST

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

| name | type | required | description |
| --- | --- | --- | --- |
| username | string | True | Username of the user |
| password | string | True | Password of the user |
</td><td>
None

</td><td>
None

</td></tr></table>

### users-USER_ID

#### DELETE

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

</td></tr></table>

#### GET

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

</td></tr></table>

#### PATCH

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

| name | type | required | description |
| --- | --- | --- | --- |
| nickname | string | False | Nickname of the user |
| password | string | False | Password of the user |
</td><td>
None

</td><td>
None

</td></tr></table>

### users-USER_ID-avatar

#### GET

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

</td></tr></table>

### users-USER_ID-games

#### GET

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

</td></tr></table>

### users-USER_ID-stats

#### GET

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

</td></tr></table>

### users-me

#### DELETE

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

</td></tr></table>

#### GET

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

</td></tr></table>

#### PATCH

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

| name | type | required | description |
| --- | --- | --- | --- |
| nickname | string | False | Nickname of the user |
| password | string | False | Password of the user |
</td><td>
None

</td><td>
None

</td></tr></table>

### users-me-avatar

#### POST

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

</td></tr></table>

### users-me-blocked

#### GET

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

</td></tr></table>

#### POST

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

| name | type | required | description |
| --- | --- | --- | --- |
| user_id | id | True | ID of the user to block |
</td><td>
None

</td><td>
None

</td></tr></table>

### users-me-blocked-USER_ID

#### DELETE

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

</td></tr></table>

### users-me-channels

#### GET

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

</td></tr></table>

### users-me-friends

#### GET

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

</td></tr></table>

### users-me-friends-USER_ID

#### DELETE

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

</td></tr></table>

### users-me-friends-requests

#### GET

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

None

</td><td>
| name | type | required | default | description |
| --- | --- | --- | --- | --- |
| type | string | True | all | Type of the friend requests returned (all, sent, received) |
</td><td>
None

</td></tr></table>

#### POST

<table>
<tr>
<th>Body Parameters</th>
<th>Query Parameters</th>
<th>Response</th>
</tr><tr><td>

| name | type | required | description |
| --- | --- | --- | --- |
| username | string | True | Username of the to send the friend request to |
</td><td>
None

</td><td>
None

</td></tr></table>

### users-me-friends-requests-REQUEST_ID

#### DELETE

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

</td></tr></table>

#### POST

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

</td></tr></table>

### users-me-notifications

#### GET

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

</td></tr></table>

### users-me-notifications-NOTIFICATION_ID

#### DELETE

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

</td></tr></table>

