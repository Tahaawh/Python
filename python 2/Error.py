try:
    # مثال یک عملیات که ممکن است خطا تولید کند
    z = int(input("Enter a number: "))
    result = 10 / z
    print(f"Result: {result}")
    
    # اضافه کردن عملیات کار با لیست و دیکشنری
    myList = [1, 2, 3]
    print(myList[5])  # این خط ممکن است خطای IndexError بدهد
    
    myDict = {"a": 1, "b": 2}
    print(myDict["c"])  # این خط ممکن است خطای KeyError بدهد
    
    # نمونه‌ای از یک خطای TypeError
    result = "string" + 10  # TypeError

    # نمونه‌ای از یک خطای MemoryError (برای این که این خطا در شرایط خاص به‌وجود بیاید، نیاز به حافظه زیاد است)
    largeList = [0] * (10**10)  # ممکن است این خط حافظه کم بیاورد

except ZeroDivisionError as e:
    print(f"Error: Division by zero is not allowed. ({e})")

except ValueError as e:
    print(f"Error: Invalid input, please enter a valid number. ({e})")

except OverflowError as e:
    print(f"Error: The number is too large to handle. ({e})")

except FileNotFoundError as e:
    print(f"Error: File not found. ({e})")

except IndexError as e:
    print(f"Error: List index out of range. ({e})")

except KeyError as e:
    print(f"Error: Key not found in dictionary. ({e})")

except TypeError as e:
    print(f"Error: Type mismatch. ({e})")

except MemoryError as e:
    print(f"Error: Memory limit exceeded. ({e})")

except Exception as e:
    # برای مدیریت خطاهای پیش‌بینی‌نشده
    print(f"An unexpected error occurred: {e}")