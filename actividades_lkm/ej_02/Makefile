# Nombre del archivo fuente principal
SRC_FILE := main
# Nombre del módulo (reemplazar con tu nombre y apellido)
MODULE_NAME := Ferrante_Santino_ej02
# Directorio para archivos de compilación
BUILD_DIR := $(PWD)/build
# Directorio que contiene los archivos de construcción del kernel
KERNEL_BUILD_DIR := /lib/modules/$(shell uname -r)/build

# Archivo objeto para agregar al módulo
obj-m += ${MODULE_NAME}.o
${MODULE_NAME}-objs := ${SRC_FILE}.o

# Regla predeterminada para compilar el módulo
all:
	@mkdir -p build; \
	cp -f ${SRC_FILE}.c Makefile ${BUILD_DIR}; \
	cd build; \
	make -C ${KERNEL_BUILD_DIR} M=${BUILD_DIR} modules \

# Regla para limpiar los archivos generados en la compilación
clean:
	@cd build; \
	make -C ${KERNEL_BUILD_DIR} M=${BUILD_DIR} clean; \
	cd .. && rm -rf build

# Cargar el módulo en el kernel
load_module:
	@sudo insmod build/${MODULE_NAME}.ko

# Retirar el módulo del kernel
unload_module:
	@sudo rmmod ${MODULE_NAME}

# Mostrar mensajes del kernel relacionados con el módulo
view_logs:
	@dmesg -wHT | grep ${MODULE_NAME}

# Ayuda con los comandos disponibles
help:
	@echo "Entorno Makefile para RPiZeroW - v1.0"
	@echo ""
	@echo "- all: Compila el módulo (comando predeterminado)"
	@echo "- clean: Limpia los archivos generados en la compilación"
	@echo "- load_module: Carga el módulo en el kernel"
	@echo "- unload_module: Retira el módulo del kernel"
	@echo "- view_logs: Muestra los mensajes del kernel relacionados con este módulo"
	@echo "- help: Muestra esta lista de comandos disponibles"
