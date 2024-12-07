def is_valid_email_structure(input_text):
    if '@' in input_text:
        at_position = input_text.index('@')
        if at_position < len(input_text) - 1:
            domain_text = input_text[at_position + 1:]
            if '.' in domain_text:
                dot_position = domain_text.index('.')
                if dot_position < len(domain_text) - 1:
                    tld_text = domain_text[dot_position + 1:]
                    if len(tld_text) >= 2:
                        return True
    return False

text = "example@domain.com"
if is_valid_email_structure(text):
    print("Valid email structure.")
else:
    print("Invalid email structure.")