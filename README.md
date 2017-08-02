# Tournament-Results
Project Submission for Udacity's Relational Databases Course 

To run this project you will need to ensure you have both **Python** and **PostgreSQL** installed

 - Clone the Udacity virtual machine repository: [Udacity VM Repo](https://github.com/udacity/fullstack-nanodegree-vm)
 - Follow the instructions here to set up your environment: [Udacity Vagrant Instructions ](https://www.udacity.com/wiki/ud197/install-vagrant)


**In your terminal**

 3. CD into the ...\fullstack-nanodegree-vm\vagrant directory.
 
 4. Run the command `vagrant up`
 
 5. Run the command `vagrant ssh`
 
 6.  CD into the /vagrant/tournament directory

 7. Type the command `psql`

 8. Type the command `\i tournament.sql` (This creates the tables)

 9. In a separate terminal CD into the ...\fullstack-nanodegree-vm\vagrant directory again and run `vagrant ssh`
 
 10.  CD into the /vagrant/tournament directory and run `python tournament_test.py`

**You will now be able to test the below functions within tournament.py**

| __tournament.py function__                                                                                                                                                                                                                                          | __tournament.py test function__ |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------|
| **Connect:**  Meant to connect to the database. Already set up for you.                                                                                                                                                                                             |                             |
| **deleteMatches:** Remove all the matches records from the database.                                                                                                                                                                                                |                             |
| **deletePlayers:** Remove all the player records from the database.                                                                                                                                                                                                 |                             |
| **countPlayers:** Returns the number of players currently registered                                                                                                                                                                                                | testCount                   |
| **registerPlayer:**  Adds a player to the tournament database.                                                                                                                                                                                                      |                             |
| **playerStandings:** Returns a list of the players and their win records, sorted by wins. You can use the player standings table created in your .sql file for reference.                                                                                           | testStandingsBeforeMatches  |
| **reportMatch:** This is to simply populate the matches table and record the winner  and loser as (winner,loser) in the insert statement.                                                                                                                           | testReportMatches           |
| **swissPairings:** Returns a list of pairs of players for the next round of a match. Here all we are doing is the pairing of alternate players  from the player standings table, zipping them up and appending  them to a list with values:(id1, name1, id2, name2) | testPairings                |
