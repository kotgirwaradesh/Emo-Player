
function addasong(){
    var name=document.getElementById("sname").value;
    var slink=document.getElementById("slink").value;
    var vlink=document.getElementById("vlink").value;
    var table = document.getElementById("mediatable");
    var x = document.getElementById("mediatable").rows.length; 
    var row = table.insertRow(x);
    var cell0 = row.insertCell(0);
    var cell1 = row.insertCell(1);
    var cell2 = row.insertCell(2);
    var cell3=row.insertCell(3);
    cell0.innerHTML = name;
    cell1.innerHTML = '<a href="'+slink+'">'+'Play'+'</a>';
    cell2.innerHTML = '<a href="'+vlink+'">'+'Play'+'</a>';
    cell3.innerHTML = '<input type="button" value="Delete" onclick="deleteRow(this)">';  
}
function deleteRow(r) {
    var i = r.parentNode.parentNode.rowIndex;
    document.getElementById("mediatable").deleteRow(i);
}