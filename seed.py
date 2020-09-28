from models import AdminModel
from connections import app, db

admins = AdminModel.query.filter(AdminModel.is_supper.is_(True)).first()
if admins is None:
    admin = AdminModel("admin","admin@gmail.com","123123", True)
    db.session.add(admin)
    db.session.commit()
    print("========== User Seeded Seccessfully ===========")
else: 
    print("\n\n========== Super Admin already exists ===========\n\n")
