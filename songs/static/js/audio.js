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
                res.push( '<table class="song_container" song="' + audio.id + '" owner="' + audio.owner + '"><tr><td> <div class="active-icon favourite "/> </td><td><div class="ui360"><a href="'+audio.url+'">'+audio.name+'</a></div></td><td> <div class="active-icon add-to-my"/> </td></tr></table>');
            }
            var container = $('#audio_list');
            container.html(res.join(''));
            container.find('.favourite').click(function(){
               if(!$(this).hasClass('active')){
                  $(this).addClass('active');
            //request
                //   httpGet('/mood/'+ $(event.target).attr('my-number'));
               }
            });
            container.find('.add-to-my').click(function(){
               if(!$(this).hasClass('active')){
                  $(this).addClass('active');
                  var parent = $(this).closest('.song_container');
                  VK.Api.call('audio.add', {
                     "audio_id": parent.attr("song"),
                     "owner_id": parent.attr("owner")
                  }, function (r) {
                  });
               }
            });
        }
    })
    }(jQuery));


