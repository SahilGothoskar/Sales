Design Requirements

 

You will check whether your tables are in First normal form (1NF), Second normal form (2NF) and Third normal form (3NF).  If not, you’ll restructure your database so that all of the tables are in Third normal form; that is, you normalize the database.

 

Your submission must include:

    A check that your tables are in First normal form (1NF)
    A check that your tables are in Second normal form (2NF)
    A check that your tables are in Third normal form (3NF)
    The final SQL of a normalized database in Third normal form (3NF).
    Views for all of your use-cases

 

First normal form (1NF)

    Each table has a primary key: minimal set of attributes which can uniquely identify a record
    The values in each column of a table are atomic (No multi-value attributes allowed).
    There are no repeating groups: two columns do not store similar information in the same table.

 

 

Second normal form (2NF)

    All requirements for 1st NF must be met.
    No partial dependencies.
    No calculated data

 

 

Third normal form (3NF)

    All requirements for 2nd NF must be met.
    Eliminate fields that do not directly depend on the primary key; that is no transitive dependencies.

 

Create Views Syntax

 

CREATE VIEW  Miley_Tweets AS

SELECT Tweets.tweetid, Tweets.text, Users.screen_name 

FROM Tweets

JOIN Users ON (Users.userid = Tweets.userid)

WHERE Users.screen_name=  ="MileyCyrus";

 

Scoring Rubric

    (25 points) Check that your tables are in First normal form (1NF)
    (25 points) Check that your tables are in Second normal form (2NF)
    (25 points) Check that your tables are in Third normal form (3NF) and the final SQL
    (25 points) Views for all of your use-cases
