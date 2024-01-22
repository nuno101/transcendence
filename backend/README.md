# Http api

## Authentication

You can login using the endpoint `POST /api/login` with the following payload:

```json
{
  "username": "your-username",
  "password": "your-password"
}
```

### User registration

You can register a new user using the endpoint `POST /api/register` with the following payload:

```json
{
  "username": "your-username",
  "password": "your-password"
}
```

# Websocket api

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