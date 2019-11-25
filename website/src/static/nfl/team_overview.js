
const getResponse = async (team_name) =>{
    const response = await fetch(`/api/games/${team_name}`)
    let data = await response.json()
    return data
  }