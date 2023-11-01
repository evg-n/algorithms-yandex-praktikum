ROMAN_TO_ARABIC = {
    "IV": 4,
    "IX": 9,
    "XL": 40,
    "XC": 90,
    "CD": 400,
    "CM": 900,
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


def convert_to_arabic(number: str) -> int:
    VLD_usage = [False] * 3
    IXCM_cont_usage = [0] * 4
    result = 0
    prev_number = None

    def update_vld_usage(i):
        num = number[i]
        if not any(num == s for s in "VLD"):
            return True

        if num == "V":
            if VLD_usage[0]:
                return False
            VLD_usage[0] = True
        if num == "L":
            if VLD_usage[1]:
                return False
            VLD_usage[1] = True
        if num == "D":
            if VLD_usage[2]:
                return False
            VLD_usage[2] = True
        return True

    def update_ixcm_usage(i):
        num = number[i]
        if num == "I":
            IXCM_cont_usage[0] += 1
        else:
            IXCM_cont_usage[0] = 0
        if num == "X":
            IXCM_cont_usage[1] += 1
        else:
            IXCM_cont_usage[1] = 0
        if num == "C":
            IXCM_cont_usage[2] += 1
        else:
            IXCM_cont_usage[2] = 0
        if num == "M":
            IXCM_cont_usage[3] += 1
        else:
            IXCM_cont_usage[3] = 0
        return all(cnt <= 3 for cnt in IXCM_cont_usage)

    i = 0
    while i < len(number):
        num = number[i]
        if not update_vld_usage(i) or not update_ixcm_usage(i):
            return -1

        if i + 1 < len(number) and num + number[i + 1] in ROMAN_TO_ARABIC:
            two_digit = num + number[i + 1]
            if not update_vld_usage(i + 1):
                return -1
            new_number = ROMAN_TO_ARABIC[two_digit]
            if prev_number is not None and prev_number < new_number:
                return -1
            prev_number = new_number
            result += new_number
            i += 1
        else:
            new_number = ROMAN_TO_ARABIC[num]
            if prev_number is not None and prev_number < new_number:
                return -1
            prev_number = new_number
            result += new_number

        i += 1
    return result


roman_number = input()
print(convert_to_arabic(roman_number))
