

# User information
$FirstName = "Franz"
$LastName = "Ferdinand"
$DisplayName = "$FirstName $LastName"
$Location = "Springfield, OR"
$CompanyName= "GlobeX USA"
$Department = "TPS Department"
$JobTitle = "TPS Reporting Lead"
$EmailAddress = "ferdi@GlobeXpower.com"
$Password = "Password"  # Replace with a strong password

# Create a new user in Active Directory
New-ADUser -Name $DisplayName -GivenName $FirstName -Surname $LastName`
    -Location $Location -CompanyName $CompanyName -Department $Department -JobTitle $JobTitle `
    -EmailAddress $EmailAddress -AccountPassword (ConvertTo-SecureString $Password -AsPlainText -Force) `
    -Enabled $true


