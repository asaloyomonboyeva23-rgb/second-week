dish_1_name = "sushi"
dish_1_price = float(80)
dish_1_quantity = 3
dish_2_name = " burger"
dish_2_price = float(300)
dish_2_quantity = 2
dish_3_name = "hot dog"
dish_3_price = float(3000)
dish_3_quantity = 1
item1_total = dish_1_price * dish_1_quantity
item2_total = dish_2_price * dish_2_quantity
item3_total = dish_3_price * dish_3_quantity
subtotal_before_discounts = item1_total + item2_total + item3_total
name = "asaloy"
has_student_id = "yes"
order_time = 14
subtotal_before_discounts = dish_1_price * dish_1_quantity + dish_2_price * dish_2_quantity + dish_3_price * dish_3_quantity
student_discount_eligibility = has_student_id == "yes"
student_discount =(student_discount_eligibility) * 0.15 * subtotal_before_discounts
subtotal_after_student_discount = subtotal_before_discounts - student_discount
student_discount_eligibility = True if  order_time >= 14 else False
happy_hour = 0.2 * subtotal_before_discounts
subtotal_after_happy_hour = subtotal_after_student_discount - happy_hour
main_discount = student_discount * (student_discount >= happy_hour) + happy_hour * (happy_hour > student_discount)
large_order_discount = 0.05 * (subtotal_before_discounts - main_discount)
subtotal_after_discounts = subtotal_before_discounts - main_discount
service_charge = (subtotal_after_discounts )* 0.1 
delivery_fee = (subtotal_after_discounts >= 100000 ) * 15000
final = subtotal_after_discounts + service_charge + delivery_fee 
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
print(f"Subtotal after Discounts: {subtotal_after_discounts:.2f}")
print(f"Service Charge (10%): {service_charge:.2f}")
print(f"Delivery Fee: {delivery_fee:.2f} ")
print(f"==============================")
print(f"FINAL TOTAL: {final:.2f}")
print(f"total_amount_saved {total_amount_saved:.2f}")
print(f"==============================")
