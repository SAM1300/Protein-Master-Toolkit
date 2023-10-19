const job_name = jobname
const email_n = email
const Q_P_n = Q_P
const Q_P_S_n = Q_P_S
const ip = inputs_j
//let ba = document.getElementById("bada");
let bts = document.getElementsByClassName("btns");
let lis = document.getElementsByClassName("lis");
let user_input = ["AlphaFold", "interpro", "CoeViz2", "reactome", "swiss",
                      "PDBflex", "TrRosseta", "SAS", "IntFold", "DeepGO", "Modweb", "Consurf_Structure",
                      "Iupred3", "LigandSite", "FunFold2", "Expresso", "nFOLD3", "ModFOLD", "Kalign", "CrystalP2", "Muscle",
                      "xtal_pred", "ITASSER", "flDPnnS", "flDPnnM", "serp", "mTMalign", "CUPSAT", "P2RANK", "iCn3D", "ProteinContactAtlas", "PLIP","SDM", "Dynamut_NMS", "Modeller", "Dynamut_Smutaion", "Dynamut_Mmutaion", "Deeprefiner", "Quickgo", "PDBeFold", "PDBsum", "Profun", "Probis", "MAFFT","Mcofee", "SuMo", "eFseek"]

/*bts[j].addEventListener("click", function struct() {

    let snav = document.getElementsByClassName("s-s-nav");
    for(let p=0; p<snav.length; p++){
      if(p!==j){
      snav[p].style.display = "none"}

    else{
    snav[j].style.display = "flex";
    snav[p].style.transition = "all 0.5s ease-in-out";
    snav[j].style.opacity = "1";

    }}});*/

    /*let links = [];
    {% for i in url_1 %}
    url_new = String({{i}});
    links.push(url_new);
    {% endfor %}*/
    console.log(links);
    //links = ["https://alphafold.ebi.ac.uk/search/text/succinate%20dehydrogenase%20%5Bubiquinone%5D%20flavoprotein%20subunit","https://www.ebi.ac.uk/interpro/result/InterProScan/#table","https://research.cchmc.org/CoevLab/cgi-bin/coevlab.cgi?ID=d14fd24be4ded15","https://reactome.org/content/query?q=succinate+dehydrogenase+%5Bubiquinone%5D+flavoprotein+subunit&species=Homo+sapiens&species=Entries+without+species&cluster=true","https://pdbflex.org/cluster.html#!/1yq4A/5393/1yq4A","https://yanglab.nankai.edu.cn/cgi-bin/rosetta.cgi","https://consurf.tau.ac.il/ConSurf_Or_ConSeq.php","https://iupred3.elte.hu/plot","http://www.reading.ac.uk/bioinf/servlets/nFOLD/IntFOLD4confirm.jsp?REPLY-E-MAIL=NoEmail&TARGET-","https://www.reading.ac.uk/bioinf/servlets/nFOLD/IntFOLD6confirm.jsp?REPLY-E-MAIL=user@addresshasjobrunning&TARGET-NAME=Riya-","https://msa.sbc.su.se/cgi-bin/msa.cgi"]
    for (let i=0; i<lis.length; i++ ){
    lis[i].addEventListener("click", function(){
        console.log("enetered for loop");
        for(let key in links){
        console.log(lis[i].id);
        if (key == "seq."+lis[i].id+"()"){
            console.log("kill me")
            console.log(lis.length);
            if(lis[i].id === "nFOLD3" || lis[i].id === "Iupred3" || lis[i].id === "Modweb" || lis[i].id === "ModFOLD" || lis[i].id === "LigandSite"){
            console.log("Chal rha hai");
            let ifra = document.createElement("div");

            let link = document.createElement("a");
            link.textContent = "Results can be found here";
            link.id = "result"
            let img = document.createElement("img");
            link.href = links[key][1];
            link.target = "_blank";
            img.src = links[key][0];
            ifra.id = `ifra-${i}`;
            ifra.className = "ifra";
            ifra.appendChild(link);
            ifra.appendChild(img);
             if(!!document.getElementById("bada")){
            document.getElementById("bada").replaceWith(ifra);}
             for( let j=0; j<lis.length; j++){
            if(j!==i && !!document.getElementById(`ifra-${j}`)){
            document.getElementById(`ifra-${j}`).replaceWith(ifra)}}
            for(let i=0; i<visualizers.length; i++){
            if(!!visualizers[i]){
            visualizers[i].style.display = "none"
            visualizers[i].replaceWith(ifra);
            }
             }
            }
            else{
            let ifra = document.createElement("iframe");
            ifra.src= links[key];
            ifra.id = `ifra-${i}`;
            if(!!document.getElementById("bada")){
            document.getElementById("bada").replaceWith(ifra);}
            for( let j=0; j<lis.length; j++){
            if(j!==i && !!document.getElementById(`ifra-${j}`)){
            document.getElementById(`ifra-${j}`).replaceWith(ifra)}}
            for(let i=0; i<visualizers.length; i++){
            if(visualizers[i].style.display != "none"){
            visualizers[i].style.display = "none";
            document.body.appendChild(ifra);
            }
             }}}}})
    };

let U_D = document.getElementsByClassName("pred coll");
U_D[0].addEventListener("click",function() {
console.log(typeof(document.getElementById("bada")));
for (let p=0 ; p<lis.length ; p++){
 if(typeof(document.getElementById("bada")) === "undefined" || document.getElementById("bada")==null && !!document.getElementById(`ifra-${p}`)){
 console.log("entered if statement");
 var divi = document.createElement("div");
 divi.id = "bada";
 divi.className = "details";
 divi.innerHTML = ` <div class="al">
                    <h2> USER DETAILS </h2><br>
                    <p> Jobname: ${job_name}</p><br>
                    <p>Email: ${email}</p><br>
                    <p>Job Submission Status: Submitted Successfully</p><br>
                    <p>Time Taken:</p><br>
                    <hr>
                    <h2> SUBMISSION DETAILS</h2><br>
                    </div>`
 para = document.createElement("p");
 para.textContent = "Methods Selected:"
 para.id = "para"
 div = document.createElement("div");
 div.id = "div"
 ul = document.createElement("ul");
 for (let i=0 ; i<inputs_j.length ; i++){
 let li = document.createElement("li");
 let input = inputs_j[i];
 li.appendChild(document.createTextNode(input));
 ul.appendChild(li);
 }
 div.appendChild(ul)
 protein_name = document.createElement("p");
 protein_name.innerHTML = `Query Protein Name:${Q_P}`;
 protein_name.id = "protein"
 div2 = document.createElement("div");
 div2.className = "al";
 div2.appendChild(para);
 div2.appendChild(div);
 div2.appendChild(protein_name);
 divi.appendChild(div2);
if(!!document.getElementById(`ifra-${p}`)){
document.getElementById(`ifra-${p}`).replaceWith(divi);
}

}
}})
let colla = document.getElementsByClassName("pred coll");
console.log(colla);
for (let i = 1; i < colla.length; i++) {
 colla[i].addEventListener("click", function () {
                  // this.classList.toggle("pred_sel");
 let coco = this.nextElementSibling;

if (coco.style.height !== "0px" && colla[i].classList.contains("pred_sel") ) {
  colla[i].classList.remove("pred_sel");
  coco.style.height = "0px";
  console.log("My name is sanket 1");
     }
else {
       console.log("My name is Sanket");
       colla[i].classList.add("pred_sel");
       coco.style.height = coco.scrollHeight + "px";
                   }
                })

            };
/*else{
document.body.innerHTML=`Some error ocuured`
}
}
xhr.send();*/

let rel = document.getElementsByClassName("rel-art");
const divi = document.getElementsByClassName("API");
for (let i=0 ; i<rel.length; i++){
rel[i].addEventListener("click",function(){
//const divi = document.getElementsByClassName("API");
//for (let j=0 ; j<divi.length; j++){
//if (j === i){
divi[i].style.display = "inline-block";
/*var divi = document.createElement("div");
divi.id = "API";
divi.className = "det";
for(let k in dat){
para = document.createElement("p")
para.id = "paper"
para.innerHTML= `Title: ${dat[k].title}<br>
PMCid: ${dat[k].pmcid}<br><br>`
divi.appendChild(para)
}*/
for(let p=0 ; p<lis.length; p++){
if(!!document.getElementById(`ifra-${p}`)){
document.getElementById(`ifra-${p}`).replaceWith(divi[i]);
}
}
if(!!document.getElementById("bada")){
document.getElementById("bada").replaceWith(divi[i]);
}

for(let p=0 ; p<2; p++){
if(p!==i){
if(document.getElementById(`API-${p}`).style.display == "inline-block"){
document.getElementById(`API-${p}`).style.display = "none";

}
}
}


}
)}
const vis = document.getElementsByClassName("vis");
const visualizers = document.getElementsByClassName("visualizers");
for (let i=0 ; i<vis.length; i++){
if (i===0){
vis[i].addEventListener("click",function(){
let mol = document.getElementById("myViewer");
mol.style.display = "inline-block";
if(!!document.getElementById("bada")){
document.getElementById("bada").replaceWith(mol);
}
for(let p=0 ; p<lis.length; p++){
if(!!document.getElementById(`ifra-${p}`)){
document.getElementById(`ifra-${p}`).replaceWith(mol);
}
}
for(let j=0; j<visualizers.length; j++){
if (visualizers[j].id !== mol.id && visualizers[j]){
mol.style.display = "inline-block"
visualizers[j].style.display = "none"
}
}
})
}
if(i===1){
vis[i].addEventListener("click",function(){
let NGL = document.getElementById("NGL");
NGL.style.display = "inline-block";
if(!!document.getElementById("bada")){
document.getElementById("bada").replaceWith(NGL);
}
for(let p=0 ; p<lis.length; p++){
if(!!document.getElementById(`ifra-${p}`)){
document.getElementById(`ifra-${p}`).replaceWith(NGL);
}
}
for(let j=0; j<visualizers.length; j++){
if (visualizers[j].id !== NGL.id && visualizers[j]){
NGL.style.display = "inline-block"
visualizers[j].style.display = "none"
}}
})
}
if(i===2){
vis[i].addEventListener("click",function(){
let jsmol = document.getElementById("jsmol");
jsmol.style.display = "inline-block";
if(!!document.getElementById("bada")){
document.getElementById("bada").replaceWith(jsmol);
}
for(let p=0 ; p<lis.length; p++){
if(!!document.getElementById(`ifra-${p}`)){
document.getElementById(`ifra-${p}`).replaceWith(jsmol);
}
}
for(let j=0; j<visualizers.length; j++){
if (visualizers[j].id !== jsmol.id && visualizers[j]){
jsmol.style.display = "inline-block"
visualizers[j].style.display = "none"
}}
})
}
if(i===3){
vis[i].addEventListener("click",function(){
let PDB = document.getElementById("PDB");
PDB.style.display = "inline-block";
if(!!document.getElementById("bada")){
document.getElementById("bada").replaceWith(PDB);
}
for(let p=0 ; p<lis.length; p++){
if(!!document.getElementById(`ifra-${p}`)){
document.getElementById(`ifra-${p}`).replaceWith(PDB);
}
}
for(let j=0; j<visualizers.length; j++){
if (visualizers[j].id !== PDB.id && visualizers[j]){
PDB.style.display = "inline-block"
visualizers[j].style.display = "none"
}}
})
}
if(i===4){
vis[i].addEventListener("click",function(){
let icn3d = document.getElementById("icn3dwrap");
icn3d.style.display = "inline-block";
if(!!document.getElementById("bada")){
document.getElementById("bada").replaceWith(icn3d);
}
for(let p=0 ; p<lis.length; p++){
if(!!document.getElementById(`ifra-${p}`)){
document.getElementById(`ifra-${p}`).replaceWith(icn3d);
}
}
for(let j=0; j<visualizers.length; j++){
if (visualizers[j].id != icn3d.id && visualizers[j]){
icn3d.style.display = "inline-block"
visualizers[j].style.display = "none"
}}
})
}
}

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
window.location.href = "";
}
})
};
