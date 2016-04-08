# Tournament Results

Module Python and database to keep track of pairs and matches in a game 
tournament that use the Swiss system. This systems pairing up players in 
each round following some rules:
* players are not eliminated, 
* each player should be paired with another player with the same number of wins,
 or as close as possible.

## Features
* Written in Python 2.7
* Works with Windows

## Project structure

This project consist of two files:
* tournament.sql, database structure to stores the game matches between players.
* tournament.py, module to rank the players and pair them up in matches in a 
  tournament. 

## How to use this code

To start you have to create a database for that you have to run the 
*tournament.sql* file.
Finally, you have to run `python tournament.py`.