var PICTURES_NUM = 10;
function addRandomPictures(){
    var $table = $('<table></table>'),
        num = 0;
    $('.right-side').empty().append($table);
    for (var i = 0 ; i < 3 ; i++){
        var $tr = $('<tr></tr>');
        for (var j = 0; j < 3; j++){
            $tr.append('<td class="mood-picture-'+ num +'"></td>');
            num++;
        }
        $table.append($tr);
    }
}