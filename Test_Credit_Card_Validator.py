
import pytest


class Test_Credit_Card_Validator:
    
    # ===== POSITIVE CASES (should return True) =====

    def test_visa_starts_with_4(self):
        """Test that a visa card starts with 4 works"""
        assert credit_card_validator(4929702602759872) == True

    def test_mastercard_starts_in_range(self):
        """Test that a mastercard start is in range of 51-55"""
        assert credit_card_validator(5105105105105100) == True
    
    def test_mastercard_starts_in_range_2221_to_2720(self):
        """Test that a mastercard that starts between 2221 and 2720 works"""
        assert credit_card_validator(2223003122003222) == True

    def test_amex_starts_in_range_34_to_37(self):
        """Test that an amex card that starts between 34 and 37 works"""
        assert credit_card_validator(340000000000009) == True
  
    # ===== NEGATIVE CASES (should return False) =====

    def test_visa_starts_with_not_4(self):
        """Test that a visa card that starts with not 4 doesnt work"""
        assert credit_card_validator(9648188554374845) == False

    def test_mastercard_starts_not_in_range_51(self):
        """Test that a mastercard number thats lower than 51 doesnt work"""
        assert credit_card_validator(3415995671546939) == False

    def test_mastercard_starts_not_in_range_55(self):
        """Test that a mastercard number thats higher than 55 doesnt work"""
        assert credit_card_validator(5910952703965038) == False
    
    def test_mastercard_starts_not_in_range_2221(self):
        """Test that a mastercard number thats lower than 2221 doesnt work"""
        assert credit_card_validator(2220263456784267) == False
    
    def test_mastercard_starts_not_in_range_2720(self):
        """Test that a mastercard number thats higher than 2720 doesnt work"""
        assert credit_card_validator(2721263456784675) == False
    
    def test_amex_starts_not_in_range_34(self):
        """Test that an amex number thats lower than 34 doesnt work"""
        assert credit_card_validator(349804648204183) == False
    
    def test_amex_starts_not_in_range_37(self):
        """Test that an amex number thats higher than 37 doesnt work"""
        assert credit_card_validator(963228270664800) == False
    
    def test_invalid_length_for_correct_prefix_visa(self):
        """Test that a visa card with a valid number but invalid length doesnt work"""
        assert credit_card_validator(453957876362149) == False
    
    def test_invalid_length_for_correct_prefix_amex(self):
        """Test that an amex card with a valid number but invalid length doesnt work"""
        assert credit_card_validator(37828224631003) == False

    def test_invalid_length_for_correct_prefix_mastercard(self):
        """Test that a mastercard with a valid number but invalid length doesnt work"""
        assert credit_card_validator(550000555555550) == False

    def test_unsupported_prefixes_doesnt_work_16(self):
        """Test that a card with a valid 16 digit number but invalid prefix doesnt work"""
        assert credit_card_validator(1402478374733632) == False
    
    def test_unsupported_prefixes_doesnt_work_15(self):
        """Test that a card with a valid 16 digit number but invalid prefix doesnt work"""
        assert credit_card_validator(656226165971316) == False
    
    def test_fail_luhn_check_16(self):
        """Test that a number with valid prefix and length but fails the luhn check"""
        assert credit_card_validator(4676767676767676) == False
    
    def test_fail_luhn_check_15(self):
        """Test that a number with valid prefix and length but fails the luhn check"""
        assert credit_card_validator(467676767676767) == False

    def test_empty_input(self):
        """Test that an empty input does not work"""
        assert credit_card_validator("") == False
