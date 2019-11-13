# NFL Database ReadMe

This directory is intended to refresh and query the MySQL Database. We are using Armchair's API to seed our Database. There are 3 main classes

1. Query - Handles queries from the database
2. dbImporter  - Imports API calls into MySQL databse
3. apiGetter - Handles API calls from different Armchair endpoints

## All updates follow the schedule below via Airflow ETL

Wednesday 11:00pm: Injury and Player CSV's and API endpoints are updated.
Thursday Midnight: All CSV's and API endpoints are updated post-game except Chart and Snap.
Saturday 1:00pm: Injury, Player and Twitter CSV's/endpoints are updated. Team and Chart CSV's/endpoints are updated to include game-charted data from
the previous weeks games.
Sunday Midnight: All CSV's and API endpoints are updated post-game except Chart and Snap.
Monday Midnight: All CSV's and API endpoints are updated post-game except Chart and Snap
Tuesday 11:00am: Snap data is updated for previous weekends games. This affects Snap, Team, Offense and Defense CSV's and their related endpoints.