
def digit_count_and_sum(n):
    n_str = str(n)
    count = len(n_str)
    total = sum(int(digit) for digit in n_str)
    return count, total

def reverse_number(n):
    n_str = str(n)
    reversed_str = n_str[::-1]
    return int(reversed_str)

def is_palindrome(n):
    n_str = str(n)
    return n_str == n_str[::-1]

def find_palindromes_in_range(start, end):
    palindromes = []
    for num in range(start, end + 1):
        if is_palindrome(num):
            palindromes.append(num)
    return palindromes

def is_symmetric(n):
    n_str = str(n)
    length = len(n_str)
    
    if length % 2 != 0:
        return False
        
    mid = length // 2
    first_half = n_str[:mid]
    second_half = n_str[mid:]
    
    return first_half == second_half

def digital_root(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

def main():
    print("Анализатор чисел")
    
    try:
        n = int(input("Введите натуральное число для анализа: "))
        if n < 1:
            print("Ошибка! Число должно быть натуральным (больше 0).")
            return
        
        print(f"\nАнализ числа {n}:")
        
        count, total_sum = digit_count_and_sum(n)
        print(f"Количество цифр: {count}")
        print(f"Сумма цифр: {total_sum}")
        
        reversed_num = reverse_number(n)
        print(f"Число в обратном порядке: {reversed_num}")
        
        palindrome_check = "Да" if is_palindrome(n) else "Нет"
        print(f"Является палиндромом? {palindrome_check}")
        
        symmetric_check = "Да" if is_symmetric(n) else "Нет"
        print(f"Является симметричным? {symmetric_check}")
        
        dr = digital_root(n)
        print(f"Цифровой корень: {dr}")
        
        print("\nПоиск палиндромов в диапазоне:")
        
        try:
            start = int(input("Введите начало диапазона: "))
            end = int(input("Введите конец диапазона: "))
            
            if start > end:
                print("Начало диапазона не может быть больше конца.")
            else:
                palindromes = find_palindromes_in_range(start, end)
                if palindromes:
                    print(f"\nПалиндромы между {start} и {end}:")
                    for i in range(0, len(palindromes), 10):
                        print(" ".join(map(str, palindromes[i:i+10])))
                else:
                    print("В данном диапазоне палиндромов не найдено.")
                    
        except ValueError:
            print("Нужно ввести числа для диапазона.")
            
    except ValueError:
        print("Пожалуйста, введите корректное натуральное число.")

if __name__ == "__main__":
    main()
    input("\nНажмите Enter для выхода...")
