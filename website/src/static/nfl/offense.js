
const getResponse = async (team_name) =>{
    const response = await fetch(`/api/games/?team_name=${team_name}`)
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

const offense = async (team_name, season) => {
    let visuals =  mainFunction(team_name, season)
    return visuals
}


const displayTable = (team_name, season) => {
    getResponse(team_name).then(function(data){
   
        // EXTRACT VALUE FOR HTML HEADER. 
        // ('Book ID', 'Book Name', 'Category' and 'Price')
        var col = [];
        for (var i = 0; i < data.length; i++) {
            for (var key in data[i]) {
                if ((col.indexOf(key) === -1) & (key !='gid')) {
                    col.push(key);
                }
            }
        }
        console.log(data[1])

        // CREATE DYNAMIC TABLE.
        var table = document.createElement("table");
        table.className = 'table-sm' // Add Bootstrap Styling

        // CREATE HTML TABLE HEADER ROW USING THE EXTRACTED HEADERS ABOVE.

        var tr = table.insertRow(-1);                   // TABLE ROW.

        for (var i = 0; i < col.length; i++) {
            var th = document.createElement("th");      // TABLE HEADER.
            th.innerHTML = col[i];
            tr.appendChild(th);
        }

        // ADD JSON DATA TO THE TABLE AS ROWS.
        for (var i = 0; i < data.length; i++) {

            tr = table.insertRow(-1);

            for (var j = 0; j < col.length; j++) {
                if (data[i]['seas'] == season){
                    var tabCell = tr.insertCell(-1);
                    tabCell.innerHTML = data[i][col[j]];
                }
                
            }
        }
        
        // FINALLY ADD THE NEWLY CREATED TABLE WITH JSON DATA TO A CONTAINER.
        var divContainer = document.getElementById("showData");
        divContainer.innerHTML = "";
        divContainer.appendChild(table);
    }
)
}