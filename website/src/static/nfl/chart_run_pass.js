// function getGames(team_name){
//     let x_1 = [];
//     let y_1 = [];
//     fetch(`/api/games/${team_name}`)
//     .then((res) => {
//         if(res.ok){
//             return res.json()
//         } else{
//             throw new Error('Server response wasn\'t OK');
//         }
//     })
// }
// So since the data takes a minute to load, we need another then statement to catch the loaded data. Think we should just send the bulk
// amount of data and then parse it in the graphing function

// function graphGames(y, tag){
    
//     var ele = document.getElementById(tag)
//     var data = [
//         {
//             x: y,
//             type: 'histogram'
//         }];
//     Plotly.plot(ele, data)
// }

// const asynchronousFunction = async () => {
//     const response = await fetch('/api/games/ATL')
//     return response.json()
//   }

//   const mainFunction = () => {
//     const result = asynchronousFunction()
//     return result
//   }
  
 