from fastapi import APIRouter, HTTPException
from starlette.responses import JSONResponse
from utils.utils import load_data
from crud.crud import get_employees, search_employee
from schemas.api_input import FileConfig

router = APIRouter()
@router.get("/")
def get_data() -> JSONResponse:
    """
        Lấy danh sách tất cả nhân viên từ file JSON
    """
    data = load_data(r"D:\BaiTapNM\app\utils\dummy_data.json")
    result = get_employees(data=data)
    return JSONResponse(result)

@router.post("/search")
def search(employee: FileConfig) -> JSONResponse:
    """
        Tìm nhân viên theo ID và trả về thông tin nhân viên.
        VD: {  "id": "CT001"   } (json)

    """
    data = load_data(r"D:\BaiTapNM\app\utils\dummy_data.json")
    employee_info = search_employee(data=data, employee_id=employee.id)
    if employee_info:
        return JSONResponse(employee_info)
    return JSONResponse({"detail" : "Not found"}, status_code=404)

# @router.post("/employee/{employee_id}")
# async def read_employ(employee_id: str):
#     data = load_data(r"D:\BaiTapNM\app\utils\dummy_data.json")
#     employee = search_employee(data=data, employee_id=employee_id)
#     if not employee:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return {"item": employee[employee_id]}