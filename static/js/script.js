$(document).ready(function () {
    startRequest()
    setInterval("startRequest()",3000);
});

function startRequest()
{
    $.ajax({
        type:'post',
        url:'/refurbish',
        // data:{'number':$("#number")},
        data:{},
        dataType:'html',
        success:function (datas) {
            var d = document.getElementById('insert')
            d.innerHTML = datas
        }

    })
}