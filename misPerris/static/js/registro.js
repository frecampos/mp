class registro{
    nombre;
    apellido;
    email;
    usuario;
    pass;
    fono;
    rut;
    //mutadores
    setNombre(nombre){
        this.nombre=nombre;
    }
    setApellido(apellido){
        this.apellido=apellido;
    }
    setEmail(email){
        this.email=email;
    }
    setUsuario(usuario){
        this.usuario=usuario;
    }
    setPass(pass){
        this.pass=pass;
    }
    setFono(fono){ this.fono=fono;}
    setRut(rut){ this.rut=rut;}
    //accesadores
    getNombre(){ return this.nombre;}
    getApellido(){ return this.apellido;}
    getEmail(){ return this.email;}
    getUsuario(){ return this.usuario;}
    getPass(){ return this.pass;}
    getFono(){ return this.fono;}
    getRut(){ return this.rut;}
    // toString
    imprimir(){
        return this.getNombre()+' '+this.getApellido()+' '+this.getEmail();
    }
} 