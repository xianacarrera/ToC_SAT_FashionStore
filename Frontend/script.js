var All_clothes = ["Cappello","Maglietta","Completo","Gonna","Calzoni","Scarpe","Sandali","Calzini"];
var All_color = ["Blu","Bianco","Nero","Rosso","Rosa","Verde","Viola"]
var All_Shop = [ './Img/Vuoto.png','./Img/Vuoto.png','./Img/Vuoto.png','./Img/Vuoto.png','./Img/Vuoto.png','./Img/Vuoto.png','./Img/Vuoto.png','./Img/Vuoto.png']
var old_type = undefined


function dress_char(){
    console.log()
    for(let i = 1; i < All_clothes.length; ++i){
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

function openDress(type){

    if(old_type != undefined){
        for (var i = 0; i < All_color.length; i++) {
            doc_tmp = document.getElementById("Img/" + old_type + "_" + All_color[i] + ".png")
            doc_tmp.style.display = "none";
        }
    }

    old_type = type

    for (var i = 0; i < All_color.length; i++) {
        doc_tmp = document.getElementById("Img/" + type + "_" + All_color[i] + ".png")
        doc_tmp.style = "cursor: pointer;padding: 15px";
    }
}


function addCloth(j, i){
    All_Shop[j] = "Img/" + All_clothes[j] + "_" + All_color[i] + ".png";
}



function openDressStart() {
  var clothesDiv = document.getElementById("Clothes");

    for(let j = 0; j < All_clothes.length; ++j){
        type = All_clothes[j]
        for (var i = 0; i < All_color.length; i++) {
            var newDiv = document.createElement("div");
            newDiv.id = "Img/" + type + "_" + All_color[i] + ".png";

           
            newDiv.onclick = (function(j, i) {
                return function() {
                  addCloth(j, i);
                };
              })(j, i);
              
            newDiv.style.display = "none"; // Imposta display: none per il nuovo div
        
            var img = document.createElement("img");
            img.src = "Img/" + type + "_" + All_color[i] + ".png";
            if(j == 0){
                img.style = "margin-top:120px; "
                img.src = "Img/" + type + "_" + All_color[i] + ".png"
            }
            if(j >= 1){
                img.style = "margin-top:20px; "
            }

            if(j >= 3){
                img.style = "margin-top:-30px;"
            }

            if(j >= 5){
                img.style = "margin-top:-70px;"
            }
            if(j == 7){
                img.style = "margin-top:-0px;"
                img.src = "Img/" + type + "_" + All_color[i] + "-trimmy.png"
            }
            // Aggiungi l'immagine al div
            newDiv.appendChild(img);
        
            // Aggiungi il nuovo div all'elemento "Clothes"
            clothesDiv.appendChild(newDiv);
          }
    }

    var clothesDiv = document.getElementById("Clothes");
    clothesDiv.removeChild(clothesDiv.firstChild);
    clothesDiv.removeChild(clothesDiv.firstChild);
}



function openDressStart2() {
    var clothesDiv = document.getElementById("Clothes");
    All_clothes.forEach(function(type, j) {
        All_color.forEach(function(color, i) {
          var newDiv = document.createElement("div");
          newDiv.id = "Img/" + type + "_" + All_color[i] + ".png";

          newDiv.onclick = function() {
            addCloth(j, i);
          };

          newDiv.style.display = "none"; // Imposta display: none per il nuovo div
        
          var img = document.createElement("img");
          img.src = "Img/" + type + "_" + All_color[i] + ".png";
          if(j == 0){
              img.style = "margin-top:120px; "
              img.src = "Img/" + type + "_" + All_color[i] + ".png"
          }
          if(j >= 1){
              img.style = "margin-top:20px; "
          }

          if(j >= 3){
              img.style = "margin-top:-30px;"
          }

          if(j >= 5){
              img.style = "margin-top:-70px;"
          }
          if(j == 7){
              img.style = "margin-top:-0px;"
              img.src = "Img/" + type + "_" + All_color[i] + "-trimmy.png"
          }
          // Aggiungi l'immagine al div
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

function dress_character(){
    for(let i = 0; i < All_Shop.length; ++i){
        img_tmp = document.getElementById((i+1))
        img_tmp.src = All_Shop[i]
    }
}

unloadScrollBars()
openDressStart2()