#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach

import logging


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    database = connect()
    cursor = database.cursor()
    cursor.execute("DELETE FROM matches")
    database.commit()
    database.close()


def deletePlayers():
    """Remove all the player records from the database."""
    database = connect()
    cursor = database.cursor()
    cursor.execute("DELETE FROM players")
    database.commit()
    database.close()


def countPlayers():
    """Returns the number of players currently registered."""
    database = connect()
    cursor = database.cursor()
    cursor.execute("SELECT COUNT(*) FROM players")
    playercount = cursor.fetchone()[0]
    database.close()

    return playercount


def registerPlayer(name):
    """Adds a player to the tournament database"""

    database = connect()
    cursor = database.cursor()
    cursor.execute("INSERT INTO players (player_name) VALUES (%s)", (name,))
    database.commit()
    database.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    database = connect()
    cursor = database.cursor()

    # large query has been put into a var below
    sql = """SELECT player_id,
                   player_name,
                   (SELECT COUNT(*) FROM matches WHERE player_id=winner_id) as wins,
                   (SELECT COUNT(*) FROM matches WHERE player_id=winner_id OR player_id=loser_id) as total_matches
            FROM players
            ORDER BY wins DESC"""

    cursor.execute(sql)
    # returns the standings list
    standings_list = cursor.fetchall()  
    return standings_list


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    database = connect()
    cursor = database.cursor()
    cursor.execute("INSERT INTO matches (loser_id, winner_id) VALUES (%s, %s)", (loser, winner,))
    database.commit()
    database.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
    """
    database = connect()
    cursor = database.cursor()

    standings = playerStandings()
    #confirm standings are correctly returned
    print standings
    pairings = []
    player_count = countPlayers()
    #for each entry in standings, select values from 0 to 1 and put them in a list
    players = [i[0:2] for i in standings]
    i = 0

    while i < player_count:
        pair = players[i] + players[i+1]
        pairings.append(pair)
        i += 2
    return pairings
