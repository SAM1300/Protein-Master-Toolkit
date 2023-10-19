
let bn1 = document.getElementById("btn-1");
let bn2 = document.getElementById("btn-2");
let bn3 = document.getElementById("btn-3");
let bn4 = document.getElementById("btn-4");
let bn5 = document.getElementById("btn-5");
let ba = document.getElementById("bada")
bn1.addEventListener("click", function struct() {

    let snav = document.getElementById("s-s-nav");
    snav.style.opacity = "1";
    let lis = document.getElementsByClassName("lis");
    

});
let lis = document.getElementsByClassName("lis");

for (let i=0; i<lis.length; i++ ){
    lis[i].addEventListener("click", function(){
        let ifra = document.createElement("iframe");
        ifra.id = "bada"
        ifra.src="https://alphafold.ebi.ac.uk/search/text/succinate%20dehydrogenase%20%5Bubiquinone%5D%20flavoprotein%20subunit";
        
        ba.replaceWith(ifra);
    })
}