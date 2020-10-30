# Proyecto_DWY
seccion 003D - Grupo 1

Casos de Prueba 

========================================================

a) Tabla de Guardado en base de datos

--- las acciones que desarrollamos en esta tabla es de insertar datos en la base de datos.
    haciendo 1 definicion para agregar un insumo y otra definicion para agregar un usuario

====

codigo:

      class TestAgregar(unittest.TestCase):
          def test_grabar_insumo(self):
              valor = 0
              try:
                  insumo = Insumos(
                      nombre="silicona",
                      descripcion="lo mejor",
                      precio=500,
                      stock=10
                  )
                  insumo.save()
                  valor = 1
              except:
                  valor = 0
              self.assertEqual(valor,1)

          def test_grabar_usuario(self):
              valor = 0
              try:
                  nombre ="Juan"
                  apellido = "Herrera"
                  email = "JH@gmail.com"
                  usuario = "JHerrera"
                  pass1 = "123456789"
                  pass2 = "123456789"

                  if pass1!=pass2:
                      valor = 0

                  else:

                      usu = User()

                      usu.first_name = nombre
                      usu.last_name = apellido
                      usu.email = email
                      usu.username = usuario
                      usu.set_password(pass1)

                      usu.save()
                      valor = 1
              except:
                  valor = 0
              self.assertEqual(valor,1)


========================================================
========================================================

a) Tabla de Eliminar en base de datos

--- las acciones que desarrollamos en esta tabla es para borrar los datos de la base de datos que hicimos en la tabla anterior. aqui hacemos
    1 definicion para eliminar el insumo agregado anteriormente y otra para eliminar al usuario añadido.

====

codigo:

      class TestBorrar(unittest.TestCase):

          def test_borrar_insumo(self):
              valor = 0
              id ="silicona"

              try:
                  insumo = Insumos.objects.get(nombre=id)
                  insumo.delete()
                  valor = 1
              except:
                  valor = 0
              self.assertEqual(valor,1)

          def test_borrar_usuario(self):
              valor = 0
              usuario ="JHerrera"

              try:
                  usu = User.objects.get(username=usuario)
                  usu.delete()
                  valor = 1
              except:
                  valor = 0
              self.assertEqual(valor,1)
              
             
             
========================================================
