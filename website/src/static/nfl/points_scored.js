
const getResponse = async (team_name) =>{
    const response = await fetch(`/api/games/${team_name}`)
    let data = await response.json()
    return data
  }


const mainFunction = (team_name, season) => {
    getResponse(team_name).then(function(data){
        xAxis = []
        yAxis = []
        pointsScored = []
        weekLabels = []

        console.log(data)
        data.forEach(function(game){
            if (game.v == `${team_name}` && game.seas == `${season}`){
                yAxis.push(game.ptsv)
                xAxis.push(game.seas)
                pointsScored.push(game.ptsv)
                weekLabels.push('Week ' + game.wk)
            }
            if (game.h == `${team_name}` && game.seas == `${season}`){
                yAxis.push(game.ptsh)
                xAxis.push(game.seas)
                pointsScored.push(game.ptsh)
                weekLabels.push('Week ' + game.wk)
            }
    }
    )
    var ele = document.getElementById('data')
    var awayHome = Highcharts.chart('graph', {
        xAxis:{
            categories: weekLabels
        },
        plotOptions: {
            series: {
                // general options for all series
            },
            line: {
                // shared options for all line series
            }
        },
        series: [{
            // specific options for this series instance
            type: 'line',
            data: pointsScored
        }]
    });

    var myChart = Highcharts.chart('data', {
        title: {
            text: 'Distribution of Points by Season'
        },
        xAxis: [{
            title: { text: 'Count' },
            alignTicks: false
        }, {
            title: { text: 'Histogram' },
            alignTicks: false,
            opposite: true
        }],

        yAxis: [{
            title: { text: 'Points' }
        }, {
            title: { text: 'Histogram' },
            opposite: true
        }],
            series: [{
                type: 'histogram',
                xAxis: 1,
                yAxis: 1,
                baseSeries: 1
            }, {
                name: 'Data',
                type: 'scatter',
                data: yAxis,
                id: 's1',
                marker: {
                    radius: 1.5
            }}]
        });
    }).then(function(xAxis) {
          return xAxis
      });
    }

const test = async (team_name, season) => {
    let t =  mainFunction(team_name, season)
    return t
}
