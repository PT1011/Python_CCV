
import pytest


class TestUsernameValidator:
    # ===== POSITIVE CASES (should return True) =====
    
    def test_valid_username_basic(self):
        """Test a simple valid username"""
        assert username_validator("alice") == True

    def test_valid_username_with_numbers(self):
        """Test valid username with numbers"""
        assert username_validator("user123") == True

    def test_valid_username_with_underscore(self):
        """Test valid username with underscore"""
        assert username_validator("john_doe") == True

    def test_valid_username_minimum_length(self):
        """Test valid username at minimum length"""
        assert username_validator("abc") == True

    def test_valid_username_maximum_length(self):
        """Test valid username at maximum length"""
        assert username_validator("a" * 20) == True

    # ===== NEGATIVE CASES (should return False) =====

    def test_invalid_empty_username(self):
        """Test that empty string is rejected"""
        assert username_validator("") == False

    def test_invalid_too_short(self):
        """Test username below minimum length"""
        assert username_validator("ab") == False

    def test_invalid_too_long(self):
        """Test username exceeding maximum length"""
        assert username_validator("a" * 30) == False

    def test_invalid_special_characters(self):
        """Test username with special characters"""
        assert username_validator("user@123") == False

    def test_invalid_spaces(self):
        """Test username with spaces"""
        assert username_validator("user name") == False

    # ===== BOUNDARY VALUE ANALYSIS =====

    def test_boundary_min_valid(self):
        """Test at minimum valid boundary"""
        assert username_validator("abc") == True

    def test_boundary_below_min(self):
        """Test just below minimum boundary"""
        assert username_validator("ab") == False

    def test_boundary_max_valid(self):
        """Test at maximum valid boundary"""
        assert username_validator("x" * 20) == True

    def test_boundary_above_max(self):
        """Test just above maximum boundary"""
        assert username_validator("x" * 21) == False

    # ===== EDGE CASES =====

    def test_edge_only_numbers(self):
        """Test username with only numbers"""
        assert username_validator("12345") == True

    def test_edge_only_underscores(self):
        """Test username with only underscores"""
        assert username_validator("____") == False


