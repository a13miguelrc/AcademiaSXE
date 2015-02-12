# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "a13miguelrc"
__date__ = "$Feb 9, 2015 12:12:04 PM$"


from openerp.osv import fields, orm

#Aula: nombre, descripción, código, ubicación
class Aula(orm.Model):    
    _name = 'aula'
    _columns = {                
         'nombre':fields.char('Nombre',size=50),     
         'descripcion':fields.char('Descripción',size=50),
         'codigo':fields.char('Código',size=3),
         'ubicacion':fields.char('Ubicación',size=50)
       }
Aula()

#Curso: nombre, descripción, estudios, aula (many2many)
class Curso(orm.Model):
    _name = 'curso'
    _columns = {
        'descripcion':fields.char('Descripción',size='50'),
        'estudios':fields.char('Estudios',size=50),
        'aula_ids':fields.many2many('aula','curso_aula_rel','curso_id','aula_id','Aulas') 
    }
Curso()

#Alumno: nombre, dirección, localidad, provincia, teléfono, email, fechaNacimiento, 
#curso (many2one)
class Alumno(orm.Model):
    _name = 'alumno'
    _columns = {
        'nombre':fields.char('Nombre',size=50), 
        'direccion':fields.char('Dirección',size=50), 
        'localidad':fields.char('Localidad',size=50),
        'provincia_id':fields.many2one('res.country.state','Provincia'), 
        'telefono':fields.char('Teléfono',size=9), 
        'email':fields.char('email',size=50),
        'fecha_nacimiento':fields.date('Fecha Nacimiento'),
        'curso_id':fields.many2one('curso','Curso')
    }
Alumno()

#Holaaaaa probando probando 1,2 sisisisisnononononsisisisinonononsusnonsyisnosnusnonuishnflaisufg