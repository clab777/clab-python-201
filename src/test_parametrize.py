import pytest
import re

from validator import validate_ip

  
# Make a regular expression 
# for validating an Ip-address 
regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''
      
# Define a function for 
# validate an Ip addess 
@pytest.mark.parametrize('ip_address', ['172.24.21.8', '172.24.21.9', '172.24.21.10', '172.24.21.11', '172.24.21', '172.1.2'])
def test_check(ip_address):
    """test that exception is raised for invalid Ip address"""
    validIp = validate_ip(ip_address)
    assert(validIp == True)