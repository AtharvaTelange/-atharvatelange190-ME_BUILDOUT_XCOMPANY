from typing import List
from src.company import Employee, Gender


class Company:
    def __init__(self,company_name: str, founder: Employee) -> None:
        self._company_name = company_name
        self._founder = founder
        self._employee_book = {}
        self._employee_book[founder.get_name()] = founder

    def get_company_name(self) -> str:
        return self._company_name

    # TODO: CRIO_TASK_MODULE_XCOMPANY
    # Please define all the methods required here as mentioned in the XCompany BuildOut Milestone before implementing the logic.
    # This will ensure that the project can be compiled successfully.
    def register_employee(self, employee_name: str, gender: Gender) -> None:
        self._employee_book[employee_name] = Employee(employee_name, gender)

    def get_employee(self, employee_name) -> Employee:
        if self._employee_book.get(employee_name) == None:
            return None
        else:
            return self._employee_book[employee_name]
    
    def delete_employee(self,employee_name) -> None:
        if self.get_employee(employee_name):
            del self._employee_book[employee_name]
        else:
            return None

    def assign_manager(self,employee_name : str, manager_name: str) -> None:
        self._employee_book[manager_name].assign_manager(employee_name)
        self._employee_book[employee_name].set_manager_name(manager_name)

    def get_direct_reports(self,manager_name: str) -> List[Employee]:
        array = []
        for element in self._employee_book[manager_name].get_direct_reports():
            array.append(self._employee_book[element])
        return array

    def get_team_mates(self,employee_name: str) -> List[Employee]:
        array = []
        manager_name = self._employee_book[employee_name].get_manager_name()
        array.append(self.get_employee(manager_name))
        array.extend(self.get_direct_reports(manager_name))
        return array

    def get_employee_hierarchy(self,manager_name: str) -> List[List[Employee]]:
        #similar to tree traversal logic implementation
        array = []
        queue = []
        next_queue = []
        answer = []
        queue.append(manager_name)
        while len(queue)!= 0:
            element = queue.pop(0)
            array.append(self._employee_book[element])
            if len(self._employee_book[element].get_direct_reports()) != 0:
                next_queue.extend(self._employee_book[element].get_direct_reports())
            if len(queue) == 0:
                queue, next_queue = next_queue, []
                answer.append(array)
                array = []
        return answer


    




    

    