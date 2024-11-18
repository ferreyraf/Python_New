width = 5

for renglon in range(width,0,-1):
	cadena = ""
	for linea in range(renglon,0,-1):
		cadena += str(linea) + " "
	print(f"{cadena} ")


#################################################################################################
# 											Funciones											#
# 	Siempre se declaran antes de ser usadas,este orden importa!									#
# 	Probar que pasa si haces la llamada de la funcion antes de escribir la propia Funciones		#
#																								#
#################################################################################################


##############################
# USO CORRECTO DE LA FUNCION #
##############################

# Paso 1 : Declarar la funcion, por lo general no haces la funcion hasta que 
# no sabes que hace un proceso anterior
# Por lo que mas normal,es dejar declarada una funcion y colocar el pass para 
# indicar que si se llama a la funcion no hace nada y esto no te tire un error
# de que la funcion esta vacia al pedo basicamente

def funcion(parametros_variables):
	pass


# Paso 2: Llamar finalmente a la funcion pasandole o no un parametro
funcion(parametros_variables)


################################
# USO INCORRECTO DE LA FUNCION #
################################

# Esta forma de declararlo te va a dar siempre error, porque python funcion de arriba abajo.
# Por mas que no uses la funcion desde el principio,python tiene que "verla" antes de ser llamada propiamente


funcion(parametros_variables)

def funcion(parametros_variables):
	pass

# No es lo mismo llamar la funcion y luego declararla,asi no funciona,da error.!