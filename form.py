from operator import add
import csv
import os

def main():
  print("=== 東京都運輸事業者向け燃料費高騰緊急対策事業支援金フォーム ===")

  familyName = input("姓: ")
  firstName = input("名: ")

  while True:
    age = input("年齢を入力してください(半角数字): ")
    if age.isdigit():
      age = int(age)
      if 0 <= age <= 120:
        break
      else:
        print("\033[31m年齢は0-120の範囲で入力してください。\033[0m")
    else:
      print("\033[31m年齢は半角数字で入力してください。\033[0m")

  while True:
    post_number = input("郵便番号(例: 123-4567): ")
    if post_number.replace("-", "").isdigit() and len(post_number.replace("-", "")) == 7:
      break
    else:
      print("\033[31m郵便番号はハイフンを含めて正しい形式で入力してください。\033[0m")

  while True:
    address = input("住所(例: 東京都千代田区千代田１−１): ")
    if "東京都" in address:
      break
    else:
      print("\033[31m申請対象地域は東京都のみです。入力間違いの場合、もう一度入力してください。\033[0m")

  while True:
    phone = input("電話番号(例: 090-1234-5678): ")
    if phone.replace("-", "").isdigit():
      break
    else:
      print("\033[31m電話番号は数字とハイフンのみで入力してください。\033[0m")

  #車検証番号の入力
  car_number = input("車検証番号を入力してください。(半角英数字): ")

  while True:
    vehicle_type = input("車両タイプを入力してください(一般貨物/軽貨物/バス/タクシー): ").strip()
    if vehicle_type in ["一般貨物", "軽貨物", "バス", "タクシー"]:
      break
    else:
      print("\033[31m車両タイプは「一般貨物」「軽貨物」「バス」「タクシー」のいずれかを入力してください。\033[0m")

  vehicle_subsidy = {"一般貨物": 23000, "軽貨物": 8000, "バス": 35000, "タクシー": 12000}
  application_amount = vehicle_subsidy[vehicle_type]

  #入力内容確認
  print("\n== 入力確認 ==")
  print(f"苗字: {familyName}")
  print(f"名前: {firstName}")
  print(f"年齢: {age}")
  print(f"郵便番号: {post_number}")
  print(f"住所: {address}")
  print(f"電話番号: {phone}")
  print(f"車検証番号: {car_number}")
  print(f"車両タイプ: {vehicle_type}")
  print(f"申請金額: {application_amount}円")


  #条件に応じた応答を作成
  if age < 18:
    print("\033[31m未成年の方は、補助金の対象外です。\033[0m")
  else:
    print("補助金を申請いたしました。")
    print("指定口座への振り込み、または担当者からの連絡があるまでお待ちください。")

    #申請内容の保存
    save_to_file(familyName, firstName, age, post_number, address, phone, car_number, vehicle_type, application_amount)

  view_saved_data()

def save_to_file(familyName, firstName, age, post_number, address, phone, car_number, vehicle_type, application_amount):
  """申請内容をCSVファイルに保存"""
  file_name = "subsidy_applications.csv"
  headers = ["苗字", "名前", "年齢", "郵便番号", "住所", "電話番号", "車検証番号", "車両タイプ", "申請額"]

  #ファイルが存在しない場合はヘッダーを追加
  write_headers = not os.path.exists(file_name)

  with open(file_name, mode="a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    if write_headers:
      writer.writerow(headers)
    writer.writerow([familyName, firstName, age, post_number, address, phone, car_number, vehicle_type, application_amount])

  print("\033[32m申請内容が保存されました。\033[0m")

def view_saved_data():
  """保存された申請内容を表示"""
  file_name = "subsidy_applications.csv"
  if not os.path.exists(file_name):
    print("\033[33m保存された申請はありません。\033[0m")
    return

  print("\n=== 保存された申請内容 ===")
  with open(file_name, mode="r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
      print(", ".join(row))

if __name__ == "__main__":
  main()



