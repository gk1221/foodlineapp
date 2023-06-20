$(".main").css("visibility", "hidden");
$(document).ready(function () {

    var div1 = $(".main");
    var div2 = $("#loadon");




    div1.css("visibility", "visible").hide().fadeIn(1200);
    console.log("OK1");


    $(".test-ani").click(function () {

        var div = $("#div2");
        div.css({
            "border-radius": "5px",
        });
        div.animate({ height: '600px', width: '600px', opacity: '0.4' }, "fast");
        div.animate({ height: '100px', width: '100px', opacity: '0.4' }, "fast");

        div.animate({ height: '500px', width: '500px', opacity: '0.4' }, "slow");
        div.animate({ height: '200px', width: '200px', opacity: '0.4' }, "slow");

    });

    $("#btnfood").click(function () {


        var st = '/output/?area=' + $("#area-form").attr("value") +
            "&catagory=" + $("#catagory-form").attr("value");
        $("body").load(st);



    });

    $(".text-filt-but").click(function () {
        let id_name = $(this).attr("id");
        /* Money-card*/



    });



    $("#op1").click(function () {


        var div = $(".all-card");
        var div2 = $(".all-card2");



        div.css({
            "display": "none",
        });
        div2.fadeIn(800);


    });

    $("#op2").click(function () {


        var div = $(".all-card");
        var div2 = $(".all-card2");


        div2.css({
            "display": "none",
        });
        div.fadeIn(800);


    });


});
