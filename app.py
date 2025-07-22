from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "ระบบบันทึกอุบัติเหตุภาคพื้น (7 สาขา) พร้อมใช้งาน!"

if __name__ == "__main__":
    app.run()
