var All_clothes = ["Cappello", "Maglietta", "Completo", "Gonna", "Calzoni", "Scarpe", "Sandali", "Calzini"];
var All_color = ["Blu", "Bianco", "Nero", "Rosso", "Rosa", "Verde", "Viola"]
var All_Shop = ['./Img/Vuoto.png', './Img/Vuoto.png', './Img/Vuoto.png', './Img/Vuoto.png', './Img/Vuoto.png', './Img/Vuoto.png', './Img/Vuoto.png', './Img/Vuoto.png']
var old_type = undefined
var open_shop = false

var DummyTranslator = {
    "Cappello": "hat",
    "Maglietta": "tshirt",
    "Completo": "dress",
    "Gonna": "skirt",
    "Calzoni": "pants",
    "Scarpe": "shoes",
    "Sandali": "sandals",
    "Calzini": "socks",
    "Blu": "blue",
    "Bianco": "white",
    "Nero": "black",
    "Rosso": "red",
    "Rosa": "pink",
    "Verde": "green",
    "Viola": "purple"
};


function dress_char() {
    for (let i = 1; i < All_clothes.length; ++i) {
        let el_tmp = document.getElementById(i)
        el_tmp.src = All_clothes[i]
    }
}

function myFunction(obj) {
    // example: let obj = [7, './Img/Scarpe_Rosa.png']
    All_clothes[obj[0]] = obj[1]
    console.log(All_clothes)
    dress_char()
}

function openDress(type) {
    if (open_shop) {
        close_ssop()
        open_shop = false
    }

    if (old_type != undefined) {
        for (var i = 0; i < All_color.length; i++) {
            doc_tmp = document.getElementById("Img/" + old_type + "_" + All_color[i] + ".png")
            doc_tmp.style.display = "none";
        }
    }

    old_type = type

    if("Calzini" == type || "Sandali" == type  || "Scarpe" == type ){
        tmp_div = document.getElementById("Clothes")
        tmp_div.className = "mt-4 grid grid-cols-3 gap-5"
    }else{
        tmp_div = document.getElementById("Clothes")
        tmp_div.className = "mt-4 grid grid-cols-4 gap-5"
    }

    for (var i = 0; i < All_color.length; i++) {
        doc_tmp = document.getElementById("Img/" + type + "_" + All_color[i] + ".png")
        doc_tmp.style = "cursor: pointer;padding: 15px ;";
        doc_tmp.className = "fade-in"
    }
}


function addCloth(j, i) {
    All_Shop[j] = "Img/" + All_clothes[j] + "_" + All_color[i] + ".png";
}






function openDressStart2() {
    var clothesDiv = document.getElementById("Clothes");
    All_clothes.forEach(function (type, j) {
        All_color.forEach(function (color, i) {
            var newDiv = document.createElement("div");
            newDiv.id = "Img/" + type + "_" + All_color[i] + ".png";

            newDiv.onclick = function () {
                addCloth(j, i);
            };

            newDiv.style.display = "none"; // Imposta display: none per il nuovo div

            var img = document.createElement("img");
            img.src = "Img/" + type + "_" + All_color[i] + "-trimmy.png";
            

            img.className = "trasparente-al-hover"
            newDiv.appendChild(img);

            // Aggiungi il nuovo div all'elemento "Clothes"
            clothesDiv.appendChild(newDiv);

        });
    });
    var clothesDiv = document.getElementById("Clothes");
    clothesDiv.removeChild(clothesDiv.firstChild);
    clothesDiv.removeChild(clothesDiv.firstChild);
}

function unloadScrollBars() {
    document.documentElement.style.overflow = 'hidden';  // firefox, chrome
    document.body.scroll = "no"; // ie only
}

function dress_character() {
    for (let i = 0; i < All_Shop.length; ++i) {
        img_tmp = document.getElementById((i + 1))
        img_tmp.src = All_Shop[i]
    }
}

function shop() {
    if (open_shop) {
        close_ssop()
        open_shop = false
    } else {
        shop_show()
        open_shop = true
    }
}

function addTrimmy(str) {
    const parts = str.split(".");
    const fileName = parts[0];
    const extension = parts[1];
    const newFileName = `${fileName}-trimmy.${extension}`;
    return newFileName;
}

function shop_show() {
    if (old_type != undefined) {
        for (var i = 0; i < All_color.length; i++) {
            doc_tmp = document.getElementById("Img/" + old_type + "_" + All_color[i] + ".png")
            doc_tmp.style.display = "none";
        }
    }

    tmp_div = document.getElementById("Clothes")
    tmp_div.className = "mt-4 grid grid-cols-4 gap-5"

    old_type = undefined;
    var clothesDiv = document.getElementById("Clothes");
    for (let i = 0; i < All_Shop.length; ++i) {
        if (All_Shop[i] === './Img/Vuoto.png') {
            continue;
        } else {
            var newDiv = document.createElement("div");
            newDiv.style.position = "relative";
            newDiv.style.display = "inline-block"; // Per mantenere le dimensioni del div basate sul contenuto

            newDiv.id = "SHOP_" + All_Shop[i];

            var img = document.createElement("img");
            img.src = All_Shop[i] === './Img/Vuoto.png' ? './Img/Vuoto.png' : addTrimmy(All_Shop[i]);
            newDiv.appendChild(img);
            var svgSpan = document.createElement("span");
            if ('./Img/Vuoto.png' !== All_Shop[i]) {
                svgSpan.innerHTML = '<svg style="color: rgb(221, 170, 152); position: absolute; top: 0; right: 0;" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-x-circle-fill" viewBox="0 0 16 16"> <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM5.354 4.646a.5.5 0 1 0-.708.708L7.293 8l-2.647 2.646a.5.5 0 0 0 .708.708L8 8.707l2.646 2.647a.5.5 0 0 0 .708-.708L8.707 8l2.647-2.646a.5.5 0 0 0-.708-.708L8 7.293 5.354 4.646z" fill="#ddaa98"></path> </svg>';
                svgSpan.style = "cursor: pointer;"
                svgSpan.addEventListener("click", (function (index, image, svg_a, div_parent) {
                    return function () {
                        All_Shop[i] = './Img/Vuoto.png';
                        image.src = './Img/Vuoto.png';
                        svg_a.remove();
                        div_parent.id = "SHOP_" + All_Shop[i];
                        var elementToRemove = document.getElementById("SHOP_" + All_Shop[i]);
                        elementToRemove.parentNode.removeChild(elementToRemove);
                    };
                })(i, img, svgSpan, newDiv));

                newDiv.appendChild(svgSpan);
            }

            clothesDiv.appendChild(newDiv);
        }
    }
}



function close_ssop() {
    for (let i = 0; i < All_Shop.length; ++i) {
        if (All_Shop[i] === './Img/Vuoto.png') {
            continue;
        } else {
            var elementToRemove = document.getElementById("SHOP_" + All_Shop[i]);
            elementToRemove.parentNode.removeChild(elementToRemove);
        }
    }
}

function remove_shop() {

    if (open_shop) {
        close_ssop()
        open_shop = false
    }

    for (let i = 0; i < All_Shop.length; ++i) {
        All_Shop[i] = './Img/Vuoto.png';
    }
    dress_character()
}



function parseImageString(imageString) {
    if (imageString === './Img/Vuoto.png') {
        return false
    }
    var startIndex = imageString.lastIndexOf("/") + 1;
    var endIndex = imageString.lastIndexOf(".");
    var substring = imageString.substring(startIndex, endIndex);
    var parts = substring.split("_");

    return DummyTranslator[parts[0]] + ", " + DummyTranslator[parts[1]] + "\n";

}


function gettxtContent() {
    res = ""
    for (let i = 0; i < All_Shop.length; ++i) {
        let tmp_str = parseImageString(All_Shop[i]);
        if (tmp_str) {
            res += tmp_str;
        }
    }
    return res.slice(0, -1);
}

function writeTxt() {
    content = gettxtContent()
    const url = 'http://localhost:3000/writefile';

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ content: content })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('BO broken something and no write ');
        }
        return response.text();  // Aggiungi questa riga
    })
    .then(data => {
        console.log(data);  // Modifica questa riga per loggare i dati
        msg = JSON.parse(data)
        console.log(msg.message)
        console.log('Write File Stonks');
    })
    .catch(error => {
        console.error(error);
    });
}


unloadScrollBars()
openDressStart2()