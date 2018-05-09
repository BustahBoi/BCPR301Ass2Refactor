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
        self.bmi = "^(Normal|Overweight|Obesity|Underweight)$"
        self.salary = "^([\d]{2}|[\d]{3})$"
        self.birthday = "^(0[1-9]|[1-2][0-9]|3(0|1))(-|/)(0[1-9]|1[0-2])(-|/)(19|20)[0-9]{2}$"

    def check(self, attr, data):
        check_attr = getattr(self, attr.lower(), False)
        data = str(data)
        result = False
        if check_attr:
            match = re.match(check_attr, data)
            if match:
                result = data
            else:
                result = self.change_regexp(attr.lower(), data)
        return result

    def change_regexp(self, attr, data):
        result = False
        formatting = {"gender": {"((m|M)ale)$": "M", "((f|F)emale)$": "F"},
                      "bmi": {"^(normal|overweight|obesity|underweight)$": data.capitalize()},
                      "birthday": {"(/|\\|.|:|;|,|_)": "/\\.:;,_"}}
        try:
            new_format = formatting[attr]
            for key, value in new_format.items():
                c = re.compile(key)
                if attr == "birthday" and c.search(data) is not None:
                    result = c.sub('-', data)
                elif re.match(key, data) is not None:
                    result = value
                    break
                else:
                    result = False
            return result
        except KeyError:
            return False

    @staticmethod
    def xlsx_date(a_date):
        return a_date.date().strftime("%d-%m-%Y")

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
                    if value is None or a.check("Gender", value) is False:
                        result = False
                        return result
                    else:
                        a.push_value(key, a.check("Gender", value))
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
                if value is None or a.check("BMI", value) is False:
                    result = False
                    return result
                else:
                    a.push_value(key, a.check("BMI", value))
            elif key == "Salary":
                if value is None or a.check("Salary", value) is False:
                    result = False
                    return result
                else:
                    a.push_value(key, a.check("Salary", value))
            elif key == "Birthday":
                if value is None or a.check("Birthday", value) is False:
                    result = False
                    return result
                else:
                    a.push_value(key, a.check("Birthday", value))
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
