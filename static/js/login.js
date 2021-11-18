function sliding() {
    $(".container-fluid").hide().fadeIn(2000);
    $(".navbar-brand").hide().show("slide", { direction: 'left' }, 2000);
    $("input").hide().show("slide", { direction: 'left' }, 3000);
}
var flag = 0;
$(".darkMode-btn").click(function() {

    if (flag == 0) {
        darkMode();
        flag = 1;
    } else {
        defaultMode();
        flag = 0;
    }

});


function darkMode() {
    $("body").css("backgroundColor", "black");
    $("body").css("color", "white");
    $(".container-fluid").css("backgroundColor", "#0b0b0f");
    $(".btn, input").css("color", "white");
    $(".btn").css("backgroundColor", "#0f0f0f");
    $(".input-fields").css("backgroundColor", "rgba(0,0,0,5.142)");
}


function defaultMode() {
    $("body").css("backgroundColor", "whitesmoke");
    $("body").css("color", "black");
    $(".container-fluid").css("backgroundColor", "white");
    $("input").css("color", "black");
    $(".btn:nth-child(odd) , .darkMode-btn").css("backgroundColor", "rgb(11, 90, 165)");
    $(".input-fields").css("backgroundColor", "rgba(245,245,245,5.142)");
}