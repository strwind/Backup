(function(){
    var treeBlock = document.getElementById("treeBlock");
    function expand(e){
        var e = window.event || e,
            target = e.target || e.srcElement,
            ul = target.parentNode.getElementsByTagName("ul")[0];
        if(!ul || target.tagName !== "H3"){ return null;}
        if(ul.style.display == "block"){
            ul.style.display = "none";
        }else{
            ul.style.display = "block";
        }
    }
   document.addEventListener ?
   treeBlock.addEventListener("click", expand, false):
   treeBlock.attachEvent("onclick", expand);
})();
