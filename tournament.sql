-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

--if prior database exists, delete it
DROP DATABASE IF EXISTS tournament;

CREATE DATABASE tournament;

--connect to the database
\c tournament;


--if prior tables exist, delete them
DROP TABLE IF EXISTS players CASCADE;
DROP TABLE IF EXISTS matches CASCADE;

--create the tables

CREATE TABLE players(
  player_id SERIAL PRIMARY KEY,
  player_name TEXT
);

CREATE TABLE matches(
  match_id SERIAL PRIMARY KEY,
  winner_id int references players(player_id),
  loser_id int references players(player_id)
);
