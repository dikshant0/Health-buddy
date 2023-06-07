from project import passwordValidator, adminLoginValidator, validate
import pytest

def main():
    test_passwordValidator()
    test_adminLoginValidator()
    test_validate()

def test_passwordValidator():
    assert passwordValidator("Hello") == False
    assert passwordValidator("dikshant@01") == False
    assert passwordValidator("DIKS@00101") == False
    assert passwordValidator("Dikshant@") == False
    assert passwordValidator("DIKS00101") == False

def test_adminLoginValidator():
    assert adminLoginValidator("Admin", "Admin@1325") == True
    assert adminLoginValidator("admin", "admin@1325") == False
    assert adminLoginValidator("XYZ_ABC", "Dikshant") == False

def test_validate():
    assert validate("Korma21", "Panchi@175") == False
    assert validate("bcuucc1@1", "qwertyuiop") == False
    assert validate("bcuucc11", "lkjhgfdsa1234567890") == False

if __name__ == "__main__":
    main()