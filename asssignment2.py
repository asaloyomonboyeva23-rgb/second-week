dish_1_name = str(input("enter your first dish :"))
dish_1_price = float(input("enter the first dish price"))
dish_1_quantity = int(input("enter the first dish quantity :"))
dish_2_name = str(input("enter your second dish :"))
dish_2_price = float(input("enter your second dish price "))
dish_2_quantity = int(input("enter the second dish quantity :"))
dish_3_name =  str(input("enter your third dish :"))
dish_3_price = float(input(" enter the third dish price"))
dish_3_quantity = int(input("enter the third dish quantity :"))
item1_total = dish_1_price * dish_1_quantity
item2_total = dish_2_price * dish_2_quantity
item3_total = dish_3_price * dish_3_quantity
subtotal_before_discounts = item1_total + item2_total + item3_total
name = input("please enter your name : ")
has_student_id = str(input(" do you have a studend id  yes / no : "))
order_time = int(input( " enter the order time :"))
subtotal_before_discounts = dish_1_price * dish_1_quantity + dish_2_price * dish_2_quantity + dish_3_price * dish_3_quantity

student_discount_eligibility = has_student_id == "yes"
student_discount =(student_discount_eligibility) * 0.15 * subtotal_before_discounts


happy_hour = order_time >= 14
happy_hour = 0.2 * subtotal_before_discounts

main_discount = student_discount * (student_discount >= happy_hour) + happy_hour * (happy_hour > student_discount)
subtotal_after_main_discount = subtotal_before_discounts - main_discount  

large_order_discount = 0.05 * (subtotal_after_main_discount)

service_charge = (subtotal_after_main_discount)* 0.1 
delivery_fee = (subtotal_after_main_discount>= 100000 ) * 15000

final = subtotal_after_main_discount + service_charge + delivery_fee 
total_amount_saved = subtotal_before_discounts - final
print(f"\n==============================")
print(f"       RESTAURANT RECEIPT      ")
print(f"==============================")
print(f"Customer Name: {name}")
print(f"Has Student ID: {has_student_id}")
print(f"Order Time: {order_time}:00")
print(f"------------------------------")
print(f"Items Ordered:")
print(f"{dish_1_name} x {dish_1_quantity} = {item1_total}")
print(f"{dish_2_name} x {dish_2_quantity} = {item2_total}")
print(f"{dish_3_name} x {dish_3_quantity} = {item3_total}")
print(f"------------------------------")
print(f"Subtotal before discounts: {subtotal_before_discounts:.2f}")
print(f"Discount Eligibility and Amounts:")
print(f"Student Discount (15%) → {student_discount_eligibility}, Amount: {student_discount:.2f}")
print(f"Happy Hour Discount (20%) → {student_discount_eligibility}, Amount: {happy_hour:.2f}")
print(f"Main Discount Applied:, Amount: {main_discount:.2f}")
print(f"Large Order Discount (5%) →, Amount: {large_order_discount:.2f}")
print(f"-------------------------------")
print(f"Subtotal after Discounts: {subtotal_after_main_discount:.2f}")
print(f"Service Charge (10%): {service_charge:.2f}")
print(f"Delivery Fee: {delivery_fee:.2f} ")
print(f"==============================")
print(f"FINAL TOTAL: {final:.2f}")
print(f"total_amount_saved {total_amount_saved:.2f}")
print(f"==============================")
