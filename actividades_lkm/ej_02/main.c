#include <linux/kernel.h>       // Para funciones de depuración como printk
#include <linux/module.h>       // Para creación de módulos en el kernel
#include <linux/init.h>         // Para inicialización y limpieza de módulos
#include <linux/kthread.h>      // Para crear y manejar hilos en el kernel
#include <linux/sched.h>        // Para manejar la programación de tareas
#include <linux/delay.h>        // Para funciones de espera como msleep
#include <linux/sched/signal.h> // Para manejar señales de los hilos

// Punteros para los hilos del kernel
static struct task_struct *thread_1 = NULL; // Primer hilo
static struct task_struct *thread_2 = NULL; // Segundo hilo

// Función ejecutada por el primer hilo
static int thread_function_1(void *params) {
    while (!kthread_should_stop()) { // Corre hasta que el hilo sea detenido
        printk("kernel_thread_example: Mensaje desde el Hilo 1");
        msleep(500); // Pausa de 500 ms para evitar saturación de mensajes
    }
    return 0; // Finaliza la ejecución del hilo
}

// Función ejecutada por el segundo hilo
static int thread_function_2(void *params) {
    while (!kthread_should_stop()) { // Corre hasta que el hilo sea detenido
        printk("kernel_thread_example: Mensaje desde el Hilo 2");
        msleep(500); // Pausa de 500 ms
    }
    return 0; // Finaliza la ejecución del hilo
}

// Función de inicialización del módulo
static int __init kernel_thread_module_init(void) {
    // Crear el primer hilo
    thread_1 = kthread_create(thread_function_1, NULL, "kernel_thread_1");
    if (thread_1 == NULL) { // Verifica si se pudo crear correctamente
        printk(KERN_INFO "kernel_thread_example: Error al crear el Hilo 1");
        return -1;
    }

    // Crear el segundo hilo
    thread_2 = kthread_create(thread_function_2, NULL, "kernel_thread_2");
    if (thread_2 == NULL) { // Verifica si se pudo crear correctamente
        printk(KERN_INFO "kernel_thread_example: Error al crear el Hilo 2");
        return -1;
    }

    // Activar ambos hilos
    wake_up_process(thread_1);
    wake_up_process(thread_2);

    printk(KERN_INFO "kernel_thread_example: Módulo cargado correctamente");
    return 0; // Indica que el módulo fue cargado exitosamente
}

// Función de limpieza del módulo
static void __exit kernel_thread_module_exit(void) {
    // Detener ambos hilos
    if (thread_1) {
        kthread_stop(thread_1);
    }
    if (thread_2) {
        kthread_stop(thread_2);
    }
    printk(KERN_INFO "kernel_thread_example: Módulo descargado correctamente");
}

// Asocia las funciones de inicialización y limpieza con el módulo
module_init(kernel_thread_module_init);
module_exit(kernel_thread_module_exit);

// Información del módulo
MODULE_LICENSE("GPL"); // Licencia GNU GPL
MODULE_AUTHOR(""); // Autor (puedes completarlo)
MODULE_DESCRIPTION("Ejemplo de hilos en el kernel"); // Descripción del módulo
