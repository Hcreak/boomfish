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
                var d = document.getElementById('insert');
                d.innerHTML = d.innerHTML + datas;
                var s = document.getElementById('number');
                s.innerText = $(".numcomment").length;
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