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
                   FROM players"""

    cursor.execute(sql)
    standings_list = cursor.fetchall()  # returns the standings list
    return standings_list


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    # create a row in the 'matches' table, recording who won
    database = connect()
    cursor = database.cursor()

    cursor.execute("INSERT INTO matches (loser_id, winner_id) VALUES (%s, %s)", (loser, winner,))
    database.commit()
    database.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    database = connect()
    cursor = database.cursor()

    # large query has been put into a var below
    sql = """SELECT player_id,
                   player_name,
                   (SELECT COUNT(*) FROM matches WHERE player_id=winner_id) as wins,
                   (SELECT COUNT(*) FROM matches WHERE player_id=winner_id OR player_id=loser_id) as total_matches
                   FROM players"""

    cursor.execute(sql)
    pairings_list = cursor.fetchall()  # returns the pairings list
    return pairings_list