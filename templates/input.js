const togg = document.getElementById("togg");
document.getElementById("q1-selectInput").addEventListener("click", function () {
    
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
    text_area.name = "qps";
    text_area.placeholder = "";
    di.appendChild(label);
    di.appendChild(text_area);
    togg.appendChild(di);

});
document.getElementById("q2-selectInput").addEventListener("click", function () {
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
    input.name = "qps";
    input.placeholder = "";
    input.type = "file";
    di.appendChild(label);
    di.appendChild(br);
    di.appendChild(input);
    togg.appendChild(di);

});
document.getElementById("q3-selectInput").addEventListener("click", function () {

    togg.removeChild(document.getElementById("togg-child"));

    let di = document.createElement("div");
    di.id = "togg-child"
    di.innerHTML = `<label for="q33-qps class="form-label"> Query Protein Sequence </label><br>
    <input type="file" id="q33-qps" name="qps"><br><br>
    <label for="q33-qps1" class="form-label">Query Protein Sequence </label><br>
    <textarea class="form-textarea custom-hint-group form-custom-hint form-control"></textarea> `
    togg.appendChild(di);

});
let chk = document.getElementsByClassName("form-check-input");
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
mod = [];
meth = [];
for (let j = 0; j < chk.length; j++) {
    mod.push(`modeller-${j}`)
    meth.push(`structure prediction-${j}`)

}
for (let i = 0; i < chk.length; i++) {
    chk[i].addEventListener("change", function () {

        let di1 = document.getElementById("req");
        let di2 = document.createElement("div");
        let al = document.getElementById("alert")

        if (chk[i].checked) {
            if (chk[i].value=="ITASSER"){
                al.style.height = al.scrollHeight + "px";
                setTimeout(() => {
                    al.style.height = "0px";
                }, 3000);
            }
            di2.id = `req_sub-${i}`;

            di2.innerHTML = `<h2>${meth[i]}</h2>
        <label for="mod" id="lab">${mod[i]}</label>
        <input type="text" id="mod"><br><br>`;
            di1.appendChild(di2);
        }
        else {
            console.log(di1.childNodes)
            di2 = document.getElementById(`req_sub-${i}`);
            di2.remove();
        }
    })

}
