function encode () {
    var enusername = md5($("#inputEmail3").val());
    $("#inputEmail3").val(enusername);
    var enpassword = md5($("#inputPassword3").val());
    $("#inputPassword3").val(enpassword);
};