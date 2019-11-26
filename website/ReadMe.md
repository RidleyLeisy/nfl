# Frontend

1. Home
    a. Tweet updates from players
    b. Recent news scraped from ESPN, Yahoo Sports, other..
    c. Stat of the day
2. Teams (Two Sided with NFL Averages)
    a. Offensive stats
        i. Games overview in table (seas, wk, day, v, h, stad, temp, humd, wspd, wdir, cond, surf, ou, sprv, ptsv, ptsh) 
        ii. Point distribution
        iii. Rush and Pass attack (direction, completion, attempts) - Check Team Stats Table
        iv. Top rushers and receivers 
        v. Touchdown analysis (play type, distance, quarter scored)
    b. Defensive stats
        i. Interceptions
        ii. Sacks
        iii. Defensive Play Calling - Check Team Stats Table
3. Players
    a. Height, weight, college, dob, nfl debut - Check Player Table
    b. Sub category dashboard based on postion
4. Match Ups
    a. Predictable stats for upcoming week game winners
    b. Weather related corrections


# REST API

## GET api/games


| Parameters | Type | Description |
| :-----------: | :--------: | :--------: |
| team_name | String | Team abbreviation is required to successfully retrieve data. Examples are ATL, SF, NO etc.. | 

Successful Response

> * HTTP 200 OK
> * Allow: GET, HEAD, OPTIONS
> * Content-Type: application/json
> * Vary: Accept

```[
    {
        "gid": 1,
        "seas": 2000, 
        "wk": 1,
        "day": "SUN",
        "v": "SF",
        "h": "ATL",
        "stad": "Georgia Dome",
        "temp": "79",
        "humd": "",
        "wspd": "",
        "wdir": "",
        "cond": "Dome",
        "surf": "AstroTurf",
        "ou": "42.5",
        "sprv": "7.0",
        "ptsv": 28,
        "ptsh": 36
    }
```
## GET api/teams


| Parameters | Type | Description |
| :-----------: | :--------: | :--------: |
| team_name | String | Team abbreviation is required to successfully retrieve data. Examples are ATL, SF, NO etc.. | 

Successful Response

> * HTTP 200 OK
> * Allow: GET, HEAD, OPTIONS
> * Content-Type: application/json
> * Vary: Accept

```[
    {
        "tid": 2,
        "gid": 1,
        "tname": "ATL",
        "pts": 36,
        "q1p": 6,
        "q2p": 16,
        "q3p": 14,
        "q4p": 0,
        "rfd": 6,
        "pfd": 13,
        "ifd": 3,
        "ry": 95,
        "ra": 32,
        "py": 264,
        "pa": 31,
        "pc": 16,
        "sk": 0,
        "ints": 0,
        "fum": 1,
        "pu": 2,
        "gpy": 95,
        "pr": 2,
        "pry": 21,
        "kr": 5,
        "kry": 145,
        "ir": 1,
        "iry": 36,
        "pen": 51,
        "top": "31.5",
        "td": 3,
        "tdr": 0,
        "tdp": 2,
        "tdt": 1
        ...
```

## GET api/player


| Parameters | Type | Description |
| :-----------: | :--------: | :--------: |
| player_name | String | Player name should be First and Last with capitalization ex.. MattRyan, LamarJackson | 

Successful Response

> * HTTP 200 OK
> * Allow: GET, HEAD, OPTIONS
> * Content-Type: application/json
> * Vary: Accept

```[
    {
        "player": "MR-2500",
        "fname": "Matt",
        "lname": "Ryan",
        "pname": "M.Ryan",
        "pos1": "QB",
        "pos2": "",
        "height": 77,
        "weight": 220,
        "dob": "1985-05-17",
        "forty": "4.89",
        "bench": 0,
        "vertical": "0.0",
        "broad": 0,
        "shuttle": "4.51",
        "cone": "7.40",
        "arm": "32.375",
        "hand": "9.500",
        "dpos": 3,
        "col": "Boston College",
        "dv": "Atlantic Coast (ACC)",
        "start": 2008,
        "cteam": "ATL",
        "posd": "QB",
        "jnum": 2,
        "dcp": 1,
        "nflid": "310\r"
    }
]
```

## GET api/offense


| Parameters | Type | Description |
| :-----------: | :--------: | :--------: |
| filter | String | player or team| 
| For player, player_name | String | Player name should be First and Last with capitalization ex.. MattRyan, LamarJackson |
| For team, team_name | String | Team abbreviation is required to successfully retrieve data. Examples are ATL, SF, NO etc.. | 
| For team, season | Int | Season to view Examples are 2001, 2009 etc.. |

Successful Response

> * HTTP 200 OK
> * Allow: GET, HEAD, OPTIONS
> * Content-Type: application/json
> * Vary: Accept

#### Player Name Response
```[
    {
        "uid": 44045,
        "gid": 2127,
        "player": "MR-2500",
        "pa": 13,
        "pc": 9,
        "py": 161,
        "ints": 0,
        "tdp": 1,
        "ra": 5,
        "sra": 0,
        "ry": -2,
        "tdr": 0,
        "trg": 0,
        "rec": 0,
        "recy": 0,
        "tdrec": 0,
        "ret": 0,
        "rety": 0,
        "tdret": 0,
        "fuml": 0,
        "peny": 0,
        "conv": 0,
        "snp": 0,
        "fp": "10.24",
        "fp2": "10.24",
        "fp3": "10.24",
        ...
```

#### Team Name Response
```
[
    {
        "uid": 55113,
        "gid": 2661,
        "player": "JN-1800",
        "pa": 0,
        "pc": 0,
        "py": 0,
        "ints": 0,
        "tdp": 0,
        "ra": 2,
        "sra": 2,
        "ry": 8,
        "tdr": 0,
        "trg": 3,
        "rec": 1,
        "recy": 9,
        "tdrec": 0,
        "ret": 3,
        "rety": 63,
        "tdret": 0,
        "fuml": 0,
        "peny": 0,
        "conv": 0,
        "snp": 0,
        "fp": "1.70",
        "fp2": "2.20",
        "fp3": "2.70",
        ...
```

## GET api/passing


| Parameters | Type | Description |
| :-----------: | :--------: | :--------: |
| filter | String | qb or wr | 
| For qb, team_name | String | Team abbreviation is required to successfully retrieve data. Examples are ATL, SF, NO etc..  | 
| For qb, season | Int | Season to view Examples are 2001, 2009 etc.. | 
| For wr, player_name | String |  Player name should be First and Last with capitalization ex.. MattRyan, LamarJackson | 

Successful Response

> * HTTP 200 OK
> * Allow: GET, HEAD, OPTIONS
> * Content-Type: application/json
> * Vary: Accept

#### WR

```
[
    {
        "pid": 785547,
        "psr": "MR-2500",
        "trg": "CR-0862",
        "loc": "SR",
        "yds": 0,
        "comp": 0,
        "succ": 0,
        "spk": 0,
        "dfb": "JH-3675"
    },
```
#### QB
```[
    {
        "pid": 431794,
        "psr": "MR-2500",
        "trg": "RW-2200",
        "loc": "SR",
        "yds": 4,
        "comp": 1,
        "succ": 1,
        "spk": 0,
        "dfb": ""
    },
```

## GET api/touchdowns


| Parameters | Type | Description |
| :-----------: | :--------: | :--------: |
| team_name | String | Team abbreviation is required to successfully retrieve data. Examples are ATL, SF, NO etc..  | 
| season | Int | Season to view Examples are 2001, 2009 etc.. |

Successful Response

> * HTTP 200 OK
> * Allow: GET, HEAD, OPTIONS
> * Content-Type: application/json
> * Vary: Accept

```
[
    {
        "pid": 431944,
        "qtr": 5,
        "min": 12,
        "sec": 36,
        "dwn": 1,
        "yds": 50,
        "pts": 6,
        "player": "RM-3900",
        "type": "RUSH"
    },
```