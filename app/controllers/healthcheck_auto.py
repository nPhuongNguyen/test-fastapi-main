# # app/controllers/healthcheck_auto.py
# from fastapi import APIRouter
# from healthcheck import HealthCheck
# from sqlalchemy.orm import Session
# from app.config.database import get_db
# from sqlalchemy import text
# import time

# router = APIRouter()
# health = HealthCheck()

# # Check database
# def check_database():
#     try:
#         db: Session = next(get_db())
#         db.execute(text("SELECT 1"))
#         return True, "database ok"
#     except Exception as e:
#         return False, str(e)

# # Check 1s delay
# def check_delay():
#     time.sleep(1)  # dùng sleep đồng bộ
#     return True, "1s delay ok"

# # Thêm vào healthcheck
# health.add_check(check_database)
# health.add_check(check_delay)

# @router.get("/healthcheck_auto")
# def healthcheck():
#     return health.run()
