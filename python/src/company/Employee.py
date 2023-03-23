from typing import List
from src.company import Gender


class Employee:
    def __init__(self,name: str , gender: Gender) -> None:
        self._name = name
        self._gender = gender
        self._working_under = []
        self._manager_name = ""

    def get_name(self) -> str:
        return self._name

    def get_gender(self) -> str:
        return self._gender

    # TODO: CRIO_TASK_MODULE_XCOMPANY
    # Please define all the methods required here as mentioned in the XCompany BuildOut Milestone before implementing the logic.
    # This will ensure that the project can be compiled successfully.
    def assign_manager(self,employee) -> None:
        self._working_under.append(employee)
    
    def set_manager_name(self, manager_name):
        self._manager_name = manager_name
    
    def get_manager_name(self):
        return self._manager_name

    def get_direct_reports(self) -> List:
        return self._working_under

    def __repr__(self) -> str:
        return f'Employee [name={self._name}, gender={self._gender.value}]'





    

