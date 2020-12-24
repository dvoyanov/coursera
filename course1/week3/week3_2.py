import os
import csv


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        if brand:
            self.brand = brand
        else:
            raise ValueError("Error brand", brand)
        img_ext = [".jpg", ".jpeg", ".png", ".gif"]
        if os.path.splitext(photo_file_name)[1] in img_ext:
            self.photo_file_name = photo_file_name
        else:
            raise ValueError("Error file ext", photo_file_name)
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "car"
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "truck"
        body_list = []
        body_whl = body_whl.split("x")
        try:
            if len(body_whl) != 3:
                raise ValueError("Error body_whl", body_whl)
            for i in range(3):
                body_list.append(float(body_whl[i]))
        except (ValueError, IndexError):
            body_list = [0.0, 0.0, 0.0]
        self.body_length, self.body_width, self.body_height = body_list


    def get_body_volume(self):
        return self.body_length*self.body_width*self.body_height


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "spec_machine"
        if extra:
            self.extra = extra
        else:
            raise ValueError



def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            try:
                if row[0] == "car":
                    car_list.append(Car(row[1], row[3], row[5], row[2]))
                elif row[0] == "truck":
                    car_list.append(Truck(row[1], row[3], row[5], row[4]))
                elif row[0] == "spec_machine":
                    car_list.append(SpecMachine(row[1], row[3], row[5], row[6]))
            except Exception:
                print("except")
    return car_list
