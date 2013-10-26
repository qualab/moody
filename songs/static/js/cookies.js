/**
 * Created with PyCharm.
 * User: noname
 * Date: 26.10.13
 * Time: 17:47
 */

        VK.init({
            apiId: 3956483
        });

        function eraseCookie(name) {
            document.cookie = name + '=; Max-Age=0'
        }


        function setcookie(name, value, expires, path, domain, secure) {
            document.cookie = name + "=" + escape(value) +
                    ((expires) ? "; expires=" + (new Date(expires)) : "") +
                    ((path) ? "; path=" + path : "") +
                    ((domain) ? "; domain=" + domain : "") +
                    ((secure) ? "; secure" : "");
        }



function getcookie(name)
{
    var cookie = " " + document.cookie;
    var search = " " + name + "=";
    var setStr = null;
    var offset = 0;
    var end = 0;

    if (cookie.length > 0)
    {
        offset = cookie.indexOf(search);

        if (offset != -1)
        {
            offset += search.length;
            end = cookie.indexOf(";", offset)

            if (end == -1)
            {
                end = cookie.length;
            }

            setStr = unescape(cookie.substring(offset, end));
        }
    }

    return(setStr);
}