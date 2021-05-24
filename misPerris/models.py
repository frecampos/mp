from django.db import models

# Create your models here.
class TipoMascota(models.Model):
    nombre = models.CharField(primary_key=True,max_length=45)
    annos = models.IntegerField()

    def __str__(self):
        return self.nombre
    
class Mascota(models.Model):
    nombre = models.CharField(primary_key=True,max_length=50)
    edad = models.IntegerField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='mascotas',default='mascotas/default.png')
    publicar = models.BooleanField(default=False)
    comentario= models.TextField(default='--')
    usuario = models.CharField(null=True,max_length=45)
    tipo = models.ForeignKey(TipoMascota, on_delete=models.CASCADE)
    dueno = models.CharField(max_length=45,default='--')

    def __str__(self):
        return self.nombre+" - "+str(self.publicar)+" - "+self.comentario

class galeria(models.Model):
    auto_inc = models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to='galeria')
    mascota = models.ForeignKey(Mascota,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.auto_inc)