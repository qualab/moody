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
                res.push( '<table class="song_container" song="' + audio.id + '" owner="' + audio.owner + '"><tr><td> <div title="Отметить подходящей по настроению" class="active-icon favourite "/> </td><td><div class="ui360"><a href="'+audio.url+'">'+audio.name+'</a></div></td><td> <div class="active-icon add-to-my" title="Добавить в мои аудиозаписи"/> </td><td> <div class="active-icon to-friends" title="Рассказать друзьям"/> </td></tr></table>');
            }
            var container = $('#audio_list');
            container.html(res.join(''));
            container.find('.favourite').click(function(){
               if(!$(this).hasClass('active')){
                  $(this).addClass('active');
                  var parent = $(this).closest('.song_container'),
                      mood = $('.mood-icon').attr('mood');
                  httpGet('/rate?song='+ parent.attr("owner") + parent.attr("song") + '&mood=' + mood + '&rating=1');
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
            container.find('.to-friends').click(function(){
               if(!$(this).hasClass('active')){
                  var parent = $(this).closest('.song_container');
                  VK.Api.call('wall.post', {
                     "friends_only": 1,
                     "message": "Эта песня подошла мне под настроение. Найти помогло приложение MoodMusic",
                     "attachments": ["audio", parent.attr("owner"), "_", parent.attr("song"), window.location].join('')
                  }, function (r) {
                  });
                  $(this).hide();
               }
            });
        }
    })
    }(jQuery));


