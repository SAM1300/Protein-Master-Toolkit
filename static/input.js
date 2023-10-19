let chk = document.getElementsByClassName("form-check-input");
let sub = document.getElementById("submit");
//const inputs = [];
function ajax(){
console.log(document.getElementById("q30-jobname").value);
/*for(let i=0 ; i<chk.length; i++){
if (chk[i].checked === true) {
inputs.push(chk[i].value);
}
}*/
if (document.getElementById("q30-jobname").value != '' || null && document.getElementById("q31-email").value != '' || null && document.getElementById("q32-qpn").value != '' || null && chk.length > 1){
console.log("Start Ajax");

console.log("SANKET");
const xhr = new XMLHttpRequest();
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');
 xhr.open("POST","/results/",true);
 xhr.setRequestHeader('X-CSRFToken',csrftoken);
 xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
 xhr.onprogress = function(){

 document.head.innerHTML = `
 <style>
 body {
	margin: 0;
	height: 100vh;
	width: 100vw;
	display: flex;
	align-items: center;
	justify-content: center;
	background-image: linear-gradient(to bottom, rgb(230,230,250,1),rgb(230,230,250,0.2));
}

.loader {
    width: 20em;
    height: 20em;
    font-size: 10px;
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
}

.loader .face {
    position: absolute;
    border-radius: 50%;
    border-style: solid;
    animation: animate 3s linear infinite;
}
.loader .face:nth-child(1) {
    width: 100%;
    height: 100%;
    color: rgb(0,0,430);
    border-color: currentColor transparent transparent currentColor;
    border-width: 0.2em 0.2em 0em 0em;
    --deg: -45deg;
    animation-direction: normal;
}



.loader .face:nth-child(2) {
    width: 70%;
    height: 70%;
    color: rgb(0,0,205);
    border-color: currentColor currentColor transparent transparent;
    border-width: 0.2em 0em 0em 0.2em;
    --deg: -135deg;
    animation-direction: reverse;
}

.loader .face .circle {
    position: absolute;
    width: 50%;
    height: 0.1em;
    top: 50%;
    left: 50%;
    background-color: transparent;
    transform: rotate(var(--deg));
    transform-origin: left;
}

.loader .face .circle::before {
    position: absolute;
    top: -0.5em;
    right: -0.5em;
    content: '';
    width: 1em;
    height: 1em;
    background-color: currentColor;
    border-radius: 50%;
    box-shadow: 0 0 2em,
                0 0 4em,
                0 0 6em,
                0 0 8em,
                0 0 10em,
                0 0 0 0.5em rgba(255, 255, 0, 0.1);
}

@keyframes animate {
    to {
        transform: rotate(1turn);
    }
}
p {
  position:relative;
  left:-8rem;
  color: black;
  font-size:21px;
}
#load{
  position:relative;
  top: 8rem;
  left: -19rem;

}

</style>`
document.body.innerHTML = `<div class="loader">
  <div class="face">
    <div class="circle"> </div>
  </div>
  <div class="face">
    <div class="circle"> </div>
  </div>
</div>
<p>Loading</p>
<p  id="load"> Please wait your results are getting ready...</p>`

 }
 /*function(){
    let ani = document.createElement("div");
    ani.className = "ring";
    ani.innerHTML = `Loading
    <span id="spa"></span>`
    document.body.appendChild(ani);
    document.body.style = `margin:0;
    padding:0;
    background:#262626;
    z-index: 4;`
 };*/
 xhr.onload = function(){

    if(this.status===200){
    console.log("good");
    }
    else{
    console.log("erroe ocuured");
    }
 }
 xhr.send();
}};
const form_sub = document.getElementById("form_sub");
form_sub.addEventListener("submit", function(e){
e.preventDefault();
//e.stopImmediatePropagation();
//sub.disabled = true;
ajax();
return false;
});
const togg = document.getElementById("togg");
document.getElementById("q1-selectInput").addEventListener("click",function(){
    console.log(togg.childNodes)
    togg.removeChild(document.getElementById("togg-child"));
    
    let di = document.createElement("div");
    di.id = "togg-child";
    let label = document.createElement("label");
    label.for = "q33-qps";
    label.className = "form-label";
    label.innerHTML = "Query Protein Sequence <br>";
    let text_area = document.createElement("textarea");
    text_area.className = "form-textarea custom-hint-group form-custom-hint form-control";
    text_area.id = "q33-qps";
    text_area.name = "qps-text";
    text_area.placeholder = "";
    text_area.required= true;
    di.appendChild(label);
    di.appendChild(text_area);
    togg.appendChild(di);

});
document.getElementById("q2-selectInput").addEventListener("click", function () {
    console.log(togg.childNodes)
    togg.removeChild(document.getElementById("togg-child"));
    
    let di = document.createElement("div");
    let br = document.createElement("br")
    di.id = "togg-child";
    let label = document.createElement("label");
    label.for = "q33-qps";
    label.className = "form-label";
    label.textContent = "Query Protein Sequence";
    let input = document.createElement("input");
    input.id = "q33-qps";
    input.name = "qps-file";
    input.placeholder = "";
    input.type="file";
    di.appendChild(label);
    di.appendChild(br);
    di.appendChild(input);
    togg.appendChild(di);

});
document.getElementById("q3-selectInput").addEventListener("click", function () {
    console.log(togg.childNodes)
    togg.removeChild(document.getElementById("togg-child"));
    
    let di = document.createElement("div");
    di.id="togg-child"
    di.innerHTML = `<label for="q33-qps class="form-label"> Query Protein Sequence </label><br>
    <input type="file" id="q33-qps" name="qps-file"><br><br>
    <label for="q33-qps1" class="form-label">Query Protein Sequence </label><br>
    <textarea class="form-textarea custom-hint-group form-custom-hint form-control" required></textarea> `
    togg.appendChild(di); 

});
function validateForm() {
  var x = document.forms["myForm"]["fname"].value;
  if (x == "") {
    console.log("Name must be filled out");

  }
}

/*chk.forEach((element,index) => {
    mod=[];
    meth=[];
    for(let i=0; i<chk.length; i++){
        mod.push(`modeller-${i}`)
        meth.push(`structure prediction-${i}`)
    }

    element.addEventListener("click", function(){
        let di1 = document.getElementById("req");
        let di2 = document.createElement("div");
        di2.id = "req_sub";
        di2.innerHTML=`<h2>${meth[index]}</h2>
        <label for="mod" id="lab">${mod[index]}</label>
        <input type="text" id="mod">`;
        di1.appendChild(di2);

    })
});*/
mod = ["Modeller key","Modeller Key"];
meth = ["AlphaFold", "Consurf Sever"];
const sanity = [];
const Protein_chain =[];
const Mut_lis = [];
for (let j = 2; j < chk.length; j++) {
    mod.push(`modeller-${j}`)
    meth.push(`structure prediction-${j}`)

}
let al = document.getElementById("alert");
for (let i = 0; i < chk.length; i++) {
if (i === 33|| i===5 || i===21 || i===38 || i===23 || i===22 || i===36 ){
    chk[i].addEventListener("change", function () {

        let di1 = document.getElementById("req");
        let di2 = document.createElement("div");
        di2.id = `req_sub-${i}`;
        var myele = chk[i].id;

       if(chk[i].checked){
             if (chk[i].value=="ITASSER"){
                al.style.height = al.scrollHeight + "px";
                setTimeout(() => {
                    al.style.height = "0px";
                }, 3000);
            }
            if(chk[i].value == "CrystalP2"){
                al.style.height = al.scrollHeight + "px";
                setTimeout(() => {
                    al.style.height = "0px";
                }, 3000);
            }
            if(chk[i].value == "eFseek"){
                al.style.height = al.scrollHeight + "px";
                setTimeout(() => {
                    al.style.height = "0px";
                }, 3000);
            }
            if(chk[i].value == "serp"){
                al.style.height = al.scrollHeight + "px";
                setTimeout(() => {
                    al.style.height = "0px";
                }, 3000);
            }

           if(chk[i].value == "xtal_pred"){
                al.style.height = al.scrollHeight + "px";
                setTimeout(() => {
                    al.style.height = "0px";
                }, 3000);
           }

            
           // di2.id = `req_sub-${i}`;
            if(di2.id === "req_sub-33" || di2.id === "req_sub-36"){
            di2.innerHTML = `
        <label for="mod" id="lab">Mutation text</label>
        <input type="text" id="mod" name="Mutation Text"><br><br>`;
            di1.appendChild(di2);
       }

         /*  if(di2.id === "req_sub-36"){
           di2.innerHTML = `<h2>Dynamut-Multimutation</h2>
        <label for="mod" id="lab">Mutation File</label>
        <input type="file" id="mod" name="Mutation File"><br><br>`;
            di1.appendChild(di2);
           }*/

          /*if(di2.id==="req_sub-7" || di2.id==="req_sub-8" || di2.id ==="req_sub-9" || di2.id ==="req_sub-10" || di2.id ==="req_sub-11" || di2.id ==="req_sub-12"){
          if(sanity.length===0){
          di2.innerHTML = `<h2>Muscle</h2>
        <label for="mod" id="lab">Multiple Sequence File</label>
        <input type="file" id="mod"><br><br>`;
            di1.appendChild(di2);
            sanity.push("1");
          }
          }*/

       }
        else {
            console.log(di1.childNodes)
            let di2 = document.getElementById(`req_sub-${i}`);
            di2.remove();

        }})}
    if(i=>8 && i<=13){
    chk[i].addEventListener("change",function(){
    let di1 = document.getElementById("req");
    let di2 = document.createElement("div");
    di2.id = `req_sub-${i}`;
    if(chk[8].checked === true || chk[9].checked=== true || chk[10].checked === true || chk[11].checked === true || chk[12].checked === true || chk[13].checked === true){
          if(sanity.length===0){
          di2.innerHTML = `<label for="mod" id="lab"><h2>Multiple Sequence File</h2></label>
        <input type="file" id="mod" name="MSF"><br><br>`;
            di1.appendChild(di2);
            sanity.push("1");
          }
          }
    if(chk[8].checked === false && chk[9].checked === false && chk[10].checked === false && chk[11].checked === false && chk[12].checked === false && chk[13].checked === false){
       console.log("entered second loop");
       for(let j=8 ; j<14; j++){
       if(!!document.getElementById(`req_sub-${j}`)){
       console.log("Sanket kuch kar");
       let di2 = document.getElementById(`req_sub-${j}`);
       di2.remove();
       sanity.length = 0;
       }}}})}
    if(i=== 34 || i === 0 || i === 25 || i===33 || i=== 31 || i===36){
    chk[i].addEventListener("change",function(){
    let di1 = document.getElementById("req");
    let di2 = document.createElement("div");
    di2.id = `req_sub-${i}`;

    if(chk[i].checked === true){

    if(chk[i].value == "Consurf_Structure"){
                al.style.height = al.scrollHeight + "px";
                setTimeout(() => {
                    al.style.height = "0px";
                }, 3000);
           }

        if(Protein_chain.length === 0){
        di2.innerHTML = `<label for="mod" id="lab"><h2>Protein Chain</h2></label>
        <input type="text" id="mod" name="Protein Chain"><br><br>`;
            di1.appendChild(di2);
            Protein_chain.push("1");
        }
    }
    if (chk[34].checked === false && chk[0].checked === false && chk[25].checked === false && chk[33].checked === false && chk[31].checked === false && chk[36].checked === false){
       console.log("entered second loop");
       for(let j=0 ; j<chk.length; j++){
       if(j === 34 || j === 0 || j===25 || j===33 || j===31 || j===36){
       if(!!document.getElementById(`req_sub-${j}`)){
       console.log("Sanket kuch kar");
       let di2 = document.getElementById(`req_sub-${j}`);
       di2.remove();
       Protein_chain.length = 0;
    }}}
    }})}
    if(i===34 || i===31 || i===32){
    console.log("Sanket bhadwe sirf ek mahina bacha hai, Chutiya");
    chk[i].addEventListener("change",function(){
    let di1 = document.getElementById("req");
    let di2 = document.createElement("div");
    di2.id = `req_sub_mut-${i}`;
     if(chk[i].checked === true){
        if(Mut_lis.length === 0){
        di2.innerHTML = `<label for="mod" id="lab"><h2>Mutation List</h2></label>
        <input type="file" id="mod" name="Mutation List"><br><br>`;
            di1.appendChild(di2);
            Mut_lis.push("1");
        }
    }
     if (chk[34].checked === false && chk[31].checked === false  && chk[32].checked === false){
       console.log("entered second loop");
       for(let j=0 ; j<chk.length; j++){
       if(j === 34 || j===31 || j===32){
       if(!!document.getElementById(`req_sub_mut-${j}`)){
       let di2 = document.getElementById(`req_sub_mut-${j}`);
       di2.remove();
       Mut_lis.length = 0;}
    }}}
    })
    }
    if(i===37){
    chk[i].addEventListener("change",function(){
    let di1 = document.getElementById("req");
    let di2 = document.createElement("div");
    di2.id = `req_sub_NMS`;
    if(chk[i].checked === true){
        di2.innerHTML = `<label for="mod" id="lab"><h2>Forcefields</h2></label>
        <input type="text" id="mod" name="Forcefields"><br><br>`;
        di1.appendChild(di2);
    }
    if(chk[i].checked === false){
     if(!!document.getElementById(`req_sub_NMS`)){
       let di2 = document.getElementById(`req_sub_NMS`);
       di2.remove();
    }
    }})}

    if(i===6){
    chk[i].addEventListener("change",function(){
    let di1 = document.getElementById("req");
    let di2 = document.createElement("div");
    di2.id = `req_sub_ff`;
    if(chk[i].checked === true){
        di2.innerHTML = `<label for="mod" id="lab"><h2>Modeller License Key</h2></label>
        <input type="text" id="mod" name="MLK"><br><br>`;
        di1.appendChild(di2);
    }
    if(chk[i].checked === false){
    if(!!document.getElementById(`req_sub_ff`)){
       let di2 = document.getElementById(`req_sub_ff`);
       di2.remove();
    }
    }})
    }}





var tt = document.getElementsByClassName("fa-solid fa-circle-question");
for (let i = 0 ; i<tt.length; i++){
tt[i].addEventListener("mouseover", function(){
 let t_t = document.getElementsByClassName("tooltiptext");
 t_t[i].style.visibility = "visible";
})}
for (let j = 0 ; j<tt.length; j++){
tt[j].addEventListener("mouseout",function(){
 let t_t = document.getElementsByClassName("tooltiptext")
 t_t[j].style.visibility = "hidden";
 })}
const redir = document.getElementsByClassName("redirect");
for(let i=0 ; i<redir.length; i++){
redir[i].addEventListener("click",function(){
if(i==1){
    window.location.href="/Contacts";
}
if(i==3){
    window.location.href = "/About";
}
if(i==0){
window.location.href = "/";
}})
};

