<? php

try{
    $db = new POD('Sqlite:movies.db');
    


    $db->exec("CREATE TABLE Movies(id INTEGER PRIMARY KEY, Title TEXT, Actor TEXT, Actoress TEXT, Director TEXT, Year_of_release INTEGER)");
    

    $db->exec("INSERT INTO Movies(id,Title, Actor, Actoress, Director, Year_of_release VALUES (1,'','','','',);");
    $db->exec("INSERT INTO Movies(id,Title, Actor, Actoress, Director, Year_of_release VALUES (2,'','','','',);");
    $db->exec("INSERT INTO Movies(id,Title, Actor, Actoress, Director, Year_of_release VALUES (3,'','','','',);");
    $db->exec("INSERT INTO Movies(id,Title, Actor, Actoress, Director, Year_of_release VALUES (4,'','','','',);");
    $db->exec("INSERT INTO Movies(id,Title, Actor, Actoress, Director, Year_of_release VALUES (5,'','','','',);");

    print "<table border=1>";

    print"<tr><td> id </td><td> Title </td><td> Actor </td><td> Actoress </td><td> Director </td><td> Year_of_release </td></tr>";

    $result = $db->query('SELECT * from Movies');

    foreach($reult as $row) {
        print"<tr><td> $row['id']."</td>";
        print"<td> $row['Title']."</td>";
        print"<td> $row['Actor']."</td>";
        print"<td> $row['Actoress']."</td>";
        print"<td> $row['Director']."</td>";
        print"<td> $row['Year_of_release']."</td></tr>";


    }

}catch(PODException $e) {
    echo $e->getMessage();
}

?>