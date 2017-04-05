<!DOCTYPE html>
<html>
<head>

</head>
<body>
   <?php

    $str = "Saya ingin ke pasar. Untuk membeli ke pasar";
     echo"<strong>Berdasarkan titik</strong>";
     echo"<br>";
       $a = (explode(".",$str));

    for($i=0;$i<count($a);$i++){
       echo "kalimat $i: ".$a[$i]."<br>";
    }

    echo"<strong>Berdasarkan enter</strong>";
    echo"<br>";
    $b = (explode(PHP_EOL, $str));
    for($j=0;$j<count($b);$j++){
       echo "kalimat $j: ".$b[$j]."<br>";
    }

 






?> 
</body>

</html>

