An Overview of Election Audit for 
1. Overview of Election Audit
    The purpose of this election audit analysis is to help Seth and Tom do an election audit to ensure the county elections have been counted accurately and to get a sense of other factors such as voter turnout for each county and percentage of votes from each county out of the total count. Aside from verifying that this has been couted fairly, it can inform policy makers and and candidates themself in the next election and how to maximize voter turnout by perhaps focusing in those counties that had a low turnout (providing cheap transportation to voter center in the next elections, etc.)

2. How many votes were cast?
    A total of 369,711 votes were cast in the election (showing code below)
    >>> print(county_votes)
{'Jefferson': 38855, 'Denver': 306055, 'Arapahoe': 24801}
- A summary of the results is as follows

Election Results
-------------------------
Total Votes: 369,711
-------------------------

County Votes:
Jefferson: received 10.509560169970598% of the vote (38,855)
Denver: received 82.78222719908253% of the vote (306,065)
Arapahoe: received 6.708212630946875% of the vote (24,801)

-------------------------
Largest County Turnout: Denver
-------------------------
Charles Casper Stockham: 23.0% (85,213)
Diana DeGette: 73.8% (272,892)
Raymon Anthony Doane: 3.1% (11,606)
-------------------------
Winner: Diana DeGette
Winning Vote Count: 272,892
Winning Percentage: 73.8%
-------------------------


>>> 
3. Election-Audit Summary
    This script can be modified by taking state-level data rather than county-level data, or use senators rather than county-level candidates. 
