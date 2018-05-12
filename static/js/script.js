$(document).ready(function () {
    startRequest();
    setInterval("startRequest()", 3000);
});

function startRequest() {
    var n = [];
    $(".numcomment").each(function () {
        n.push($(this).attr('id'));
    });
    n = JSON.stringify(n);

    $.ajax({
        type: 'post',
        async: false,
        url: '/refurbish',
        data: {data: n},
        dataType: 'json',
        success: function (datas) {
            if (datas['Norefurbish'] != '1') {
                var d = $("#insert");
                if (datas['add']) {
                    d.append(datas['add']);
                }
                if (datas['del']) {
                    for (var i = 0; i < datas['del'].length; i++) {
                        $("#n" + datas['del'][i]).remove();
                    }
                }
                var s = $("#number");
                s.html($(".numcomment").length);
            }
        }

    })
}

function sendcommit() {
    $.ajax({
        type: 'post',
        async: false,
        url: '/comment',
        data: {
            author: $('#author').val(),
            mail: $('#mail').val(),
            url: $('#url').val(),
            text: $('#committext').val()
        },
        success: function () {
            startRequest();
            $('#author').val(''),
            $('#mail').val(''),
            $('#url').val(''),
            $('#committext').val('')
        }

    })
}