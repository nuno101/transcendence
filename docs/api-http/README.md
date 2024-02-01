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

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| - | - | - | - |

#### POST

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| name | string | ✅ | Name of the channel |

### channels-CHANNEL_ID

#### DELETE

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| - | - | - | - |

#### GET

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| - | - | - | - |

#### PATCH

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| name | string | ❌ | Name of the channel |

### channels-CHANNEL_ID-members

#### GET

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| - | - | - | - |

#### PATCH

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| user_id | id | ✅ | ID of the user to add to the channel |

### channels-CHANNEL_ID-members-USER_ID

#### DELETE

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| - | - | - | - |

### channels-CHANNEL_ID-messages

#### GET

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| - | - | - | - |

#### POST

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| content | string | ✅ | Content of the message |

### games

#### GET

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| - | - | - | - |

#### POST

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| tournament_id | id | ❌ | ID of the tournament |
| player1_id | id | ✅ | ID of the first player |
| player2_id | id | ✅ | ID of the second player |
| player1_score | integer | ✅ | Score of the first player |
| player2_score | integer | ✅ | Score of the second player |

### games-GAME_ID

#### DELETE

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| - | - | - | - |

#### GET

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| - | - | - | - |

#### PATCH

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| player1_score | integer | ❌ | Score of the first player |
| player2_score | integer | ❌ | Score of the second player |
| status | string | ❌ | Status of the game |

### login

#### POST

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| username | string | ✅ | Username of the user |
| password | string | ✅ | Password of the user |

### logout

#### POST

| Param | Type | Required | Description |
| --- | --- | --- | --- |

### messages

#### GET

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| - | - | - | - |

### messages-MESSAGE_ID

#### DELETE

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| - | - | - | - |

#### PATCH

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| content | string | ✅ | Content of the message |

### tournaments

#### GET

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| - | - | - | - |

#### POST

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| title | string | ✅ | Title of the tournament |
| description | string | ❌ | Description of the tournament |

### tournaments-TOURNAMENT_ID

#### GET

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| - | - | - | - |

#### PATCH

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| title | string | ❌ | Title of the tournament |
| description | string | ❌ | Description of the tournament |

### users

#### GET

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| - | - | - | - |

#### POST

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| username | string | ✅ | Username of the user |
| password | string | ✅ | Password of the user |

### users-USER_ID

#### DELETE

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| - | - | - | - |

#### GET

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| - | - | - | - |

#### PATCH

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| nickname | string | ❌ | Nickname of the user |
| password | string | ❌ | Password of the user |

### users-USER_ID-avatar

#### GET

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| - | - | - | - |

### users-USER_ID-games

#### GET

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| - | - | - | - |

### users-USER_ID-stats

#### GET

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| - | - | - | - |

### users-me

#### DELETE

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| - | - | - | - |

#### GET

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| - | - | - | - |

#### PATCH

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| nickname | string | ❌ | Nickname of the user |
| password | string | ❌ | Password of the user |

### users-me-avatar

#### POST

| Param | Type | Required | Description |
| --- | --- | --- | --- |

### users-me-blocked

#### GET

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| - | - | - | - |

#### POST

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| user_id | id | ✅ | ID of the user to block |

### users-me-blocked-USER_ID

#### DELETE

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| - | - | - | - |

### users-me-channels

#### GET

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| - | - | - | - |

### users-me-friends

#### GET

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| - | - | - | - |

### users-me-friends-USER_ID

#### DELETE

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| - | - | - | - |

### users-me-friends-requests

#### GET

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| - | - | - | - |

#### POST

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| username | string | ✅ | Username of the to send the friend request to |

### users-me-friends-requests-REQUEST_ID

#### DELETE

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| - | - | - | - |

#### POST

| Param | Type | Required | Description |
| --- | --- | --- | --- |

### users-me-notifications

#### GET

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| - | - | - | - |

### users-me-notifications-NOTIFICATION_ID

#### DELETE

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| - | - | - | - |

