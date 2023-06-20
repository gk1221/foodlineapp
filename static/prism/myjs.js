async function f1() {

    var colrol = ['red', 'green'];



    var sd = 'div1';
    var d1 = document.getElementById('div1');
    d1.style.width = '400px';
    await sleep(200);
    d1.style.width = '200px';
    await sleep(200);
    d1.style.width = '800px';
    await sleep(200);
    d1.style.width = '400px';
    await sleep(200);
}

async function tf2() {
    var d1 = document.getElementById('div1');
    f3(100, 900, 80, d1);
    console.log("1");
    await sleep(200);

    f3(900, 30, 90, d1);
    console.log("2");
    await sleep(200);

    f3(30, 700, 80, d1);
    console.log("3");
    await sleep(200);

    f3(700, 200, 80, d1);
    console.log("4");
    await sleep(200);

    f3(200, 600, 5, d1);
    console.log("5");
    await sleep(100);

    var d1 = document.getElementById('div1');
    console.log(d1.offsetWidth);

}


async function tf3(startw, endw, intve, d1) {
    if (startw > endw) {
        for (var i = startw; i > endw; i = i - intve) {
            wid = i + "px";
            d1.style.width = wid;
            d1.style.height = wid;
            console.log("over");
            await sleep(2);
        }
    } else {
        for (var i = startw; i < endw; i = i + intve) {
            wid = i + "px";
            d1.style.width = wid;
            d1.style.height = wid;
            console.log("hhhh");
            await sleep(2);
        }
    }

}


async function f2() {
    var card = document.getElementsByClassName('card');

    for (var i = 0; i < card.length; i++) {
        f3(100, 900, 80, card[i]);
    }

    for (var i = 0; i < card.length; i++) {
        f3(100, 900, 80, card[i]);
    }
    console.log("1");
    await sleep(200);

    for (var i = 0; i < card.length; i++) {
        f3(900, 30, 90, card[i]);
    }
    console.log("2");
    await sleep(200);

    for (var i = 0; i < card.length; i++) {
        f3(30, 700, 90, card[i]);
    }
    console.log("3");
    await sleep(200);

    for (var i = 0; i < card.length; i++) {
        f3(700, 200, 90, card[i]);
    }
    console.log("4");
    await sleep(200);

    for (var i = 0; i < card.length; i++) {
        f3(200, 600, 5, card[i]);
    }
    console.log("5");
    await sleep(100);

    for (var i = 0; i < card.length; i++) {
        card[i].style.width = "auto";
        card[i].style.height = "auto";
    }
    console.log("6");
    await sleep(100);

}


async function f3(startw, endw, intve, d1) {
    if (startw > endw) {
        for (var i = startw; i > endw; i = i - intve) {
            wid = i + "px";
            d1.style.width = wid;
            d1.style.height = wid;
            console.log("over");
            await sleep(2);
        }
    } else {
        for (var i = startw; i < endw; i = i + intve) {
            wid = i + "px";
            d1.style.width = wid;
            d1.style.height = wid;
            console.log("hhhh");
            await sleep(2);
        }
    }

}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

filterSelection("")

function filterSelection(c) {
    var x, i;
    x = document.getElementsByClassName("cardlist");

    console.log(x);
    for (i = 0; i < x.length; i++) {
        RemoveClass(x[i], "cardshow");
        if (x[i].className.indexOf(c) > -1) AddClass(x[i], "cardshow");
    }


}

function AddClass(element, name) {
    var i, arr1, arr2;
    arr1 = element.className.split(" ");
    arr2 = name.split(" ");
    for (i = 0; i < arr2.length; i++) {
        if (arr1.indexOf(arr2[i]) == -1) {
            element.className += " " + arr2[i];
        }
    }
}

function RemoveClass(element, name) {
    var i, arr1, arr2;
    arr1 = element.className.split(" ");
    console.log(arr1);
    arr2 = name.split(" ");
    console.log(arr2);
    for (i = 0; i < arr2.length; i++) {
        while (arr1.indexOf(arr2[i]) > -1) {
            arr1.splice(arr1.indexOf(arr2[i]), 1);
        }
    }
    element.className = arr1.join(" ");
}



$("button").click(function() {
    $("div").animate({
        left: '250px',
        opacity: '0.5',
        height: '150px',
        width: '150px'
    });
});