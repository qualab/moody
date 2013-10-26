var PICTURES_NUM = 10;
function addRandomPictures(){
    var $table = $('<table class="pictures-table hidden-picture"></table>'),
        num = 0;
    $('#popupContact').append($table);
    for (var i = 0 ; i < 3 ; i++){
        var $tr = $('<tr></tr>');
        for (var j = 0; j < 3; j++){
            $tr.append('<td class="mood-picture-'+ num +'"  my-number="' + num +'"></td>');
            num++;
        }
        $table.append($tr);
    }
    $table.find('td').bind('click',function(event){
        $('.button').removeClass().addClass('button ' + $(event.target).attr('class'));
        disablePopup();
      //  console.log($(event.target).attr('my-number'));
        httpGet('/mood/'+ $(event.target).attr('my-number'));
    });
}

function httpGet(theUrl){
    var xmlHttp=null;
    xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET",theUrl,false);
    xmlHttp.send(null);
    return;
}

var popupStatus = 0;

function loadPopup(){
    if(popupStatus==0){
        $('.hidden-picture').toggleClass('hidden-picture');

        $("#backgroundPopup").css({
            "opacity": "0.5"
        });
        $("#backgroundPopup").fadeIn("slow");
        $("#popupContact").fadeIn("slow");
        popupStatus = 1;
    }
}

function disablePopup(){
    $('.hidden-picture').toggleClass('hidden-picture');

    if(popupStatus==1){
        $("#backgroundPopup").fadeOut("slow");
        $("#popupContact").fadeOut("slow");
        popupStatus = 0;
    }
}

function centerPopup(){
    var windowWidth = document.documentElement.clientWidth;
    var windowHeight = document.documentElement.clientHeight;
    var popupHeight = $("#popupContact").height();
    var popupWidth = $("#popupContact").width();
    $("#popupContact").css({
        "position": "absolute",
        "top": windowHeight/2-popupHeight/2,
        "left": windowWidth/2-popupWidth/2
    });
    $("#backgroundPopup").css({
        "height": windowHeight
    });
}

function deleteSong(id)   {
//request
    httpGet('/rate?song='+ id + '&mood=' + mood_id + '&rating=1');
//    debugger;
    document.getElementById(id).remove();
}

function checkSong(id)   {
//request
    //   httpGet('/mood/'+ $(event.target).attr('my-number'));
//    debugger;
//    if (document.getElementById(id).checked());
}

//
//$(document).ready(function(){
//    $("#button").click(function(){
//        debugger;
//        centerPopup();
//        loadPopup();
//    });
//    $("#popupContactClose").click(function(){
//        disablePopup();
//    });
//    $("#backgroundPopup").click(function(){
//        disablePopup();
//    });
//    $(document).keypress(function(e){
//        if(e.keyCode==27 && popupStatus==1){
//            disablePopup();
//        }
//    });
//});