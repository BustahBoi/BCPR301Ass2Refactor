import re
from copy import deepcopy


class Validator:
    def __init__(self):
        self.temp_dict = dict()
        self.valid_dict = dict()
        self.id = "^[A-Z][\d]{3}$"
        self.gender = "^(M|F)$"
        self.age = "^[\d]{2}$"
        self.sales = "^[\d]{3}$"
        self.BMI = "^(Normal|Overweight|Obesity|Underweight)$"
        self.salary = "^([\d]{2}|[\d]{3})$"
        self.birthday = "^(0[1-9]|[1-2][0-9]|3(0|1))(-|/)(0[1-9]|1[0-2])(-|/)(19|20)[0-9]{2}$"

    def check(self, attr, data):
        check_attr = getattr(self, attr.lower(), False)
        data = str(data)
        if check_attr:
            match = re.match(check_attr, data)
            if match:
                return data
            else:
                return False

    def check_gender(self, new_gender):
        """
        Checks the gender matches validation rules
        :param new_gender:
        :return:
        # Wesley
        >>> v = Validator()
        >>> v.check_gender("M")
        'M'
        """
        match = re.match(self.gender, new_gender)
        if match:
            return new_gender
        else:
            # James (new reg ex)
            match = re.match("^((m|M)ale)$", new_gender)
            if match:
                new_gender = "M"
                return new_gender
            fmatch = re.match("^((f|F)emale)$", new_gender)
            if fmatch:
                new_gender = "F"
                return new_gender
            new_gender = False
            # print("false new_gender")
            return new_gender

    def check_BMI(self, new_BMI):
        """
        Checks the BMI matches validation rules
        :param new_BMI:
        :return:
        # Wesley
        >>> v = Validator()
        >>> v.check_BMI("normal")
        'Normal'
        """
        match = re.match(self.BMI, new_BMI)
        if match:
            return new_BMI
        else:
            # James (new reg ex)
            match = re.match("^(normal|overweight|obesity|underweight)$", new_BMI)
            if match:
                new_BMI = new_BMI.capitalize()
                return new_BMI
            new_BMI = False
            # print("false new_BMI")
            return new_BMI

    def check_salary(self, new_salary):
        new_salary = str(new_salary)
        match = re.match(self.salary, new_salary)
        if match:
            return new_salary
        else:
            new_salary = False
            # print("false new_salary")
            return new_salary

    @staticmethod
    def xlsx_date(a_date):
        return a_date.date().strftime("%d-%m-%Y")

    def check_birthday(self, new_birthday):
        match = re.match(self.birthday, new_birthday)
        if match:
                return new_birthday
        else:
            invalid_delims = "(/|\\|.|:|;|,|_)"
            match = re.search(invalid_delims, new_birthday)
            if match:
                invalid = "/\\.:;,_"
                for c in invalid:
                    new_birthday = new_birthday.replace(c, '-')
            else:
                new_birthday = False
            return new_birthday

    @staticmethod
    def checker(row):
        result = True
        # try:
        for key, value in row.items():
            if key == "ID":
                try:
                    if value is None or a.check("ID", value) is False:
                        result = False
                        return result
                    else:
                        a.push_value(key, a.check("ID", value))
                except TypeError:
                    print("TypeError")
            elif key == "Gender":
                try:
                    if value is None or a.check_gender(value) is False:
                        result = False
                        return result
                    else:
                        a.push_value(key, a.check_gender(value))
                except TypeError:
                    print("TypeError")
            elif key == "Age":
                if value is None or a.check("Age", value) is False:
                    result = False
                    return result
                else:
                    a.push_value(key, a.check("Age", value))
            elif key == "Sales":
                if value is None or a.check("Sales", value) is False:
                    result = False
                    return result
                else:
                    a.push_value(key, a.check("Sales", value))
            elif key == "BMI":
                if value is None or a.check_BMI(value) is False:
                    result = False
                    return result
                else:
                    a.push_value(key, a.check_BMI(value))
            elif key == "Salary":
                if value is None or a.check_salary(value) is False:
                    result = False
                    return result
                else:
                    a.push_value(key, a.check_salary(value))
            elif key == "Birthday":
                if value is None or a.check_birthday(value) is False:
                    result = False
                    return result
                else:
                    a.push_value(key, a.check_birthday(value))
        # except TypeError:
        #     print("Sorry, there was a type error for a record value")

    # James' changes (13/03)
    @staticmethod
    def save_dict(loaded_dict):
        for empno, row in loaded_dict.items():
            b = a.checker(row)
            if b is False:
                print("Error at entry: " + str(empno))
            else:
                a.push_row(empno)
        return a.return_dict()

    def push_value(self, key, val):
        self.temp_dict[key] = val

    def push_row(self, empno):
        temp = deepcopy(self.temp_dict)
        if len(temp) == 7:
            # print("Adding Row " + str(empno))
            self.valid_dict[empno] = temp
            # print(self.valid_dict[empno])
        self.temp_dict = dict()

    def return_dict(self):
        return self.valid_dict


a = Validator()