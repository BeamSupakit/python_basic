"""
#
# Part: Python PIP
#
"""

import camelcase
camel = camelcase.CamelCase()
txt = "hello"
print(camel.hump(txt))

INSERT INTO customers
(`customer_name` , `contact_name` , `address` , `city` , `postal` , `country`)
VALUES
('Supakit2', 'Student', 'NULL', 'Phuket', '8300', 'Thailand')