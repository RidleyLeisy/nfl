## games table has multiple game ids since we have to pull all teams data. We are solving this by deleted duplicate rows once they are in the db
## rather than deleting them in the json file before uploading
use this to delete multiple game ids
ALTER IGNORE TABLE games
ADD UNIQUE INDEX idx_name (gid);

