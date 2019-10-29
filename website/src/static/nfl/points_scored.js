
const getResponse = async (team_name) =>{
    const response = await fetch(`/api/games/${team_name}`)
    let data = await response.json()
    return data
  }


const mainFunction = (team_name, season) => {
    getResponse(team_name).then(function(data){
        xAxis = []
        yAxis = []
        xHome = []
        xAway = []
        console.log(data)
        data.forEach(function(game){
            if (game.v == `${team_name}` && game.seas == `${season}`){
                yAxis.push(game.ptsv)
                xAxis.push(game.seas)
                xHome.push(game.ptsv)
            }
            if (game.h == `${team_name}` && game.seas == `${season}`){
                yAxis.push(game.ptsh)
                xAway.push(game.ptsh)
                xAxis.push(game.seas)
            }

    }
    )
    var ele = document.getElementById('data')

    var charts = [],
    $containers = $('#home_away td'),
    datasets = [{
        name: 'Away',
        data: xAway},
    {
        name: 'Home',
        data: xHome}];


    $.each(datasets, function(i, dataset) {
        charts.push(new Highcharts.Chart({

            chart: {
                renderTo: $containers[i],
                type: 'column',
                marginLeft: i === 0 ? 100 : 10
            },

            title: {
                text: dataset.name,
                x: i === 0 ? 90 : 0
            },

            credits: {
                enabled: false
            },

            yAxis: {
                allowDecimals: false,
                title: {
                    text: null
                },
                min: 0,
                max: 50
            },


            legend: {
                enabled: false
            },

            series: [dataset]

        }));
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
