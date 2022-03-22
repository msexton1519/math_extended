import itertools
import re
import math_extended
import math


# These are my solutions to an assortment of Project Euler problems.
# Currently, some problems aren't quite generic enough or
# do not have an in depth explanation of how they work; I am
# going to improve on these issues and add more solutions soon.
# Note: all solutions are correct, however.

#Helper function
#Returns unicode value to represent capital letter characters in numeric form.
# A = 65, hence 65 - 64 = 1, 1st character.
def string_order(stri):
    summ = 0
    for i in stri:
        summ += (ord(i) - 64)
    return summ


#Complete and correct
def project_euler1():
    sum_of_3s = 3*(int(1000/3) + 1)*int(1000/3)/2
    sum_of_5s = 5*(int(1000/5))*(int(1000/5) - 1)/2
    sum_of_15s = 15*(int(1000/15) + 1)*int(1000/15)/2
    return sum_of_5s + sum_of_3s - sum_of_15s


#Comlete and correct
#Implemented with a formula for the even Fibonacci numbers (n_1 = 0, n_2 = 2, n_k = 4 * n_k + n_(k-1))
#Also includes optional upper bound.
def project_euler2(upper=4000000):
    n_1 = 0
    n_2 = 2
    next = 4 * n_2 + n_1
    sum = n_1 + n_2 + next

    while 4*next + n_2 < upper:
        temp = n_2
        n_2 = next
        n_1 = temp
        next = 4*n_2 + n_1
        sum += next

    return sum


#Complete and correct
#Simply find all prime factors, then return largest with max().
def project_euler3(num):
    primes = math_extended.prime_factors(num)
    return max(primes)


#Complete and correct
#Computes the largest palindrome product by taking in an optional argument
#Then checking if the product is a palindrome and is larger than current maximum.
def project_euler4(num=10000):
    maxim = -1
    for i in range(1, num):
        for j in range(1, num):
            if math_extended.is_palindrome(i * j) and i * j > maxim:
                maxim = i * j
    return maxim


#Correct and complete
#LCM of all numbers ranging from 1 to 20 produces the smallest number
# all numbers from 1 to 20 divide into.
#--Going to make more generic soon--
def project_euler5():
    return math.lcm(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)


#Complete and correct
#Use the sum of squares formula as well as triangle number formula squared, find the difference
#between them.
def project_euler6(num):
    first = num * (num + 1) * (2 * num + 1) / 6
    second = ((num + 1) * num / 2) ** 2
    return second - first


#Complete and correct
#Brute force function, will improve, to check primes, and when total reaches 10001
#finish and return the last prime.
def project_euler7(num=10001):
    num_primes = 0
    curr = 2
    prime = 0
    while num_primes <= num:
        if math_extended.is_prime(curr):
            num_primes += 1
            prime = curr
        curr += 1
    return prime


#Correct but needs tightening up.
def project_euler8(sub_size):
    with open('project_euler8') as file:
        large_set = []
        str = file.read(1)
        while str != '':
            if str != '\n':
                num = int(str)
                large_set.append(num)
            str = file.read(1)
        start = 0
        end = sub_size
        max = -1
        while sub_size < len(large_set):
            temp = math.prod(large_set[start: sub_size])
            if temp > max:
                max = temp
            start += 1
            sub_size += 1
        return max


#Complete and correct. Tighten up the implementation.
#Uses Euclid's Pythagorean triple formula. Returns triple where
# a + b + c = 1000
def project_euler9(num=1000):
    perim = 0
    n = 2
    m = 1
    sides = (0, 0, 0)
    while perim != num:
        while m < n:
            a = n ** 2 - m ** 2
            b = 2 * m * n
            c = n ** 2 + m ** 2
            perim = a + b + c
            sides = (a, b, c)
            if perim == num:
                return a*b*c
            m += 1
        m = 1
        n += 1
    return sides


#Complete and correct. Use sieve though.
#Sums all primes below num. Needs improvement.
def project_euler10(num=2000000):
    sum = 0
    for i in range(2, num):
        if math_extended.is_prime(i):
            sum += i
    return sum


#Complete and correct
#Returns first triangle number with num_div divisors.
def project_euler12(num_div=500):
    curr = 1
    num = 1
    tri = 0
    while curr <= num_div:
        num += 1
        tri = math_extended.triangle_num(num)
        curr = math_extended.number_of_factors(tri)
    return tri


#Complete and correct
#Reads the file and determines the first 10 digits of the 100 50-digit numbers.
def project_euler13():
    with open('project_euler13') as file:
        sum = 0
        str = file.readline()
        while str != '':
            num = int(str)
            sum += num
            str = file.readline()
        while sum > 9999999999:
            sum //= 10
    return sum


#Complete and correct. Could use memoization?
def project_euler14(num):
    max_val = -1
    start = 0
    for i in range(1, num):
        temp = math_extended.collatz(i)
        if temp > max_val:
            max_val = temp
            start = i
    return start


#Complete and correct
#The trick is that Pascal's triangle reveals the number of paths in grid.
def project_euler15(num=20):
    return math.comb(2 * num, num)


#Complete and correct.
def project_euler16(num=2, exp=1000):
    num = num ** exp
    sum = math_extended.sum_of_digits(num)
    return sum


#Complete and correct
def project_euler20(num):
    fact = math.factorial(num)
    return math_extended.sum_of_digits(fact)


#Complete and correct
#Checks to see if numbers are ammicable but if statement removes double counting
# since sum_of_divisors(284) = 220 but sum_of_divisors(220) = 284.
def project_euler21(num=10000):
    summ = 0
    for i in range(2, num):
        sum_div = math_extended.sum_of_divisors(i) - i
        sum_div2 = math_extended.sum_of_divisors(sum_div) - sum_div
        if i == sum_div2 and i != sum_div:
            summ += i
    return summ


#Complete and correct
#Read file and calculate value of capital letter character and sums all characters
#in each name, and sums all of the sums. Returning the sum of all sums of each character.
def project_euler22(fi):

    with open(fi) as file:
        reg = re.compile('[a-zA-Z]+')
        lst = sorted(reg.findall(file.read()))
        num = 1
        summ = 0
        for i in lst:
            summ += num * string_order(i)
            num += 1
        return summ


#Complete and correct. slow though
#Brute force way to cycle through all amicable numbers and check which numbers cannot
#be formed from the sums of them.
def project_euler23(num):
    lst = []
    set1 = set()
    sum = 0
    counter, counter2 = 2, 2
    while counter <= num:
        if math_extended.sum_of_divisors(counter) > 2 * counter:
            lst.append(counter)
        counter += 1
    counter, counter2 = 0, 0
    while counter < len(lst):
        while counter2 < len(lst):
            if lst[counter] + lst[counter2] <= 28123:
                set1.add(lst[counter] + lst[counter2])
            counter2 += 1
        counter2 = counter
        counter += 1
    for i in range(len(set1)):
        sum += set1.pop()
    return 28123 * (28123 + 1) // 2 - sum


#Complete and correct
#Brute force way to find the millionth permutation of '0123456789'.
#Working on improving efficiency.
def project_euler24(perm=1000000):
    list = itertools.permutations('0123456789')
    counter = 1
    for i in list:
        if counter == perm:
            return i
        counter += 1
    return None


#Complete and correct
#Creates a new Fibonacci number on each iteration and  checks
#whether the number has more digits than num_digits and increments index.
def project_euler25(num_digits=1000):
    big_num = 10 ** (num_digits - 1)
    prev = 1
    curr = 1
    next = prev + curr
    index = 3
    while next // big_num < 1:
        temp = curr
        curr = next
        prev = temp
        next = prev + curr
        index += 1
    return index


#Complete and correct.
#Trick to compute the numbers of each 'row' and not actually create a 2d array.
#Pattern follows this method.
def project_euler28(max_rows):
    start = 1
    rows = 3
    sum = 1
    while rows <= max_rows:
        for i in range(4):
            start += rows - 1
            sum += start
        rows += 2
    return sum


#Complete and correct
#Brute force computes all powers from 2 to power, with bases 2 to base. Add them to a set to check
#uniqueness.
def project_euler29(base, power):
    unique = set()
    math_extended.validation(base, 2)
    math_extended.validation(power, 2)
    for i in range(2, base):
        for j in range(2, power):
            unique.add(i ** j)
    print(len(unique))


#Complete and correct.
def project_euler30():
    max = 999999
    num_check = 2
    total = 0
    while num_check <= max:
        temp = num_check
        summ = 0
        while temp > 0:
            summ += (temp % 10) ** 5
            temp //= 10
        if summ == num_check:
            total += num_check
        num_check += 1
    return total


#Complete and correct
def project_euler33():
    numer = 1
    denom = 1
    for i in range(10, 100):
        for j in range(i + 1, 100):
            if j % 10 != 0 and i % 10 == j // 10 and i/j == (i // 10)/(j % 10):
                numer *= i
                denom *= j
    return denom // math_extended.gcd(numer, denom)


#Complete and correct.
def project_euler34():
    total = 0
    for i in range(10, 2999999):
        temp = i
        sum = 0
        while temp > 0:
            sum += math.factorial(temp % 10)
            temp //= 10
        if sum == i:
            total += i
    return total


#Complete and correct
def project_euler36(num):
    summ = 0
    for i in range(1, num):
        if math_extended.is_palindrome(i) and math_extended.is_palindrome(int(bin(i)[2:])):
            summ += i
    return summ


#Complete and correct
def project_euler42(fi):
    with open(fi) as file:
        reg = re.compile('[a-zA-Z]+')
        lst = sorted(reg.findall(file.read()))
        total = 0
        for i in lst:
            summ = string_order(i)
            temp = 2 * summ
            temp = math.floor(math.sqrt(temp))
            if temp * (temp + 1) // 2 == summ:
                total += 1
        return total


#Complete and correct
def project_euler43():

    def str_to_int(str1, str2, str3, num):
        return (int(str1) * 100 + int(str2) * 10 + int(str3)) % num

    lst = itertools.permutations('0123456789')
    is_true = True
    summ = 0
    for i in lst:
        if str_to_int(i[1], i[2], i[3], 2) != 0:
            is_true = is_true and False
        if str_to_int(i[2], i[3], i[4], 3) != 0 and is_true:
            is_true = is_true and False
        if str_to_int(i[3], i[4], i[5], 5) != 0 and is_true:
            is_true = is_true and False
        if str_to_int(i[4], i[5], i[6], 7) != 0 and is_true:
            is_true = is_true and False
        if str_to_int(i[5], i[6], i[7], 11) != 0 and is_true:
            is_true = is_true and False
        if str_to_int(i[6], i[7], i[8], 13) != 0 and is_true:
            is_true = is_true and False
        if str_to_int(i[7], i[8], i[9], 17) != 0 and is_true:
            is_true = is_true and False
        if is_true:
            temp = 0
            power = 9
            while power >= 0:
                temp += int(i[9 - power]) * (10 ** power)
                power -= 1
            summ += temp
        is_true = True
    return summ


#Complete and correct
def project_euler48(power, modu=1):
    sum = 0
    for i in range(1, power + 1):
        sum += pow(i, i, modu)
    return sum % modu


#Complete and correct
def project_euler53(num, maxi):
    math_extended.validation(num, 0)
    math_extended.validation(maxi, 0)
    total = 0
    for i in range(1, num + 1):
        for j in range(1, num + 1):
            if math.comb(i, j) > maxi:
                total += 1
    return total


#Complete and correct
def project_euler56(max_base, max_pow):
    max = 0
    for base in range(1, max_base + 1):
        for power in range(1, max_pow + 1):
            curr = math_extended.sum_of_digits(base ** power)
            if curr > max:
                max = curr
    return max


#Complete and correct
def project_euler69(num=2):
    maxi = 0
    n = 0
    for i in range(2, num + 1):
        next = i / math_extended.phi(i)
        if next > maxi:
            maxi = next
            n = i
    return n


#Complete and correct
def project_euler97(num_digits):
    num = 28433
    power = 1
    raised = 10 ** num_digits
    while power <= 7830457:
        num = (num * 2) % raised
        power += 1
    num += 1
    return num


#Complete and correct
def project_euler112(num=0):
    bouncy = 0
    counter = 100
    denom = 1
    while bouncy / denom != .9:
        if not math_extended.non_increasing_number(counter) and not math_extended.non_decreasing_number(counter):
            bouncy += 1
            denom = counter
        counter += 1
    return denom


def project_euler124(n, k):
    def rad(num):
        primes = math_extended.prime_factors2(num)
        mult = 1
        for (x, y) in primes:
            mult *= x
        return mult

    set1 = [(1, 1)]
    for i in range(2, n + 1):
        set1.append((i, rad(i)))

    set2 = sorted(set1, key=lambda x: x[1])
    return set2[k - 1]

