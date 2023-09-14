#!/usr/bin/env python3
# Script:                       Op Challenge 14
# Author:                       Jermain 
# Date of latest revision:      09/14/2023
# Purpose:       Making a new user on AD


#User Information
$firstname= "Franz"
$Lastname= "ferdinand"
$Displayname= "$Firstname $Lastname"
$Location= "Spronfield, OR"
$CompanyName= "Globex USA"
$Department= "TPS Department"
$Jobtitle= "TPS Reporting Lead"
$EmailAddress= "ferdi@globeXpower.com"
$Password= "Password"

#Create a new user in Active Directory
New ADUser -Name $Displayname -GivenName $FirstName -Surname $Lastname 
    -Location $Location -CompanyName $CompanyName -Department $Department
    -EmailAddress $EmailAddress -AccountPassword (convertTo-SecureString)
    -Enabled $true