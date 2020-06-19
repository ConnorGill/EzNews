<?php
   $mysqli = new mysqli('rehodb.cagxsdx2k0ey.us-east-2.rds.amazonaws.com','admin','rehoboam');
   $myArray = array();

   $query1="UPDATE rehoboamSchema.rehoboamFull SET RADII = FLOOR(RAND()*(1200-100) + 100) #END";
   $mysqli->query("$query1");

   if ($result = $mysqli->query("SELECT indexKey, radii, source, headline, siteurl, DATE_FORMAT(dateAdded, '%m.%d.%y') as dateAdded FROM rehoboamSchema.vw_rehoboam")) {
   
       while($row = $result->fetch_array(MYSQLI_ASSOC)) {
               $myArray[] = $row;
       }
       
       echo json_encode($myArray);
   }
   
   $result->close();
   $mysqli->close();