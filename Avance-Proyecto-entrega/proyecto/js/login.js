function iniciar(){
    let f = document.getElementById("flogin");
    let u = f.txtUsr.value;
    let p = f.txtPwd.value;
    let m = document.getElementById("msg");
    m.innerHTML = "";
    if(u =="admin" && p =="123"){
        
        window.location = "admin.html";
        alert("Bienvenido admin");
    }
    if(u =="uag" && p =="85"){
        
        window.location = "alumno.html";
        alert("Bienvenido alumno");
    }
    else{
        m.innerHTML = "Datos de acceso incorrectos";
    }
    //alert (u + " "+p );
}