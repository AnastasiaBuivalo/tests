str1 = "one"
str2 = "two"
str3 = "three"
print(f"Let's count together: {str1}, then goes {str2}, and then {str3}")



def test_input_text(expected_result, actual_result):
    #проверка на равенство assert и сообщение об ошибке
    assert expected_result == actual_result, f"expected {expected_result}, got {actual_result}"

# test_input_text(8, 11)
# test_input_text(11, 11)
# test_input_text(11, 15)

def test_substring(full_string, substring):
    #вхождение подстроки в строку assert и сообщение об ошибке
    assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"

test_substring("fulltext","some_value")