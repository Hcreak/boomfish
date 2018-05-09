$(document).ready(function () {
    startRequest();
    setInterval("startRequest()",3000);
});

function startRequest()
{
    var n = [];
    $(".numcomment").each(function () {
        n.push($(this).attr('numid'));
    });
    n = JSON.stringify(n);

    $.ajax({
        type:'post',
        async: false,
        url:'/refurbish',
        data:{data:n},
        dataType:'html',
        success:function (datas) {
            if (datas != 'Norefurbish') {
                var d = $("#insert");
                d.append(datas);
                // d.remove(d.filter(data));
                var s = $("#number");
                s.html($(".numcomment").length);
            }
        }

    })
}

// function  sendcommit() {
//     $.ajax({
//         type:'post',
//         url:'/commit',
//
//     })
// }