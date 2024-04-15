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
    
def generate_nested_components(depth):
    if depth <= 0:
        return None
    list_of_objects = [1, {1, 2, 3}, [1, 2, 3]]
    circular_ref = SelfReferencingEntity()
    component = SomeComponent(23, list_of_objects, circular_ref)
    circular_ref.set_parent(component)

    # Simulate processing time of 2 seconds
    time.sleep(2)

    component.some_list_of_objects.append(generate_nested_components(depth - 1))
    return component

if __name__ == "__main__":
    # Generate 20 nested components
    root_component = generate_nested_components(20)

    # Perform deep copy
    deep_copied_component = copy.deepcopy(root_component)

    # Test the deep copy
    print(f"id(deep_copied_component.some_circular_ref.parent): {id(deep_copied_component.some_circular_ref.parent)}")
    print(f"id(deep_copied_component.some_circular_ref.parent.some_circular_ref.parent): {id(deep_copied_component.some_circular_ref.parent.some_circular_ref.parent)}")
    print("^^ This shows that deepcopied objects contain the same reference, they are not cloned repeatedly.")
