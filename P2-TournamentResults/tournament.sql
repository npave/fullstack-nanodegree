-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;

\connect tournament;

-- players contains the name of players in the tournament.
CREATE TABLE players (
	id_player serial PRIMARY KEY, 
	name varchar
);

  
-- results contains the results of each match.    
CREATE TABLE results(
    	id_result serial PRIMARY KEY,
    	winner integer references players(id_player),
    	loser integer references players(id_player)
);
 
-- winner view contains each player with the number of matches won.
CREATE VIEW winner AS SELECT players.id_player AS id_player, COUNT(winner) AS total_win
        FROM players LEFT JOIN results ON players.id_player = winner GROUP BY id_player;

-- matches view contains each player with the number of matches played.
CREATE VIEW matches AS SELECT players.id_player AS id_player, COUNT(winner + loser) AS total_match
        FROM players LEFT JOIN results ON players.id_player = results.winner OR
	players.id_player = results.loser GROUP BY players.id_player;

    
    
