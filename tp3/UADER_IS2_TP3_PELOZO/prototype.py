import copy
import time

class SelfReferencingEntity:
    def __init__(self):
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent


class SomeComponent:
    def __init__(self, some_int, some_list_of_objects, some_circular_ref):
        self.some_int = some_int
        self.some_list_of_objects = some_list_of_objects
        self.some_circular_ref = some_circular_ref

    def __copy__(self):
        some_list_of_objects = copy.copy(self.some_list_of_objects)
        some_circular_ref = copy.copy(self.some_circular_ref)
        new = self.__class__(
            self.some_int, some_list_of_objects, some_circular_ref
        )
        new.__dict__.update(self.__dict__)
        return new

    def __deepcopy__(self, memo=None):
        if memo is None:
            memo = {}
        some_list_of_objects = copy.deepcopy(self.some_list_of_objects, memo)
        some_circular_ref = copy.deepcopy(self.some_circular_ref, memo)
        new = self.__class__(
            self.some_int, some_list_of_objects, some_circular_ref
        )
        new.__dict__ = copy.deepcopy(self.__dict__, memo)
        return new

    def create_nested_components(self, levels):
        if levels > 0:
            for i in range(5):  # Creamos 5 componentes en cada nivel
                some_list_of_objects = [1, {1, 2, 3}, [1, 2, 3]]
                circular_ref = SelfReferencingEntity()
                component = SomeComponent(23, some_list_of_objects, circular_ref)
                circular_ref.set_parent(component)
                component.create_nested_components(levels - 1)


if __name__ == "__main__":
    list_of_objects = [1, {1, 2, 3}, [1, 2, 3]]
    circular_ref = SelfReferencingEntity()
    component = SomeComponent(23, list_of_objects, circular_ref)
    circular_ref.set_parent(component)

    # Generar 20 niveles de anidamiento
    component.create_nested_components(20)

    # Simular carga de procesamiento
    print("Simulando carga de procesamiento durante 2 segundos...")
    component.some_list_of_objects.append("processing")  # Marcar el inicio de la carga de procesamiento
    time.sleep(2)  # Simular carga de procesamiento
    print("Carga de procesamiento completada.")
