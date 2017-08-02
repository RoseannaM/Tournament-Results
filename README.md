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

**You will now be able to test the functions within tournament.py**
