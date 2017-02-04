var connection = new ActiveXObject("ADODB.Connection") ;

var connectionstring="Driver={ODBC Driver 13 for SQL Server};Server=tcp:cudevfest2017.database.windows.net,1433;Database=cudevfest2017;Uid=devfest@cudevfest2017;Pwd=!23QweAsdZxc;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;";

connection.Open(connectionstring);
var rs = new ActiveXObject("ADODB.Recordset");

rs.Open("SELECT * FROM dbo.EmotionSection ORDER BY date ASC", connection);
rs.MoveFirst()
while(!rs.eof)
{
   console.log(rs.fields(2));
   rs.movenext();
}

rs.close();
connection.close(); 
