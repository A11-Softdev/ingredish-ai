from fastapi import APIRouter, HTTPException
from app.models.menu_model import MenuRequest
from app.services.menu_service import generate_menu

router = APIRouter()

@router.get("/")
def getDefault():
    return {"Hello" : "World!"}

@router.post("/generate-menu/")
def generate_menu_api(request: MenuRequest):
    try:
        # Call the service function to generate the menu
        menu_item = generate_menu(request.optional_dish, request.ingredients, request.supplies)
        return {"Menu" : menu_item}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get('/mock-data/')
def get_mock_data():
    data = {
                "MenuItem": {
                    "Name": "Duck Confit",
                    "Description": "ต้นขาเป็ดส่วนสะโพกหมักเกลือและเครื่องเทศแล้วนำไปปรุงช้าๆ ในไขมันเป็ดจนนุ่มละมุน เสิร์ฟพร้อมมันฝรั่งอบและสลัดผักกาดหอม",
                    "EstimatedTimeCook": "60 นาที"
                },
                "Recipe": {
                    "Ingredients": [
                        {
                            "name": "ต้นขาเป็ดส่วนสะโพก",
                            "quantity": "4 ชิ้น",
                            "preparation": "ตัดแต่งไขมันส่วนเกิน"
                        },
                        {
                            "name": "เกลือ",
                            "quantity": "1 ช้อนชา"
                        },
                        {
                            "name": "พริกไทยดำ",
                            "quantity": "1/2 ช้อนชา"
                        },
                        {
                            "name": "ใบไทม์",
                            "quantity": "1 ช้อนโต๊ะ"
                        },
                        {
                            "name": "ใบกระวาน",
                            "quantity": "2 ใบ"
                        },
                        {
                            "name": "กระเทียม",
                            "quantity": "2 กลีบ",
                            "preparation": "บด"
                        },
                        {
                            "name": "ไขมันเป็ด",
                            "quantity": "พอท่วมเป็ด"
                        }
                    ],
                    "Instructions": [
                        {
                            "step": 1,
                            "description": "ผสมเกลือ พริกไทย ใบไทม์ ใบกระวาน และกระเทียมในชามใบใหญ่ เคล้ากับเป็ดให้ทั่ว"
                        },
                        {
                            "step": 2,
                            "description": "นำเป็ดที่เตรียมแล้วใส่ภาชนะ ภาชนะที่เข้าเตาอบได้ปกติ หรือหม้อหุงช้า"
                        },
                        {
                            "step": 3,
                            "description": "ราดไขมันเป็ดให้ท่วมเป็ด"
                        },
                        {
                            "step": 4,
                            "description": "ปิดภาชนะให้มิดชิดและนำไปแช่ในตู้เย็นเป็นเวลา 24 ชั่วโมง"
                        },
                        {
                            "step": 5,
                            "description": "นำเป็ดออกจากตู้เย็นและตั้งทิ้งไว้ที่อุณหภูมิห้องประมาณ 1 ชั่วโมงก่อนปรุงอาหาร"
                        },
                        {
                            "step": 6,
                            "description": "นำภาชนะที่มีเป็ดเข้าเตาอบที่อุณหภูมิ 160 องศาเซลเซียส และปรุงอาหารเป็นเวลา 3 ชั่วโมง หรือจนกว่าเป็ดนุ่ม เมื่อจิ้มด้วยส้อมแล้วไม่มีเลือดไหลออกมา"
                        },
                        {
                            "step": 7,
                            "description": "นำเป็ดออกจากเตาอบและพักไว้ให้เย็นลงเล็กน้อยก่อนเสิร์ฟ"
                        }
                    ]
                }
            }
    return {"Menu" : data} 