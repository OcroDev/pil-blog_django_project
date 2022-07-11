# El usuario administrador es
user: admin
password: admin

# Este usuario permite acceso al admin de django, donde se pueden cargar los articulos
de la tienda, los servicios, y entradas del blog

# Para los usuarios clientes hay que registrarse, estos usuarios pueden realizar
todas las acciones de la pagina tienda, especificamente el manejo del carro

# Antes de empezar se deben instalar los plugins (o dependencias) del archivo requirements.txt

# Además se deben cambiar los valores de las constantes en  el archivo settings.py
 EMAIL_HOST_USER="prueba@gmail.com"
 EMAIL_HOST_PASSWORD="123456789"
 Y cambiar el correo del usuario admin que es donde recibiras el pedido por correo electronico

#Los valores establecidos para el envío de correos unicamente funciona con GMAIL, 
de tener otro tipo de correo debes arreglar (settings.py):

 EMAIL_HOST = "smtp.gmail.com"
 EMAIL_USE_TLS = True
 EMAIL_PORT=587

#Los datos introducidos en la base de datos son datos de prueba
