<?php
   $mysqli = new mysqli('database-1.cluster-ro-cagxsdx2k0ey.us-east-2.rds.amazonaws.com','admin','rehoboam');
   $myArray = array();

   $query1="UPDATE rehoboamSchema.rehoboamFull SET RADII = FLOOR(RAND()*(1000-100) + 100) #END";
   $mysqli->query("$query1");

   if ($result = $mysqli->query("SELECT indexKey, radii FROM rehoboamSchema.vw_rehoboam LIMIT 300")) {
   
       while($row = $result->fetch_array(MYSQLI_ASSOC)) {
               $myArray[] = $row;
       }
       
       echo json_encode($myArray);
   }
   
   $result->close();
   $mysqli->close();