<table border="1px solid black">
  <tr>
    <th>
      Year
    </th>
    <th>
      Language
    </th>
  </tr>
<?php
$file = fopen("https://en.wikipedia.org/wiki/History_of_programming_languages", "r") or die("unable to open file!");
$text = "";
while(!feof($file)) {
  $text .= fread($file, 9999999);
}
preg_match_all('/<li>(\d{4}) - <a href="[^\>]+>([A-Za-z0-9+ #\/-]+)/', $text, $match);

foreach ($match[2] as $key=>$value){
  echo "<tr>
          <td>
            {$match[1][$key]}
          </td>
          <td>
            {$match[2][$key]}
          </td>
        </tr>";
}
?>
</table>
