<html>
<head>
    <title>SQL SELECT Statement</title>
</head>
<body>
<table align="center" border="1">
<tr>
<th><a href="?sort=exhange">Exchange</a></th>
<th><a href="?sort=symbol">Symbol</a></th>
<th><a href="?sort=company">Company</a></th>
<th><a href="?sort=volume">Volume</a></th>
<th><a href="?sort=price">Price</a></th>
<th><a href="?sort=change">Change</a></th>
<th><a href="?sort=id">ID</a></th>
</tr>
<?php
    $cnx = new mysqli('localhost', 'root', 'Divastar1998', 'demo');

    if ($cnx->connect_error)
        die('Connection failed: ' . $cnx->connect_error);
    /*Code modified from stack overflow*/
    $query = 'SELECT * FROM stocks';

    if (!isset($_GET['sort']))
    {
    } 
    elseif ($_GET['sort'] == 'exchange')
    {
        $query .= " ORDER BY exchange";
    }
    elseif ($_GET['sort'] == 'symbol')
    {
        $query .= " ORDER BY symbol";
    }
    elseif ($_GET['sort'] == 'company')
    {
        $query .= " ORDER BY company";
    }
    elseif($_GET['sort'] == 'volume')
    {
        $query .= " ORDER BY volume";
    }
    elseif($_GET['sort'] == 'price')
    {
        $query .= " ORDER BY price";
    }
    elseif($_GET['sort'] == 'change')
    {
        $query .= " ORDER BY changee"; /*used changee as change is a reserved word in sql*/
    }
    elseif($_GET['sort'] == 'id')
    {
        $query .= " ORDER BY idsym";
    }
    $cursor = $cnx->query($query);
    while ($row = $cursor->fetch_assoc()) {
        echo '<tr>';
        echo '<td>' . $row['exchange'] . '</td><td>' . $row['symbol'] . '</td><td>' . $row['company'] .'</td><td>'. $row['volume'] .'</td><td>'. $row['price'] .'</td><td>'. $row['changee'] .'</td><td>'. $row['idsym'] .'</td>';
        echo '</tr>';
    }

    $cnx->close();
?>
</table>
</body>
</html>