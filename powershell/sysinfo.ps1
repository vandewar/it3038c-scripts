function getIP{
 (Get-NetIPAddress).IPAddress | Select-String "192*"
 }

function getUser{
 (Get-LocalUser) | Select-String "Admin*"
 } 

 function getHostName{
 (Get-ComputerInfo).CsDNSHostName
 }

$USER=getUser
$IP=getIP
$HOSTNAME=getHostName
$DATE=Get-Date

$BODY="This machine's IP Address is $IP. The user logged in is $USER. The DNS HostName is $HOSTNAME. Right now, the time is $DATE"

Write-Host $BODY
Send-MailMessage -To "vandewar@mail.uc.edu" -From "alexvan2008@gmail.com" -Subject "IT3038C Windows SysInfo" -Body $BODY -SmtpServer smtp.gmail.com -port 587 -UseSsl -Credential (Get-Credential)