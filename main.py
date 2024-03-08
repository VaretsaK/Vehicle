class Vehicle:
    """
        A class to represent a vehicle.
        ...

        Attributes
        ----------
        model : int
            model of the vehicle
        top_speed : int
            top speed of the vehicle
        price : ine
            price of the vehicle

        Methods
        -------

        """
    def __init__(self, model: str, top_speed: int, price: int) -> None:
        """
        Constructs all the necessary attributes for a vehicle object.
        :param model:
        :param top_speed:
        :param price:
        """
        self.model = model
        self.top_speed = top_speed
        self.price = price

    def __repr__(self) -> str:
        """
        Representation of an instance.
        :return:
        """
        return f"Vehicle('{self.model}'; speed {self.top_speed}; price {self.price})"

    def __gt__(self, other) -> bool:
        """
        Check if the object is greater than another object.
        :param other:
        :return:
        """
        if isinstance(other, Vehicle):
            return self.top_speed > other.top_speed
        raise TypeError("Unsupported operand type for >")


if __name__ == "__main__":
    bmw = Vehicle("x5", 220, 44000)
    mercedes = Vehicle("S500", 270, 49000)
    audi = Vehicle("A7", 250, 34000)

    list_of_cars = sorted([bmw, mercedes, audi])
    print(list_of_cars)
    print(bmw > mercedes)
