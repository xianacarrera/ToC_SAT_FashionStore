var All_clothes = [];

for (let i = 0; i < 9; i++) {
  All_clothes.push('./Img/Vuoto.png');
}


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
