# Endpoint documentation

## Statistics

Total number of urls: 29
- [/channels](#`/channels`)
- [/channels/CHANNEL_ID](#`/channels/CHANNEL_ID`)
- [/channels/CHANNEL_ID/members](#`/channels/CHANNEL_ID/members`)
- [/channels/CHANNEL_ID/members/USER_ID](#`/channels/CHANNEL_ID/members/USER_ID`)
- [/channels/CHANNEL_ID/messages](#`/channels/CHANNEL_ID/messages`)
- [/games](#`/games`)
- [/games/GAME_ID](#`/games/GAME_ID`)
- [/login](#`/login`)
- [/logout](#`/logout`)
- [/messages](#`/messages`)
- [/messages/MESSAGE_ID](#`/messages/MESSAGE_ID`)
- [/tournaments](#`/tournaments`)
- [/tournaments/TOURNAMENT_ID](#`/tournaments/TOURNAMENT_ID`)
- [/users](#`/users`)
- [/users/USER_ID](#`/users/USER_ID`)
- [/users/USER_ID/avatar](#`/users/USER_ID/avatar`)
- [/users/USER_ID/games](#`/users/USER_ID/games`)
- [/users/USER_ID/stats](#`/users/USER_ID/stats`)
- [/users/me](#`/users/me`)
- [/users/me/avatar](#`/users/me/avatar`)
- [/users/me/blocked](#`/users/me/blocked`)
- [/users/me/blocked/USER_ID](#`/users/me/blocked/USER_ID`)
- [/users/me/channels](#`/users/me/channels`)
- [/users/me/friends](#`/users/me/friends`)
- [/users/me/friends/USER_ID](#`/users/me/friends/USER_ID`)
- [/users/me/friends/requests](#`/users/me/friends/requests`)
- [/users/me/friends/requests/REQUEST_ID](#`/users/me/friends/requests/REQUEST_ID`)
- [/users/me/notifications](#`/users/me/notifications`)
- [/users/me/notifications/NOTIFICATION_ID](#`/users/me/notifications/NOTIFICATION_ID`)

Total number of methods: 48
- GET: 20
- POST: 11
- PATCH: 7
- DELETE: 10

## Endpoints

### `/channels`

| Method | Params | Params Optional |
| --- | --- | --- |
| GET |  |  |
| POST | name |  |

### `/channels/CHANNEL_ID`

| Method | Params | Params Optional |
| --- | --- | --- |
| DELETE |  |  |
| GET |  |  |
| PATCH |  | name |

### `/channels/CHANNEL_ID/members`

| Method | Params | Params Optional |
| --- | --- | --- |
| GET |  |  |
| PATCH | user_id |  |

### `/channels/CHANNEL_ID/members/USER_ID`

| Method | Params | Params Optional |
| --- | --- | --- |
| DELETE |  |  |

### `/channels/CHANNEL_ID/messages`

| Method | Params | Params Optional |
| --- | --- | --- |
| GET |  |  |
| POST | content |  |

### `/games`

| Method | Params | Params Optional |
| --- | --- | --- |
| GET |  |  |
| POST | tournament_id, player1_id, player2_id, player1_score, player2_score |  |

### `/games/GAME_ID`

| Method | Params | Params Optional |
| --- | --- | --- |
| DELETE |  |  |
| GET |  |  |
| PATCH |  | player1_score, player2_score, status |

### `/login`

| Method | Params | Params Optional |
| --- | --- | --- |
| POST | username, password |  |

### `/logout`

| Method | Params | Params Optional |
| --- | --- | --- |
| POST |  |  |

### `/messages`

| Method | Params | Params Optional |
| --- | --- | --- |
| GET |  |  |

### `/messages/MESSAGE_ID`

| Method | Params | Params Optional |
| --- | --- | --- |
| DELETE |  |  |
| PATCH | content |  |

### `/tournaments`

| Method | Params | Params Optional |
| --- | --- | --- |
| GET |  |  |
| POST | title, description |  |

### `/tournaments/TOURNAMENT_ID`

| Method | Params | Params Optional |
| --- | --- | --- |
| GET |  |  |
| PATCH |  | title, description |

### `/users`

| Method | Params | Params Optional |
| --- | --- | --- |
| GET |  |  |
| POST | username, password |  |

### `/users/USER_ID`

| Method | Params | Params Optional |
| --- | --- | --- |
| DELETE |  |  |
| GET |  |  |
| PATCH |  | nickname, password |

### `/users/USER_ID/avatar`

| Method | Params | Params Optional |
| --- | --- | --- |
| GET |  |  |

### `/users/USER_ID/games`

| Method | Params | Params Optional |
| --- | --- | --- |
| GET |  |  |

### `/users/USER_ID/stats`

| Method | Params | Params Optional |
| --- | --- | --- |
| GET |  |  |

### `/users/me`

| Method | Params | Params Optional |
| --- | --- | --- |
| DELETE |  |  |
| GET |  |  |
| PATCH | nickname, password |  |

### `/users/me/avatar`

| Method | Params | Params Optional |
| --- | --- | --- |
| POST |  |  |

### `/users/me/blocked`

| Method | Params | Params Optional |
| --- | --- | --- |
| GET |  |  |
| POST | user_id |  |

### `/users/me/blocked/USER_ID`

| Method | Params | Params Optional |
| --- | --- | --- |
| DELETE |  |  |

### `/users/me/channels`

| Method | Params | Params Optional |
| --- | --- | --- |
| GET |  |  |

### `/users/me/friends`

| Method | Params | Params Optional |
| --- | --- | --- |
| GET |  |  |

### `/users/me/friends/USER_ID`

| Method | Params | Params Optional |
| --- | --- | --- |
| DELETE |  |  |

### `/users/me/friends/requests`

| Method | Params | Params Optional |
| --- | --- | --- |
| GET |  |  |
| POST | user_id |  |

### `/users/me/friends/requests/REQUEST_ID`

| Method | Params | Params Optional |
| --- | --- | --- |
| DELETE |  |  |
| POST |  |  |

### `/users/me/notifications`

| Method | Params | Params Optional |
| --- | --- | --- |
| GET |  |  |

### `/users/me/notifications/NOTIFICATION_ID`

| Method | Params | Params Optional |
| --- | --- | --- |
| DELETE |  |  |

