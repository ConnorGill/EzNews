<?php
   $mysqli = new mysqli('server','user','pass');
   $myArray = array();

   $query1="UPDATE rehoboamSchema.rehoboamFull SET RADII = FLOOR(RAND()*(1200-100) + 100) #END";
   $mysqli->query("$query1");

   $query2="UPDATE rehoboamSchema.rehoboamReal SET RADII = FLOOR(RAND()*((minRadii+500)-(minRadii-500)) + (minRadii-500))";
   $mysqli->query("$query2");

   if ($result = $mysqli->query("SELECT indexKey, radii, source, headline, siteurl, DATE_FORMAT(dateAdded, '%m.%d.%y') as dateAdded, storyAge FROM rehoboamSchema.vw_rehoboam")) {
   
       while($row = $result->fetch_array(MYSQLI_ASSOC)) {
               $myArray[] = $row;
       }
       
       echo json_encode($myArray);
   }
   
   $result->close();
   $mysqli->close();
