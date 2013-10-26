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
                res += '<table><tr><td>fdssdfadsfa</td><td><div class="ui360"><a href="'+audio.url+'">'+audio.name+'</a></div></td><td>dfadsfasfd</td></tr></table>'
            }
            $('#audio_list').html(res)
        }
    })
    }(jQuery))


