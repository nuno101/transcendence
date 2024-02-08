# Http api

## Authentication

You can login using the endpoint `POST /api/login` with the following payload:

```json
{
  "username": "your-username",
  "password": "your-password"
}
```

## User registration

You can register a new user using the endpoint `POST /api/register` with the following payload:

```json
{
  "username": "your-username",
  "password": "your-password"
}
```

## Endpoints

See [api postman collection](../docs/api-http/ft_transcendence-http.postman_collection.json) or the [README](../docs/api-http/README.md) documentation.

# Websocket event notification api

## Authentication

You need to login via the http [authentication endpoint](#authentication) before you can use the websocket api.

## Request/response format

```json
{
  "event": "event-name",
  "payload": {
    EVENT SPECIFIC DATA
  }
}
```

### Table of contents

- [Server to client Events](#server-to-client-events)
  - [error](#error)
  - [pong](#pong)
  - [update_user](#update_user)
  - [delete_user](#delete_user)
  - [create_notification](#create_notification)
  - [delete_notification](#delete_notification)
  - [remove_friend](#remove_friend)
  - [create_friend_request](#create_friend_request)
  - [accept_friend_request](#accept_friend_request)
  - [cancel_friend_request](#cancel_friend_request--decline_friend_request)
  - [create_message](#create_message)
  - [update_message](#update_message)
  - [delete_message](#delete_message)
  - [create_channel](#create_channel)
  - [update_channel](#update_channel)
  - [delete_channel](#delete_channel)
- [Client to server Events](#client-to-server-events)
  - [ping](#ping)

### Server to client Events

#### `error`

This event is sent when an error occurs.

PAYLOAD: [Error](#error-payload)

#### `pong`

This event is sent in response to a [ping](#ping) event.

PAYLOAD: [empty object](#empty-object)

#### `update_user`

This event is sent when a user is updated.

PAYLOAD: [User](#user)

#### `delete_user`

This event is sent when a user is deleted.

PAYLOAD:
  
```json
{
  "id": "user-id"
}
```

#### `create_notification`

This event is triggered when a new user notification is created in the backend

PAYLOAD: [Notification](#notification)

#### `create_notification`

This event is triggered when a user notification is deleted

PAYLOAD:
  
```json
{
  "id": "notification-id"
}
```

#### `remove_friend`

This event is sent when a friend is removed.

PAYLOAD:
  
```json
{
  "id": "friend-id"
}
```

#### `create_friend_request`

This event is sent when a friend request is created.

PAYLOAD: [Friend request](#friend-request)

#### `accept_friend_request`

This event is sent when a friend request is accepted.

PAYLOAD: [Friend request](#friend-request)

#### `cancel_friend_request`/ `decline_friend_request`

This event is sent when a friend request is cancelled/declined.

PAYLOAD:
    
  ```json
  {
    "id": "friend-request-id"
  }
  ```

#### `create_message`

This event is sent when a message is created.

PAYLOAD: [Message](#message)

#### `update_message`

This event is sent when a message is updated.

PAYLOAD: [Message](#message)

#### `delete_message`

This event is sent when a message is deleted.

PAYLOAD:
  
```json
{
  "id": "message-id"
}
```

#### `create_channel`

This event is sent when a channel is created.

PAYLOAD: [Channel](#channel)

#### `update_channel`

This event is sent when a channel is updated.

PAYLOAD: [Channel](#channel)

#### `delete_channel`

This event is sent when a channel is deleted.

PAYLOAD:
  
```json
{
  "id": "channel-id"
}
```

### Client to server Events

#### Table of contents

- [ping](#ping)

#### `ping`

This event can be sent to ping the server.

PAYLOAD: [empty object](#empty-object)

Response event: [pong](#pong)

### Payloads

#### `empty object`

```json
{}
```

#### `Error payload`

```json
{
  "message": "error-message"
}
```

#### `User`

```json
{
  "id": "user-id",
  "username": "user-username",
  "nickname": "user-nickname",
  "created_at": "user-creation-date",
  "updated_at": "user-last-update-date"
  "status": "online|offline" or null
}
```

#### `Friend request`

```json
{
  "id": "friend-request-id",
  "from_user": USER_PAYLOAD,
  "to_user": USER_PAYLOAD,
  "created_at": "friend-request-creation-date"
}
```

#### `Tournament`

```json
{
  "id": "tournament-id",
  "title": "tournament-title",
  "description": "tournament-description",
  "creator_id": "tournament-creator-id",
  "status": "created|registration_open|registration_closed|ongoing|done|cancelled",
  "created_at": "tournament-creation-date",
  "updated_at": "tournament-last-update-date"
}
```

#### `Game`

```json
{
  "id": "game-id",
  "tournament_id": "tournament-id",
  "player1": USER_PAYLOAD,
  "player2": USER_PAYLOAD,
  "status": "created|ongoing|done|cancelled",
  "player1_score": "player1-score",
  "player2_score": "player2-score",
  "created_at": "game-creation-date",
  "updated_at": "game-last-update-date"
}
```

#### `Notification`

```json
{
  "id": "notification-id",
  "type": "type",
  "content": "content",
  "user_id": "user-id",
  "created_at": "notification-creation-date"
}
```

#### `Channel`

```json
{
  "id": "channel-id",
  "name": "channel-name",
  "created_at": "channel-creation-date",
  "updated_at": "channel-last-update-date",
  "members": [
    USER_PAYLOAD,
    ...
  ]
}
```

#### `Message`

```json
{
  "id": "message-id",
  "content": "message-content",
  "author_id": "author-id",
  "channel_id": "channel-id",
  "created_at": "message-creation-date",
  "updated_at": "message-last-update-date"
}
```