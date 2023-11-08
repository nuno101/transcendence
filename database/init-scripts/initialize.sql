CREATE TYPE "t_status" AS ENUM (
  'created',
  'registration_open',
  'registration_closed',
  'ongoing',
  'done',
  'cancelled'
);

CREATE TYPE "m_status" AS ENUM (
  'created',
  'ongoing',
  'done',
  'cancelled'
);

CREATE TABLE "users" (
  "id" integer PRIMARY KEY,
  "username" varchar UNIQUE NOT NULL,
  "fullname" varchar,
  "avatar" bytea NOT NULL,
  "password_hash" varchar,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "sessions" (
  "session_id" integer PRIMARY KEY,
  "user_id" integer,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "friends" (
  "user_id" integer,
  "friend_id" integer,
  "created_at" timestamp
);

CREATE TABLE "tournaments" (
  "id" integer PRIMARY KEY,
  "title" varchar NOT NULL,
  "description" text,
  "creator_id" integer,
  "status" t_status NOT NULL,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "matches" (
  "id" integer PRIMARY KEY,
  "tournament_id" integer NOT NULL,
  "player1_id" integer,
  "player2_id" integer,
  "status" m_status NOT NULL,
  "score" varchar,
  "created_at" timestamp,
  "updated_at" timestamp
);

COMMENT ON COLUMN "tournaments"."description" IS 'Description of the tournament';

COMMENT ON COLUMN "matches"."tournament_id" IS 'tournament_id may be NULL';

ALTER TABLE "sessions" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id");

ALTER TABLE "friends" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id");

ALTER TABLE "friends" ADD FOREIGN KEY ("friend_id") REFERENCES "users" ("id");

ALTER TABLE "tournaments" ADD FOREIGN KEY ("creator_id") REFERENCES "users" ("id");

ALTER TABLE "matches" ADD FOREIGN KEY ("tournament_id") REFERENCES "tournaments" ("id");

ALTER TABLE "matches" ADD FOREIGN KEY ("player1_id") REFERENCES "users" ("id");

ALTER TABLE "matches" ADD FOREIGN KEY ("player2_id") REFERENCES "users" ("id");
