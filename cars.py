import os
import csv


class CarBase:
    def __init__(self, car_type, brand, photo_file_name, carrying):
        self.car_type = car_type
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        photo_file = self.photo_file_name
        photo_file = os.path.splitext(photo_file)
        if photo_file[1] in [".jpg", ".jpeg", ".png", ".gif"] and len(photo_file) == 2:
            return photo_file[1]

def is_good_photo(string):
    photo_file = string
    photo_file = os.path.splitext(photo_file)
    if photo_file[1] in [".jpg", ".jpeg", ".png", ".gif"] and len(photo_file) == 2:
        return True
    else:
        return False

def is_digit(string):
    if string.isdigit():
        return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        self.car_type = 'car'
        self.passenger_seats_count = int(passenger_seats_count)
        super().__init__(self.car_type, brand, photo_file_name, carrying)


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        self.car_type = 'truck'
        self.body_whl = str(body_whl)
        self.body_length, self.body_width, self.body_height = self.get_body_length_width_height
        super().__init__(self.car_type, brand, photo_file_name, carrying)

    def parse_body_length_width_height(self):
        parse = self.body_whl
        parse = parse.split("x")
        for i in parse:
            # print(i)
            if is_digit(i) is not True:
                return False
        return True

    @property
    def get_body_length_width_height(self):
        body_whl = self.body_whl
        parse = self.parse_body_length_width_height()
        # print(parse)
        if body_whl == "" or body_whl == body_whl.split("x") or parse is not True or len(body_whl.split("x")) != 3:
            width = 0.0
            height = 0.0
            length = 0.0
            return length, width, height

        body_whl = body_whl.split("x")
        length = float(body_whl[0])
        width = float(body_whl[1])
        height = float(body_whl[2])

        return length, width, height


    def get_body_volume(self):
        length, width, height = self.get_body_length_width_height
        volume = width * height * length
        return volume


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        self.car_type = 'spec_machine'
        self.extra = str(extra)
        super().__init__(self.car_type, brand, photo_file_name, carrying)


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            try:
                if row[0] == 'car' and row[1] != '' and row[3] != '' and row[5] != '' and row[2] != ''\
                        and is_good_photo(row[3]) is True:
                    car = Car(row[1], row[3], row[5], row[2])
                    car_list.append(car)
                elif row[0] == 'truck' and row[1] != '' and row[3] != '' and row[5] != ''\
                        and is_good_photo(row[3]) is True:
                    truck = Truck(row[1], row[3], row[5], row[4])
                    car_list.append(truck)
                elif row[0] == 'spec_machine' and row[1] != '' and row[3] != '' and row[5] != '' and row[6] != '' \
                        and is_good_photo(row[3]) is True:
                    spec_machine = SpecMachine(row[1], row[3], row[5], row[6])
                    car_list.append(spec_machine)
            except IndexError:
                continue
            except ValueError:
                continue
    return car_list


# path = "C:/test.csv"
# print(path)
# test = get_car_list(path)
# print(test)
# print(test[1].get_body_volume())
# test = Truck('Nissan', '1.jp', '2.5', '')
# print(test.body_height)
# print(test.body_length)
# print(test.get_photo_file_ext())
