/**
 * Created with PyCharm.
 * User: Andrey Smirnov
 * Date: 26.10.13
 * Time: 15:07
 */


(function ($, undefined) {
    $.fn.extend({
        create_list: function (list) {
            var res = "";
            for (var i = 0; i < list.length; i++) {
                var audio = list[i]
                res += '<div class="ui360"><a href="'+audio.url+'">'+audio.name+'</a></div>'
            }
            $('#audio_list').html(res)
        }
    })
    }(jQuery))


