/**
 * Created with PyCharm.
 * User: Andrey Smirnov
 * Date: 26.10.13
 * Time: 15:07
 */


(function ($, undefined) {
    $.fn.extend({
        create_list: function (list) {
            var res = [];
            for (var i = 0; i < list.length; i++) {
                var audio = list[i];
               console.log(audio);
                res.push( '<table><tr><td> <div class="favourite " id="' + audio.aid + '" owner="' + audio.owner_id + '" /> </td><td><div class="ui360"><a href="'+audio.url+'">'+audio.name+'</a></div></td><td> <input class="remove_button_style" type="image" src="/images/ic_action_remove.png" onclick="deleteSong(audio.url)"> </td></tr></table>');
            }
            var container = $('#audio_list');
            container.html(res.join(''));
            container.find('.favourite').click(function(){
               if(!$(this).hasClass('star-active')){
                  $(this).addClass('star-active');
            //request
                //   httpGet('/mood/'+ $(event.target).attr('my-number'));
               }
            });
        }
    })
    }(jQuery));


