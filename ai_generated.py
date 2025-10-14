dish_1_name = "sushi"
dish_1_price = float(80)
dish_1_quantity = 3

dish_2_name = "burger"
dish_2_price = float(300)
dish_2_quantity = 2

dish_3_name = "hot dog"
dish_3_price = float(3000)
dish_3_quantity = 1

name = "Asaloy"
has_student_id = "yes"  
order_time = 15 
item1_total = dish_1_price * dish_1_quantity
item2_total = dish_2_price * dish_2_quantity
item3_total = dish_3_price * dish_3_quantity
subtotal_before_discounts = item1_total + item2_total + item3_total
eligible_student = (has_student_id.lower() == "yes")
eligible_happy_hour = (order_time >= 14) and (order_time <= 17)
eligible_large_order = (subtotal_before_discounts >= 150000)
student_discount = subtotal_before_discounts * 0.15 * eligible_student
happy_hour_discount = subtotal_before_discounts * 0.20 * eligible_happy_hour
main_discount = (student_discount * (student_discount >= happy_hour_discount) +
                 happy_hour_discount * (happy_hour_discount > student_discount))

main_discount_name = ("Student" * (student_discount >= happy_hour_discount) +
                      "Happy Hour" * (happy_hour_discount > student_discount))
large_order_discount = 0.05 * (subtotal_before_discounts - main_discount) * eligible_large_order
total_discounts = main_discount + large_order_discount
subtotal_after_discounts = subtotal_before_discounts - total_discounts
service_charge = subtotal_after_discounts * 0.10
delivery_fee = (subtotal_after_discounts < 100000) * 15000
free_delivery = not (subtotal_after_discounts < 100000)

final_total = subtotal_after_discounts + service_charge + delivery_fee
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
print(f"Subtotal before discounts: {subtotal_before_discounts}")
print()
print(f"Discount Eligibility and Amounts:")
print(f"Student Discount (15%) → {eligible_student}, Amount: {student_discount}")
print(f"Happy Hour Discount (20%) → {eligible_happy_hour}, Amount: {happy_hour_discount}")
print(f"Main Discount Applied: {main_discount_name}, Amount: {main_discount}")
print(f"Large Order Discount (5%) → {eligible_large_order}, Amount: {large_order_discount}")
print(f"------------------------------")
print(f"Total Discounts: {total_discounts}")
print(f"Subtotal after Discounts: {subtotal_after_discounts}")
print(f"Service Charge (10%): {service_charge}")
print(f"Delivery Fee: {delivery_fee} (Free Delivery: {free_delivery})")
print(f"==============================")
print(f"FINAL TOTAL: {final_total}")
print(f"==============================")