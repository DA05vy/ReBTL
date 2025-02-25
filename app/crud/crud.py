def get_employees(data: list):
    """
        Trả về danh sách tất cả nhân viên.
    """
    return data
def search_employee(data: list, employee_id: str):
    """
        Tìm nhân viên theo ID và trả về thông tin nhân viên.
    """
    for employee in data:
        if employee["id"] == employee_id:
            return employee
    return None