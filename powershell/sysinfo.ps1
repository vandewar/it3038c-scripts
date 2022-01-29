function getIP{
 (Get-NetIPAddress).IPAddress | Select-String "192*"
 }

$IP=getIP