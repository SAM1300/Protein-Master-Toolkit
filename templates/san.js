
let bn1 = document.getElementById("btn-1");
let bn2 = document.getElementById("btn-2");
let bn3 = document.getElementById("btn-3");
let bn4 = document.getElementById("btn-4");
let bn5 = document.getElementById("btn-5");
let chk = document.getElementById("check");
let d_1 = document.createElement("div");

//chk.className="jk";
bn1.addEventListener("click", function struct() {
    //let chk = document.getElementById("check");
    //let d_1 = document.createElement("div");
    //let btn = document.createElement("button");
    //chk.className= "jk";
    // if (chk.className === "jk") 

    let det = document.getElementById("bada");
    //let d_1 = document.createElement("div");
    d_1.id = "bada";
    d_1.innerText = "Structure Prediction";
    let arr = ["Alpha Fast", "method-1", "method-2", "method-4", "method"]
    arr.forEach(function (ele, index) {
        let btn = document.createElement("button");
        let di = document.createElement("div");
        //let pa = document.createElement("p");
        //let pr = document.createElement("pre");
        let img = document.createElement("img");
        let ifra = document.createElement("iframe");
        let i = document.getElementById("input");
        //let coll = document.getElementsByClassName('collapsible');
        btn.type = "button";
        btn.className = "collapsible";
        btn.classList.add("anim");
        btn.id = `col-${index}`;
        btn.innerText = `${ele}`;
        di.className = "content";
        ifra.src="https://alphafold.ebi.ac.uk/search/text/succinate%20dehydrogenase%20%5Bubiquinone%5D%20flavoprotein%20subunit"
        ifra.width = "1293px"
       /* fetch("san.txt").then(Response => Response.text()).then(data => {
            pr.textContent = data;
        })*/
       
        img.id = "PM";
        img.src = "PM.png"
        img.width = "700px";

        /*btn.opacity="1";
        btn.style.transition="opacity 5s ease-in-out 2s";*/
        /* btn.style.transition="opacity 5s ease-in-out 2s"
         btn.style.opacity="1";*/
        d_1.appendChild(btn);
        d_1.appendChild(di);
        di.appendChild(ifra);
        di.appendChild(img);

    })
    det.replaceWith(d_1);
    var coll = document.getElementsByClassName("collapsible");
    var i;

    for (i = 0; i < coll.length; i++) {
        coll[i].addEventListener("click", function () {
            this.classList.toggle("active");
            var content = this.nextElementSibling;
            if (content.style.maxHeight) {
                content.style.maxHeight = null;
               
            } else {
                content.style.maxHeight= content.scrollHeight + "px";
             }})
    
    
}}
)
// chk.className = "njk"

/* else {
     d_1.id = "bada";
     d_1.innerText = "Structure Prediction";
     let arr = ["Alpha Fast", "method-1", "method-2", "method-4", "method"]
     arr.forEach(function (ele, index) {
         //let btn= document.createElement("button");
         btn.type = "button";
         btn.className = "collapsible";
         btn.id = "col-1";
         btn.innerText = `${ele}`;
         d_1.appendChild(btn);
     })
 }*/


bn2.addEventListener("click", function str() {
    //let chk = document.getElementById("check");
    //let d_1 = document.createElement("div");
    //let btn = document.createElement("button");
    //chk.className="jk";
    //if (chk.className === "jk") {
    let det = document.getElementById("bada");
    let d_1 = document.createElement("div");
    d_1.id = "bada";
    d_1.innerText = "Structure Prediction";
    let arr = ["Alpha Fast", "method-4", "method-2", "method-4", "method"]
    arr.forEach(function (ele, index) {
        let btn = document.createElement("button");
        btn.type = "button";
        btn.className = "collapsible";
        btn.classList.add("anim");
        btn.id = "col-1";
        btn.innerText = `${ele}`;
        d_1.appendChild(btn);
    })
    det.replaceWith(d_1);

    //else {
    /* d_1.id= "bada";
     d_1.innerText = " Prediction";
     let arr = ["Alpha Fast", "method-3", "method-2", "method-4", "method"]
     arr.forEach(function (ele, index) {
         //let btn= document.createElement("button");
         btn.type= "button";
         btn.className= "collapsible";
         btn.id="col-1";
         btn.innerText = `${ele}`;
         d_1.appendChild(btn);*/

})
   // chk.replaceChild(d_1,d_1)}})


/*let col = document.getElementsByClassName("collapsible");

console.log(typeof (col));
Array.from(col).forEach(function inn(element, index) {
   element.textContent = `Meth-${index}`;
});
});
bn2.addEventListener("click", function call() {
    let col = document.getElementsByClassName("collapsible");

    console.log(typeof (col));
    Array.from(col).forEach(function inn(element, index) {
        element.textContent = `Meth-${index + 1}`;
    });
})*/