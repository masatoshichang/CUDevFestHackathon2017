var connection = new ActiveXObject("ADODB.Connection") ;

var connectionstring="Driver={ODBC Driver 13 for SQL Server};Server=tcp:cudevfest2017.database.windows.net,1433;Database=cudevfest2017;Uid=devfest@cudevfest2017;Pwd=!23QweAsdZxc;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;";

connection.Open(connectionstring);
var rs = new ActiveXObject("ADODB.Recordset");

rs.Open("SELECT distinct section from dbo.EmotionSection", connection);
rs.MoveFirst()
var sections = [];
while(!rs.eof)
{
   sections.push(rs.fields("section").value);
   rs.movenext();
}

rs.close();

var data = [];
for(var i = 0; i < 1; i++){
  console.log(sections[i]);
  rs.Open("SELECT * FROM dbo.EmotionSection where section = \'" + sections[i] + "\' and not sadness = 0 order by date asc")
  while(!rs.eof)
  {
    console.log(rs.fields("date").value);
    var obj = {date: rs.fields("date").value, anger: rs.fields("anger")};
    data.push(obj);
    rs.movenext();
  }
  rs.close();
}
connection.close(); 


// Set the dimensions of the canvas / graph
var margin = {top: 30, right: 20, bottom: 30, left: 50},
    width = 600 - margin.left - margin.right,
    height = 270 - margin.top - margin.bottom;

// Parse the date / time
var parseDate = d3.time.format("%d-%b-%y").parse;

// Set the ranges
var x = d3.time.scale().range([0, width]);
var y = d3.scale.linear().range([height, 0]);

// Define the axes
var xAxis = d3.svg.axis().scale(x)
    .orient("bottom").ticks(5);

var yAxis = d3.svg.axis().scale(y)
    .orient("left").ticks(5);

// Define the line
var valueline = d3.svg.line()
    .x(function(d) { return x(d.date); })
    .y(function(d) { return y(d.close); });
    
// Adds the svg canvas
var svg = d3.select("body")
    .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
    .append("g")
        .attr("transform", 
              "translate(" + margin.left + "," + margin.top + ")");

svg.selectAll("circle")
   .data(data)
   .enter()
   .append("circle")
   .attr("cx", function(d) {
        return d['date'];
   })
   .attr("cy", function(d) {
        return d['anger'];
   })
   .attr("r", 5);

// Get the data
// d3.data(data, function(error, data) {
//     data.forEach(function(d) {
//         d.date = parseDate(d.date);
//         d.anger = d.anger;
//     });

//     // Scale the range of the data
//     x.domain(d3.extent(data, function(d) { return d.date; }));
//     y.domain([0, d3.max(data, function(d) { return d.close; })]);

//     // Add the valueline path.
//     svg.append("path")
//         .attr("class", "line")
//         .attr("d", valueline(data));

//     // Add the scatterplot
//     svg.selectAll("dot")
//         .data(data)
//       .enter().append("circle")
//         .attr("r", 3.5)
//         .attr("cx", function(d) { return x(d.date); })
//         .attr("cy", function(d) { return y(d.close); });

//     // Add the X Axis
//     svg.append("g")
//         .attr("class", "x axis")
//         .attr("transform", "translate(0," + height + ")")
//         .call(xAxis);

//     // Add the Y Axis
//     svg.append("g")
//         .attr("class", "y axis")
//         .call(yAxis);

// });