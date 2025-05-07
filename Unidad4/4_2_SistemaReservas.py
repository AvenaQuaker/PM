import asyncio
import random
import time

class SistemaReservas:
    def __init__(self,capacidad_total = 10,solicitudes_concurrentes = 3):
        """
        Inicializar el Sistema de Reservas.

        Args:
            capacidad_total (int): Capacidad total del sistema de reservas.
            solicitudes_concurrentes (int): Número máximo de solicitudes concurrentes.
        """

        self.capacidad_total = capacidad_total
        self.reservas_actuales = 0
        self.semaforo = asyncio.Semaphore(solicitudes_concurrentes)
        self.lock = asyncio.Lock()

    async def procesar_solicitudes(self,id_cliente):
        """
        Procesar una solicitud de reserva.

        Arg:
            id_cliente (int): ID del cliente que realiza la solicitud.

        Returns:
            bool: True si la reserva fue exitosa, False en caso contrario.
        """

        async with self.semaforo:
            print(f"[{time.strftime('%H:%M:%S')}] Cliente {id_cliente} está intentando reservar.")
            await asyncio.sleep(random.uniform(0.5, 2))

            async with self.lock:
                if self.reservas_actuales < self.capacidad_total:
                    self.reservas_actuales += 1
                    disponibilidad_restante = self.capacidad_total - self.reservas_actuales
                    print(f"[{time.strftime('%H:%M:%S')}] Reserva exitosa para el cliente {id_cliente}." + f"Disponibilidad restante: {disponibilidad_restante}/{self.capacidad_total}")
                    return True
                else:
                    print(f"[{time.strftime('%H:%M:%S')}] No hay disponibilidad para el cliente {id_cliente}.")
                    return False

    async def cancelar_reserva(self,id_cliente):
        """
        Cancelar una reserva.

        Arg:
            id_cliente (int): ID del cliente que cancela la reserva.
        """
        await asyncio.sleep(random.uniform(0.3, 1))

        async with self.lock:
            if self.reservas_actuales > 0:
                self.reservas_actuales -= 1
                disponibilidad_restante = self.capacidad_total - self.reservas_actuales
                print(f"[{time.strftime('%H:%M:%S')}] Reserva cancelada por el cliente {id_cliente}." + f"Disponibilidad restante: {disponibilidad_restante}/{self.capacidad_total}")

async def cliente(sistema, id_cliente):
    """
    Simula el comportamiento de un cliente que intenta hacer una reserva.

    Args: 
        sistema: Instancia de SistemaReservas
        id_cliente: Identificador único del cliente
    """
    try:
        print(f"[{time.strftime('%H:%M:%S')}] Cliente {id_cliente}: Intentando realizar reserva.")
        reserva_exitosa = await sistema.procesar_solicitudes(id_cliente)
        if reserva_exitosa:
            if random.random() < 0.3:
                await asyncio.sleep(random.uniform(1, 3)) # Simula el tiempo que el cliente mantiene la reserva
                await sistema.cancelar_reserva(id_cliente)
        else:
            if random.random() < 0.5:
                espera = random.uniform(0.5, 3)
                print(f"[{time.strftime('%H:%M:%S')}] Cliente {id_cliente}: Esperando para volver a intentar.")
                await asyncio.sleep(espera)
                print(f"[{time.strftime('%H:%M:%S')}] Cliente {id_cliente}: Reintentando reserva.")
                await sistema.procesar_solicitudes(id_cliente)
    except Exception as e: 
        print(f"[{time.strftime('%H:%M:%S')}] Cliente {id_cliente}: Error: {e}")

async def main():
    # Crear el sistema de reservas (10 plazas, máximo 3 solicitudes concurrentes)
    sistema = SistemaReservas(capacidad_total=10, solicitudes_concurrentes=3)
    
    # Simular 15 clientes que llegan casi al mismo tiempo
    clientes = [cliente(sistema, i) for i in range(1, 16)]
    
    # Ejecutar todos los clientes concurrentemente
    await asyncio.gather(*clientes)
    
    print(f"\n[{time.strftime('%H:%M:%S')}] Simulación completa. " +
        f"Reservas finales: {sistema.reservas_actuales}/{sistema.capacidad_total}")

# Ejecutar la simulación
if __name__ == "__main__":
    print("Iniciando simulación del sistema de reservas...")
    asyncio.run(main())